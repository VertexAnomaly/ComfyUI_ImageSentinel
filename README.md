# ♻️ ComfyUI ImageSentinel Node Pack

**Author:** VertexAnomaly  
**Version:** 1.0.0

---

## What is ImageSentinel?

**ImageSentinel** is a custom node pack for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) that automatically watches and reloads images from a specified folder. It supports common image formats (e.g., PNG, JPG) as well as PSD files, automatically converting them into standard RGB images using **psd-tools**. The node delivers the images as Torch FloatTensors, making them immediately usable in your ComfyUI workflows.

---

## Why Use ImageSentinel?

- **Automatic Image Reloading**  
  ImageSentinel continuously monitors your selected image file. If the image changes, the node detects this via hashing and automatically reloads it.

- **Built-in PSD Support**  
  Seamlessly loads PSD files, automatically converting them to a flattened RGB image for immediate use.

- **Integrated Delay for Instant Queue Mode**  
  In Instant Queue mode, ComfyUI can execute nodes repeatedly in quick succession. To manage this, ImageSentinel has an optional delay parameter to pause before each file check.  
  **This delay ensures your node doesn’t run repeatedly without a pause**, giving external processes (like editing and saving images) adequate time to complete.

- **Recommended Fixed Seed Usage**  
  It is recommended to use fixed seeds in Instant Queue mode when using this node. Fixed seeds help prevent ComfyUI from repeatedly resampling the same input unnecessarily when no actual changes to your image have occurred. This helps save computational resources and ensures consistent results across runs.

- **Failsafe Placeholder**  
  If the specified image cannot be found or loaded correctly, ImageSentinel returns a default black 512×512 placeholder to ensure your workflow continues smoothly.

---

## Dependencies and Installation

### Dependencies:
- [psd-tools](https://pypi.org/project/psd-tools/)
- [Pillow](https://pillow.readthedocs.io/)
- [numpy](https://numpy.org/)
- [torch](https://pytorch.org/)

Install these via pip:

```bash
pip install -r requirements.txt
