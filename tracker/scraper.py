import requests
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def GetInfo():
    def clean_price(price_str):
        cleaned = price_str.replace("R$", "").replace(".", "").replace(",", ".").strip()
        return float(cleaned)
    
    print("Starting...")
    driver = webdriver.Firefox()
    driver.get("https://www.kabum.com.br/produto/320797/processador-amd-ryzen-7-5700x-3-4ghz-4-6ghz-max-turbo-cache-36mb-am4-sem-video-100-100000926wof")
    assert "5700X" in driver.title
    
    print("Geting data...")
    product_name = driver.find_element(By.CLASS_NAME, "brTtKt").text.split(",")[0]
    price_raw = driver.find_element(By.CLASS_NAME, "finalPrice").text
    normal_price_raw = driver.find_element(By.CLASS_NAME, "oldPrice").text

    driver.quit()
    print("Successfully collected data.")
    
    price = clean_price(price_raw)
    normal_price = clean_price(normal_price_raw)
    
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S"), product_name, normal_price, price