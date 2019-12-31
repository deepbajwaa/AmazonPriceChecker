import requests
from bs4 import BeautifulSoup
import smtplib

URL = "https://www.amazon.ca/Samsung-RU7100-UN75RU7100FXZC-Canada-Version/dp/B07NC7N3G6/ref=sr_1_3?keywords=samsung+tv&qid=1577636170&refinements=p_n_size_browse-bin%3A17304154011&rnid=3236496011&s=electronics&sr=1-3"

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers) #This is used to request the URL from the server

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id= "productTitle").get_text() #Used to parse the html page
    price = soup2.find(id="priceblock_ourprice").get_text()

    convert_price = price[5:10]
    s = list(convert_price)
    s[1] = '.'
    convert_price = float("".join(s))

    if(convert_price <= 1.50):
        print("okie")
    print(convert_price)
    print(title.strip())

#establish connection with gmail
def send_mail():
    server = smtplib.STMP('stmp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('deep43055@gmail.com', 'zqytsqsydkgusyxw')

    subject = 'TV is on a HUGE SALE'
    body = 'Check the amazon link: https://www.amazon.ca/Samsung-RU7100-UN75RU7100FXZC-Canada-Version/dp/B07NC7N3G6/ref=sr_1_3?keywords=samsung+tv&qid=1577636170&refinements=p_n_size_browse-bin%3A17304154011&rnid=3236496011&s=electronics&sr=1-3. The Price has dipped below $1500.'

    msg = f"Subject: {subject}\n\n{body}"
    server.send_mail(
        'The python price checker program',
        'deep43055@gmail.com',
        msg
    )

    print('An email has been sent!')
    server.quit()
    