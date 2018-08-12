from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")

# # 자식
# for child in bsObj.find("table", {"id":"giftList"}).children:
# 	print(child)

# # 자손
# for child in bsObj.find("table", {"id":"giftList"}).descendants:
# 	print(child)

# 형제
for sibling in bsObj.find("table", {"id":"giftList"}).tr.next_siblings:
	print(sibling)

# 자식 > 바로 밑, 자손 > 밑에 전부다
# table에 타이틀 행이 포함되는지가 child와 next_siblings 함수의 차이점
