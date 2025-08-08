from PIL import Image
import os

def compress_image(input_path, output_path=None, quality=70):
    """
    Compresses an image without changing its extension.

    Args:
        input_path (str): Path to the input image.
        output_path (str): Path to save compressed image (optional).
                           If None, overwrites the original file.
        quality (int): Compression quality (1-100 for JPEG/WebP).
    """
    try:
        # Open the image
        img = Image.open(input_path)
        
        # Get original extension and format
        ext = os.path.splitext(input_path)[1].lower()
        img_format = img.format

        # Set output path
        if output_path is None:
            output_path = input_path

        # Save compressed (JPEG/WebP get quality, PNG uses optimize)
        if img_format in ["JPEG", "JPG", "WEBP"]:
            img.save(output_path, format=img_format, quality=quality, optimize=True)
        elif img_format == "PNG":
            img.save(output_path, format=img_format, optimize=True)
        else:
            img.save(output_path, format=img_format)  # Other formats untouched

        print(f"✅ Compressed: {output_path}")
    except Exception as e:
        print(f"❌ Error compressing {input_path}: {e}")

# Example usage
if __name__ == "__main__":
    folder_path = "images"  # Change to your folder
    for filename in os.listdir(folder_path):
        if filename.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
            file_path = os.path.join(folder_path, filename)
            compress_image(file_path, quality=70)
