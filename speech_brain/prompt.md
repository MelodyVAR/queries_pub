# Prompt for SpeechBrain Speaker Separation and Denoising Task

Please write a Python script using the SpeechBrain library to perform speaker separation and denoising on the mixed audio file `input/mixed_input.wav`.

Requirements:
- Input: The script should specifically process the file located at `input/mixed_input.wav`.
- Output: Save the separated and denoised audio streams for each speaker into separate `.wav` files within the `pred_audio/` directory. Ensure this directory is created if it doesn't exist.
- Method: Utilize a pre-trained SpeechBrain model suitable for joint separation and denoising (e.g., SepFormer + enhancement model if available, or a specific separation model followed by a denoiser).
- The script should accept the input file path (`input/mixed_input.wav`) and output directory path (`pred_audio/`) as command-line arguments, although the prompt specifies the exact paths to use for this task.
- Ensure the script handles potential errors, such as file not found or issues during model loading/inference.
- The reference audio files for evaluation are located in `ref_audio/`. 