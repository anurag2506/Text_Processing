from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

def crawl_url(url):

    # Initialising a chrome driver
    driver = webdriver.Chrome()

    # fetching the url using the driver
    driver.get(url)
    page_source = driver.page_source

    soup = BeautifulSoup(page_source, 'html.parser')

    article_title = soup.find('h1').text
    article_content = [p.text for p in soup.find_all('p')]

    # Printing the article title and content
    print(f"Article Title: {article_title}")
    print("Article Content:")
    for content in article_content:
        print(content)

    driver.quit()