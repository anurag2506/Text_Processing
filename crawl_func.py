from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import pandas as pd

# Function for crawling the data
def crawl_url(url):

    driver = webdriver.Chrome()
    driver.get(url)
    page_source = driver.page_source
    driver.quit()

    soup = BeautifulSoup(page_source, 'html.parser')
    page_title = soup.title.string if soup.title else "No Title Found"

    # div that contains all the content
    main_content = soup.find('div', class_='td-post-content')

    content = []
    if main_content:
        for element in main_content.find_all(['h1','h2', 'h3','p', 'li','ol','strong' 'blockquote'], recursive=True):
            content.append(f"{element.get_text(strip=True)}\n")

    # Formatted the output:
    formatted_content = f"{page_title}\n" + "\n".join(content)
    return formatted_content


# # Testing the function on the given data
# data = pd.read_csv('Input.xlsx - Sheet1.csv')
# article_content_1 = crawl_url(data.iloc[1]['URL'])

# # Saving the scraped data into a text file
# with open(f"content/{data.iloc[1]['URL_ID']}.txt", 'w') as file:
#     file.write(article_content_1)




# Function for the entire scraping and saving the data into a txt file:

def save_content_in_file(data):
    os.makedirs("scraped_articles",exist_ok = True)
    for i in range(len(data)):
        article_url = data.iloc[i]['URL']
        article_content = crawl_url(article_url)
        article_id = data.iloc[i]['URL_ID']

        with open(f"scraped_articles/{article_id}.txt", 'w') as file:
            file.write(article_content)
        print(f"Saved content for the article {article_id}")
    
    print(f"Saved the files for all the urls")

    
if __name__ == "__main__":
    data = pd.read_csv('Input.xlsx - Sheet1.csv')
    save_content_in_file(data)