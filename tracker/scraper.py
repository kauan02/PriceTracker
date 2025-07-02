import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.kabum.com.br/produto/320797/processador-amd-ryzen-7-5700x-3-4ghz-4-6ghz-max-turbo-cache-36mb-am4-sem-video-100-100000926wof")
assert "5700X" in driver.title

product_name = driver.find_element(By.CLASS_NAME, "brTtKt")
price = driver.find_element(By.CLASS_NAME, "finalPrice")
normal_price = driver.find_element(By.CLASS_NAME, "oldPrice")

print(product_name.text)
print(normal_price.text)
print(price.text)

driver.quit()