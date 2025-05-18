from bs4 import BeautifulSoup
import requests

def check_sales(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    sales = []

    # Each product is inside an <article>
    for item in soup.select("article"):
        # Find <h3> with an <a> inside (title area)
        h3 = item.find("h3")
        if not h3:
            continue

        a_tag = h3.find("a")
        if not a_tag:
            continue

        # Brand is usually in a <strong> tag
        brand_tag = a_tag.find("strong")
        brand = brand_tag.get_text(strip=True) if brand_tag else ""

        # Full title includes brand + description
        full_title = a_tag.get_text(strip=True)
        description = full_title.replace(brand, "", 1).strip()

        # Price: first <span> containing a $
        price_tag = item.find("span", string=lambda s: s and "$" in s)
        price = price_tag.get_text(strip=True) if price_tag else "N/A"

        sales.append(f"{brand} {description} - {price}")

    return sales
