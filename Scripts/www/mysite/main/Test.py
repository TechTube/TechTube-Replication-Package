import csv

def TagFinder(search):
    Tag1 = []
    Address1 = []
    cnt1 = []
    with open("/.csv", "r") as csvFile1:
        reader1 = csv.reader(csvFile1)
        for row1 in reader1:
            Tags1 = row1[1]
            Tag1.append(Tags1)
            Address1.append(row1[0])
        csvFile1.close()
    
    for i1 in Tag1:
        counter1 = 0
        for x1 in search.split():
            if x1 in i1:
                counter1 += 1
        cnt1.append(counter1)
   

    dic1 = dict(zip(Address1, cnt1))
    sorted_dic1 = dict(sorted(dic1.items(), key=lambda x: x[1], reverse=True))

    final = []
    for i in sorted_dic1:
        final.append(i)

    video1 = final[0]


	with open('topics.txt') as f:
    	for line in f:
       	value, *keys = line.strip().split('~')
        	for key in filter(None, keys):
            	if key=='earn':
               	d[key].append(folderpath+value+".txt")

   	for key, value in d.items() :
        print(value)


	word_count_dict={}

	for file in d.values():
    	with open(file,"r") as f:
        	words = re.findall(r'\w+', f.read().lower())
        	counter = counter + Counter(words)
        	for word in words:
            	word_count_dict[word].append(counter)              


	for word, counts in word_count_dict.values():
    	search = search + word


    Tag1 = []
    Address1 = []
    cnt1 = []
    with open("/.csv", "r") as csvFile1:
        reader1 = csv.reader(csvFile1)
        for row1 in reader1:
            Tags1 = row1[1]
            Tag1.append(Tags1)
            Address1.append(row1[0])
        csvFile1.close()
    
    for i1 in Tag1:
        counter1 = 0
        for x1 in search.split():
            if x1 in i1:
                counter1 += 1
        cnt1.append(counter1)
   

    dic1 = dict(zip(Address1, cnt1))
    sorted_dic1 = dict(sorted(dic1.items(), key=lambda x: x[1], reverse=True))

    final = []
    for i in sorted_dic1:
        final.append(i)
    video1 = final[0]
    video2 = final[1]
    video3 = final[2]
    video4 = final[3]
    video5 = final[4]
    
    return video1, video2, video3, video4, video5

