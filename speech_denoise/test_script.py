import os
import numpy as np
import argparse
import soundfile as sf
from pesq import pesq
from scipy.signal import resample

def calculate_snr(clean, noisy):
    noise = clean - noisy
    return 10 * np.log10(np.mean(clean ** 2) / (np.mean(noise ** 2) + 1e-8))

def calculate_pesq(clean, enhanced, fs):
    # PESQ 要求为 8k 或 16k 采样率
    if fs not in [8000, 16000]:
        raise ValueError("PESQ 仅支持 8000 或 16000 Hz 采样率")
    return pesq(fs, clean, enhanced, 'wb')

def load_audio(path, target_fs=16000):
    audio, fs = sf.read(path)
    if audio.ndim > 1:
        audio = np.mean(audio, axis=1)  # 转单通道
    if fs != target_fs:
        audio = resample(audio, int(len(audio) * target_fs / fs))
    return audio, target_fs

def evaluate(clean_dir, enhanced_dir, pesq_threshold=2.8, snr_threshold=10.0, sample_rate=16000):
    results = []
    all_pass = True

    for fname in os.listdir(clean_dir):
        if not fname.endswith(".wav"):
            continue

        clean_path = os.path.join(clean_dir, fname)
        enhanced_path = os.path.join(enhanced_dir, fname)

        if not os.path.exists(enhanced_path):
            print(f"❌ 缺失文件：{enhanced_path}")
            all_pass = False
            continue

        clean, fs = load_audio(clean_path, sample_rate)
        enhanced, _ = load_audio(enhanced_path, sample_rate)

        min_len = min(len(clean), len(enhanced))
        clean, enhanced = clean[:min_len], enhanced[:min_len]

        try:
            pesq_score = calculate_pesq(clean, enhanced, fs)
        except Exception as e:
            print(f"⚠️ PESQ计算失败：{fname}，原因：{e}")
            pesq_score = -1.0

        snr_score = calculate_snr(clean, enhanced)
        passed = pesq_score >= pesq_threshold and snr_score >= snr_threshold
        all_pass = all_pass and passed
        results.append((fname, pesq_score, snr_score, passed))

    print("\n=== 降噪语音评估报告 ===")
    for fname, pesq_score, snr_score, passed in results:
        print(f"{fname}:\tPESQ={pesq_score:.2f}\tSNR={snr_score:.2f} dB\t{'✅ 通过' if passed else '❌ 不通过'}")

    if all_pass:
        print("\n🎉 所有语音通过评估（PESQ ≥ {:.1f}, SNR ≥ {:.1f} dB）".format(pesq_threshold, snr_threshold))
    else:
        print("\n❌ 存在语音不满足指标，测试未通过")

def parse_args():
    parser = argparse.ArgumentParser(description="语音降噪质量评估脚本（支持SNR与PESQ）")
    parser.add_argument('--clean_dir', type=str, required=True, help='参考干净语音的目录')
    parser.add_argument('--enhanced_dir', type=str, required=True, help='降噪后语音的目录')
    parser.add_argument('--pesq_threshold', type=float, default=2.8, help='PESQ阈值，默认2.8')
    parser.add_argument('--snr_threshold', type=float, default=10.0, help='SNR阈值，默认10 dB')
    parser.add_argument('--sample_rate', type=int, default=16000, help='统一采样率（推荐16000）')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    evaluate(args.clean_dir, args.enhanced_dir, args.pesq_threshold, args.snr_threshold, args.sample_rate)