from PIL import Image
import os
import subprocess

def compress_image(input_path, output_path=None, quality=70):
    """
    Compresses an image without changing its extension.
    JPG/WEBP - Uses quality compression
    PNG - Reduces color palette + optimization
    """
    try:
        img = Image.open(input_path)
        img_format = img.format.upper()

        if output_path is None:
            output_path = input_path  # overwrite original

        if img_format in ["JPEG", "JPG", "WEBP"]:
            img.save(output_path, format=img_format, quality=quality, optimize=True)
        elif img_format == "PNG":
            img = img.convert("P", palette=Image.ADAPTIVE, colors=256)
            img.save(output_path, format="PNG", optimize=True)
        else:
            img.save(output_path, format=img_format)

        print(f"✅ Image compressed: {output_path}")

    except Exception as e:
        print(f"❌ Error compressing image {input_path}: {e}")

def compress_webm(input_path, output_path=None, crf=28):
    """
    Compress a WebM video using FFmpeg without changing its extension.
    Lower CRF = higher quality. Typical range: 15–35.
    """
    try:
        if output_path is None:
            output_path = input_path  # overwrite original

        temp_output = output_path + ".temp.webm"

        # Run FFmpeg command
        subprocess.run([
            "ffmpeg", "-i", input_path,
            "-c:v", "libvpx-vp9",
            "-crf", str(crf),
            "-b:v", "0",
            "-c:a", "libopus",
            temp_output
        ], check=True)

        # Replace original with compressed
        os.replace(temp_output, output_path)
        print(f"✅ Video compressed: {output_path}")

    except Exception as e:
        print(f"❌ Error compressing video {input_path}: {e}")

if __name__ == "__main__":
    folder_path = "images"  # Folder with images/videos

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if filename.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
            compress_image(file_path, quality=70)
        elif filename.lower().endswith(".webm"):
            compress_webm(file_path, crf=28)
