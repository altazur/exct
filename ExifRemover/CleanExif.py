from PIL import Image
import os.path as path

def return_image_without_exif(image_file_input, image_file_output):
    """Takes an Image file as an argument and return image file without exif simply by resaving it"""
    image = Image.open(image_file_input)
    image.save(f"{image_file_output}/{path.basename(image.filename)}")
