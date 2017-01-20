import requests
import time
import urllib
from bs4 import BeautifulSoup as bs


# Don't hardcode this link make it a selection afterwards!!!!
subreddit = input("Please Input Your Subreddit: ")
while "Porn" not in subreddit:
    subreddit = input("Not a correct Subreddit. Try Again:")

# Getting the URL of the Subreddit and all its HTML
url = "https://www.reddit.com/r/" + subreddit + "/"
response = requests.get(url, headers={'User-agent': 'Reddit Image Bot'})
html = response.content

soup = bs(html, "lxml")


# This command finds the siteTable division in the html file for the website
# always use this its super useful lets you look by ID
entry_table = soup.find("div", {"id": "siteTable"})


# Next, we are gonna go through with a for loop and check for all the little
# things we need for our script through the classes
list_of_links = []
list_of_titles =[]
list_entry = entry_table.find_all('div',  attrs={"data-type": "link"})
for entry in list_entry:
    data_link = entry.attrs["data-url"]
    name_div = entry.find('div', class_="entry unvoted")
    name_parent = name_div.find('p')
    data_title = name_parent.find('a').string
    list_of_links.append(data_link)
    list_of_titles.append(data_title)


# Replacing stuff that can't be in file names
list_of_titles = [title.replace('"','').replace("/",'').replace("[OC]",'').replace("(OC)","").replace("|","") for title in list_of_titles]

# A counter for the loop
imagecount = 0

for string in list_of_links:
    if "jpg" in string:
        file = open( list_of_titles[imagecount] + '.jpg', 'wb')
        file.write(requests.get(string).content)
        file.close()
    elif "png" in string:
        file = open( list_of_titles[imagecount] +'.png', 'wb')
        file.write(requests.get(string).content)
        file.close()
    imagecount = imagecount + 1
print("All Done!")
