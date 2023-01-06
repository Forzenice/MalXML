import xml.etree.ElementTree as ET
import requests

#reterieve season.
api_url = "https://api.jikan.moe/v4/seasons/2022/Winter"
response = requests.get(api_url)

response.json()
#convert this to file


tree = ET.parse('animelist Copy.xml')

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
    
    if "2022" in startdate and score != "0" and status == "Completed":
        totalscore += int(score)
        count += 1
        animelist.append(animeScore(name, score))

animelist.sort(key = lambda x: int(x.score),  reverse=True)

print()
for i in animelist:
    print(i.getScore() + " | " + i.getName())

print() 
print("TotalScore : " + str(totalscore))
print("Count : " + str(count))
print("Average Score : " + str(totalscore / count))