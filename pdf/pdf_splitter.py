# Script ini akan membagi suatu pdf menjadi halaman-halaman pdf yang terpisah ke dalam folder yang bernama 'Hasil Pisah'
# Argumen 1 = nama file pdf
# Python 3.11.3
# pip install PyPDF2==3.0.1

import sys
import os
from PyPDF2 import PdfWriter, PdfReader

inputpdf = PdfReader(open(sys.argv[1], "rb"))
os.mkdir('Hasil pisah')

for i in range(len(inputpdf.pages)):
    output = PdfWriter()
    output.add_page(inputpdf.pages[i])

    with open("Hasil pisah/Halaman %s.pdf" % str(i + 1), "wb") as outputStream:
        output.write(outputStream)