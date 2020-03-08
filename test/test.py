import pytest
import shutil
import os
from ExifRemover import CleanExif
from PIL import Image

def test_prepare():
    os.makedirs("test", mode=0o777)

def test_return_image_without_exif():
    test_image_with_exif = Image.open("./test.jpg")
    test_image_exif_before = test_image_with_exif._getexif()
    CleanExif.return_image_without_exif(test_image_with_exif.filename, "./test")
    test_image_without_exif = Image.open("./test/test.jpg")
    test_image_exif_after = test_image_without_exif._getexif()
    assert(test_image_exif_before is not test_image_exif_after)

def test_clean():
    shutil.rmtree("./test/")