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


class CosineSimilarity:

    

    def __init__(self, fileName):

        self.fileName = fileName
        self.DirectPath = os.path.dirname(fileName)



    def CosineSimilarity(self):

       
        QueryPath = self.DirectPath + "/to-search/*.txt"
        QRY = glob.glob(QueryPath)
        DocumentsPath = self.DirectPath + "/Process/TextFromAudioSegmenting/*.txt"
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
        
        sw1 = ['a', 'able', 'about', 'above', 'according', 'accordingly', 'across', 'actually', 'after', 'afterwards', 'again', 'against', 'all', 'allow', 'allows', 'almost', 'alone', 'along', 'already', 'also', 'although', 'always', 'am', 'among', 'amongst', 'an', 'and', 'another', 'any', 'anybody', 'anyhow', 'anyone', 'anything', 'anyway', 'anyways', 'anywhere', 'apart', 'appear', 'appreciate', 'appropriate', 'are', 'around', 'as', 'aside', 'ask', 'asking', 'associated', 'at', 'available', 'away', 'awfully', 'b', 'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been', 'before', 'beforehand', 'behind', 'being', 'believe', 'below', 'beside', 'besides', 'best', 'better', 'between', 'beyond', 'both', 'brief', 'but', 'by', 'c', 'came', 'can', 'cannot', 'cant', 'cause', 'causes', 'certain', 'certainly', 'changes', 'clearly', 'co', 'com', 'come', 'comes', 'concerning', 'consequently', 'consider', 'considering', 'contain', 'containing', 'contains', 'corresponding', 'could', 'course', 'currently', 'd', 'definitely', 'described', 'despite', 'did', 'different', 'do', 'does', 'doing', 'done', 'down', 'downwards', 'during', 'e', 'each', 'edu', 'eg', 'eight', 'either', 'else', 'elsewhere', 'enough', 'entirely', 'especially', 'et', 'etc', 'even', 'ever', 'every', 'everybody', 'everyone', 'everything', 'everywhere', 'ex', 'exactly', 'example', 'except', 'f', 'far', 'few', 'fifth', 'first', 'five', 'followed', 'following', 'follows', 'for', 'former', 'formerly', 'forth', 'four', 'from', 'further', 'furthermore', 'g', 'get', 'gets', 'getting', 'given', 'gives', 'go', 'goes', 'going', 'gone', 'got', 'gotten', 'greetings']
        sw2 = ['h', 'had', 'happens', 'hardly', 'has', 'have', 'having', 'he', 'hello', 'help', 'hence', 'her', 'here', 'hereafter', 'hereby', 'herein', 'hereupon', 'hers', 'herself', 'hi', 'him', 'himself', 'his', 'hither', 'hopefully', 'how', 'howbeit', 'however', 'i', 'ie', 'if', 'ignored', 'immediate', 'in', 'inasmuch', 'inc', 'indeed', 'indicate', 'indicated', 'indicates', 'inner', 'insofar', 'instead', 'into', 'inward', 'is', 'it', 'its', 'itself', 'j', 'just', 'k', 'keep', 'keeps', 'kept', 'know', 'knows', 'known', 'l', 'last', 'lately', 'later', 'latter', 'latterly', 'least', 'less', 'lest', 'let', 'like', 'liked', 'likely', 'little', 'll', 'look', 'looking', 'looks', 'ltd', 'm', 'mainly', 'many', 'may', 'maybe', 'me', 'mean', 'meanwhile', 'merely', 'might', 'more', 'moreover', 'most', 'mostly', 'much', 'must', 'my', 'myself', 'n', 'name', 'namely', 'nd', 'near', 'nearly', 'necessary', 'need', 'needs', 'neither', 'never', 'nevertheless', 'new', 'next', 'nine', 'no', 'nobody', 'non', 'none', 'noone', 'nor', 'normally', 'not', 'nothing', 'novel', 'now', 'nowhere', 'o', 'obviously', 'of', 'off', 'often', 'oh', 'ok', 'okay', 'old', 'on', 'once', 'one', 'ones', 'only', 'onto', 'or', 'other', 'others', 'otherwise', 'ought', 'our', 'ours', 'ourselves', 'out', 'outside', 'over', 'overall', 'own', 'p', 'particular', 'particularly', 'per', 'perhaps', 'placed', 'please', 'plus', 'possible', 'presumably', 'probably', 'provides', 'q', 'que', 'quite', 'qv', 'r', 'rather', 'rd', 're', 'really', 'reasonably', 'regarding', 'regardless', 'regards', 'relatively', 'respectively', 'right', 's', 'said', 'same', 'saw', 'say', 'saying', 'says', 'second', 'secondly', 'see', 'seeing', 'seem', 'seemed', 'seeming', 'seems', 'seen', 'self', 'selves', 'sensible', 'sent', 'serious', 'seriously', 'seven', 'several', 'shall', 'she', 'should', 'since', 'six', 'so', 'some', 'somebody', 'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhat', 'somewhere', 'soon', 'sorry', 'specified', 'specify', 'specifying', 'still', 'sub', 'such', 'sup', 'sure']
        sw3 = ['t', 'take', 'taken', 'tell', 'tends', 'th', 'than', 'thank', 'thanks', 'thanx', 'that', 'thats', 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'thence', 'there', 'thereafter', 'thereby', 'therefore', 'therein', 'theres', 'thereupon', 'these', 'they', 'think', 'third', 'this', 'thorough', 'thoroughly', 'those', 'though', 'three', 'through', 'throughout', 'thru', 'thus', 'to', 'together', 'too', 'took', 'toward', 'towards', 'tried', 'tries', 'truly', 'try', 'trying', 'twice', 'two', 'u', 'un', 'under', 'unfortunately', 'unless', 'unlikely', 'until', 'unto', 'up', 'upon', 'us', 'use', 'used', 'useful', 'uses', 'using', 'usually', 'uucp', 'v', 'value', 'various', 've', 'very', 'via', 'viz', 'vs', 'w', 'want', 'wants', 'was', 'way', 'we', 'welcome', 'well', 'went', 'were', 'what', 'whatever', 'when', 'whence', 'whenever', 'where', 'whereafter', 'whereas', 'whereby', 'wherein', 'whereupon', 'wherever', 'whether', 'which', 'while', 'whither', 'who', 'whoever', 'whole', 'whom', 'whose', 'why', 'will', 'willing', 'wish', 'with', 'within', 'without', 'wonder', 'would', 'would', 'x', 'y', 'yes', 'yet', 'you', 'your', 'yours', 'yourself', 'yourselves', 'z', 'zero']

        sw = sw1 + sw2 + sw3

        #lem = WordNetLemmatizer()
       
        
        self.cosineFinal = []
        self.XFinal = []
        self.YFinal = []
        
        

        self.fileAddressFinal = []
        self.QueryAddressFinal = []
        
        for elementX in range(len(QueryText)):
            QAddress = QueryAddress[elementX]
            X = QueryText[elementX]
            X = X.lower()            
            X_token = X.split()
            X_list = []
            
            for words in X_token:
                words = ps.stem(words)
                #wordslem = lem.lemmatize(words)
                X_list.append(words)
                #if words != wordslem:
                    #X_list.append(wordslem)
                
            X_set = {wordX for wordX in X_list if not wordX in sw}

            
            for Speech in SpeechTextList:
                with open(Speech, "r") as Speechfile:

                    reader = Speechfile.read()

                Y = reader
                if Y != "":
                    Y = Y.lower()
                    Y_token = Y.split()
                    Y_list = []
                    
                    for words in Y_token:
                        
                        words = ps.stem(words)
                        Y_list.append(words)
                        #if words != wordslem:
                            #Y_list.append(wordslem)

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
                    self.fileAddressFinal.append(fileAddress1)
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


        chunkPath = self.DirectPath + "/Process/Chunks/*.wav"
        chunkList = sorted(glob.glob(chunkPath))
        durationList = []

        with contextlib.closing(wave.open(self.DirectPath + "/Process/speech.wav", 'r')) as chunkFile:
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
            writingFile.close()

        os.chmod(self.DirectPath + "/CosineSimilarityResult.csv", 0o777)
