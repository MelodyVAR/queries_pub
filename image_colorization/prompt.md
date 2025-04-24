**任务目标:** 利用 `DeOldify` 代码库，为黑白图像 (`./input/bw_image.jpg`) 进行上色，并将结果保存为彩色图像 (`./output/bw_image_colorized.jpg`)。

**核心前提:**
1.  **阅读文档:** 在开始任何操作前，必须仔细阅读 `DeOldify/README.md`。充分理解其工作原理、命令行参数、依赖需求、模型下载和运行示例。
2.  **禁止修改评估脚本:** 绝对不允许修改 `colorfulness_evaluator.py` 文件，该文件仅用于最终结果的验证。
3.  **强制使用指定库:** 必须使用任务指定的 `DeOldify` 库。如果因任何原因无法使用该库（例如安装困难、模型下载失败、运行错误等），则应停止任务，而不是尝试使用其他库或方法。

**通用环境配置方法论:**
1.  **确认工作目录:** 确保在正确的项目根目录下执行所有命令。
2.  **检查代码库:** 确认任务指定的代码库 (`DeOldify`) 已经克隆或存在于预期的相对路径下。
3.  **依赖安装:**
    *   仔细阅读代码库的 `README.md` 或 `requirements.txt` (或 `pyproject.toml` 等) 文件，确定所有必需的依赖项。
    *   强烈建议创建并激活一个独立的虚拟环境 (使用 `conda` 或 `python -m venv`) 来安装依赖，以避免与其他项目冲突。
    *   使用指定的包管理器 (通常是 `pip` 或 `conda`) 安装依赖。例如: `pip install -r requirements.txt` 或根据文档进行安装。
    *   特别注意 Python 版本、主要框架 (`fastai`, `torch`) 的版本以及其他特殊库的安装要求和步骤。
4.  **模型下载:**
    *   根据代码库文档 (`DeOldify/README.md`) 的指示，下载所需的预训练模型文件 (通常是 `.pkl` 文件)。
    *   确保将下载的模型文件放置在代码库预期的目录结构中 (通常在 `DeOldify/models/` 下)。
5.  **验证安装:** (可选但推荐) 如果代码库提供了测试脚本或简单的运行示例，尝试运行它们以初步验证环境、依赖和模型是否配置正确。

**执行流程:**
1.  **环境设置:**
    *   确认你处于正确的项目工作目录。
    *   检查 `DeOldify` 代码库是否存在。
    *   根据 `DeOldify/README.md` 和通用环境配置方法论完成依赖安装和模型下载。
2.  **执行图像上色:**
    *   参考 `DeOldify/README.md` 或其示例代码，找到执行图像上色的命令或 Python 脚本调用方法。
    *   构造并执行命令或脚本，指定输入图像路径为 `./input/bw_image.jpg`。
    *   确保将输出结果指定保存到 `./output/bw_image_colorized.jpg`。注意 `DeOldify` 可能有特定的参数来控制输出路径和文件名。
    *   注意 `DeOldify` 可能提供不同的模型或渲染因子 (`render_factor`) 参数，根据需要进行调整（如果文档中有说明），以获得最佳效果。
3.  **结果验证:**
    *   确认 `./output/bw_image_colorized.jpg` 文件已成功生成。
    *   运行以下命令来评估生成结果的色彩丰富度（注意：这只是验证命令）：
        ```bash
        python colorfulness_evaluator.py ./output/bw_image_colorized.jpg --threshold 35
        ```
    *   检查评估脚本的输出，确保满足阈值要求。

**文件路径约定:**
-   **输入黑白图像:** `./input/bw_image.jpg`
-   **输出彩色图像:** `./output/bw_image_colorized.jpg`
-   **代码库:** `./DeOldify/`

请严格按照此流程执行任务。