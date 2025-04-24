# speech_funasr/test_script.py
import argparse
import subprocess
import sys
import os
from pathlib import Path

def run_command(command: list[str], cwd: str | None = None) -> tuple[int, str, str]:
    """执行子进程命令并返回退出码、stdout 和 stderr"""
    try:
        process = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=False, # Don't raise exception on non-zero exit
            cwd=cwd or Path(__file__).parent, # Run in script's directory by default
            encoding='utf-8',
            errors='ignore' # Ignore decoding errors if any
        )
        # print(f"Running command: {' '.join(command)}")
        # print(f"Stdout:\\n{process.stdout}")
        # print(f"Stderr:\\n{process.stderr}")
        return process.returncode, process.stdout, process.stderr
    except Exception as e:
        print(f"Error running command {' '.join(command)}: {e}", file=sys.stderr)
        return -1, "", str(e) # Indicate execution error

def main():
    parser = argparse.ArgumentParser(description="运行 FunASR 转录并评估结果")
    parser.add_argument('--input_dir', type=str, required=True, help='包含输入音频文件的目录')
    parser.add_argument('--output_dir', type=str, required=True, help='存放转录结果的目录')
    parser.add_argument('--ground_truth_file', type=str, required=True, help='标准答案转录文件路径 (格式: speaker:text)')
    parser.add_argument('--cer_threshold', type=float, default=0.05, help='评估通过的 CER 阈值 (默认: 0.05)')
    # Add arguments for transcribe.py if needed (e.g., model path)
    # parser.add_argument('--model_path', type=str, default='path/to/model', help='FunASR 模型路径')

    args = parser.parse_args()

    script_dir = Path(__file__).parent.resolve()
    transcribe_script = str(script_dir / 'transcribe.py')
    evaluate_script = str(script_dir / 'evaluate.py')
    system_output_file = str(Path(args.output_dir).resolve() / 'transcripts.txt')

    # --- Step 1: Run Transcription ---
    print("--- Running Transcription Step ---")
    transcribe_cmd = [
        sys.executable, # Use the same python interpreter
        transcribe_script,
        '--input_path', str(Path(args.input_dir).resolve()),
        '--output_dir', str(Path(args.output_dir).resolve()),
        # Add other args like '--model_path', args.model_path here if needed
    ]
    transcribe_exit_code, _, transcribe_stderr = run_command(transcribe_cmd, cwd=str(script_dir))

    if transcribe_exit_code != 0:
        print(f"❌ Transcription script failed with exit code {transcribe_exit_code}.", file=sys.stderr)
        print(f"Stderr:\\n{transcribe_stderr}", file=sys.stderr)
        sys.exit(1) # Exit if transcription fails
    else:
        print("✅ Transcription script completed successfully.")


    # --- Step 2: Run Evaluation ---
    print("\n--- Running Evaluation Step ---")
    if not Path(system_output_file).exists():
         print(f"❌ Error: Transcription output file not found: {system_output_file}", file=sys.stderr)
         sys.exit(2) # Specific exit code for missing output file

    evaluate_cmd = [
        sys.executable,
        evaluate_script,
        '--system_output', system_output_file,
        '--ground_truth', str(Path(args.ground_truth_file).resolve()),
        '--cer_threshold', str(args.cer_threshold)
    ]
    evaluate_exit_code, evaluate_stdout, evaluate_stderr = run_command(evaluate_cmd, cwd=str(script_dir))

    # evaluate.py doesn't have a clear exit code logic based on pass/fail yet.
    # We need to parse its output or modify evaluate.py to return a proper exit code.
    # For now, check if the script ran successfully (exit code 0) and look for pass message.
    # A better approach is to modify evaluate.py to exit 0 on pass, 1 on fail.

    if evaluate_exit_code != 0:
        print(f"❌ Evaluation script failed with exit code {evaluate_exit_code}.", file=sys.stderr)
        print(f"Stderr:\\n{evaluate_stderr}", file=sys.stderr)
        sys.exit(3) # Specific exit code for evaluation script error
    else:
        # Parse the output of evaluate.py to determine the final outcome
        # This is brittle; modifying evaluate.py for a clear exit code is better.
        print("\n--- Evaluation Script Output ---")
        print(evaluate_stdout)
        # print(f"Stderr:\\n{evaluate_stderr}") # Usually empty if no errors

        if "测试通过！" in evaluate_stdout:
             print("✅ Evaluation PASSED based on script output.")
             sys.exit(0) # Final success exit code
        elif "测试未通过" in evaluate_stdout:
             print("❌ Evaluation FAILED based on script output.")
             sys.exit(4) # Specific exit code for evaluation failure
        else:
             print("⚠️ Could not determine evaluation pass/fail status from script output.")
             sys.exit(5) # Specific exit code for ambiguous result


if __name__ == '__main__':
    main() 