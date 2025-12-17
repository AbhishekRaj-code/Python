# To track the price and title of any product on an e-commerce website
# Installed modules - requests, beautifulsoup4, lxml

import requests
from bs4 import BeautifulSoup

class PriceTracer:
    def __init__(self, url):
        self.url = url
        self.user_agent = {"User-Agent" :"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36" }
        self.response = requests.get(url=self.url, headers= self.user_agent).text
        self.soup = BeautifulSoup(self.response, "lxml")
    
    def product_title(self):
        title = self.soup.find("span", {"id":"productTitle"})
        if title is not None:
            return title.text.strip()
        else:
            return "Tag not found"
        

    def product_price(self):
        price = self.soup.find("span", {"class": "a-price-whole"})
        if price is not None:
            return price.text
        else:
            return "Price  not found"

# 
# 

device = PriceTracer(url = "https://www.amazon.in/Chuwi-Android-Snapdragon-Display-Widevine/dp/B0FFGR9M3S/ref=pd_dp_d_dp_dealz_etdr_d_sccl_1_3/260-4862555-4592043")
print(device.product_title())
print(device.product_price())

device = PriceTracer(url = "https://www.amazon.in/Samsung-Hexagonal-Dynamic-Display-Refresh/dp/B0FNWQ1FW6/")
print(device.product_title())
print(device.product_price())