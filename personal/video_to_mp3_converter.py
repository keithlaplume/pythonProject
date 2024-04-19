import os
import subprocess

music_dir = r"C:\Users\Keith\Desktop\BirthdayMusic\new"

ffmpeg = r"C:\Users\Keith\Desktop\ffmpeg\bin\ffmpeg.exe"

for f in os.listdir(music_dir):
    print(f)
    if os.path.isfile(os.path.join(music_dir, f)):
        if f.endswith(".mp4"):
            full_filename = os.path.join(music_dir, f)
            cmd = [ffmpeg, "-i", full_filename, full_filename.replace(".mp4", ".mp3")]
            print(cmd)
            subprocess.run(cmd, shell=True)