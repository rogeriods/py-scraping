from bs4 import BeautifulSoup

import requests

# Get the content from my URL request
html = requests.get("https://www.gov.br/receitafederal/pt-br/assuntos/noticias").content

# Interprets the HTML document
soup = BeautifulSoup(html, "html.parser")

# Extract all news title from a page URL
temperature = soup.find_all("h2", class_="titulo")

# Treat data to print
titles = []
for t in temperature:
    children = t.findChildren("h2")
    titles.append(t.text.replace("\n", ""))

for value in titles:
    print("- {}".format(value))
