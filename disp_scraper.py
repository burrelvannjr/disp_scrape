from bs4 import BeautifulSoup
import pandas as pd
import urllib,re,csv,os,urllib2,requests,itertools
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
os.chdir('/Users/burrelvannjr/Desktop/')

ids=[]
names=[]
urls=[]

site = "https://weedmaps.com/dispensaries/in/united-states"
text = requests.get(site).text
soup = BeautifulSoup(text)
soup = soup.encode("utf-8")
id = re.findall(',"wmid":(.*?),"url',soup)
ids.append(id)
names = re.findall('","name":"(.*?)","avatar_url"',soup)
names.append(names)
names.pop(300)
url = re.findall(',"url":"http(.*?)","name":"',soup)
urls.append(url)




names = re.findall('',soup)

names.append(name)
time.append(year)
fullnames.append(name)
fulltime.append(year)


#converts list of lists into a list, concatenating by everything that falls between major , (such as [], [] as two items not minor commas within elements)
names = map(','.join, names)

cities = zip(names,time)

csvfile = "cities" + year + ".csv"

with open(csvfile, "w") as output:
	writer = csv.writer(output, lineterminator='\n')
	#writer.writerow(["Dispensary Name", "Address", "Numbers", "Website"])
	writer.writerow(["v1", "Year"])
	writer.writerows(cities)
