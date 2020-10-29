import os
import sys
from os.path import expanduser

script = sys.argv[0]
directory = sys.argv[1]
path = os.path.dirname(directory)
home = expanduser("~")

rules = ('.mkv', '.webm', '.mp4')

for file in os.listdir(path):
    new_path = home + "/" + path + "/" + file + "/"
    for each in os.listdir(new_path):
        if each.endswith(".json"):
            src = new_path + each
            dst = new_path + "video.json"
            os.rename(src, dst)

        if each == "Video1":
            src = new_path + each
            dst = new_path + "video.mkv"
            os.rename(src, dst)

