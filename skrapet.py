import requests
from bs4 import BeautifulSoup

URL = "https://skinport.com/market"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")