import xml.etree.ElementTree as ET

tree = ET.parse('animelist_1672058399_-_4491121.xml')

root = tree.getroot()

totalscore = 0
count = 0

for child in root.findall('anime'):
    name = child.find('series_title').text
    score = child.find('my_score').text
    startdate = child.find("my_start_date").text
    enddate = child.find("my_finish_date").text
    status = child.find("my_status").text
    
    if "2022" in startdate and score != "0" and status == "Completed":
        totalscore += int(score)
        count += 1
        print(name, score)

print (totalscore, count)
print(totalscore / count)