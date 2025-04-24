# Prompt for Speech Denoise Task

Please write a Python script to denoise the audio file located at `input/noisy_audio.wav`.

Requirements:
- Input: The script must process the specific file `input/noisy_audio.wav`.
- Output: Save the denoised audio to `output/denoised_audio.wav`. Ensure the `output/` directory is created if it doesn't exist.
- Method: You can use classic methods like spectral subtraction or leverage a pre-trained deep learning model if available (e.g., from libraries like `speechbrain` or `torchaudio`).
- The script should be callable from the command line, accepting the input file path (`input/noisy_audio.wav`) and output file path (`output/denoised_audio.wav`) as arguments, although the prompt specifies the exact paths for this task.
- Handle potential errors gracefully (e.g., file not found). 