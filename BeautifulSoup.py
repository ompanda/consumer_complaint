#import the library used to query a website
import urllib2
'''
#specify the url
consumer_complaint_site_url = "https://www.consumercomplaints.in"

#Query the website and return the html to the variable 'page'
page = urllib2.urlopen(consumer_complaint_site_url)

#import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup

#Parse the html in the 'page' variable, and store it in Beautiful Soup format
soup = BeautifulSoup(page)
#print(soup.prettify())
all_links = soup.find_all('a')
count=1
for link in all_links:
    href = link.get('href')
#dont include links starts with https as they are for some images
    if 'https://' in href:
        continue

    print(href)

#individual complaint content
    print(consumer_complaint_site_url + href)
    link_content = urllib2.urlopen(consumer_complaint_site_url + href)
#read the content and save the content in a file
    content=link_content.read()
    f = open("data\\PageContent_"+str(count)+".html", "wb")
    f.write(content)
    f.close()
    count=count+1
    link_content_soup= BeautifulSoup(link_content)

#extract complaint information
   # main_div = link_content_soup.find_all("td", class_="compl-text")

    #print(main_div)

#'''
#import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup
#Read all the files in data folder
f = open("C:/ConsumerComplaint/consumer_complaint-master/data/PageContent_3.html")
read_data = f.read()
f.close()

#Create a JSON file
import json
#Get the file object in html format
soup = BeautifulSoup(read_data, "html.parser")
#print(soup.prettify())
complaint_data=[]
#Get the each complaint section table(Contains Title, Complaint,Date,CreatedBy
soupTable=soup.find_all("table", style="width:100%")
#print(soupTable)

#From each table extract the inner text (Title, CreatedBy, Complaint text)
for table in soupTable:
    #print(table.get_text())
    if table.find("td", class_="compl-text")!= -1:
        complTitle = table.find("h4")
        complTitleSoup= BeautifulSoup(str(complTitle), "lxml")
        #print(complTitleSoup.get_text())
        ComplCreatedBy = table.find("td", class_="small")
        ComplCreatedBySoup=BeautifulSoup(str(ComplCreatedBy), "lxml")
        #print(ComplCreatedBySoup.get_text())
        complText = table.find("td", class_="compl-text")
        complTextSoup= BeautifulSoup(str(complText), "lxml")
        #print(complTextSoup.get_text())
        #Append each complaint details in complaint_data array
        complaint_data.append({"Title": complTitleSoup.get_text(),"CreatedBy": ComplCreatedBySoup.get_text(),"Complaint":complTextSoup.get_text()})
#Create a JSON file and dump the complain_data
with open('complaint_data1.json', 'wb') as f1:
    json.dump(complaint_data,f1)

'''
#Get the complaint text
complaint_data=soup.find_all("td",attrs={"class": "compl-text","class": "complaint","class": "small"})
print(complaint_data)
dataJson = []

for data in complaint_data:

'''


