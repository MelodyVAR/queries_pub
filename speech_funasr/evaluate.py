import os
from difflib import SequenceMatcher
import argparse

def cer(ref, hyp):
    """
    计算字符错误率 CER（Character Error Rate）
    """
    matcher = SequenceMatcher(None, ref, hyp)
    edit_ops = sum(
        [max(triple[2] - triple[1], triple[2] - triple[1]) # This calculation seems wrong, should be sum of ins/del/sub
         for triple in matcher.get_opcodes() if triple[0] != 'equal']
    )
    # Correct calculation: edits = sum(max(i2 - i1, j2 - j1) for op, i1, i2, j1, j2 in matcher.get_opcodes() if op != 'equal')
    # Let's use a simpler way often used for CER:
    s, d, i = 0, 0, 0
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == 'replace':
            s += (i2 - i1)
        elif tag == 'delete':
            d += (i2 - i1)
        elif tag == 'insert':
            i += (j2 - j1)
    
    edit_ops = s + d + i
    return edit_ops / max(len(ref), 1)

def load_transcripts(file_path):
    """
    从文本文件加载说话人转录，格式要求：
    每一行为：speaker_id:transcript
    同一个说话人的多条记录将被合并为一个完整的字符串。
    """
    transcripts = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if ':' not in line:
                    print(f"Skipping invalid line in {file_path}: {line}")
                    continue
                parts = line.split(':', 1)
                if len(parts) == 2:
                    speaker, text = parts
                    speaker = speaker.strip() # Ensure no leading/trailing spaces
                    text = text.strip() # Ensure no leading/trailing spaces
                    if speaker not in transcripts:
                        transcripts[speaker] = []
                    transcripts[speaker].append(text)
                else:
                     print(f"Skipping invalid line format in {file_path}: {line}")
    except FileNotFoundError:
        print(f"Error: File not found {file_path}")
        return None
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None
    
    # 合并每个说话人的所有转录文本
    for speaker in transcripts:
        transcripts[speaker] = " ".join(transcripts[speaker])
    
    return transcripts

def evaluate(system_output_file, ground_truth_file, cer_threshold=0.05):
    """
    主评估函数：对比系统输出与标准答案，逐个说话人计算 CER
    """
    print(f"Loading system output from: {system_output_file}")
    system_trans = load_transcripts(system_output_file)
    print(f"Loading ground truth from: {ground_truth_file}")
    ground_truth = load_transcripts(ground_truth_file)

    if system_trans is None or ground_truth is None:
        print("Evaluation cannot proceed due to file loading errors.")
        return

    total_pass = True
    results = {}
    all_speakers = set(ground_truth.keys()) | set(system_trans.keys())

    if not all_speakers:
        print("No speakers found in either ground truth or system output.")
        return

    # 遍历所有出现过的说话人 (ground truth 和 system output)
    for speaker in all_speakers:
        gt_text = ground_truth.get(speaker, "")
        # Handle potential speaker ID variations (e.g., 'spk1' vs 's1') - simple replacement example
        # A more robust solution might involve mapping based on order or using a dedicated library
        sys_speaker_key = speaker # Assume keys match initially
        if speaker not in system_trans:
            # Try common variations if direct match fails
            alt_speaker_key = speaker.replace('spk', 's') 
            if alt_speaker_key in system_trans:
                sys_speaker_key = alt_speaker_key
            else:
                 alt_speaker_key = speaker.replace('s', 'spk')
                 if alt_speaker_key in system_trans:
                    sys_speaker_key = alt_speaker_key

        sys_text = system_trans.get(sys_speaker_key, "") 
        
        if not gt_text and not sys_text:
             print(f"Speaker {speaker}: Both ground truth and system output are empty. Skipping.")
             continue # Skip if both are empty
        elif not gt_text:
            print(f"Warning: Speaker {speaker} present in system output but not in ground truth.")
            # Calculate CER against empty string - results in 100% CER if sys_text is not empty
            score = cer("", sys_text) 
        elif not sys_text:
            print(f"Warning: Speaker {speaker} present in ground truth but not in system output.")
            # Calculate CER against empty string - results in 100% CER
            score = cer(gt_text, "")
        else:
            score = cer(gt_text, sys_text)
            
        results[speaker] = score
        if score > cer_threshold:
            total_pass = False

    # 输出结果
    print("\n=== 评估结果 ===")
    if not results:
         print("No speakers were evaluated.")
    else:
        for speaker, score in results.items():
            pass_status = score <= cer_threshold
            print(f"说话人: {speaker}\tCER: {score:.2%}\t{'✅ 通过' if pass_status else '❌ 不通过'}")

    print("\n--- 测试总结 ---")
    if total_pass:
        print(f"🎉 所有评估的说话人 CER ≤ {cer_threshold:.2%}，测试通过！")
    else:
        print(f"❌ 存在说话人 CER > {cer_threshold:.2%} 或文件处理错误，测试未通过。")

def parse_args():
    parser = argparse.ArgumentParser(description="评估ASR系统对不同说话人的转录准确率（基于CER）")
    parser.add_argument('--system_output', type=str, required=True,
                        help='系统输出的转录文件路径（每行格式为 speaker_id:transcript）')
    parser.add_argument('--ground_truth', type=str, required=True,
                        help='标准答案的转录文件路径（每行格式为 speaker_id:transcript）')
    parser.add_argument('--cer_threshold', type=float, default=0.05,
                        help=f'CER 阈值，默认值为 0.05 (5%)')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    evaluate(args.system_output, args.ground_truth, cer_threshold=args.cer_threshold) 