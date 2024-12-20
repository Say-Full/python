import os
import subprocess

opus_path = './Convert'
out_dir = './Output'

if not os.path.exists(out_dir):
    os.makedirs(out_dir)

paths = [path for path in os.listdir(opus_path) if path.endswith('.opus')]


for path in paths:
    filename = path.split('.')[0] + '.mp3'
    print(filename)
    subprocess.run(f"ffmpeg -hide_banner -v 8 -i {opus_path}/{path} -ar 16000 -ac 1 -f wav -acodec pcm_s16le {out_dir}/{filename}")