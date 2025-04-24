# Prompt for Speech Denoise Task

**任务目标:** 编写一个 Python 脚本，对带有噪声的音频文件 (`./input/noisy_audio.wav`) 进行降噪处理，并将处理后的干净音频保存为 `./output/denoised_audio.wav`。

**核心前提:**
1.  **选择降噪方法:** 
    *   需要选择一种有效的语音降噪技术。
    *   **方法:** 必须使用基于深度学习的预训练模型，例如 `SpeechBrain` 库或 `torchaudio.pipelines` 中提供的模型。
2.  **理解所选库:** 需要查阅所选库（如 `SpeechBrain` 或 `torchaudio`）的文档，了解如何加载降噪模型、处理音频以及保存结果。
3.  **强制使用指定库/方法:** 必须使用任务指定的基于深度学习的库 (如 `SpeechBrain`, `torchaudio`) 进行降噪。如果无法使用这些库或其模型，则应停止任务，而不是尝试实现其他方法（如谱减法）。

**通用环境配置方法论:**
1.  **确认工作目录:** 确保在正确的项目根目录下执行所有命令。
2.  **检查代码库/安装库:** 确认任务选用的库 (`SpeechBrain`, `torchaudio` 等) 已经安装到当前 Python 环境中。
3.  **依赖安装:**
    *   检查所选库的文档，确认所有依赖项已安装。
    *   强烈建议创建并激活一个独立的虚拟环境 (使用 `conda` 或 `python -m venv`) 来安装依赖。
    *   确保主要框架 (PyTorch) 版本与所选库兼容。
4.  **模型下载:**
    *   库通常会在首次使用预训练模型时自动下载。确保网络连接正常，且有权限写入缓存目录。
    *   如果需要手动下载，请遵循文档指示。
5.  **验证安装:** (可选但推荐) 运行库官方文档中的简单示例代码，验证库是否安装成功且模型能正常加载。

**脚本实现要求:**
1.  **功能:**
    *   根据所选库，加载合适的预训练降噪模型。
    *   读取输入含噪音频文件 (`./input/noisy_audio.wav`)。
    *   应用降噪处理。
    *   将降噪后的音频保存到输出文件 (`./output/denoised_audio.wav`)。
2.  **输入/输出:**
    *   **固定输入文件:** 脚本应直接处理 `./input/noisy_audio.wav` 文件。
    *   **固定输出文件:** 处理结果应保存在 `./output/denoised_audio.wav`。脚本需要确保在保存前 `./output/` 目录存在（如果不存在则创建）。
    *   **(可选命令行参数):** 良好的实践是让脚本能通过命令行参数接收输入和输出文件路径。例如: `python your_script.py --input_wav ./input/noisy_audio.wav --output_wav ./output/denoised_audio.wav`
3.  **依赖与环境:**
    *   脚本应包含所有必要的 `import` 语句。
    *   确保运行脚本的环境已安装所需的库 (如 `speechbrain`, `torch`, `torchaudio`, `numpy`, `soundfile` 等)，且环境配置正确。
4.  **错误处理:**
    *   加入基本的错误处理，如文件未找到、模型加载失败等。
5.  **代码风格:**
    *   编写清晰、注释良好的 Python 代码。

**验证:**
*   脚本执行完毕后，`./output/denoised_audio.wav` 文件应包含降噪后的音频。
*   (注意：该任务目录下的 `test_script.py` 可能用于评估生成结果的信噪比等指标，请了解其用途，但不要修改它。)

**文件路径约定:**
-   **输入含噪音频:** `./input/noisy_audio.wav`
-   **输出降噪音频:** `./output/denoised_audio.wav`

请根据以上要求编写 Python 脚本。 