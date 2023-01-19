import os
import subprocess

base_dir = os.getcwd()

for root, dirs, filenames in (os.walk(base_dir, topdown=True)):
    for filename in filenames:
        if ".mov" not in filename.lower():
            continue
        print("Converting", filename)
        filename = os.path.join(root, filename)
        outfile_name = filename.replace(".mov", ".mp4")
        subprocess.call(["ffmpeg", "-i", filename, outfile_name])
