# web2.py 
#웹서버와 통신
import urllib.request
#웹크롤링 
from bs4 import BeautifulSoup

#파일에 저장(기존 파일이 있으면 첨부)
f = open("c:\\work\\webtoon.txt", "a+", encoding="utf-8")
#페이징 처리가 된 경우 
for i in range(1,6):
    url = "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page=" + str(i)
    data = urllib.request.urlopen(url)
    #검색을 할 객체를 생성
    soup = BeautifulSoup(data, "html.parser")
    cartoons = soup.find_all("td", class_="title")
    #전체 리스트 
    for item in cartoons:
        title = item.find("a").text 
        print( title.strip() )
        f.write(title.strip() + "\n")

f.close() 


                        