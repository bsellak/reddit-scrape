import requests
from bs4 import BeautifulSoup

#Don't hardcode this link make it a selection afterwards
url = "https://www.reddit.com/r/EarthPorn/"
response = requests.get(url , headers = {'User-agent':'Bilals Bot'})
html = response.content

soup = BeautifulSoup(html, "lxml")

#This command finds the siteTable division in the html file for the website
#always use this its super useful lets you look by ID
entry_table = soup.find("div", {"id": "siteTable"})


#Next, we are gonna go through with a for loop and check for all the little
#things we need for our script through the classes

list_entry = entry_table.find_all('div',  attrs= {"data-type": "link"})
for entry in list_entry:
    #gonna hardcode a upvote limit but this should be by user discretion or just
    #top photos idk yet
