import os
import cv2
import numpy as np
from skimage.metrics import peak_signal_noise_ratio as psnr
from skimage.metrics import structural_similarity as ssim


def evaluate_image_pair(gt_path, sr_path):
    gt = cv2.imread(gt_path)
    sr = cv2.imread(sr_path)

    if gt is None or sr is None:
        raise ValueError(f"读取图像失败：{gt_path} 或 {sr_path}")

    if gt.shape != sr.shape:
        sr = cv2.resize(sr, (gt.shape[1], gt.shape[0]))

    gt_y = cv2.cvtColor(gt, cv2.COLOR_BGR2GRAY)
    sr_y = cv2.cvtColor(sr, cv2.COLOR_BGR2GRAY)

    psnr_score = psnr(gt_y, sr_y, data_range=255)
    ssim_score = ssim(gt_y, sr_y, data_range=255)

    return psnr_score, ssim_score


def evaluate_folder(gt_dir, sr_dir):
    gt_files = sorted(os.listdir(gt_dir))
    psnr_list = []
    ssim_list = []

    for fname in gt_files:
        gt_path = os.path.join(gt_dir, fname)
        sr_path = os.path.join(sr_dir, fname)

        if not os.path.exists(sr_path):
            print(f"⚠️ 未找到对应高清化图像：{fname}")
            continue

        try:
            psnr_val, ssim_val = evaluate_image_pair(gt_path, sr_path)
            psnr_list.append(psnr_val)
            ssim_list.append(ssim_val)
            print(f"[{fname}] PSNR: {psnr_val:.2f}, SSIM: {ssim_val:.4f}")
        except Exception as e:
            print(f"❌ 处理失败 {fname}: {str(e)}")

    if not psnr_list or not ssim_list:
        raise RuntimeError("❌ 无可评估图像对，检查路径或图像内容。")

    avg_psnr = np.mean(psnr_list)
    avg_ssim = np.mean(ssim_list)

    return avg_psnr, avg_ssim


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="超分图像质量评估 (PSNR & SSIM)")
    parser.add_argument('--gt_dir', type=str, required=True, help='原始高分辨率图像文件夹')
    parser.add_argument('--sr_dir', type=str, required=True, help='超分生成图像文件夹')
    args = parser.parse_args()

    print("🚀 开始评估图像高清化结果...")
    psnr_val, ssim_val = evaluate_folder(args.gt_dir, args.sr_dir)

    print("\n📊 评估结果:")
    print(f"✅ 平均 PSNR: {psnr_val:.2f}")
    print(f"✅ 平均 SSIM: {ssim_val:.4f}")

    print("\n🎯 达标检查:")
    if psnr_val >= 28.0:
        print("✔ PSNR ≥ 28.0 ✅")
    else:
        print("❌ PSNR 不达标")

    if ssim_val >= 0.90:
        print("✔ SSIM ≥ 0.90 ✅")
    else:
        print("❌ SSIM 不达标")

    if psnr_val >= 28.0 and ssim_val >= 0.90:
        print("\n🎉 任务完成：高清化图像符合质量标准！")
    else:
        print("\n⚠️ 任务未完成：请检查输出图像质量。")