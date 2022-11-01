from bs4 import BeautifulSoup
import urllib.request

with open("index.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

print(soup.title)

print(soup.title.name)

print(soup.title.string)

print(soup.title.parent)

print(soup.title.parent)

soup_find = soup.find("div")

print(soup_find)

soup_find_all = soup.find_all("div")

print(soup_find_all)

soup.find('a').get('href')
soup.find('a').get_text()

site_names = soup.find_all('a') # 모든 a 태그

for name in site_names:
	print(name.get('href'))
	print(name.get_text())

id1 = soup.select('div#id1') # [id1]
class1 = soup.select('div.class1') # [class1]
class1_a = soup.select('div.class1 a')

with open("contents.html", 'r', encoding="UTF-8") as fp:
    soup2 = BeautifulSoup(fp, 'html.parser') 

title  = soup2.find('p', { 'id': 'title' })
contents = soup2.find_all('p', { 'id': 'content' })

print(title)
print(contents)

for content in contents:
    print(content.get_text())

# 인터넷 웹페이지에서 가져오기
