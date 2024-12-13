from .nodes import VideoSubtitleRemoverNode
print("ComfyUI-video-subtitle-remover loaded")

# 这个字典用于注册节点
NODE_CLASS_MAPPINGS = {
    "VideoSubtitleRemover": VideoSubtitleRemoverNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "VideoSubtitleRemover": "Video Subtitle Remover"
} 
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS'] 
