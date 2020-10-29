
import csv
import re
import pysubs2
import sys
import os
from os.path import expanduser


script = sys.argv[0]
filename = sys.argv[1]


subs = pysubs2.load(filename)


def GetSec(timeString):
    h, m, s, = timeString.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


def TextCleaner(Sentence):
    Sentence = str(Sentence)
    Sentence = Sentence.replace("['", "")
    Sentence = Sentence.replace('"', "")
    Sentence = Sentence.replace("']", "")
    Sentence = Sentence.replace("[", "")
    Sentence = Sentence.replace("]", "")
    Sentence = Sentence.replace("\\\\", "")
    return Sentence


def TimeCleaner(time):
    time = str(time)
    time = time.replace("['", "")
    time = time.replace("']", "")
    return time


MainStartTimeText = []
MainEndTimeText = []
MainSentence = []
Sentence = []
SentenceCounter = []
StartTimeDef = []
EndTimeDef = []

EndTime = 0

removalSuffix = "N @@!!"

counter = 1

for line in subs:
    line = str(line)
    line = line.replace("<SSAEvent type=Dialogue ", "")
    line = str(line)
    line = line.replace("'>", "@@!!")


    if line.endswith(removalSuffix):
        line = re.sub("(.*?)", "", line)


    elif "\\N" not in line:
        line = re.sub("(.*?)", "", line)


    else:

        line = line.replace("\\N", "@@SentenceSeparator@@")


        StartTime = re.findall("start=(.*?) end", line)
        StartTime = TimeCleaner(StartTime)
        MainStartTimeText.append(StartTime)
        StartTime = GetSec(StartTime)
        StartTimeDef.append(StartTime)


        EndTime = re.findall("end=(.*?) text", line)
        EndTime = TimeCleaner(EndTime)
        MainEndTimeText.append(EndTime)
        EndTime = GetSec(EndTime)
        EndTimeDef.append(EndTime)


        Sentence1 = re.findall("text='(.*?)@@SentenceSeparator@@", line)
        Sentence.append(TextCleaner(Sentence1))


        Sentence2 = re.findall("@@SentenceSeparator@@(.*?)@@!!", line)
        Sentence.append(TextCleaner(Sentence2))


        counter += 1


MainSentence = list(dict.fromkeys(Sentence))


SentenceElementCounter = 1
for element in MainSentence:
    SentenceCounter.append(SentenceElementCounter)
    SentenceElementCounter += 1


if SentenceElementCounter > counter:
    insertRows = SentenceElementCounter - counter


    for addRows in range(insertRows):
        StartTimeDef.append(EndTime)
        ExtraEndTime = EndTime + addRows + 1
        EndTimeDef.append(ExtraEndTime)


with open(filename + "-SubTitleCSV.csv", "w") as SubtitleMain:

    wr = csv.writer(SubtitleMain)
    wr.writerows(zip(SentenceCounter, StartTimeDef, EndTimeDef, MainSentence))

SubtitleMain.close()


home = expanduser('~')
DirectPath = os.path.dirname(filename)
os.mkdir(DirectPath + "/VideoTextReadByLine")


with open(filename + "-SubTitleCSV.csv", 'r') as subtitle:
    reader = csv.reader(subtitle)
    for row in reader:
        counter = row[0]
        text = row[3]


        with open(DirectPath + "/VideoTextReadByLine/" + counter + '.txt', "w") as file:
            file.write(text)































































