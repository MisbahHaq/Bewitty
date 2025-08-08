from PIL import Image
import os

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

        # JPEG / WEBP compression
        if img_format in ["JPEG", "JPG", "WEBP"]:
            img.save(output_path, format=img_format, quality=quality, optimize=True)

        # PNG compression (reduce colors + optimize)
        elif img_format == "PNG":
            img = img.convert("P", palette=Image.ADAPTIVE, colors=256)
            img.save(output_path, format="PNG", optimize=True)

        else:
            img.save(output_path, format=img_format)

        print(f"✅ Compressed: {output_path}")

    except Exception as e:
        print(f"❌ Error compressing {input_path}: {e}")


if __name__ == "__main__":
    folder_path = "images"  # Folder where images are stored

    for filename in os.listdir(folder_path):
        if filename.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
            file_path = os.path.join(folder_path, filename)
            compress_image(file_path, quality=70)
