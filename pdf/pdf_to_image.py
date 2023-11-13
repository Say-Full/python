from pdf2image import convert_from_path

pages = convert_from_path('Tes.pdf', 500)

for count, page in enumerate(pages):
    page.save(f'out{count}.jpg', 'JPEG')

# for page in pages:
#     page.save('out.png', 'PNG')

# for i in range(len(pages)):
#     pages[i].save('Halaman ' + str(i) + '.jpg', 'JPEG')