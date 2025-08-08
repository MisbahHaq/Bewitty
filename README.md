# Image & WebM Compressor

A simple Python script to compress images (`.png`, `.jpg`, `.jpeg`, `.webp`) and `.webm` videos without changing their original file extensions.  
Uses **Pillow** for images and **FFmpeg** for videos.

## Features

- Compresses `.png`, `.jpg`, `.jpeg`, `.webp` without changing extensions  
- Optimizes PNG by reducing color palette  
- Compresses `.webm` videos with quality settings  
- Overwrites files in place or can be modified to save elsewhere  
- Minimal and easy to use  

---

## 🛠 Requirements

- Python 3.x  
- Pillow  
```bash
pip install pillow
