#the hindu paper scrap

import requests
from bs4 import BeautifulSoup
import unicodedata


url = "http://www.thehindu.com/todays-paper/"

r = requests.get(url)

soup = BeautifulSoup(r.content, "lxml")

#text_file = open("test.txt", "w")

def article_scrap(str)
	r = requests.get(str)

	soup = BeautifulSoup(r.content)
	
	title = soup.find_all("h1")
	
	title[0].text.encode('ascii','ignore')
	
	