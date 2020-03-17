import requests
import urllib.request
import os
from PIL import Image
import shutil
from bs4 import BeautifulSoup

LeSite = "https://mangakakalot.com/"

os.chdir("C://Users/new pc/Desktop/Manga")

def Navigate(url):
    if url != "Fin du Manga":
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        ListeLiens=image(soup)
    return [soup,ListeLiens]


def image(soup):
    ListeLiens = []
    Im = soup.findAll('img')
    for elt in Im:
        if 'class' in elt.attrs and elt['class']==["img-responsive"]:
            var = elt['data-src']
            ListeLiens.append(var)
    return ListeLiens


def Next(soup,url):
    uuu=isole1(url)
    bbb=isole(url)
    NextUrl=uuu+str(bbb+1)
    a=str(NextUrl)
    if image(soup) == []:
        NextUrl = "Fin du Manga"
        print(NextUrl)
    else:
        print(NextUrl)
    return NextUrl

def isole(url):
    bac=url.split('/')[-1]
    return int(bac)


def isole1(url):
    url2 = url.split(str(isole(url)))[0]
    return url2