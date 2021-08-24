from PIL import Image
import pyheif
import glob

def convert(file_name):
    heif = pyheif.read(file_name)
    data = Image.frombytes(
        heif.mode,
        heif.size,
        heif.data,
        "raw",
        heif.mode,
        heif.stride,
        )
    data.save(file_name.replace('HEIC', 'png'), "png")

file_names = glob.glob("*.HEIC")
for f in file_names:
    convert(f)
