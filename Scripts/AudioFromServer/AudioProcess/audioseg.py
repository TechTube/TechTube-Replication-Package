import contextlib
import wave
import subprocess


fname = ""
with contextlib.closing(wave.open(fname, 'r')) as chunkFile:
    frames = chunkFile.getnframes()
    rate = chunkFile.getframerate()
    TotalDuration = frames / float(rate)


reminder = TotalDuration % 4
dividable = TotalDuration - reminder
duration = dividable / 4
duration2 = duration * 2
duration3 = duration * 3

a1hour = int(duration / 3600)
durationRestMin = duration % 3600
a1min = int(durationRestMin / 60)
a1sec = int(durationRestMin % 60)


a2hour = int(duration2 / 3600)
durationRestMin2 = duration2 % 3600
a2min = int(durationRestMin2 / 60)
a2sec = int(durationRestMin2 % 60)

a3hour = int(duration3 / 3600)
durationRestMin3 = duration3 % 3600
a3min = int(durationRestMin3 / 60)
a3sec = int(durationRestMin3 % 60)

a4hour = int(TotalDuration / 3600)
durationRestMin4 = int(TotalDuration) % 3600
a4min = int(durationRestMin4 / 60)
a4sec = int(durationRestMin4 % 60)

a1hour = str("{0:0=2d}".format(a1hour))
a1min = str("{0:0=2d}".format(a1min))
a1sec = str("{0:0=2d}".format(a1sec))
a2hour = str("{0:0=2d}".format(a2hour))
a2min = str("{0:0=2d}".format(a2min))
a2sec = str("{0:0=2d}".format(a2sec))
a3hour = str("{0:0=2d}".format(a3hour))
a3min = str("{0:0=2d}".format(a3min))
a3sec = str("{0:0=2d}".format(a3sec))
a4hour = str("{0:0=2d}".format(a4hour))
a4min = str("{0:0=2d}".format(a4min))
a4sec = str("{0:0=2d}".format(a4sec))

time1 = a1hour + ":" + a1min + ":" + a1sec
time2 = a2hour + ":" + a2min + ":" + a2sec
time3 = a3hour + ":" + a3min + ":" + a3sec
time4 = a4hour + ":" + a4min + ":" + a4sec


command = ['ffmpeg', '-i', fname, '-acodec', 'copy', '-ss', '00:00:00', '-to', time1, "/home/hoomanvhd/Desktop/Video1-done/Process/FirstPart.wav",
                                  '-acodec', 'copy', '-ss', time1, '-to', time2, "/home/hoomanvhd/Desktop/Video1-done/Process/SecondPart.wav",
                                  '-acodec', 'copy', '-ss', time2, '-to', time3, "/home/hoomanvhd/Desktop/Video1-done/Process/ThirdPart.wav",
                                  '-acodec', 'copy', '-ss', time3, '-to', time4, "/home/hoomanvhd/Desktop/Video1-done/Process/FourthPart.wav"]



subprocess.run(command, stdout=subprocess.PIPE, stdin=subprocess.PIPE)

