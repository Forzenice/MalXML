import xml.etree.ElementTree as ET
import requests
import time
import statistics

#Request Function into JSON
def getRequest(url):
     return requests.get(url).json()

#Test Variable
seasons = ["Winter","Spring","Summer","Fall"]

seasonList = []
for s in seasons:

    #reterieve total page
    api_url = "https://api.jikan.moe/v4/seasons/2023/" + s
    totalPage = getRequest(api_url)['pagination']['last_visible_page']

    #get all in season
    for x in range(1,totalPage+1):
        api_url = "https://api.jikan.moe/v4/seasons/2023/"+ s + "?page=" + str(x)
        seasonJson = getRequest(api_url)
        for i in range (0,len(seasonJson['data'])):
            seasonList.append(seasonJson['data'][i]['title'])
    time.sleep(5)

#Read MAL XML
root = ET.parse('animelist.xml').getroot()
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
    #startdate = child.find("my_start_date").text
    #enddate = child.find("my_finish_date").text
    status = child.find("my_status").text
    
    if name in seasonList and score != "0" and (status == "Completed" or status =="Watching"):
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

sumarr=[]
print()
for i in animelist:
    print(i.getScore() + " | " + i.getName())

for x in range (0,10):
    sumarr.append(sum(1 for u in animelist if u.getScore() == str(x+1)))

print() 
print("TotalScore : " + str(totalscore))
print("Count : " + str(count))
print("Average Score : " + str(totalscore / count))
print("stdev : " + str(statistics.stdev([int(x.getScore()) for x in animelist])))
print("Median : " + str(statistics.median([int(x.getScore()) for x in animelist])))
print("Mode : " + str(statistics.mode([int(x.getScore()) for x in animelist])))

print()
print("Count")
print("[1  2  3  4  5  6  7  8  9  10]")
print(sumarr)

print("1 to 5")
print(sumarr[0] + sumarr[1] + sumarr[2] + sumarr[3] + sumarr[4])
print("6 to 10")
print(sumarr[5] + sumarr[6] + sumarr[7] + sumarr[8] + sumarr[9])