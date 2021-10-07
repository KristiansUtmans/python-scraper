import requests
from bs4 import BeautifulSoup
import time
import csv


URL = 'https://skinport.com/market'
page = requests.get(URL)


def getSkins():
    skins = []

    soup = BeautifulSoup(page.content, 'html.parser')

    time.sleep(1)

    results = soup.find(id="content")

    skinListings = results.find_all("div", class_="CatalogPage-item CatalogPage-item--grid")

    time.sleep(1)

    for skinListing in skinListings:
        skin = {}


        skin['fullInfo'] = skinListing.find("a", class_="ItemPreview-href").text
        skin['itemName'] = skinListing.find("div", class_="ItemPreview-itemTitle").text
        skin['skinName'] = skinListing.find("div", class_="ItemPreview-itemName").text
        skin['skinRarity'] = skinListing.find("div", class_="ItemPreview-itemText").text
        
        try:
            skin['floatValue'] = skinListing.find("div", class_="WearBar-value").text.replace("<div class=\"WearBar-value\">", "").replace("</div>","")
        except:
            skin['floatValue'] = "None"

        skin['price'] = skinListing.find("div", class_="Tooltip-link").text.replace("€", "").replace(",", "")

        tradeTop = skinListing.find("div", class_="ItemPreview-top")
        if tradeTop.div.text == "Tradeable":
            skin['tradeLock'] = "Tradeable"
        else:
            skin['tradeLock'] = tradeTop.div.text.replace("in ", "")
        

        try:
            skin['skinDiscount'] = skinListing.find("div", class_="GradientLabel ItemPreview-discount").text.replace("- ", "")
        except:
            skin['skinDiscount'] = "None"


        skinWebpage = skinListing.find("a", class_="ItemPreview-link")["href"]
        skin['webpage'] = f"https://skinport.com{skinWebpage}"

        skin['previewImage'] = skinListing.find("img")["src"]


        skins.append(skin)

    time.sleep(1)
    
    return skins
    
def save_data(skins):
    with open("data/skins_market.csv", 'w', encoding='UTF-8', newline="") as f:
        colon_name = ['fullInfo', 'itemName', 'skinName', 'skinRarity', 'floatValue', 'price', 'tradeLock', 'skinDiscount', 'webpage', 'previewImage']
        w = csv.DictWriter(f, fieldnames= colon_name)
        w.writeheader()
        for skin in skins:
            w.writerow(skin)

save_data(getSkins())



