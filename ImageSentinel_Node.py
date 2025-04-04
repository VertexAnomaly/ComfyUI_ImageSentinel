# ComfyUI_ImageSentinel/ImageSentinel_Node.py

import os
import time
import hashlib
import numpy as np
import torch
from PIL import Image

# Import psd_tools for PSD support
# Make sure you've installed it: pip install psd-tools
from psd_tools import PSDImage


class ImageSentinel:

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "folder_path": (
                    "STRING",
                    {
                        "default": "./ComfyUI/input",
                        "multiline": False
                    }
                ),
                "image_name": (
                    "STRING",
                    {
                        "default": "example.png",
                        "multiline": False
                    }
                ),
            },
            "optional": {
                "delay_seconds": (
                    "FLOAT",
                    {
                        "default": 0.0,
                        "min": 0.0,
                        "max": 300.0,
                        "step": 1.0,
                        "label": "Delay (seconds)"
                    }
                )
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "load_image"
    CATEGORY = "♻️ ImageSentinel"

    def load_image(self, folder_path, image_name, delay_seconds=0.0):
        """
        Load the image (including .psd support). If .psd, we'll use psd-tools
        to get the composite image. Otherwise, we fall back to Pillow.
        Returns a Torch float tensor in shape (1,H,W,3).
        """
        file_path = os.path.join(folder_path, image_name)

        if not os.path.isfile(file_path):
            print(f"[ImageSentinel] File not found: {file_path}")
            placeholder = torch.zeros((1, 512, 512, 3), dtype=torch.float32)
            return (placeholder,)

        # Determine file extension
        _, ext = os.path.splitext(file_path)
        ext = ext.lower()

        try:
            if ext == ".psd":
                print(f"[ImageSentinel] Detected .psd file: {file_path}")
                psd = PSDImage.open(file_path)
                # Obtain a flattened Pillow image of the PSD
                pil_img = psd.composite()
                pil_img = pil_img.convert("RGB")
            else:
                with Image.open(file_path) as img:
                    pil_img = img.convert("RGB")

        except Exception as e:
            print(f"[ImageSentinel] Error loading {file_path}: {e}")
            placeholder = torch.zeros((1, 512, 512, 3), dtype=torch.float32)
            return (placeholder,)

        # Convert Pillow -> NumPy -> Torch float tensor (1,H,W,3)
        np_img = np.array(pil_img, dtype=np.float32) / 255.0
        tensor_img = torch.from_numpy(np_img)[None,]
        return (tensor_img,)

    @classmethod
    def IS_CHANGED(cls, folder_path, image_name, delay_seconds=0.0):
        """
        Incorporate a delay BEFORE checking the file's hash. 
        This means the pipeline is blocked while we wait, even 
        if the file turns out to be unchanged.
        """
        if delay_seconds > 0:
 #           print(f"[ImageSentinel] Delaying before hash check by {delay_seconds} second(s)...")
            time.sleep(delay_seconds)

        file_path = os.path.join(folder_path, image_name)
        if not os.path.isfile(file_path):
            return ""

        try:
            with open(file_path, 'rb') as f:
                file_bytes = f.read()
            return hashlib.sha256(file_bytes).hexdigest()
        except:
            return ""


# Node mappings for ComfyUI
NODE_CLASS_MAPPINGS = {
    "ImageSentinel": ImageSentinel
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ImageSentinel": "♻️ ImageSentinel"
}