# pip install pillow==9.5.0
# Pillow==9.5.0 | pillow-heif==0.11.1

# Compress semua gambar di dalam direktori ini

import os
from PIL import Image
  
def main():                      
    cwd = os.getcwd()
    formats = ('.jpg', '.jpeg')

    for file in os.listdir(cwd):
        if os.path.splitext(file)[1].lower() in formats:
            print('compressing', file)
            filepath = os.path.join(os.getcwd(), file)
            picture = Image.open(filepath)
            
            # quality++ = compress--
            picture.save("Compressed_"+file, "JPEG", optimize = True, quality = 7)
  
    print("Done")
  
if __name__ == "__main__":
    main()