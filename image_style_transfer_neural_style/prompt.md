**重要前提**: 在开始编码之前，请务必仔细阅读当前目录下克隆的 `neural-style` 代码仓库根目录中的 `README.md` 文件。理解其功能、用法、依赖项和示例对于成功完成任务至关重要。

任务: 请使用当前工作目录中的 `neural-style` (PyTorch 实现的 Neural Style) 代码，将 `./input/content.jpg` (内容图) 和 `./input/style.jpg` (风格图) 进行风格迁移。将生成的结果图片保存在 `./output/result.jpg` 文件中。

目录约定:
- 内容输入文件位于: `./input/content.jpg`
- 风格输入文件位于: `./input/style.jpg`
- 输出文件应保存到: `./output/result.jpg`

你可能需要在 `neural-style` 库代码中进行必要的修改或调用以完成风格迁移任务，并确保安装所有必需的依赖项。

重要提示: 请绝对不要修改 `evaluate_style_transfer.py` 文件。它是一个外部评估工具，仅用于验证结果。

完成后，需要通过以下测试命令验证结果:
`python evaluate_style_transfer.py --reference_input ./input/content.jpg --generated_output ./output/result.jpg`