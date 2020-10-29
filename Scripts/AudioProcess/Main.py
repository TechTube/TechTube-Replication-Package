from AudioSegmenting import AudioSegmenting
from SpeechRecognizer import SpeechRecognizer
from CosineSimilarity import CosineSimilarity
from LCS import LCS
import sys
import subprocess
import os
from os.path import expanduser


script = sys.argv[0]
file = sys.argv[1]


home = expanduser("~")

AudioSeg = AudioSegmenting()
SpeechRec = SpeechRecognizer()

PATHPATH = os.path.dirname(file)

address = os.listdir(PATHPATH)



videosType = ('.mkv', '.webm', '.mp4')

for i in address:
    FullPath = home + "/" + PATHPATH + "/" + i + "/"
    for element in os.listdir(FullPath):
        if element.endswith(videosType):
            command = "ffmpeg -i " + FullPath + element + " -vn " + FullPath + "speech.wav"
            subprocess.call(command, shell=True)
            print("ffmpeg Video to audio - done for " + element)

            AudioSeg.AudioSegmenting(FullPath + "speech.wav")
            print("AudioSegemnting - done for " + element)

            SpeechRec.SpeechRecognizer(FullPath + "speech.wav")
            print("SpeechRecognition - done for ")

            Cosine = CosineSimilarity(FullPath + "speech.wav")
            Cosine.CosineSimilarity()
            Cosine.ChunkStartTime()
            Cosine.CosineWriter()
            print("CosineSimilarity - done for " + element)

            lcs = LCS(FullPath + "speech.wav")
            lcs.CosineResultReturner()
            lcs.allConsecutiveSequence()
            lcs.LongestConsecutiveSequence()
            lcs.SuggestedConsecutiveSequence()
            lcs.VideoTimeIdentifier()
            print("LCS - done for " + element)
            LCS.VideoCutter()




















