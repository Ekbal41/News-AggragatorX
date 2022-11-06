from django.shortcuts import render
import requests
from bs4 import BeautifulSoup




data = requests.get("https://www.risingbd.com/bangladesh")
soup = BeautifulSoup(data.content, 'html5lib')


allimg = soup.find_all('img',{"class": "img-fluid img100"})

titles = []
imgsrcs = []


for img in allimg:
    title = img['title']
    titles.append(title)
    imgsrc = img['src']

    imgsrcs.append(imgsrc)



def index(req):
    
    return render(req, 'news.html', {'titles':titles})
