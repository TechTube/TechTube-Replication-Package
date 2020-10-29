from AudioSegmenting import AudioSegmenting
from SpeechRecognizer import SpeechRecognizer
from CosineSimilarity import CosineSimilarity
from LCS import LCS
import sys
import subprocess
import os
from os.path import expanduser
from multiprocessing import Pool


script = sys.argv[0]
file = sys.argv[1]


home = expanduser("~")


DIR_HPATH = os.path.dirname(file)
print(DIR_HPATH)
os.mkdir(DIR_HPATH + "/Process/")
New_DIR_PATH = DIR_HPATH + "/Process"

videosType = ('.mkv', '.webm', '.mp4')

try:
    try:
        if file.endswith(videosType):
            command = "ffmpeg -i " + file + " -vn " + New_DIR_PATH + "/speech.wav"
            subprocess.call(command, shell=True)
            print("*****************************************************************************************************************************************************************")
            print("ffmpeg is done for " + DIR_HPATH)
    except:
        print("ffmpge has problem on " + DIR_HPATH)
    
    try:
        AudioSeg = AudioSegmenting()
        AudioSeg.AudioSegmenting(New_DIR_PATH + "/speech.wav")
        print("AudioSegmenting is done for " + DIR_HPATH)

    except:
        print("AudioSegmenting has problem on " + DIR_HPATH)

    try:
        SpeechRec = SpeechRecognizer()
        SCtuple, SCpath, counter = SpeechRec.SpeechRecognizer(New_DIR_PATH + "/speech.wav")
 
  
        def run_process(process):
            os.system('python3 ' + SCpath + '{}'.format(process))

        pool = Pool(processes=counter)
        pool.map(run_process, SCtuple)
 
        print("Speech Recognition is done for " + DIR_HPATH)

    except:
        print("Speech Recognition has problem on " + DIR_HPATH)

except:
    print("file is broken")

print("****************************************************************************************************")


try:
   cos = CosineSimilarity(New_DIR_PATH)
   cos.CosineSimilarity()
   cos.ChunkStartTime()
   cos.CosineWriter()
   print("Cosine Done")    
except:
   print("Cosine has problem")        

try:

   lcs = LCS(New_DIR_PATH)
   lcs.CosineResultReturner()
   lcs.allConsecutiveSequence()
   lcs.LongestConsecutiveSequence()
   lcs.SuggestedConsecutiveSequence()
   lcs.VideoTimeIdentifier()
   print("LCS Done")
except:
   print("LCS has problem")











# SpeechRec = SpeechRecognizer()
# for i in address:
#     FullPath = home + "/" + PATHPATH + "/" + i + "/"
#     for element in os.listdir(FullPath):
#         if element.endswith(videosType):
#             command = "ffmpeg -i " + FullPath + element + " -vn " + FullPath + "speech.wav"
#             subprocess.call(command, shell=True)
#             print("ffmpeg Video to audio - done for " + element)
#
#             AudioSeg.AudioSegmenting(FullPath + "speech.wav")
#             print("AudioSegemnting - done for " + element)
#
#             SpeechRec.SpeechRecognizer(FullPath + "speech.wav")
#             print("SpeechRecognition - done for ")
            #
            # Cosine = CosineSimilarity(FullPath + "speech.wav")
            # Cosine.CosineSimilarity()
            # Cosine.ChunkStartTime()
            # Cosine.CosineWriter()
            # print("CosineSimilarity - done for " + element)
            #
            # lcs = LCS(FullPath + "speech.wav")
            # lcs.CosineResultReturner()
            # lcs.allConsecutiveSequence()
            # lcs.LongestConsecutiveSequence()
            # lcs.SuggestedConsecutiveSequence()
            # lcs.VideoTimeIdentifier()
            # print("LCS - done for " + element)
            # LCS.VideoCutter()




















