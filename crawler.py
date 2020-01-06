import requests
from bs4 import BeautifulSoup

def trade(max_pages):
    page=1;
    while page<= max_pages:
        url='https://www.oyorooms.com/oyos-in-bangalore?adults=1&checkin=03%2F09%2F2017&checkout=04%2F09%2F2017&children=0&city=bangalore&country=india&guests=1&latitude=null&location=Bangalore&longitude=null&page='+str(page)+'&rooms=1&searchType=city'
        source_code=requests.get(url)
        plain_text=source_code.text
        soup=BeautifulSoup(plain_text,"html.parser")
        for link in soup.findAll('a', {'class': 'newHotelCard__hotelMeta'}):
            href="https://www.oyorooms.com" + link.get('href')
            title=link.get('title')
            #print(href)
            #print(title)
            get_single_title(href)
        page+=1

def get_single_title(i_url):
    source_code=requests.get(i_url)
    plain_text=source_code.text
    soup=BeautifulSoup(plain_text,"html.parser")
    for i in soup.findAll('h1',{'class':'hero__byline gallery__heading__byLine'}):
        print(i)
    #for link in soup.findAll('span'):
     #   href = "https://www.oyorooms.com" + link.get('href')
      #  print(href)

trade(1)
