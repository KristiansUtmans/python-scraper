import requests
from bs4 import BeautifulSoup
import time

URL = 'https://skinport.com/market'
page = requests.get(URL)


def getSkins():
    skins = []

    soup = BeautifulSoup(page.content, 'html.parser')

    time.sleep(1)

    results = soup.find(id="content")

    time.sleep(1)

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
        noFloatItems = ["StatTrak™ Music Kit", "Sticker", "Container", "Graffiti", "Music Kit", "Key", "Patch", "Collectible", "Pass"]
        
        # if skin['itemName'] in noFloatItems:
        #     skin['floatValue'] = "None"
        # elif "Agent" in skin['skinRarity']:
        #     skin['floatValue'] = "None"
        # else:

        #     floatValue = skinListing.find("div", class_="WearBar-value")
        #     skin['floatValue'] = floatValue.replace('<div class="WearBar-value">', '')

        skin['price'] = skinListing.find("div", class_="Tooltip-link").text.replace("€", "")

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
    


print(getSkins())
# print(results.prettify())