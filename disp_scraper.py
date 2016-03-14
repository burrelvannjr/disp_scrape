from bs4 import BeautifulSoup
from BeautifulSoup import SoupStrainer
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
licenses=[]
addresses=[]
cities=[]
states=[]
zips=[]
phones=[]
itemlist2=[]
dates=[]

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
	license = re.findall(',"license_type":"(.*?)","address":"',i)
	licenses.append(license)
	address = re.findall(',"address":"(.*?)","city":"',i)
	addresses.append(address)
	city = re.findall(',"city":"(.*?)","state":"',i)
	cities.append(city)
	state = re.findall(',"state":"(.*?)","zip_code":"',i)
	states.append(state)
	zipc = re.findall(',"zip_code":"(.*?)","phone_number":"',i)
	zips.append(zipc)
	phone = re.findall(',"phone_number":"(.*?)","latitude"',i)
	phones.append(phone)




ids = map(','.join, ids)
names = map(','.join, names)
pages = map(','.join, pages)
licenses = map(','.join, licenses)
addresses = map(','.join, addresses)
cities = map(','.join, cities)
states = map(','.join, states)
zips = map(','.join, zips)
phones = map(','.join, phones)
addresses = [a.replace('CALL FOR VERIFICATION', 'N/A') for a in addresses]
cities = [c.replace('CALL FOR VERIFICATION', 'N/A') for c in cities]
zips = [z.replace('  OPEN 24/7', '') for z in zips]
zips = [z.replace('CALL FOR VERIFICATION', 'N/A') for z in zips]
phones = [p.replace('(', '') for p in phones]
phones = [p.replace(')', '') for p in phones]
phones = [p.replace('-', '') for p in phones]
phones = [p.replace(' ', '') for p in phones]



for page in pages:
	page = "http" + page
	urls.append(page)
	detail = page + "#/details"
	details.append(detail)


startpoint = 0
for det in details:
	newpage = det
	text = requests.get(newpage).text
	soup = BeautifulSoup(text)
	soup2 = soup.encode("utf-8")
	divs = soup.find_all('div', attrs={'class':'details-card-item'})
	date = divs[-1]
	date = date.encode("utf-8")
	date = re.findall('</div><div class="details-card-item-data">(.*?)</div></div>',date)
	dates.append(date)
	itemlist2.append(soup2)
	print(startpoint)
	startpoint += 1


dates = map(','.join, dates)


disps = zip(ids,names,addresses,cities,states,zips,phones,dates,licenses,details)
	
csvfile = "disp_scrape/data/disp.csv"

with open(csvfile, "w") as output:
	writer = csv.writer(output, lineterminator='\n')
	#writer.writerow(["Dispensary Name", "Address", "Numbers", "Website"])
	writer.writerow(["id", "names", "addresses", "cities", "states", "zips", "phones", "dates", "licences", "websites"])
	writer.writerows(disps)


