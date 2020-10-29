from django.shortcuts import render
import csv


def index(request):
    return render(request, 'VideoSeg/index.html')


def result(request):

    search = request.POST.get('search')

    searchQuery = str(search)
    words = searchQuery.split()



    with open("./VideoSeg/DataBase.csv", "r") as csvFile:
        reader = csv.reader(csvFile)

        tagCounter = []
        videoURL=[]
        videoStartTime = []
        videoEndTime = []

        for row in reader:
            count = 0
            videoURL.append(row[1])
            videoStartTime.append(row[2])
            videoEndTime.append(row[3])
            for word in words:
                if word in row[4]:
                    count += 1

            tagCounter.append(count)

        MaximumMatch = max(tagCounter)
        index = tagCounter.index(MaximumMatch)
        source = videoURL[index]
        StartTime = videoStartTime[index]
        EndTime = videoEndTime[index]
        csvFile.close()

    startTime = int(float(StartTime))
    startMin = int(startTime/60)
    startHour = int(startMin/60)
    startSec = (startTime - (startMin * 60)) - (startHour * 3600)

    endTime = int(float(EndTime))
    endMin = int(endTime / 60)
    endHour = int(endMin / 60)
    endSec = (endTime - (endMin * 60)) - (endHour * 3600)

    stuff_for_result_page = {
        'search': search,
        'URL': source,

        'startTime': startTime,
        'endTime': endTime,

        'endMin': endMin,
        'endHour': endHour,
        'endSec': endSec,

        'startMin': startMin,
        'startHour': startHour,
        'startSec': startSec,

    }


    return render(request, 'VideoSeg/result.html', stuff_for_result_page)







