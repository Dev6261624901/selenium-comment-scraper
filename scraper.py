# scraper.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Made by a 2nd year student Devendra Kushwah for learning Selenium

# Step 1: I Setup Chrome browser
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

# In Step 2 I Use Input Function To Ask user for URL to scrape 
url = input("🔗 Enter the URL of a public webpage with comments: ")
driver.get(url)
input("🔐 If login is required, please login manually and press Enter...")

# In Step 3 Scroll & extract comments Logic so it will scroll and extract comments for url which we given in step 2

for i in range(5):
    print(f"🔄 Scanning part {i + 1}...")
    driver.execute_script("window.scrollBy(0, 1000);")
    time.sleep(3)

    try:
        comments = driver.find_elements(By.XPATH, '//div[contains(@class, "comment")]')
        for comment in comments:
            try:
                author = comment.find_element(By.XPATH, './/strong').text
            except:
                author = "Anonymous"

            try:
                text = comment.find_element(By.XPATH, './/span').text
            except:
                text = ""

            if text.strip():
                data.append({
                    "Author": author,
                    "Comment": text
                })
    except:
        pass

#In Step 4 I Use Pandas TO Save Data to CSV Formate
df = pd.DataFrame(data)
df.to_csv("scraped_comments.csv", index=False, encoding='utf-8-sig')
print("✅ Scraping complete. Data saved to scraped_comments.csv")
driver.quit()