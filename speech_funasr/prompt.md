# Prompt for FunASR Speaker Diarization and Transcription Task

Please write a Python script using the FunASR library to perform speaker diarization (separation) and automatic speech recognition (ASR) on the audio file `input/merged_audio.wav`.

Requirements:
- Input: Process the audio file located at `input/merged_audio.wav`.
- Task: Identify the different speakers and transcribe their speech, handling potential overlaps.
- Output: Save the final combined transcription (including speaker information if possible, but formatted as required by the evaluation) into a file named `system_transcription.txt` in the current directory.
- Method: Utilize appropriate FunASR models/pipelines for speaker diarization and transcription.
- The script should be callable and produce the `system_transcription.txt` file.
- Note: The ground truth transcription for evaluation is located at `ground_truth.txt`. 