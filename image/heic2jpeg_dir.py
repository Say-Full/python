# pip install pillow==9.5.0 pillow-heif==0.11.1

from PIL import Image
import pillow_heif
import os
import sys

input_dir = sys.argv[1]
ekstensi_hasil_konversi = sys.argv[2]
output_dir = 'Hasil konversi'

if (not os.path.exists(input_dir)) :
    sys.exit('Direktori/folder \"{}\" tidak ditemukan!'.format(input_dir))

if (os.path.exists(output_dir)) :
    sys.exit('Harap hapus direktori {} dan jalani ulang script ini'.format(output_dir))

os.makedirs(output_dir)


for image in [img for img in os.listdir(input_dir) if img.lower().endswith('.heic')]:
    nama_image = image.split('.HEIC')[0]
    nama_baru = nama_image + '.' + ekstensi_hasil_konversi

    heif_file = pillow_heif.read_heif(os.path.join(input_dir, image))
    image = Image.frombytes(heif_file.mode, heif_file.size, heif_file.data, "raw")
    image.save(os.path.join(output_dir, nama_baru), format=ekstensi_hasil_konversi) # PNG > JPEG
