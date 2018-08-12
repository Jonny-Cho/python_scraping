from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")

images = bsObj.findAll("img", {"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})
for image in images:
	print(image["src"])


# 제품이미지만 출력하고 싶을때
# .findAll("img")로 모든 이미지 태그를 가져오면 되지않나?
# 모든 이미지 태그가 모두 제품이미지라고 확신할 수 없다
# 정규표현식 사용
# ../img/gifts/img로 시작 .jpg로 끝나는 이미지의 상대 경로만 출력