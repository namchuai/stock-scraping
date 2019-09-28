import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import pyrebase
from collections import OrderedDict

config = {
  "apiKey": "AIzaSyA06K1ha81mpfBGKaXqxAd9IIvh35_rSa8",
  "authDomain": "invest-bucket.firebaseapp.com",
  "databaseURL": "https://invest-bucket.firebaseio.com",
  "storageBucket": "invest-bucket.appspot.com"
#   "serviceAccount": "path/to/serviceAccountCredentials.json" // later
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()

# Update stock codes (device should run)
# stockCodes = ["fpt", "ctd"]
# for code in stockCodes:
#     db.child('stockCodes').child(code).set(code)

# print(db.child('stockCodes').get().val())

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
        priceTag = ""
        if len(priceTagUp) > 0:
            priceTag = str(int(float(priceTagUp[0].text) * 1000))
        elif len(priceTagEq) > 0:
            priceTag = str(int(float(priceTagEq[0].text) * 1000))
        elif len(priceTagDown):
            priceTag = str(int(float(priceTagDown[0].text) * 1000))
        db.child("eodPrices").child(key).set(priceTag)
        print("Stock price for " + key + " is " + priceTag)