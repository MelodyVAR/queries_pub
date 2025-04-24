import os
import numpy as np
import argparse
import soundfile as sf
from mir_eval.separation import bss_eval_sources

# 计算 SNR
def calculate_snr(ref, est):
    noise = ref - est
    snr = 10 * np.log10(np.sum(ref ** 2) / np.sum(noise ** 2) + 1e-8)
    return snr

# 计算 SDR
def calculate_sdr(ref, est):
    sdr, _, _, _ = bss_eval_sources(ref[np.newaxis, :], est[np.newaxis, :])
    return sdr[0]

# 读取语音文件
def load_audio(path):
    data, sr = sf.read(path)
    if data.ndim > 1:
        data = np.mean(data, axis=1)  # 转为单通道
    return data

# 执行评估
def evaluate(reference_dir, estimated_dir, snr_threshold=12.0, sdr_threshold=8.0):
    all_pass = True
    results = []

    for filename in os.listdir(reference_dir):
        if not filename.endswith(".wav"):
            continue

        ref_path = os.path.join(reference_dir, filename)
        est_path = os.path.join(estimated_dir, filename)

        if not os.path.exists(est_path):
            print(f"❌ 缺失文件：{est_path}")
            all_pass = False
            continue

        ref = load_audio(ref_path)
        est = load_audio(est_path)

        min_len = min(len(ref), len(est))
        ref, est = ref[:min_len], est[:min_len]

        snr = calculate_snr(ref, est)
        sdr = calculate_sdr(ref, est)

        passed = snr >= snr_threshold and sdr >= sdr_threshold
        all_pass = all_pass and passed

        results.append((filename, snr, sdr, passed))

    # 打印结果
    print("\n=== 语音分离与降噪评估报告 ===")
    for fname, snr, sdr, ok in results:
        print(f"{fname}:\tSNR={snr:.2f} dB\tSDR={sdr:.2f} dB\t{'✅ 通过' if ok else '❌ 不通过'}")

    if all_pass:
        print("\n🎉 所有语音通过评估（SNR ≥ 12 dB 且 SDR ≥ 8 dB）")
    else:
        print("\n❌ 存在语音不满足指标，测试未通过")

# 命令行参数
def parse_args():
    parser = argparse.ArgumentParser(description="语音分离与降噪质量评估脚本")
    parser.add_argument('--reference_dir', type=str, required=True,
                        help='参考纯净语音文件目录（每位说话人分离的GT）')
    parser.add_argument('--estimated_dir', type=str, required=True,
                        help='系统输出的分离语音目录（与GT按文件名对齐）')
    parser.add_argument('--snr_threshold', type=float, default=12.0,
                        help='SNR阈值，默认12 dB')
    parser.add_argument('--sdr_threshold', type=float, default=8.0,
                        help='SDR阈值，默认8 dB')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    evaluate(args.reference_dir, args.estimated_dir, args.snr_threshold, args.sdr_threshold)