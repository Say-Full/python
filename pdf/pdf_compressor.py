# Script ini akan mengompresi sebuah file PDF
# Argumen 1 = nama file pdf
# Python 3.11.3
# pip install PyPDF2==3.0.1

from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.errors import PdfReadError
import sys

input_pdf = sys.argv[1]
output_pdf = input_pdf.split('.pdf')[0] + '_terkompresi.pdf'

try :
    writer = PdfWriter()
    reader = PdfReader(open(input_pdf, "rb"))

    for page in reader.pages:
        page.compress_content_streams()
        writer.add_page(page)

    with open(output_pdf, "wb") as f:
        writer.write(f)

except PdfReadError:
    print(input_pdf + ' bukan berkas PDF yang valid')
    