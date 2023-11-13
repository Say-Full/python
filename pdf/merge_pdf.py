# Script ini akan menggabungkan berkas-berkas PDF menjadi satu berkas PDF yang bernama Gabungan.pdf dan menyimpannya ke dalam folder 'Hasil Gabung'
# Python 3.11.3
# pip install PyPDF2==3.0.1

from PyPDF2 import PdfWriter
import os

os.mkdir('Hasil Gabung')

merger = PdfWriter()
# pdf_files = ['1.pdf', '2.pdf', '3.pdf', '4.pdf', '5.pdf']

pdf_files = []
awal = 1
akhir = 70
for i in range(awal, akhir + 1) :
    pdf_files.append('Hasil Pisah/Halaman ' + str(i) + ".pdf")

for pdf_file in pdf_files:
    merger.append(pdf_file)

merger.write("Hasil Gabung/Gabungan.pdf")
merger.close()