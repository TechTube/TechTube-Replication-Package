import os

class SpeechRecognizer:

    def SpeechRecognizer(self, fileName):

        self.fileName = fileName

        DirectPath = os.path.dirname(fileName)
        os.mkdir(DirectPath + "/TextFromAudioSegmenting/")
        os.mkdir(DirectPath + "/Scripts/")

        scriptPath = DirectPath + "/Scripts/"
        path = os.listdir(DirectPath + "/Chunks/")
        chunks = []

        counter = 0

        for file in path:
            chunks.append(file)
            counter +=1

        for pyFile in range(0, counter):
            with open(scriptPath + str(pyFile) + ".py", "w") as scriptFile:
                chunk = str(chunks[pyFile])
                chunk = chunk.replace(".wav", ".txt")
                string = "import speech_recognition as sr\nfrom os.path import expanduser\n\nhome = expanduser('~')\n\nr = sr.Recognizer()\nsound = sr.AudioFile('" + scriptPath[:-8] + "Chunks/" + chunks[pyFile] + "'" + ")\n\nwith sound as source:\n    audio = r.record(source)\n\nwith open('" + scriptPath[:-8] + "TextFromAudioSegmenting/" + chunk + "'" + ", 'w') as WritingFile:\n    WritingFile.write(r.recognize_google(audio))\n    WritingFile.close()"
              
                scriptFile.write(string)
                scriptFile.close()

        scripts = os.listdir(scriptPath)
        scriptList = []
        for s_File in scripts:
            ScriptName = str(s_File)
            scriptList.append(ScriptName)

        ScriptTuple = tuple(scriptList)

        return ScriptTuple, scriptPath, counter





