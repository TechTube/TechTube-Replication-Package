import json
import sys
import csv
import os
from os.path import expanduser

script = sys.argv[0]
file = sys.argv[1]

home = expanduser('~')
path = os.path.dirname(file)
directories = os.listdir(path)

id = []
tag = []
address = []
for directory in directories:
    new_PATH = home + "/" + path + "/" + directory + "/"
    for DIR in sorted(os.listdir(new_PATH)):
        NEW_DIR = new_PATH + DIR + "/"
        address.append(NEW_DIR)
        for el in os.listdir(NEW_DIR):
            if el.endswith(".json"):
                with open(NEW_DIR + el, 'r') as jsonFile:
                    data = json.load(jsonFile)
                    youtube_id = 'https://www.youtube.com/embed/' + data['id']
                    id.append(youtube_id)
                    tags = data['tags']
                    if tags == []:
                        tags = data['description']
                        tag.append(str(tags).lower().split())
                    else:
                        tag.append(str(tags).lower())

with open(path + "/ID_TAGS.csv", 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(zip(address, tag))
    csvFile.close()


