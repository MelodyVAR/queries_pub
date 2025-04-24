# Prompt

**任务目标:** 利用 `transparent-background` 代码库，移除图像 (`./input/image_with_bg.jpg`) 的背景，并将结果保存为背景透明的 PNG 图像 (`./output/image_no_bg.png`)。

**核心前提:**
1.  **阅读文档:** 在开始任何操作前，必须仔细阅读 `transparent-background` 代码库的 `README.md` 或相关文档。充分理解其工作原理、命令行用法、Python API 调用方式、依赖需求、模型下载（如果需要）和运行示例。
2.  **理解验证脚本:** `test_script.py` 用于最终结果的验证，请勿修改其核心逻辑。
3.  **强制使用指定库:** 必须使用任务指定的 `transparent-background` 库。如果因任何原因无法使用该库（例如安装困难、模型下载失败、运行错误等），则应停止任务，而不是尝试使用其他库或方法。

**通用环境配置方法论:**
1.  **确认工作目录:** 确保在正确的项目根目录下执行所有命令。
2.  **检查代码库/安装库:** 确认任务指定的库 (`transparent-background`) 已经通过 `pip install transparent-background` 或根据其文档指引安装到当前 Python 环境中，或者其代码库存在于本地。
3.  **依赖安装:**
    *   检查库的 `README.md` 或 `requirements.txt`，确认所有依赖项已安装，特别是 `onnxruntime` 或 `torch`。
    *   强烈建议创建并激活一个独立的虚拟环境。
    *   确保 Python 版本和相关框架版本兼容。
4.  **模型下载:**
    *   库通常会在首次使用时自动下载 ONNX 模型。确保网络连接正常且有缓存写入权限。
    *   如果需要手动下载或使用特定模型变体，请遵循文档。
5.  **验证安装:** (可选但推荐) 尝试使用库提供的命令行工具或 Python API 处理一张简单图片，验证安装和模型加载。

**执行流程:**
1.  **环境设置:**
    *   确认你处于正确的项目工作目录。
    *   确认 `transparent-background` 库已安装或代码存在。
    *   根据文档和通用环境配置方法论完成依赖安装和模型准备。
2.  **执行背景移除:**
    *   根据 `transparent-background` 的文档，确定是通过命令行工具还是 Python 脚本来执行任务。
    *   **命令行方式:** 构造并执行命令，指定输入图像路径为 `./input/image_with_bg.jpg`，并指定输出路径为 `./output/image_no_bg.png`。注意库可能提供的参数，如模型类型 (`--type`) 或处理模式 (`--mode`) 等。
    *   **Python API 方式:** 编写或修改 Python 脚本，导入库，加载模型，调用相应的函数处理输入图像 (`./input/image_with_bg.jpg`)，并将结果（通常是 PIL Image 对象或 numpy 数组）保存为 `./output/image_no_bg.png` 文件。
3.  **结果验证:**
    *   确认 `./output/image_no_bg.png` 文件已成功生成，并且其背景是透明的（可以使用图像查看器检查）。
    *   运行验证脚本：
        ```bash
        python test_script.py
        ```
    *   检查验证脚本的输出，确保测试通过并且没有错误。

**文件路径约定:**
-   **输入带背景图像:** `./input/image_with_bg.jpg`
-   **输出透明背景图像:** `./output/image_no_bg.png`
-   **代码库/库:** `transparent-background`
-   **验证脚本:** `./test_script.py`

请严格按照此流程执行任务。 