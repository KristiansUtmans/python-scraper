import requests
from bs4 import BeautifulSoup

URL = 'https://skinport.com/market?pricegt=100&sort=percent&order=desc'
page = requests.get(URL)


def getSkins():
    skins = []

    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find(id="content")

    skinListings = results.find_all("div", class_="CatalogPage-item CatalogPage-item--grid")


    for skinListing in skinListings:
        weaponName = skinListing.find("div", class_="ItemPreview-itemTitle")
        skinName = skinListing.find("div", class_="ItemPreview-itemName")
        floatValue = skinListing.find("div", class_="WearBar-value")
        skinPrice = skinListing.find("div", class_="Tooltip-link")
        skinDiscount = skinListing.find("div", class_="GradientLabel ItemPreview-discount")
    

        print(skinDiscount.span)
        print("\n")
    # print(weaponName.text)
    # print(skinName.text)
    # print(floatValue.text)
    # print("\n=================\n")

    # print(skinListing.prettify(), end="\n ===================== \n")

# print(results.prettify())