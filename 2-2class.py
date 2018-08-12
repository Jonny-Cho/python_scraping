from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "html.parser")

nameList = bsObj.findAll("span", {"class":"green"})
# nameList = bsObj.findAll(text="the prince")
for name in nameList:
	print(name.get_text())

# print(len(nameList))





#get_text() : 현재 문서에서 모든 태그를 제거하고 텍스트만 들어 있는 문자열 반환
#findAll(tag, attributes, recursive, text, limit, keywords)