import time
import csv
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
d_p='/path/to/chromedriver'
d=webdriver.Chrome(executable_path=d_p)
url = "https://www.amazon.in/s?rh=n%3A6612025031&fs=true&ref=lp_6612025031_sar"
d.get(url)
time.sleep(3)
d.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
s=BeautifulSoup(d.page_source, 'html.parser')
products=s.find_all("div", {"data-component-type": "s-search-result"})
product_data=[]
for product in products:
    try:
        name = product.h2.text.strip()
        price = product.find("span", class_="a-price-whole")
        price = price.text.strip() if price else "Not Available"
        rating = product.find("span", class_="a-icon-alt")
        rating = rating.text.strip() if rating else "No rating"
        seller = product.find("span", class_="a-size-small a-color-base")
        seller = seller.text.strip() if seller else "Not Available"
        product_data.append([name, price, rating, seller])

    except Exception as e:
        print(f"Error processing product: {e}")
d.quit()
columns=["Product Name", "Price", "Rating", "Seller Name"]
df=pd.DataFrame(product_data, columns=columns)
df.to_csv("amazon_products.csv", index=False)
print("Data saved to amazon_products.csv")