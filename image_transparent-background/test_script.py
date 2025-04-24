#!/usr/bin/env python3
import sys
import argparse
import cv2   # pip install opencv-python
import numpy as np   # pip install numpy

def image_colorfulness(image):
    """
    计算图像色彩丰富度:
    Hasler & Süsstrunk (2003) 定义的公式
    """
    (B, G, R) = cv2.split(image.astype("float"))  # cv2.imread 返回 BGR 格式 :contentReference[oaicite:2]{index=2}
    rg = np.abs(R - G)
    yb = np.abs(0.5 * (R + G) - B)
    rbMean, rbStd = np.mean(rg), np.std(rg)
    ybMean, ybStd = np.mean(yb), np.std(yb)
    return np.sqrt(rbStd**2 + ybStd**2) + 0.3 * np.sqrt(rbMean**2 + ybMean**2)

def main():
    parser = argparse.ArgumentParser(
        description="评估抠图前后图像色彩丰富度差值，并据 threshold 判定是否通过"
    )
    parser.add_argument('orig', help="原始图像路径 (支持 .jpg/.png)")
    parser.add_argument('pred', help="抠图结果图像路径 (支持 .png)")
    parser.add_argument(
        '--colorfulness-diff-thresh', type=float, default=20.0,
        help="色彩丰富度差值阈值：pred - orig ≥ thresh 时判定通过"
    )
    args = parser.parse_args()  # 解析命令行参数 :contentReference[oaicite:3]{index=3}

    # 加载图像
    orig = cv2.imread(args.orig, cv2.IMREAD_UNCHANGED)
    pred = cv2.imread(args.pred, cv2.IMREAD_UNCHANGED)
    if orig is None:
        sys.exit(f"错误：无法加载原图 {args.orig}")
    if pred is None:
        sys.exit(f"错误：无法加载结果图 {args.pred}")

    # 计算色彩丰富度
    cf_orig = image_colorfulness(orig)
    cf_pred = image_colorfulness(pred)
    diff = cf_pred - cf_orig

    # 输出详细结果
    print(f"原图 Colorfulness:       {cf_orig:.2f}")
    print(f"抠图后 Colorfulness:     {cf_pred:.2f}")
    print(f"色彩丰富度差值 (pred - orig): {diff:.2f}")

    # 判定
    if diff >= args.colorfulness_diff_thresh:
        print("最终判定：满足要求")
    else:
        print("最终判定：不满足要求")

if __name__ == "__main__":
    main()