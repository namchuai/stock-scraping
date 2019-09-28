from selenium import webdriver
import time
from bs4 import BeautifulSoup
import pyrebase

config = {
  "apiKey": "AIzaSyA06K1ha81mpfBGKaXqxAd9IIvh35_rSa8",
  "authDomain": "invest-bucket.firebaseapp.com",
  "databaseURL": "https://invest-bucket.firebaseio.com",
  "storageBucket": "invest-bucket.appspot.com"
#   "serviceAccount": "path/to/serviceAccountCredentials.json" // later
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()

browser = webdriver.Chrome()
url = "http://s.cafef.vn/du-lieu-doanh-nghiep.chn"
browser.get(url) #navigate to the page

time.sleep(2)
seeAllButton = browser.find_elements_by_xpath("//*[contains(text(), 'Xem toàn bộ')]")
seeAllButton[1].click()
time.sleep(4)
innerHTML = browser.execute_script("return document.body.innerHTML")
soup = BeautifulSoup(innerHTML, "html.parser")
tables = soup.findChildren('table')
rows = tables[4].findChildren(['th', 'tr'])
for row in rows:
    cells = row.findChildren('td')
    if len(cells) > 0:
        maCk = cells[0].string
        try:
            if maCk.startswith("@"):
                print("not support coin")
            else:
                print("Ma CK: %s" %maCk)
                link = cells[0].find('a').get('href')
                print("http://s.cafef.vn%s" %link)
                print("San: %s" %cells[3].string)
                db.child("stocks").child(maCk).child("name").set(cells[1].string)
                db.child("stocks").child(maCk).child("url").set("http://s.cafef.vn%s" %link)
                db.child("stocks").child(maCk).child("san").set(cells[3].string)
        except:
            print("Exception!!")
