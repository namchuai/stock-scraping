import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import pyrebase
from collections import OrderedDict

def tryToGetThumbnailByBrief(soup):
    try:
        thumbnailUrl = soup.find("img", {"class": "img"})['src']
        return thumbnailUrl
    except Exception as e:
        return ""

def tryToGetThumbnailByAvatar(soup):
    try:
        avatar = soup.find_all("div", class_="avartar")[0]
        return avatar.img.get('src')
    except Exception as e:
        return ""

def getCompanyThumbnail(soup):
    thumbnailUrlBrief = tryToGetThumbnailByBrief(soup)
    thumbnailUrlAvatar = tryToGetThumbnailByAvatar(soup)

    if thumbnailUrlBrief != "":
        return thumbnailUrlBrief
    elif thumbnailUrlAvatar != "":
        return thumbnailUrlAvatar
    else:
        return ""

config = {
  "apiKey": "AIzaSyA06K1ha81mpfBGKaXqxAd9IIvh35_rSa8",
  "authDomain": "invest-bucket.firebaseapp.com",
  "databaseURL": "https://invest-bucket.firebaseio.com",
  "storageBucket": "invest-bucket.appspot.com"
#   "serviceAccount": "path/to/serviceAccountCredentials.json" // later
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()

## Query stock codes and update price back to firebase
dict = db.child("stocks").get().val()

for key, value in dict.items():
    print("===Getting stock price for " + key)
    url = db.child("stocks").child(key).child("url").get().val()
    if url is None:
        print("Url for " + key + " is null! Need to add!") 
    else:
        print("Url is: " + url)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        priceTagUp = soup.find_all("div", class_="dltlu-point up")
        priceTagEq = soup.find_all("div", class_="dltlu-point eq")
        priceTagDown = soup.find_all("div", class_="dltlu-point down")
        priceTagFl = soup.find_all("div", class_="dltlu-point fl")
        thumbnailUrl = getCompanyThumbnail(soup)
        priceTag = ""
        if len(priceTagUp) > 0:
            priceTag = str(int(float(priceTagUp[0].text) * 1000))
        elif len(priceTagEq) > 0:
            priceTag = str(int(float(priceTagEq[0].text) * 1000))
        elif len(priceTagDown):
            priceTag = str(int(float(priceTagDown[0].text) * 1000))
        elif len(priceTagFl):
            priceTag = str(int(float(priceTagFl[0].text) * 1000))
        if priceTag == "":
            print("Cannot get price: " + url)
        else:
            print("Price: " + priceTag)
        if thumbnailUrl == "":
            print("Cannot get thumbnail: " + url)
        elif thumbnailUrl == None:
            thumbnailUrl = ""
            print("Cannot get thumbnail: " + url)
        else:
            print("thumbnailUrl: " + thumbnailUrl)
        db.child("eodPrices").child(key).set(priceTag)
        db.child("stocks").child(key).child("thumbnail").set(thumbnailUrl);
        # print("Stock price for " + key + " is " + priceTag)
