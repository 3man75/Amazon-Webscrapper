import webbrowser
import requests
from bs4 import BeautifulSoup
import time
import datetime
import smtplib


def print_hi(name):
    
    print(f'Hi, {name}')  

if __name__ == '__main__':

    #URL will be an object of the request type.

    URL = "https://www.amazon.com/Sony-PlayStation-5-Standard-Blu-ray-Disk/dp/B094TY4NHB/ref=sr_1_1?dchild=1&keywords=playstation+5qid=1633554933&sr=8-1"

    headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv: 92.0) Gecko/20100101 Firefox/92.0"}

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
    
    title = soup2.find (id="productTitle") #note to self: What type of data is the title object here? Find out.

    print(page.text)

   # print(soup2.find_all(string='productTitle')) #print the title of the prouduct on Amazon



    
   # price = soup2.find(id='priceblodk_ourprice').get_text()
    
    # print(price)
    

   
    

    
