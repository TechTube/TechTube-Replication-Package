import os
import re


path = "/Data/data/"

dirname = os.path.dirname(path)
files = os.listdir(path)

counter = 0
for i in sorted(files):
	
	new_Path = path + i + "/to-search/Query.txt"

	with open(new_Path, "r") as queryfile:
		reader = queryfile.read()
		x = re.findall("(.+?)	", reader)
		# reader = re.sub("	", " ", reader)
		x = str(x)
		x = x.replace("'", "")
		x = x.replace("[", "")
		x = x.replace("]", "")
		x = x.replace('"', '')
		x = x.replace("x", "_")
		# queryfile.close()
	
		counter += 1


print(counter)



cnt = 0
with open("QueriesBL.txt", "r") as file:
	for i in file:
		cnt += 1

print(cnt)
