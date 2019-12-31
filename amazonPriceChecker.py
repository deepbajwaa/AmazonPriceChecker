import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.ca/Samsung-RU7100-UN75RU7100FXZC-Canada-Version/dp/B07NC7N3G6/ref=sr_1_3?keywords=samsung+tv&qid=1577636170&refinements=p_n_size_browse-bin%3A17304154011&rnid=3236496011&s=electronics&sr=1-3"

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

page = requests.get(URL, headers=headers) #This is used to request the URL from the server

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find(id= "productTitle") #Used to parse the html page

print(title)
