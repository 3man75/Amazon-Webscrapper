import webbrowser
import requests
from bs4 import BeautifulSoup



def print_hi(name):
    
    print(f'Hi, {name}')  

if __name__ == '__main__':

    #URL is loaded in as the variable URL

    URL = "https://www.amazon.com/Sony-PlayStation-5-Standard-Blu-ray-Disk/dp/B094TY4NHB/ref=sr_1_1?dchild=1&keywords=playstation+5qid=1633554933&sr=8-1"
    
    #user-agent is a string that has a particular system specs and browser

    headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv: 92.0) Gecko/20100101 Firefox/92.0"}
    
    #request module will use the above variable to create a request to pingAmazon

    page = requests.get(URL, headers=headers)
    
    #soup objects will take in the page variable and parse it for raw data

    soup1 = BeautifulSoup(page.content, "html.parser")
    
    #another soup object to use the other soup object and make it more legible

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
    
    title = soup2.find (id="productTitle")

    print(page.text)
