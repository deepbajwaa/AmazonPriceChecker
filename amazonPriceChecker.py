import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = "https://www.amazon.ca/Samsung-RU7100-UN75RU7100FXZC-Canada-Version/dp/B07NC7N3G6/ref=sr_1_3?keywords=samsung+tv&qid=1577636170&refinements=p_n_size_browse-bin%3A17304154011&rnid=3236496011&s=electronics&sr=1-3"

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

#This function is used to check if the price of the TV has dropped below $1500
def check_price():

    #This is used to request the URL from the server
    page = requests.get(URL, headers=headers)

    #Get parser
    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser") 

    #Used to parse the html page
    title = soup2.find(id= "productTitle").get_text()
    price = soup2.find(id="priceblock_ourprice").get_text()

    #Change the , in the price to a . so that the number can be converted to a float.
    convert_price = price[5:10]
    s = list(convert_price)
    s[1] = '.'
    convert_price = float("".join(s))

    #print(convert_price)
    #print(title.strip())

    #Check the price, if the price has dipped below $1500 then call the send_mail() function
    if(convert_price <= 1.50):
        send_mail()
    

#This function is used to send an email indicating that the price of the TV has droppped.
def send_mail():
    #This is used to create a connect to gmail's server.
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('deep43055@gmail.com', 'zqytsqsydkgusyxw')

    #Create the subject, body, and msg for the email.
    subject = 'TV is on a HUGE SALE'
    body = 'Check the amazon link: https://www.amazon.ca/Samsung-RU7100-UN75RU7100FXZC-Canada-Version/dp/B07NC7N3G6/ref=sr_1_3?keywords=samsung+tv&qid=1577636170&refinements=p_n_size_browse-bin%3A17304154011&rnid=3236496011&s=electronics&sr=1-3. The Price has dipped below $1500.'
    msg = f"Subject: {subject}\n\n{body}"
    
    #Send the email
    server.sendmail(
        'deep43055@gmail.com ',
        'deep43055@gmail.com',
        msg
    )

    #Indicate to the user that the email has been sent, and break the connection with the server.
    print('An email has been sent!')
    server.quit()

#This is a while loop that runs to check if the price of the TV has dropped every hour.
while(True):
    check_price()
    time.sleep(60*60)