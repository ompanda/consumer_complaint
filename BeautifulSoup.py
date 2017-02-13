#import the library used to query a website
import urllib2
#import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup
#Create a JSON file
import json

def get_complaints():
    consumer_complaint_site_url = "https://www.consumercomplaints.in"
    complaints = get_url_content(consumer_complaint_site_url,250)
    write_to_JSON_file('all_consumer_complaints.json',complaints)

    print("Crawled page successfuly")

def is_valid_url(url):
    # dont include links starts with https as they are for some images
    # ignore b
    if 'https://' in url:
        return False

    #ignore self links
    if '#' in url:
        return False

    #ignore user profiles
    if '/profile' in url:
        return False

    if '/bycategory' in url:
        return False


    return True

def get_paged_content(base_url,site_url):
    conmplaints = []
    page = urllib2.urlopen(site_url)

    # Parse the html in the 'page' variable, and store it in Beautiful Soup format
    soup = BeautifulSoup(page)
    # print(soup.prettify())
    main_div_content = soup.find("div", class_="col-wrapper")

    print(main_div_content.prettify())

    all_links = main_div_content.find_all('a')
    count = 1
    for link in all_links:
        href = link.get('href')

        if not is_valid_url(href):
            continue

        if '/page/' in href:
            continue

        print(href)
        # individual complaint content
        print(base_url + href)

        try:

            link_content = urllib2.urlopen(base_url + href)

            # parse individual page content
            individual_page_complaints = read_page_content(link_content)
            conmplaints.append(individual_page_complaints)

            print ("individual complaints length {0}",len(individual_page_complaints))

            write_to_JSON_file('single_page_consumer_complaints.json', individual_page_complaints)

            print ("Complaints - ")
            print(conmplaints)
        except:
            print("exception in getting page content.Now will continue to next page")

    return conmplaints

def get_url_content(site_url,total_page_count):
    complaints = []
    page =1

    while(page < total_page_count):
        url=site_url
        if page != 1:
            url = "{0}/page/{1}".format(site_url, page)

        print ('Getting complaints for page - '.format(page))
        page_content =  get_paged_content(site_url,url)
        complaints.append(page_content)

        write_to_JSON_file('paged_consumer_complaints.json', page_content)

        page = page+1

    return complaints

def read_page_content(page_content):
    #Get the file object in html format
    soup = BeautifulSoup(page_content, "html.parser")
    #print(soup.prettify())
    page_data=[]
    #Get the each complaint section table(Contains Title, Complaint,Date,CreatedBy
    soupTable=soup.find_all("table", style="width:100%")
    #print(soupTable)

    #From each table extract the inner text (Title, CreatedBy, Complaint text)
    for table in soupTable:
        #print(table.get_text())rr
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
            page_data.append({"Title": complTitleSoup.get_text(),"CreatedBy": ComplCreatedBySoup.get_text(),"Complaint":complTextSoup.get_text()})

    return page_data;

def write_to_JSON_file(file_name,data):
    #Create a JSON file and dump the complain_data
    with open(file_name, 'a+') as f1:
        json.dump(data,f1)


get_complaints()