import os, sys, argparse
import cv2
import torch
import lpips
from torchvision import transforms
import torch.nn.functional as F

def check_file(path, exts=('.png','.jpg','.jpeg', '.webp')):
    if not os.path.isfile(path):
        sys.exit(f"错误：文件不存在 -> {path}")
    if not path.lower().endswith(exts):
        sys.exit(f"错误：不支持的格式 -> {path}")

def load_tensor(path):
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    if img is None:
        sys.exit(f"无法读取图像：{path}")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    t = transforms.ToTensor()(img) * 2 - 1
    return t.unsqueeze(0)

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument('orig', help="原始图像路径")
    p.add_argument('stylized', help="动漫化图像路径")
    p.add_argument('--lpips-thresh', type=float, default=0.20,
                   help="LPIPS 距离阈值 (≥ 阈值 则通过)")
    args = p.parse_args()

    # 文件检测
    check_file(args.orig)
    check_file(args.stylized)

    # 载入并预处理
    img0 = load_tensor(args.orig)
    img1 = load_tensor(args.stylized)

    # 统一尺寸
    _, _, h0, w0 = img0.shape
    _, _, h1, w1 = img1.shape
    new_h, new_w = min(h0, h1), min(w0, w1)
    if (h0, w0) != (new_h, new_w):
        img0 = F.interpolate(img0, size=(new_h, new_w),
                             mode='bilinear', align_corners=False)
    if (h1, w1) != (new_h, new_w):
        img1 = F.interpolate(img1, size=(new_h, new_w),
                             mode='bilinear', align_corners=False)

    # 计算 LPIPS
    loss_fn = lpips.LPIPS(net='vgg').to(torch.device('cpu'))
    with torch.no_grad():
        dist = loss_fn(img0, img1).item()

    # 输出 & 判定
    print(f"LPIPS 距离: {dist:.4f}")
    print("最终判定：",
          "满足要求" if dist >= args.lpips_thresh else "不满足要求")