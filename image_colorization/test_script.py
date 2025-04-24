#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import argparse
import os
import sys

def calculate_image_colorfulness(image: np.ndarray) -> float:
    """
    计算图像的色彩丰富度 (colorfulness)。
    参数：
        image (np.ndarray): BGR格式图像
    返回：
        float: 色彩丰富度指标 C
    """
    if image is None:
        # 在实际脚本中，错误应该导致非零退出，但由调用者处理IO错误
        # 这里可以返回一个特殊值或抛出异常，让主处理逻辑捕获
        raise ValueError("输入图像为空或无法读取。")

    (B, G, R) = cv2.split(image.astype("float"))
    # Handle potential division by zero or invalid values if needed
    # For simplicity, assume valid image data for now
    rg = np.absolute(R - G)
    yb = np.absolute(0.5 * (R + G) - B)

    (rbMean, rbStd) = (np.mean(rg), np.std(rg))
    (ybMean, ybStd) = (np.mean(yb), np.std(yb))

    # Avoid NaN from sqrt(negative) if std deviations are zero (e.g., pure gray image)
    rbStd = max(rbStd, 1e-6)
    ybStd = max(ybStd, 1e-6)

    stdRoot = np.sqrt((rbStd ** 2) + (ybStd ** 2))
    meanRoot = np.sqrt((rbMean ** 2) + (ybMean ** 2))

    return stdRoot + (0.3 * meanRoot)


def evaluate_single_image(image_path):
    image = cv2.imread(image_path)
    try:
        colorfulness = calculate_image_colorfulness(image)
        label = "丰富 ✅" if colorfulness > 35 else "较单一 ⚠️"
        print(f"[{os.path.basename(image_path)}] 色彩丰富度: {colorfulness:.2f} → {label}")
    except Exception as e:
        print(f"[{os.path.basename(image_path)}] 处理失败: {str(e)}")


def evaluate_folder(folder_path):
    image_files = [
        f for f in os.listdir(folder_path)
        if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.webp'))
    ]
    if not image_files:
        print("❌ 没有找到有效图像文件。")
        return

    for img_file in sorted(image_files):
        full_path = os.path.join(folder_path, img_file)
        evaluate_single_image(full_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="计算图像色彩丰富度并根据阈值返回退出码")
    parser.add_argument('image_path', type=str, help='输入图像文件的路径')
    parser.add_argument('--threshold', type=float, required=True, help='色彩丰富度阈值')
    args = parser.parse_args()

    exit_code = 1 # 默认为失败

    if not os.path.exists(args.image_path):
        # print(f"❌ 错误：图像路径不存在 - {args.image_path}", file=sys.stderr)
        sys.exit(2) # 特定错误码表示文件不存在
    if not os.path.isfile(args.image_path):
        # print(f"❌ 错误：输入路径不是文件 - {args.image_path}", file=sys.stderr)
        sys.exit(3) # 特定错误码表示不是文件

    try:
        image = cv2.imread(args.image_path)
        if image is None:
            # print(f"❌ 错误：无法读取图像文件 - {args.image_path}", file=sys.stderr)
            sys.exit(4) # 特定错误码表示无法读取图像

        colorfulness = calculate_image_colorfulness(image)

        # 核心逻辑：比较并设置退出码
        if colorfulness >= args.threshold:
            exit_code = 0 # 成功
        else:
            exit_code = 1 # 失败 (低于阈值)

    except ValueError as ve:
        # print(f"❌ 错误：计算色彩丰富度时出错 - {ve}", file=sys.stderr)
        sys.exit(5) # 特定错误码表示计算错误
    except Exception as e:
        # print(f"❌ 未知错误: {str(e)}", file=sys.stderr)
        sys.exit(99) # 未知错误

    sys.exit(exit_code) 