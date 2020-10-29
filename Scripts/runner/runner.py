import os
import subprocess
import sys

script = sys.argv[0]
file = sys.argv[1]

path = os.path.dirname(file)
listDir = os.listdir(path)

count = 0

for i in listDir:
    count += 1

videoRule = (".mkv", ".webm", ".mp4")



for cnt in range(1, count+1):
    directory = path + "/Video" + str(cnt) + "/"

    for file in os.listdir(directory):
        if file.endswith(videoRule):

            command = "python3 AudioProcess/Main.py " + directory + file
            subprocess.run(command, shell=True)



