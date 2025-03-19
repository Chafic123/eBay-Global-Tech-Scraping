from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import time
from datetime import datetime
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--headless")  
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

ua = UserAgent()
options.add_argument(f"user-agent={ua.random}")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

URL = "https://www.ebay.com/globaldeals/tech"

def scroll_page():
    """Scroll down the page to trigger lazy loading of all product listings."""
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2) 
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def scrape_products():
    """Scrape product details from eBay Global Tech Deals."""
    driver.get(URL)
    time.sleep(5)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.dne-itemtile-detail"))
    )

    scroll_page()

    products = []
    try:
        product_elements = driver.find_elements(By.CSS_SELECTOR, "div.dne-itemtile-detail")
        print(f"Number of products found: {len(product_elements)}")

        for product in product_elements:
            try:
                title = product.find_element(By.CSS_SELECTOR, "h3.dne-itemtile-title").text
            except:
                title = "Title N/A"

            try:
                price = product.find_element(By.CSS_SELECTOR, "span.first").text
            except:
                price = "Price N/A"

            try:
                original_price = product.find_element(By.XPATH, './/div[@class="dne-itemtile-original-price"]/span/span').text
            except:
                original_price = "N/A"

            try:
                shipping = product.find_element(By.XPATH, ".//span[contains(@class, 'dne-itemtile-delivery')]").text
                print(shipping)
            except:
                shipping = "Shipping N/A"

            try:
                item_url = product.find_element(By.XPATH, ".//a[@itemprop='url']").get_attribute("href")
            except:
                item_url = "URL N/A"

            # timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            product_data = {
                "timestamp": timestamp,
                "title": title,
                "price": price,
                "original_price": original_price,
                "shipping": shipping,
                "item_url": item_url
            }

            products.append(product_data)

    except Exception as e:
        print("Error occurred:", e)

    return products

def save_to_csv(data):
    """Save scraped data to CSV."""
    file_name = "ebay_tech_deals.csv"
    try:
        df = pd.read_csv(file_name)
    except FileNotFoundError:
        df = pd.DataFrame(columns=[
            "timestamp", "title", "price", "original_price", "shipping", "item_url"
        ])

    new_data = pd.DataFrame(data)

    df = pd.concat([df, new_data], ignore_index=True)

    df.to_csv(file_name, index=False)

if __name__ == "__main__":
    print("Scraping eBay Global Tech Deals...")
    scraped_data = scrape_products()

    if scraped_data:
        save_to_csv(scraped_data)
        print("Data saved to ebay_tech_deals.csv")
    else:
        print("Failed to scrape data.")

    driver.quit()