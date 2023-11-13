# Script ini akan mengekstrak suatu halaman dan menyimpannya ke dalam folder 'Hasil Ekstrak'
# Argumen 1 = nama file pdf
# Argumen 2 = halaman yg mw diekstrak
# Python 3.11.3
# pip install PyPDF2==3.0.1

from PyPDF2 import PdfReader, PdfWriter
import sys
import os

pdf = PdfReader(open(sys.argv[1], "rb"))
pdf_writer = PdfWriter()
nomor_halaman = int(sys.argv[2])
# nomor_halaman = 1

# Halaman 1 dlm file pdf = indeks 0. Jd klo argumen dr CLI nya 0 = halaman 1
pdf_writer.add_page(pdf.pages[nomor_halaman - 1])
os.mkdir('Hasil Ekstrak')

with open("Hasil Ekstrak/Ekstrak Halaman %s.pdf" % str(nomor_halaman), "wb") as out:
    pdf_writer.write(out)