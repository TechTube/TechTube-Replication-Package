import re
import csv
import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import glob



class LCS:

    def __init__(self, fileName):

        self.fileName = fileName
        self.DirectPath = os.path.dirname(fileName)


    def CosineResultReturner(self):

        self.CosineResult_DocID = []
        self.CosineResult = []

        Cos = []

        with open(self.DirectPath + "/CosineSimilarityResult.csv") as CosF:
            reader = csv.reader(CosF)
            for row in reader:
               Cos.append(row[2])

        maxCos = max(Cos)
        maxCos = float(maxCos)

        with open(self.DirectPath + "/CosineSimilarityResult.csv") as CosineFile:

            reader = csv.reader(CosineFile)

            for row in reader:
                self.CosineResult.append(row[2])
                if float(row[2]) >= maxCos/2:
                    DocNum = str(row[1])
                    DocID = re.findall("(.+?)\.txt", DocNum)
                    self.CosineResult_DocID.append(DocID)



    def allConsecutiveSequence(self):
        run = []
        result = []
        expect = None
        for element in self.CosineResult_DocID:
            element = str(element)
            element = element.replace("[", "")
            element = element.replace("]", "")
            element = element.replace("'", "")
            element = int(element)
            if (element == expect):
                run.append(element)
            else:
                run = [element]
                result.append(run)


            expect = element + 1

        self.Consecutives = []

        for consec in result:
            if len(consec) >= 2:
                self.Consecutives.append(consec)


    def LongestConsecutiveSequence(self):

        if len(self.Consecutives) == 0:
            self.Longest = self.CosineResult

        elif len(self.Consecutives) == 1:
            self.Longest = self.Consecutives

        else:

            self.Longest = []
            if self.Consecutives.count(len(self.Consecutives[0])) != len(self.Consecutives):

                firstLong = max(self.Consecutives, key=len)
                self.Longest.append(firstLong)

                counter = 0

                for moreLong in self.Consecutives:
                    if len(moreLong) == len(firstLong) and moreLong != firstLong:
                        self.Longest.append(moreLong)

                SumConsineList = []
                for cns in self.Longest:
                    SumCosine = 0

                    for long in cns:
                        SumCosine = SumCosine + float(self.CosineResult[long])

                    SumConsineList.append(SumCosine)


                MaxCos = max(SumConsineList)
                self.indexCosMax = SumConsineList.index(MaxCos)
                self.SuggElement = self.Longest[self.indexCosMax]


            else:

                SumCosineList = []
                for cns in self.Consecutives:
                    SumCosine = 0

                    for long in cns:
                        SumCosine = SumCosine + float(self.CosineResult[long])

                    SumCosineList.append(SumCosine)

                MaxCos = max(SumCosineList)
                self.indexCosMax = SumCosineList.index(MaxCos)
                self.SuggElement = self.Consecutives[self.indexCosMax]


    def SuggestedConsecutiveSequence(self):

        self.SuggestedLCS = []

        if len(self.Consecutives) == 0:

            if len(self.CosineResult_DocID) == 1:

                self.SuggestedLCS.append(int(self.CosineResult_DocID[0][0]))

            if len(self.CosineResult_DocID) >= 2:
                sugg = []
                resultsugg = []
                suggest = []
                self.SuggestedLCS = []

                with open(self.DirectPath + "/CosineSimilarityResult.csv") as CosineFile:

                    reader = csv.reader(CosineFile)
                    for row in reader:
                        if float(row[2]) != 0.00000:
                            DocNum = str(row[1])
                            DocID = re.findall("(.+?)\.txt", DocNum)
                            resultsugg.append(float(row[2]))
                            sugg.append(int(DocID[0]))

                resultsugg2 = resultsugg.copy()
                suggMax = max(resultsugg)
                suggest.append(suggMax)
                resultsugg.remove(suggMax)
                suggMax2 = max(resultsugg)
                suggest.append(suggMax2)

                for element in suggest:
                    if element in resultsugg2:
                        index = resultsugg2.index(element)
                        self.SuggestedLCS.append(sugg[index])

                self.SuggestedLCS = sorted(self.SuggestedLCS)





        elif len(self.Consecutives) == 1:
            self.SuggestedLCS = sorted(self.Consecutives[0])

        else:

            medians = []
            self.Consecutives.remove(self.SuggElement)
            LongestMedian = (self.SuggElement[0] + self.SuggElement[-1]) / 2

            mediansDiffList = []
            for lcs in self.Consecutives:
                mediansDiff = abs(LongestMedian - ((lcs[0] + lcs[-1]) / 2))
                mediansDiffList.append(mediansDiff)

            secondConsecutiveSequenceMedian = min(mediansDiffList)
            secondIndex = mediansDiffList.index(secondConsecutiveSequenceMedian)


            if mediansDiffList.count(secondConsecutiveSequenceMedian) == 2:
                secondIndex = mediansDiffList.index(secondConsecutiveSequenceMedian)
                thirdIndex = mediansDiffList.index(secondConsecutiveSequenceMedian, secondIndex + 1, len(mediansDiffList))

                self.SuggestedLCS = self.SuggElement + self.Consecutives[secondIndex] + self.Consecutives[thirdIndex]
                self.SuggestedLCS = sorted(self.SuggestedLCS)


            else:

                self.SuggestedLCS = self.SuggElement + self.Consecutives[secondIndex]
                self.SuggestedLCS = sorted(self.SuggestedLCS)


        return self.SuggestedLCS




    def VideoTimeIdentifier(self):

        StartTimeTextFile = self.SuggestedLCS[0]
        EndTimeTextFile = self.SuggestedLCS[-1]

        StartTimeList = []
        EndTimeList = []

        with open(self.DirectPath + "/CosineSimilarityResult.csv") as CosineFile:
            reader = csv.reader(CosineFile)

            for row in reader:
                StartTimeList.append(row[3])
                EndTimeList.append(row[4])

        self.StartTime = StartTimeList[StartTimeTextFile]
        self.EndTime = EndTimeList[EndTimeTextFile]

        with open(self.DirectPath + "/result.txt", "w") as resultTextFile:
            resultTextFile.write("StartTime=  " + self.StartTime)
            resultTextFile.write("\n")
            resultTextFile.write("EndTime=  " + self.EndTime)

        return self.StartTime, self.EndTime

    def VideoCutter(self):
    
        start = float(self.StartTime)
        intStart = int(start)
    
        end = float(self.EndTime)
        intEnd = int(end)
    
        VideoExtension = ('.264', '.3g2', '.3gp', '.3gp2', '.3gpp', '.3gpp2', '.3mm', '.3p2', '.60d', '.787', '.89', '.aaf', '.aec', '.aep', '.aepx',
        '.aet', '.aetx', '.ajp', '.ale', '.am', '.amc', '.amv', '.amx', '.anim', '.aqt', '.arcut', '.arf', '.asf', '.asx', '.avb',
        '.avc', '.avd', '.avi', '.avp', '.avs', '.avs', '.avv', '.axm', '.bdm', '.bdmv', '.bdt2', '.bdt3', '.bik', '.bin', '.bix',
        '.bmk', '.bnp', '.box', '.bs4', '.bsf', '.bvr', '.byu', '.camproj', '.camrec', '.camv', '.ced', '.cel', '.cine', '.cip',
        '.clpi', '.cmmp', '.cmmtpl', '.cmproj', '.cmrec', '.cpi', '.cst', '.cvc', '.cx3', '.d2v', '.d3v', '.dat', '.dav', '.dce',
        '.dck', '.dcr', '.dcr', '.ddat', '.dif', '.dir', '.divx', '.dlx', '.dmb', '.dmsd', '.dmsd3d', '.dmsm', '.dmsm3d', '.dmss',
        '.dmx', '.dnc', '.dpa', '.dpg', '.dream', '.dsy', '.dv', '.dv-avi', '.dv4', '.dvdmedia', '.dvr', '.dvr-ms', '.dvx', '.dxr',
        '.dzm', '.dzp', '.dzt', '.edl', '.evo', '.eye', '.ezt', '.f4p', '.f4v', '.fbr', '.fbr', '.fbz', '.fcp', '.fcproject',
        '.ffd', '.flc', '.flh', '.fli', '.flv', '.flx', '.gfp', '.gl', '.gom', '.grasp', '.gts', '.gvi', '.gvp', '.h264', '.hdmov',
        '.hkm', '.ifo', '.imovieproj', '.imovieproject', '.ircp', '.irf', '.ism', '.ismc', '.ismv', '.iva', '.ivf', '.ivr', '.ivs',
        '.izz', '.izzy', '.jss', '.jts', '.jtv', '.k3g', '.kmv', '.ktn', '.lrec', '.lsf', '.lsx', '.m15', '.m1pg', '.m1v', '.m21',
        '.m21', '.m2a', '.m2p', '.m2t', '.m2ts', '.m2v', '.m4e', '.m4u', '.m4v', '.m75', '.mani', '.meta', '.mgv', '.mj2', '.mjp',
        '.mjpg', '.mk3d', '.mkv', '.mmv', '.mnv', '.mob', '.mod', '.modd', '.moff', '.moi', '.moov', '.mov', '.movie', '.mp21',
        '.mp21', '.mp2v', '.mp4', '.mp4v', '.mpe', '.mpeg', '.mpeg1', '.mpeg4', '.mpf', '.mpg', '.mpg2', '.mpgindex', '.mpl',
        '.mpl', '.mpls', '.mpsub', '.mpv', '.mpv2', '.mqv', '.msdvd', '.mse', '.msh', '.mswmm', '.mts', '.mtv', '.mvb', '.mvc',
        '.mvd', '.mve', '.mvex', '.mvp', '.mvp', '.mvy', '.mxf', '.mxv', '.mys', '.ncor', '.nsv', '.nut', '.nuv', '.nvc', '.ogm',
        '.ogv', '.ogx', '.osp', '.otrkey', '.pac', '.par', '.pds', '.pgi', '.photoshow', '.piv', '.pjs', '.playlist', '.plproj',
        '.pmf', '.pmv', '.pns', '.ppj', '.prel', '.pro', '.prproj', '.prtl', '.psb', '.psh', '.pssd', '.pva', '.pvr', '.pxv',
        '.qt', '.qtch', '.qtindex', '.qtl', '.qtm', '.qtz', '.r3d', '.rcd', '.rcproject', '.rdb', '.rec', '.rm', '.rmd', '.rmd',
        '.rmp', '.rms', '.rmv', '.rmvb', '.roq', '.rp', '.rsx', '.rts', '.rts', '.rum', '.rv', '.rvid', '.rvl', '.sbk', '.sbt',
        '.scc', '.scm', '.scm', '.scn', '.screenflow', '.sec', '.sedprj', '.seq', '.sfd', '.sfvidcap', '.siv', '.smi', '.smi',
        '.smil', '.smk', '.sml', '.smv', '.spl', '.sqz', '.ssf', '.ssm', '.stl', '.str', '.stx', '.svi', '.swf', '.swi',
        '.swt', '.tda3mt', '.tdx', '.thp', '.tivo', '.tix', '.tod', '.tp', '.tp0', '.tpd', '.tpr', '.trp', '.ts', '.tsp', '.ttxt',
        '.tvs', '.usf', '.usm', '.vc1', '.vcpf', '.vcr', '.vcv', '.vdo', '.vdr', '.vdx', '.veg', '.vem', '.vep', '.vf', '.vft',
        '.vfw', '.vfz', '.vgz', '.vid', '.video', '.viewlet', '.viv', '.vivo', '.vlab', '.vob', '.vp3', '.vp6', '.vp7', '.vpj',
        '.vro', '.vs4', '.vse', '.vsp', '.w32', '.wcp', '.webm', '.wlmp', '.wm', '.wmd', '.wmmp', '.wmv', '.wmx', '.wot', '.wp3',
        '.wpl', '.wtv', '.wve', '.wvx', '.xej', '.xel', '.xesc', '.xfl', '.xlmv', '.xmv', '.xvid', '.y4m', '.yog', '.yuv', '.zeg',
        '.zm1', '.zm2', '.zm3', '.zmv')
    
    
        path = glob.glob(self.DirectPath + "*")
    
        for file in path:
    
            if file.endswith(VideoExtension):
    
                ffmpeg_extract_subclip(file, start, end, targetname= "SegmentedVideo.webm")





































