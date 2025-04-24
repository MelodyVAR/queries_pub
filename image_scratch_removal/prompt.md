# Prompt

**任务目标:** 利用 `Bringing-Old-Photos-Back-to-Life` 代码库，修复带有划痕的老照片 (`./input/old_photo_with_scratches.png`)，并将修复后的照片保存为 `./output/restored_photo.png`。

**核心前提:**
1.  **阅读文档:** 在开始任何操作前，必须仔细阅读 `Bringing-Old-Photos-Back-to-Life` 代码库的 `README.md` 或相关文档。充分理解其工作原理 (可能包含划痕检测、图像修复等多个阶段)、命令行用法、Python API、依赖需求、模型下载 (该库可能涉及多个模型) 和运行示例。
2.  **理解验证脚本:** `test_script.py` 用于最终结果的验证 (例如，检查输出文件是否存在，或进行视觉评估)。请勿修改其核心逻辑。
3.  **强制使用指定库:** 必须使用任务指定的 `Bringing-Old-Photos-Back-to-Life` 库。如果因任何原因无法使用该库（例如安装困难、模型下载失败、运行错误等），则应停止任务，而不是尝试使用其他库或方法。

**通用环境配置方法论:**
1.  **确认工作目录:** 确保在正确的项目根目录下执行所有命令。
2.  **检查代码库:** 确认任务指定的代码库 (`Bringing-Old-Photos-Back-to-Life`) 已经克隆或存在于预期的相对路径下。
3.  **依赖安装:**
    *   仔细阅读代码库的 `README.md` 和 `requirements.txt`，确定所有必需的依赖项。
    *   强烈建议创建并激活一个独立的虚拟环境 (使用 `conda` 或 `python -m venv`) 来安装依赖。
    *   使用 `pip install -r requirements.txt` 安装依赖。
    *   特别注意 `dlib` 的安装，它可能需要 `CMake` 和 C++ 编译器，根据操作系统可能需要特殊步骤。
    *   确保 Python 版本和 PyTorch 版本符合要求。
4.  **模型下载:**
    *   根据代码库文档 (`README.md`) 的指示，下载所有需要的预训练模型文件（可能包括人脸检测、划痕修复、全局修复等多个模型）。这通常涉及运行一个下载脚本或手动下载。
    *   确保将下载的模型文件放置在代码库预期的目录结构中 (例如 `checkpoints/`, `models/`, `weights/` 等，务必遵循文档)。
5.  **验证安装:** (可选但推荐) 运行 `python run.py --help` 或尝试处理一张示例图片，验证环境配置正确。

**执行流程:**
1.  **环境设置:**
    *   确认你处于正确的项目工作目录。
    *   检查 `Bringing-Old-Photos-Back-to-Life` 代码库是否存在。
    *   根据文档和通用环境配置方法论完成依赖安装（特别注意 `dlib`）和所有模型的下载与放置。
2.  **执行照片修复:**
    *   该库通常提供一个集成的 Python 脚本 (如 `run.py`) 来执行整个修复流程。仔细阅读文档，了解如何使用该脚本。
    *   构造并执行命令，指定输入图像或包含输入图像的目录。对于本任务，输入文件是 `./input/old_photo_with_scratches.png`，所以可能需要使用类似 `--input_folder ./input/` 的参数。
    *   确保将输出结果指定保存到 `./output/restored_photo.png`。检查脚本参数，通常会有 `--output_folder ./output/` 参数。脚本可能会在输出目录中生成包含 `restored` 字样的文件，你需要确保最终的文件名为 `restored_photo.png` (可能需要重命名库的默认输出)。
    *   注意库可能提供的选项，例如是否启用 GPU (`--GPU 1`)，是否只进行划痕修复 (`--scratch`) 等。根据任务需求选择合适的参数。
3.  **结果验证:**
    *   确认 `./output/restored_photo.png` 文件已成功生成。
    *   运行验证脚本：
        ```bash
        python test_script.py
        ```
    *   检查验证脚本的输出，确保测试通过并且没有错误。

**文件路径约定:**
-   **输入带划痕照片:** `./input/old_photo_with_scratches.png`
-   **输出修复后照片:** `./output/restored_photo.png`
-   **代码库:** `./Bringing-Old-Photos-Back-to-Life/`
-   **验证脚本:** `./test_script.py`

请严格按照此流程执行任务。 