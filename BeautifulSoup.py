#import the library used to query a website
import urllib2

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
for link in all_links:
    href = link.get('href')

#dont include links starts with https as they are for some images
    if 'https://' in href:
        continue

    print(href)

#individual complaint content
    link_content = urllib2.urlopen(consumer_complaint_site_url + href)
    link_content_soup= BeautifulSoup(link_content)

#extract complaint information
    main_div = link_content_soup.find_all("td", class_="compl-text")
    print(main_div)


