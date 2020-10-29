import speech_recognition as sr
import glob
import os

class SpeechRecognizer:

    def SpeechRecognizer(self, fileName):

        self.fileName = fileName

        DirectPath = os.path.dirname(fileName)
        os.mkdir(DirectPath + "/TextFromAudioSegmenting/")

        FileAddress = []

        for chunk in sorted(glob.glob(DirectPath + "/Chunks/*.wav")):
            FileAddress.append(chunk)

        count = 0
        Recognizer = sr.Recognizer()

    
        for chunkFile in FileAddress:

            file = sr.AudioFile(chunkFile)

            try:
                with file as source:
                    audio = Recognizer.record(source)

                with open(DirectPath + "/TextFromAudioSegmenting/{0:04}.txt".format(count), "w") as WritingFile:
                    WritingFile.write(Recognizer.recognize_google(audio))

                count += 1

            except:
                print("last file does not have the speech" + str(count))



