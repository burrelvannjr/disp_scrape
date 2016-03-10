from bs4 import BeautifulSoup
import pandas as pd
import urllib,re,csv,os,urllib2,requests,itertools
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
os.chdir('/Users/burrelvannjr/Desktop/')

ids=[]
names=[]
pages=[]
urls=[]
details=[]
itemlist=[]

site = "https://weedmaps.com/dispensaries/in/united-states"
text = requests.get(site).text
soup = BeautifulSoup(text)
soup = soup.encode("utf-8")

items = re.findall(',"wmid":(.*?),"longitude"',soup)

for i in items:
	i = "wmid:" + i
	i = i.encode("utf-8")
	itemlist.append(i)

for i in itemlist:
	id = re.findall('wmid:(.*?),"url',i)
	ids.append(id)
	name = re.findall('","name":"(.*?)","avatar_url"',i)
	names.append(name)
	site = re.findall(',"url":"http(.*?)","name":"',i)
	pages.append(site)

ids = map(','.join, ids)
names = map(','.join, names)
pages = map(','.join, pages)

for page in pages:
	page = "http" + page
	urls.append(page)
	detail = page + "#/details"
	details.append(detail)



disps = zip(ids,names)
	
csvfile = "disp.csv"

with open(csvfile, "w") as output:
	writer = csv.writer(output, lineterminator='\n')
	#writer.writerow(["Dispensary Name", "Address", "Numbers", "Website"])
	writer.writerow(["id", "names"])
	writer.writerows(disps)


