from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import glob, os
import re
import csv
import wave
import contextlib
import nltk

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

class CosineSimilarity:


    def __init__(self, fileName):

        self.fileName = fileName
        self.DirectPath = os.path.dirname(fileName)



    def CosineSimilarity(self):

        QueryPath = self.DirectPath + "/to-search/*.txt"
        QRY = glob.glob(QueryPath)

        DocumentsPath = self.DirectPath + "/TextFromAudioSegmenting/*.txt"
        DOC = sorted(glob.glob(DocumentsPath))

        QueryTextList = []
        for element in QRY:
            QueryTextList.append(element)

        QueryText = []
        QueryAddress = []
        for Query in QueryTextList:
            with open(Query, "r") as Queryfile:
                reader = Queryfile.read()
            QueryText.append(reader)
            QueryAddress.append(Queryfile)

        SpeechTextList = []
        for element in DOC:
            SpeechTextList.append(element)

        ps = PorterStemmer()
        sw = stopwords.words('english')
        lem = WordNetLemmatizer()

        self.cosineFinal = []
        self.XFinal = []
        self.YFinal = []

        self.fileAddressFinal = []
        self.QueryAddressFinal = []

        for elementX in range(len(QueryText)):
            QAddress = QueryAddress[elementX]
            X = QueryText[elementX]
            X = X.lower()
            X_token = word_tokenize(X)
            X_list = []

            for words in X_token:
                words = ps.stem(words)
                wordslem = lem.lemmatize(words)
                X_list.append(words)
                if words != wordslem:
                    X_list.append(wordslem)

            X_set = {wordX for wordX in X_list if not wordX in sw}

            for Speech in SpeechTextList:
                with open(Speech, "r") as Speechfile:

                    reader = Speechfile.read()

                Y = reader
                if Y != "":
                    Y = Y.lower()
                    Y_token = word_tokenize(Y)
                    Y_list = []

                    for words in Y_token:
                        words = ps.stem(words)
                        wordslem = lem.lemmatize(words)
                        Y_list.append(words)
                        if words != wordslem:
                            Y_list.append(wordslem)

                    Y_set = {wordY for wordY in Y_list if not wordY in sw}

                    rvector = X_set.union(Y_set)

                    l1 = []
                    l2 = []

                    for w in rvector:
                        if w in X_set:
                            l1.append(1)
                        else:
                            l1.append(0)
                        if w in Y_set:
                            l2.append(1)
                        else:
                            l2.append(0)

                    c = 0

                    for i in range(len(rvector)):
                        c += l1[i] * l2[i]

                    cosine = (c / float((sum(l1) * sum(l2)) ** 0.5))
                    self.cosineFinal.append(cosine)

                    fileAddress1 = str(Speechfile)
                    fileAddressClear = re.findall("TextFromAudioSegmenting/(.*?)'", fileAddress1)
                    fileAddress = str(fileAddressClear)
                    fileAddress = fileAddress.replace("'", "")
                    fileAddress = fileAddress.replace("[", "")
                    fileAddress = fileAddress.replace("]", "")
                    self.fileAddressFinal.append(fileAddress)

                    self.XFinal.append(X)
                    self.YFinal.append(Y)

                    QAddress1 = str(QAddress)
                    QAddress1Clear = re.findall("to-search/(.*?)' mode='r'", QAddress1)
                    QAddressF = str(QAddress1Clear)
                    QAddressF = QAddressF.replace("'", "")
                    QAddressF = QAddressF.replace("[", "")
                    QAddressF = QAddressF.replace("]", "")
                    self.QueryAddressFinal.append(QAddressF)


        return self.QueryAddressFinal, self.fileAddressFinal, self.cosineFinal, self.DirectPath


    def ChunkStartTime(self):
        self.ChunkStartTime = []
        FirstStart = 0
        self.ChunkStartTime.append(FirstStart)


        chunkPath = self.DirectPath + "/Chunks/*.wav"
        chunkList = sorted(glob.glob(chunkPath))
        durationList = []

        with contextlib.closing(wave.open(self.fileName, 'r')) as chunkFile:
            frames = chunkFile.getnframes()
            rate = chunkFile.getframerate()
            TotalDuration = frames / float(rate)


        for element in chunkList:
            with contextlib.closing(wave.open(element, 'r')) as chunkFile:
                frames = chunkFile.getnframes()
                rate = chunkFile.getframerate()
                duration = frames / float(rate)
                durationList.append(duration)
        cnt = 0

        for element in durationList:
            expander = self.ChunkStartTime[cnt]
            expander += element
            self.ChunkStartTime.append(expander)
            cnt += 1

        silence = TotalDuration - self.ChunkStartTime[-1]
        silenceChunk = (silence/(cnt-1))

        self.ChunkEndTime = []
        FirstEnd = 0
        self.ChunkEndTime.append(FirstEnd)
        cnt = 0
        for element in durationList:
            expander = self.ChunkEndTime[cnt]
            expander += element
            expander += silenceChunk
            self.ChunkEndTime.append(expander)
            cnt += 1

        self.ChunkEndTime.remove(0)
        self.ChunkEndTime.pop()
        endTime = self.ChunkEndTime[-1] + durationList[-1]
        self.ChunkEndTime.append(endTime)


        return self.ChunkStartTime, self.ChunkEndTime

    def CosineWriter(self):
        with open(self.DirectPath + "/CosineSimilarityResult.csv", "w") as writingFile:
            writer = csv.writer(writingFile)
            writer.writerows(zip(self.QueryAddressFinal, self.fileAddressFinal, self.cosineFinal, self.ChunkStartTime, self.ChunkEndTime))









































