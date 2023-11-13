# Script ini akan mengonversi berkas video menjadi berkas audio dengan nama "output.mp3"
# Jangan lupa install FFmpeg terlebih dahulu.

import subprocess
import argparse
import sys
import os

def get_file_size(ukuran_berkas, pembagi=1024, akhiran="B"):
    """
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
        P = Petabytes
        E = Exabytes
        Z = Zetabytes
        Y = Yottabytes
    """
    for satuan in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if ukuran_berkas < pembagi:
            return f"{ukuran_berkas:.2f} {satuan}{akhiran}"
        
        ukuran_berkas /= pembagi

    return f"{ukuran_berkas:.2f} Y{akhiran}"

def convert_video_to_audio(input_video, output_audio, detail_ffmpeg=True):
    if detail_ffmpeg:
        try:
            subprocess.call(["ffmpeg", "-hide_baner", "-y", "-i", input_video, output_audio], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        except Exception as e:
            print("Gagal mengonversi video!\n" + e)
    else :
        try:
            subprocess.call(["ffmpeg", "-y", "-i", input_video, output_audio], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        except Exception as e:
            print("Gagal mengonversi video!\n" + e)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script Python sederhana untuk mengonversi atau mengekstrak berkas video menjadi berkas audio")
    parser.add_argument("video", help="Berkas video yang ingin dikonversi")
    parser.add_argument("-o", "--output-audio", type=str, help="Nama berkas audio sebagai output", default="output.mp3")
    parser.add_argument("-hb", "--hide-baner", action="store_true", help="Menyembunyikan keterangan detail yang diberikan oleh FFmpeg")
    args = parser.parse_args()

    print("=" * 27)
    print("[*]", args.video, ": ", get_file_size(os.stat(args.video).st_size))

    convert_video_to_audio(args.video, args.output_audio, args.hide_baner)

    print(f"[*] {args.output_audio} : {get_file_size(os.stat(args.output_audio).st_size)}")
    print("=" * 27)