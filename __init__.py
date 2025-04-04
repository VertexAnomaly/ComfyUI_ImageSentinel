# ComfyUI_ImageSentinel/__init__.py

"""
ComfyUI_ImageSentinel Node Pack
Author: VertexAnomaly
Version: 1.0.0

This custom node pack provides the ImageSentinel node, which monitors a single image file.
It automatically reloads the image into your workflow whenever the file changes, supports PSD files,
and includes an optional delay mechanism for use with Instant Queue mode in ComfyUI.
"""

# Import the node mappings
from .ImageSentinel_Node import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS
