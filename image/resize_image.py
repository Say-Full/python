# pip install pillow==9.5.0
# Pillow==9.5.0 | pillow-heif==0.11.1

from PIL import Image

# im = Image.open(r"D:\Lainnya\Programming\Python\Tes\1.jpg")
im = Image.open("1.jpg")
newsize = (3000, 4000)
im = im.resize(newsize)
im.save("tes_1.jpg")