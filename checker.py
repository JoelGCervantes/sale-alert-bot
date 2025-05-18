# checker.py

import requests
from bs4 import BeautifulSoup

def check_sales(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    sales = []

    for item in soup.select(".sale-item"):  # Update selectors to match site
        title = item.select_one(".item-title")
        price = item.select_one(".sale-price")

        if title and price:
            sales.append(f"{title.get_text(strip=True)} - {price.get_text(strip=True)}")

    return sales
