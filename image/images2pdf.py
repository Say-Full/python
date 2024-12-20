# pip install pillow==9.5.0
# Pillow==9.5.0 | pillow-heif==0.11.1

# 1) Harus urutkan nama-nama berkas gambarnya terlebih dahulu secara manual, seperti "1.jpg", "2.png", dst., karena jika tidak, Python akan mendeteksi daftar nama berkas sebagai:
# 1) "CamScanner 21-12-2023 12.34_1.jpg"
# 2) "CamScanner 21-12-2023 12.34_10.jpg"
# 3) "CamScanner 21-12-2023 12.34_11.jpg"
# 4) "CamScanner 21-12-2023 12.34_2.jpg"

# Yang seharusnya setelah "CamScanner 21-12-2023 12.34_1.jpg" adalah "CamScanner 21-12-2023 12.34_2.jpg".
# 2) Semua gambar harus memiliki ekstensi yang sama.

# Argumen 1 = Direktori tempat berkas-berkas gambar dihimpun
# Argumen 2 = Banyak gambar

from PIL import Image
import os
import sys

input_dir = sys.argv[1]
awal = 1
akhir = sys.argv[2]
images = []

for i in range(awal, int(akhir) + 1) :
    image_name = str(i) + ".jpg"
    images.append(Image.open(os.path.join(input_dir, image_name)))

images[0].save(
    "output.pdf", "PDF" ,resolution=100.0, save_all=True, append_images=images[1:]
)

for img in images:
    img.close()