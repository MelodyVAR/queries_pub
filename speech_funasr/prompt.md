# Prompt for FunASR Speaker Diarization and Transcription Task

**任务目标:** 编写一个 Python 脚本，使用 `FunASR` 库对包含多人对话的音频文件 (`./input/merged_audio.wav`) 进行说话人日志分割 (Speaker Diarization) 和自动语音识别 (ASR)。

**核心前提:**
1.  **理解 FunASR:** 需要了解 `FunASR` 库，特别是其提供的用于说话人日志分割和语音识别的预训练模型和推理 Pipeline。查阅 `FunASR` 的官方文档和示例至关重要。
2.  **模型选择:** 选择 `FunASR` 中适合进行说话人日志分割和 ASR 联合处理的模型或 Pipeline。`FunASR` 可能提供集成了这两项功能的 Pipeline。
3.  **强制使用指定库:** 必须使用任务指定的 `FunASR` 库。如果因任何原因无法使用该库（例如安装困难、模型下载失败、运行错误等），则应停止任务，而不是尝试使用其他库或方法编写脚本。

**通用环境配置方法论:**
1.  **确认工作目录:** 确保在正确的项目根目录下执行所有命令。
2.  **检查代码库/安装库:** 确认任务指定的库 (`FunASR`) 已经通过 `pip install funasr` 或根据其文档指引安装到当前 Python 环境中。
3.  **依赖安装:**
    *   `FunASR` 的安装通常会处理其核心依赖。但仍需检查其文档，确认是否有额外的依赖项（特别是 `onnxruntime` 相关）。
    *   强烈建议创建并激活一个独立的虚拟环境 (使用 `conda` 或 `python -m venv`) 来安装依赖。
    *   确保主要框架 (PyTorch) 版本与 `FunASR` 兼容。
4.  **模型下载:**
    *   `FunASR` 通常会在首次使用模型时自动下载。确保网络连接正常，且有权限写入缓存目录 (通常在 `~/.cache/modelscope/`)
    *   如果需要手动下载或使用特定模型，请遵循文档指示。
5.  **验证安装:** (可选但推荐) 运行 `FunASR` 官方文档提供的简单推理示例，验证库和模型是否正常工作。

**脚本实现要求:**
1.  **功能:**
    *   加载所需的 `FunASR` 模型/Pipeline (通常通过 `AutoModel` 或 pipeline 接口)。
    *   读取输入音频文件 (`./input/merged_audio.wav`)。
    *   执行说话人日志分割和 ASR。
    *   将所有转录结果整合成最终的文本输出。
2.  **输入/输出:**
    *   **固定输入文件:** 脚本必须处理 `./input/merged_audio.wav`。
    *   **固定输出文件:** 将最终的转录结果（需按评估脚本要求的格式）保存到当前目录下的 `system_transcription.txt` 文件中。确保脚本能正确生成此文件。
    *   **输出格式:** 请仔细检查评估脚本 (`evaluate.py` 或 `test_script.py`) 对 `system_transcription.txt` 文件格式的具体要求（例如，是否需要包含时间戳、说话人标签，以及标签的格式等），并确保脚本输出符合该格式。
3.  **依赖与环境:**
    *   脚本应包含所有必要的 `import` 语句 (如 `funasr` 相关的模块)。
    *   确保运行脚本的环境已正确安装 `FunASR` 及其所有依赖项，且环境配置正确。
4.  **错误处理:**
    *   加入基本的错误处理逻辑。
5.  **代码风格:**
    *   编写清晰、注释良好的 Python 代码。

**验证:**
*   脚本执行完毕后，应在当前目录生成 `system_transcription.txt` 文件。
*   (注意：该任务目录下的 `test_script.py` 或 `evaluate.py` 用于评估生成的转录文本的准确率，例如计算词错误率 (WER)。请了解其评估方式，确保输出格式正确，但不要修改评估脚本本身。)

**文件路径约定:**
-   **输入混合音频:** `./input/merged_audio.wav`
-   **输出转录文件:** `./system_transcription.txt`
-   **参考真值 (用于评估):** `./ground_truth.txt` (如果存在)
-   **库:** `FunASR` (应安装在环境中)

请根据以上要求编写 Python 脚本。 