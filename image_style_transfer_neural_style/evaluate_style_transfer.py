#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import cv2
import numpy as np
import torch
from skimage.metrics import structural_similarity as ssim
from pytorch_fid import fid_score

def calculate_average_ssim(reference_input, generated_output):
    """计算单张图像的SSIM值"""
    try:
        ref_img = cv2.imread(reference_input)
        gen_img = cv2.imread(generated_output)

        if ref_img is None or gen_img is None:
            print(f"⚠️ 无法读取图像：{reference_input} 或 {generated_output}")
            return None

        # 确保两张图像尺寸相同
        if ref_img.shape != gen_img.shape:
            print(f"⚠️ 图像尺寸不一致：ref={ref_img.shape}, gen={gen_img.shape}")
            # 调整生成图像尺寸以匹配参考图像
            gen_img = cv2.resize(gen_img, (ref_img.shape[1], ref_img.shape[0]))

        # 转换为灰度图像
        ref_gray = cv2.cvtColor(ref_img, cv2.COLOR_BGR2GRAY)
        gen_gray = cv2.cvtColor(gen_img, cv2.COLOR_BGR2GRAY)

        # 计算SSIM
        score, _ = ssim(ref_gray, gen_gray, full=True)
        return score
    except Exception as e:
        print(f"计算SSIM时出错: {e}")
        return None

def prepare_folder_for_fid(single_image_path, temp_dir):
    """为单图片准备临时目录用于FID计算"""
    if os.path.exists(temp_dir):
        os.system(f"rm -rf {temp_dir}")
    os.makedirs(temp_dir, exist_ok=True)
    
    img_name = os.path.basename(single_image_path)
    dst_path = os.path.join(temp_dir, img_name)
    os.system(f"cp {single_image_path} {dst_path}")
    return temp_dir

def evaluate_fid_single_images(reference_input, generated_output, device='cuda'):
    """使用FID评估单个图像对的风格差异"""
    # 为单张图像创建临时目录
    temp_ref_dir = f"/tmp/ref_fid_{os.getpid()}"
    temp_gen_dir = f"/tmp/gen_fid_{os.getpid()}"
    
    try:
        # 准备临时目录
        ref_dir = prepare_folder_for_fid(reference_input, temp_ref_dir)
        gen_dir = prepare_folder_for_fid(generated_output, temp_gen_dir)
        
        # 计算FID
        fid_value = fid_score.calculate_fid_given_paths(
            [ref_dir, gen_dir],
            batch_size=1,
            device=device,
            dims=2048
        )
        return fid_value
    except Exception as e:
        print(f"计算FID时出错: {e}")
        return None
    finally:
        # 清理临时目录
        if os.path.exists(temp_ref_dir):
            os.system(f"rm -rf {temp_ref_dir}")
        if os.path.exists(temp_gen_dir):
            os.system(f"rm -rf {temp_gen_dir}")

def evaluate_style_transfer_single(reference_input, generated_output):
    """评估单张图像的风格迁移效果"""
    if not os.path.isfile(reference_input) or not os.path.isfile(generated_output):
        print(f"❌ 输入文件不存在: {reference_input} 或 {generated_output}")
        return False

    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(f"使用设备: {device}")

    print("🔍 正在评估 SSIM...")
    ssim_value = calculate_average_ssim(reference_input, generated_output)
    if ssim_value is None:
        print("❌ SSIM 计算失败")
        return False
    print(f"✅ SSIM: {ssim_value:.4f}")

    print("🔍 正在评估 FID...")
    fid_value = evaluate_fid_single_images(reference_input, generated_output, device=device)
    if fid_value is None:
        print("❌ FID 计算失败")
        return False
    print(f"✅ FID: {fid_value:.2f}")

    print("\n🎯 评估结果:")
    passed_ssim = ssim_value >= 0.65
    passed_fid = fid_value <= 45.0

    if passed_ssim:
        print("✔ SSIM ≥ 0.65 ✅")
    else:
        print("❌ SSIM 不达标 (< 0.65)")

    if passed_fid:
        print("✔ FID ≤ 45.0 ✅")
    else:
        print("❌ FID 超出阈值 (> 45.0)")

    if passed_ssim and passed_fid:
        print("\n🎉 任务完成！生成图像满足风格迁移标准。")
        return True
    else:
        print("\n⚠️ 任务未完成！生成图像不满足评估标准。")
        return False

def evaluate_style_transfer_folders(reference_dir, generated_dir):
    """评估文件夹中所有图像的风格迁移效果"""
    if not os.path.isdir(reference_dir) or not os.path.isdir(generated_dir):
        print(f"❌ 目录不存在: {reference_dir} 或 {generated_dir}")
        return False

    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(f"使用设备: {device}")

    # 计算文件夹中所有图像的SSIM
    print("🔍 正在评估 SSIM...")
    scores = []
    filenames = sorted(os.listdir(reference_dir))

    for name in filenames:
        ref_path = os.path.join(reference_dir, name)
        gen_path = os.path.join(generated_dir, name)
        
        if not os.path.isfile(ref_path) or not os.path.isfile(gen_path):
            continue
            
        try:
            ref_img = cv2.imread(ref_path)
            gen_img = cv2.imread(gen_path)

            if ref_img is None or gen_img is None:
                print(f"⚠️ 无法读取图像：{name}")
                continue
                
            if ref_img.shape != gen_img.shape:
                print(f"⚠️ 图像尺寸不一致：{name}")
                gen_img = cv2.resize(gen_img, (ref_img.shape[1], ref_img.shape[0]))

            ref_gray = cv2.cvtColor(ref_img, cv2.COLOR_BGR2GRAY)
            gen_gray = cv2.cvtColor(gen_img, cv2.COLOR_BGR2GRAY)

            score, _ = ssim(ref_gray, gen_gray, full=True)
            scores.append(score)
            print(f"  - {name}: SSIM = {score:.4f}")
        except Exception as e:
            print(f"处理图像 {name} 时出错: {e}")

    if not scores:
        print("❌ 没有有效的图像对来计算 SSIM")
        return False
        
    avg_ssim = np.mean(scores)
    print(f"✅ 平均 SSIM: {avg_ssim:.4f}")

    # 计算FID
    print("🔍 正在评估 FID...")
    try:
        fid_val = fid_score.calculate_fid_given_paths(
            [reference_dir, generated_dir],
            batch_size=50,
            device=device,
            dims=2048
        )
        print(f"✅ FID: {fid_val:.2f}")
    except Exception as e:
        print(f"计算 FID 时出错: {e}")
        return False

    # 评估结果
    print("\n🎯 评估结果:")
    passed_ssim = avg_ssim >= 0.65
    passed_fid = fid_val <= 45.0

    if passed_ssim:
        print("✔ SSIM ≥ 0.65 ✅")
    else:
        print("❌ SSIM 不达标 (< 0.65)")

    if passed_fid:
        print("✔ FID ≤ 45.0 ✅")
    else:
        print("❌ FID 超出阈值 (> 45.0)")

    if passed_ssim and passed_fid:
        print("\n🎉 任务完成！生成图像满足风格迁移标准。")
        return True
    else:
        print("\n⚠️ 任务未完成！生成图像不满足评估标准。")
        return False

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="评估风格迁移图像是否达标")
    parser.add_argument('--reference_dir', type=str, help='原始图像文件夹')
    parser.add_argument('--generated_dir', type=str, help='生成图像文件夹')
    parser.add_argument('--reference_input', type=str, help='单个原始图像路径')
    parser.add_argument('--generated_output', type=str, help='单个生成图像路径')
    parser.add_argument('--threshold', type=float, default=0.65, help='SSIM阈值')
    parser.add_argument('--fid_threshold', type=float, default=45.0, help='FID阈值')
    args = parser.parse_args()

    success = False
    # 检查是文件夹模式还是单文件模式
    if args.reference_dir and args.generated_dir:
        success = evaluate_style_transfer_folders(args.reference_dir, args.generated_dir)
    elif args.reference_input and args.generated_output:
        success = evaluate_style_transfer_single(args.reference_input, args.generated_output)
    else:
        print("❌ 请提供有效的参数: 要么使用 --reference_dir 和 --generated_dir 指定文件夹，要么使用 --reference_input 和 --generated_output 指定单个文件")
        sys.exit(1)
    
    # 根据评估结果设置退出码
    sys.exit(0 if success else 1) 