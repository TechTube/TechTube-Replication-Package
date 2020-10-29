from django.shortcuts import render
from .Test import TagFinder
#from .Test2 import TagFinder2
import json
import os
import subprocess
from .CosineSimilarity import CosineSimilarity
from .LCS import LCS
import csv

def index(request):   
    return render(request, 'main/index.html')


def remover(video):
    commandA = "rm -rf " + video + "to-search/"
    subprocess.run(commandA, shell=True)
    commandB = "rm -rf " + video + "CosineSimilarityResult.csv"
    subprocess.run(commandB, shell=True)


def executer(video, search):
    fileP = video + "video.json"
    with open(fileP, 'r') as jsonFile:
        data = json.load(jsonFile)
        URL = 'https://www.youtube.com/embed/' + data['id']
        jsonFile.close()
    os.mkdir(video + "to-search/")
    os.chmod(video + "to-search/", 0o777)
    with open(video + "to-search/query.txt", "w") as queryFile:
        queryFile.write(search)
        queryFile.close()
    os.chmod(video + "to-search/query.txt", 0o777)
    cos = CosineSimilarity(video)
    cos.CosineSimilarity()
    cos.ChunkStartTime()
    cos.CosineWriter()
    lcs = LCS(video)
    lcs.CosineResultReturner()
    lcs.allConsecutiveSequence()
    lcs.LongestConsecutiveSequence()
    lcs.SuggestedConsecutiveSequence()
    sT, eT = lcs.VideoTimeIdentifier()
    startTime = int(float(sT))
    startHourF = int(startTime / 3600)
    startrestF = int(startTime % 3600)
    startMinF = int(startrestF / 60)
    startSecF = int(startrestF % 60)
    startHour = "{0:0=2d}".format(startHourF)
    startMin = "{0:0=2d}".format(startMinF)
    startSec = "{0:0=2d}".format(startSecF)
    endTime = int(float(eT))
    endHourF = int(endTime / 3600)
    endrestF = int(endTime % 3600)
    endMinF = int(endrestF / 60)
    endSecF = int(endrestF % 60)
    endHour = "{0:0=2d}".format(endHourF)
    endMin = "{0:0=2d}".format(endMinF)
    endSec = "{0:0=2d}".format(endSecF)
    commandA = "rm -rf " + video + "to-search/"
    subprocess.run(commandA, shell=True)
    commandB = "rm -rf " + video + "CosineSimilarityResult.csv"
    subprocess.run(commandB, shell=True)

    return URL, startTime, endTime, startHour, startMin, startSec, endHour, endMin, endSec



def result(request):
    

    search = request.POST.get('search')
    
    searchFinal = search
    

    try:
        video1, video2, video3, video4, video5 = TagFinder(searchFinal)


        remover(video1)
        remover(video2)
        remover(video3)
        remover(video4)
        remover(video5)

    
        URL1, startTime1, endTime1, startHour1, startMin1, startSec1, endHour1, endMin1, endSec1  =  executer(video1, searchFinal)
        URL2, startTime2, endTime2, startHour2, startMin2, startSec2, endHour2, endMin2, endSec2  =  executer(video2, searchFinal)
        URL3, startTime3, endTime3, startHour3, startMin3, startSec3, endHour3, endMin3, endSec3  =  executer(video3, searchFinal)
        URL4, startTime4, endTime4, startHour4, startMin4, startSec4, endHour4, endMin4, endSec4  =  executer(video4, searchFinal)
        URL5, startTime5, endTime5, startHour5, startMin5, startSec5, endHour5, endMin5, endSec5  =  executer(video5, searchFinal)
     	        	
        stuff_for_result_page = {
            'search': searchFinal,
            'URL1': URL1,
            'URL2': URL2,
            'URL3': URL3,
            'URL4': URL4,
            'URL5': URL5,

            'startTime1': startTime1,
            'endTime1': endTime1,
            'startTime2': startTime2,
            'endTime2': endTime2,
            'startTime3': startTime3,
            'endTime3': endTime3,
            'startTime4': startTime4,
            'endTime4': endTime4,
            'startTime5': startTime5,
            'endTime5': endTime5,

            'startHour1': startHour1,
            'startMin1': startMin1,
            'startSec1': startSec1,
            'endHour1': endHour1,
            'endMin1': endMin1,
            'endSec1': endSec1,
        
            'startHour2': startHour2,
            'startMin2': startMin2,
            'startSec2': startSec2,
            'endHour2': endHour2,
            'endMin2': endMin2,
            'endSec2': endSec2,

            'startHour3': startHour3,
            'startMin3': startMin3,
            'startSec3': startSec3,
            'endHour3': endHour3,
            'endMin3': endMin3,
            'endSec3': endSec3,

            'startHour4': startHour4,
            'startMin4': startMin4,
            'startSec4': startSec4,
            'endHour4': endHour4,
            'endMin4': endMin4,
            'endSec4': endSec4,

            'startHour5': startHour5,
            'startMin5': startMin5,
            'startSec5': startSec5,
            'endHour5': endHour5,
            'endMin5': endMin5,
            'endSec5': endSec5,
            }

        return render(request, 'main/result.html', stuff_for_result_page)

    except:
        return render(request, 'main/index.html')
       






