# Script ini akan mengompresi semua file PDF yang ada di dalam folder input dan menyimpannya di dalam folder 'PDF Hasil Kompresi'
# Argumen 1 = Direktori tempat berkas-berkas PDF dihimpun
# Python 3.11.3
# pip install PyPDF2==3.0.1

from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.errors import PdfReadError
import sys
import os

input_dir = sys.argv[1]
output_dir = 'PDF Hasil Kompresi'

if (not os.path.exists(input_dir)) :
    sys.exit('Direktori/folder \"{}\" tidak ditemukan!'.format(input_dir))

if (os.path.exists(output_dir)) :
    sys.exit('Harap hapus direktori {} dan jalani ulang script ini'.format(output_dir))

os.makedirs(output_dir)



for pdf in [p for p in os.listdir(input_dir) if p.lower().endswith('.pdf')]:
    try:
        writer = PdfWriter()
        reader = PdfReader(open(os.path.join(input_dir, pdf), "rb"))

        for page in reader.pages:
            page.compress_content_streams()
            writer.add_page(page)
        
        with open( os.path.join(output_dir, pdf), "wb" ) as f:
            writer.write(f)

    except PdfReadError:
        print(os.path.join(input_dir, pdf) + ' bukan berkas PDF yang valid')