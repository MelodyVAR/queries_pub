# Prompt

使用AnimeGANv3将人像照片转换为动漫风格 

**任务目标:** 利用 `AnimeGANv3` 代码库，将真实人像照片 (`./input/AnimeGANv3_input.png`) 转换为动漫风格，并将结果保存为 `./output/AnimeGANv3_output.png`。

**核心前提:**
1.  **代码库理解:** 在开始执行前，必须先浏览整个代码库，理解其目录结构、主要脚本的功能和代码逻辑。
2.  **阅读文档:** 在开始任何操作前，必须仔细阅读 `AnimeGANv3/README.md`。充分理解其工作原理、命令行参数、依赖需求、模型下载和运行示例。
3.  **强制使用指定库:** 必须使用任务指定的 `AnimeGANv3` 库。如果因任何原因无法使用该库（例如安装困难、模型下载失败、运行错误等），则应停止任务，而不是尝试使用其他库或方法。

**通用环境配置方法论:**
1.  **确认工作目录:** 确保在正确的项目根目录下执行所有命令。
2.  **检查代码库:** 确认任务指定的代码库 (`AnimeGANv3`) 已经克隆或存在于预期的相对路径下。
3.  **依赖安装:**
    *   仔细阅读代码库的 `README.md` 或 `requirements.txt` (或 `pyproject.toml` 等) 文件，确定所有必需的依赖项。
    *   强烈建议创建并激活一个独立的虚拟环境 (使用 `conda` 或 `python -m venv`) 来安装依赖，以避免与其他项目冲突。
    *   使用指定的包管理器 (通常是 `pip` 或 `conda`) 安装依赖。例如: `pip install -r requirements.txt` 或根据文档进行安装。
    *   如果直接使用 `pip install -r requirements.txt` 失败，请确保手动安装的依赖版本与 `requirements.txt` 中指定的版本完全一致，不要使用自动安装的默认版本。
    *   特别注意 Python 版本、主要框架 (PyTorch) 的版本以及其他特殊库的安装要求和步骤。
4.  **模型**
    *   直接在 `AnimeGANv3` 目录下查找预训练模型相关文件，常见如 `checkpoint`, `weight`等。
5.  **验证安装:** (可选但推荐) 如果代码库提供了测试脚本或简单的运行示例，尝试运行它们以初步验证环境、依赖和模型是否配置正确。

**执行流程:**
1.  **环境设置:**
    *   确认你处于正确的项目工作目录。
    *   检查 `AnimeGANv3` 代码库是否存在。
    *   根据 `AnimeGANv3/README.md` 和通用环境配置方法论完成依赖安装和模型下载。
2.  **执行动漫风格转换:**
    *   参考 `AnimeGANv3/README.md` 或其提供的示例脚本，找到执行风格转换的命令或 Python 调用方法。
    *   构造并执行命令或脚本，指定输入图像路径为 `./input/AnimeGANv3_input.png`。
    *   确保将输出结果指定保存到 `./output/AnimeGANv3_output.png`。检查 `AnimeGANv3` 是否有参数来控制输出目录和文件名。
3.  **结果验证:**
    *   确认 `./output/AnimeGANv3_output.png` 文件已成功生成。

**文件路径约定:**
-   **输入真实图像:** `./input/AnimeGANv3_input.png`
-   **输出动漫图像:** `./output/AnimeGANv3_output.png`
-   **代码库:** `./AnimeGANv3/`
-   **验证脚本:** `./test_script.py`

请严格按照此流程执行任务。 