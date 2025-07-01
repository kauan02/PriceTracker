import requests
from bs4 import BeautifulSoup

url = "https://www.kabum.com.br/produto/320797/processador-amd-ryzen-7-5700x-3-4ghz-4-6ghz-max-turbo-cache-36mb-am4-sem-video-100-100000926wof"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

def Scrap():
    
    soup = BeautifulSoup(page.content, "html.parser")
    
    name = soup.find("h2", class_="sc-58b2114e-6 brTtKt")
    price = soup.find("h4", class_="sc-5492faee-2 ipHrwP finalPrice")
    original_price = soup.find("span", class_="sc-5492faee-1 ibyzkU oldPrice")
    print(name)
    print(price)
    print(original_price)
        
Scrap()
print(page.text)