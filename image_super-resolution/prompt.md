# Prompt

**任务目标:** 利用 `image-super-resolution` 代码库，将低分辨率图像 (`./input/low_res_image.jpg`) 提升为高分辨率图像，并将结果保存为 `./output/high_res_image.png`。

**核心前提:**
1.  **阅读文档:** 在开始任何操作前，必须仔细阅读 `image-super-resolution` 代码库的 `README.md` 或相关文档。充分理解其工作原理、支持的超分辨率模型 (如 EDSR, SRGAN 等)、命令行用法、Python API、依赖需求、模型下载和运行示例。
2.  **理解验证脚本:** `test_script.py` 用于最终结果的验证 (例如，检查输出图像的分辨率、文件是否存在，或计算 PSNR/SSIM 等指标)，请勿修改其核心逻辑。
3.  **强制使用指定库:** 必须使用任务指定的 `image-super-resolution` 库。如果因任何原因无法使用该库（例如安装困难、模型下载失败、运行错误等），则应停止任务，而不是尝试使用其他库或方法。

**通用环境配置方法论:**
1.  **确认工作目录:** 确保在正确的项目根目录下执行所有命令。
2.  **检查代码库:** 确认任务指定的代码库 (`image-super-resolution`) 已经克隆或存在于预期的相对路径下。
3.  **依赖安装:**
    *   仔细阅读代码库的 `README.md` 或 `requirements.txt` (或 `pyproject.toml` 等) 文件，确定所有必需的依赖项。
    *   强烈建议创建并激活一个独立的虚拟环境 (使用 `conda` 或 `python -m venv`) 来安装依赖。
    *   使用指定的包管理器 (通常是 `pip` 或 `conda`) 安装依赖。例如: `pip install -r requirements.txt` 或根据文档进行安装。
    *   特别注意 Python 版本、主要框架 (PyTorch, TensorFlow) 的版本以及其他特殊库的安装要求和步骤。
4.  **模型下载:**
    *   根据代码库文档 (`image-super-resolution/README.md`) 的指示，下载所需的预训练超分辨率模型。
    *   确保将下载的模型文件放置在代码库预期的目录结构中 (例如 `models/`, `weights/` 等)。
5.  **验证安装:** (可选但推荐) 如果代码库提供了测试脚本或简单的运行示例，尝试运行它们以初步验证环境、依赖和模型是否配置正确。

**执行流程:**
1.  **环境设置:**
    *   确认你处于正确的项目工作目录。
    *   检查 `image-super-resolution` 代码库是否存在。
    *   根据文档和通用环境配置方法论完成依赖安装和模型下载。
2.  **执行图像超分辨率:**
    *   根据 `image-super-resolution` 的文档，确定是通过命令行工具还是 Python 脚本来执行任务。
    *   **命令行方式:** 构造并执行命令，指定输入图像路径为 `./input/low_res_image.jpg`，指定输出路径为 `./output/high_res_image.png`。注意库可能提供的参数，例如选择模型 (`--model`)、放大倍数 (`--scale`) 等。
    *   **Python API 方式:** 编写或修改 Python 脚本，导入库，加载选定的超分辨率模型，调用相应的函数处理输入图像 (`./input/low_res_image.jpg`)，并将生成的高分辨率图像保存为 `./output/high_res_image.png` 文件。
3.  **结果验证:**
    *   确认 `./output/high_res_image.png` 文件已成功生成，并且其分辨率相比输入图像有所提高。
    *   运行验证脚本：
        ```bash
        python test_script.py
        ```
    *   检查验证脚本的输出，确保测试通过并且没有错误，或者评估指标（如 PSNR/SSIM）满足要求。

**文件路径约定:**
-   **输入低分辨率图像:** `./input/low_res_image.jpg`
-   **输出高分辨率图像:** `./output/high_res_image.png`
-   **代码库:** `./image-super-resolution/`
-   **验证脚本:** `./test_script.py`

请严格按照此流程执行任务。 