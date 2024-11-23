import requests
from bs4 import BeautifulSoup
import difflib
# Step 1: Make a request to the website
# url = "https://example.com"  
# response = requests.get(url)

# Step 2: Parse the HTML content using BeautifulSoup
# soup = BeautifulSoup(response.content, "html.parser")

# Step 3: Find the unordered list(s)
# ul_elements = soup.find_all("ul")

# Step 4: Iterate through the list items and print them
baseUrl = "https://dnd5e.wikidot.com/system:list-all-pages/p/"

searchText = ["background","discipline", "disciplines","feat","lineage","multisubclass",
"poisons","sidekick","siege-equipment","spell","spells","wondrous-items"]

links = []
for i in range (1, 15):
    response = requests.get(baseUrl + str(i))
    soup = BeautifulSoup(response.content, "html.parser")
    ul_elements = soup.find_all("ul")
    for ul in ul_elements:
        list_items = ul.find_all("li")
        for li in list_items:
            a_tags = li.find_all("a")
            for a in a_tags:
                link = a.get("href")
                strLink = str(link)
                matches = difflib.get_close_matches(strLink, searchText)
                if matches:
                    links.append("\'https://dnd5e.wikidot.com" + strLink + "\'")


f = open("all-list-items.txt", "a")
sortedLinks = sorted(links)
for each in sortedLinks:
    f.write(each + "\n")

f.close()