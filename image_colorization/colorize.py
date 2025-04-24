import sys
sys.path.append('/workspace/01_image_colorization/DeOldify')

from deoldify import device
from deoldify.device_id import DeviceId
from deoldify.visualize import *
import torch
import warnings

# 设置设备为 CPU（因为我们可能没有 GPU）
device.set(device=DeviceId.CPU)

# 忽略警告
warnings.filterwarnings("ignore", category=UserWarning, message=".*?Your .*? set is empty.*?")

def colorize_image(input_path, output_path, render_factor=35):
    try:
        # 创建 colorizer 对象，使用 stable 模型（更适合一般图片）
        colorizer = get_image_colorizer(artistic=False)
        
        # 进行图像着色
        result_path = colorizer.plot_transformed_image(
            path=input_path,
            render_factor=render_factor,
            compare=False  # 不需要对比图
        )
        
        # 将结果复制到指定的输出路径
        import shutil
        shutil.copy(result_path, output_path)
        print(f"Image colorized successfully. Result saved to: {output_path}")
        
    except Exception as e:
        print(f"Error during colorization: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    input_path = "/workspace/01_image_colorization/input/bw_image.jpg"
    output_path = "/workspace/01_image_colorization/output/bw_image_colorized.jpg"
    colorize_image(input_path, output_path)