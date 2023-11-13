import subprocess

subprocess.run("ffmpeg -i 2.m4a -hide_banner")
subprocess.run("ffmpeg -hide_banner -v 8 -i 2.m4a -ar 16000 -ac 1 -f wav -acodec pcm_s16le 2.wav")
