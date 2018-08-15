from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = BeautifulSoup(html, "html.parser")

# for link in bsObj.findAll("a"):
# 	if 'href' in link.attrs:
# 		print(link.attrs['href'])

# 다른 내부 페이지가 아니라 항목페이지만 가져오기
# 1. id가 bodyContent인 div 안에 있다
# 2. URL에는 세미콜론 포함x
# 3. URL은 /wiki/로 시작

for link in bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
	if 'href' in link.attrs:
		print(link.attrs['href'])