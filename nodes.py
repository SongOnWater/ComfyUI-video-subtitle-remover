import os
import shutil
from .backend.main import *

class VideoSubtitleRemoverNode:
    """用于移除视频字幕的ComfyUI节点"""
    
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "video_path": ("STRING", {"default": ""}),
            },
            "optional": {
                "sub_area": ("BBOX", {"default": None}),  # 移到optional部分
            },
        }

    RETURN_TYPES = ("STRING",)  # 返回处理后的文件路径
    RETURN_NAMES = ("output_path",)
    FUNCTION = "remove_subtitle"
    CATEGORY = "video_subtitle"
    OUTPUT_NODE = True

    def remove_subtitle(self, video_path, sub_area):
        # 检查视频文件是否存在
        if not os.path.exists(video_path):
            raise FileNotFoundError(f"Video file not found: {video_path}")
            
        if sub_area is not None:
            x, y, width, height = sub_area
            sub_area = (y, y+height, x, x+width)
            
        # 创建SubtitleRemover实例并执行
        remover = SubtitleRemover(video_path, sub_area=sub_area)
        remover.run()
        
        # 创建ComfyUI输出目录
        output_dir = os.path.join("output", "video_subtitle_remover")
        os.makedirs(output_dir, exist_ok=True)
        
        # 构建新的输出路径
        filename = os.path.basename(remover.video_out_name)
        new_output_path = os.path.join(output_dir, filename)
        
        # 移动文件到新位置并删除原文件
        shutil.move(remover.video_out_name, new_output_path)
        
        return (new_output_path,)  # 返回新的输出路径

