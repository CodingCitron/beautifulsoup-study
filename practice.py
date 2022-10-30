from bs4 import BeautifulSoup
import urllib.request

with open("index.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

print(soup.title.name)