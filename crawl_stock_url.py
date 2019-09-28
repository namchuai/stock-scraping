import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = "http://s.cafef.vn/du-lieu-doanh-nghiep.chn"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
print(soup.text)
# priceTag = soup.find_all("div", class_="dltlu-point up")[0]
# db.child("eodPrices").child(value).set(str(int(float(priceTag.text) * 1000)))
# print("Stock price for " + value + " is " + str(int(float(priceTag.text) * 1000)) + "VND")