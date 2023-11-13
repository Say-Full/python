# pip install pillow==9.5.0 pillow-heif==0.11.1

from PIL import Image
import pillow_heif

heif_file = pillow_heif.read_heif("1.HEIC")
image = Image.frombytes(heif_file.mode, heif_file.size, heif_file.data, "raw")
image.save("./2.jpeg", format="jpeg") # PNG > JPEG