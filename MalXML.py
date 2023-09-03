import xml.etree.ElementTree as ET
import requests
import json

#reterieve season.

api_url = "https://api.jikan.moe/v4/seasons/2023/Winter"
response = requests.get(api_url)
seasonJson = response.json()
totalPage = seasonJson['pagination']['last_visible_page']

seasonList = []
for x in range(1,totalPage+1):
    api_url = "https://api.jikan.moe/v4/seasons/2023/Winter?page=" + str(x)
    response = requests.get(api_url)
    seasonJson = response.json()
    for i in range (0,len(seasonJson['data'])):
        seasonList.append(seasonJson['data'][i]['title'])

print("Season List Len")
print(len(seasonList))
print("--------------------")
#convert this to file

tree = ET.parse('animelist.xml')
root = tree.getroot()
totalscore = 0
count = 0

class animeScore:
    
    def __init__(self, name, score):
        self.name = name
        self.score = score
        #self.season = season
    
    def getName(self):
        return str(self.name)

    def getScore(self):
        return str(self.score)


    
animelist = []

for child in root.findall('anime'):
    name = child.find('series_title').text
    score = child.find('my_score').text
    startdate = child.find("my_start_date").text
    enddate = child.find("my_finish_date").text
    status = child.find("my_status").text
    
    if name in seasonList and score != "0" and status == "Completed":
        totalscore += int(score)
        count += 1
        animelist.append(animeScore(name, score))

    '''
    if "2022" in startdate and score != "0" and status == "Completed":
        totalscore += int(score)
        count += 1
        animelist.append(animeScore(name, score))
    '''

animelist.sort(key = lambda x: int(x.score),  reverse=True)


print()
for i in animelist:
    print(i.getScore() + " | " + i.getName())

print() 
print("TotalScore : " + str(totalscore))
print("Count : " + str(count))
print("Average Score : " + str(totalscore / count))
