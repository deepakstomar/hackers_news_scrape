import time

import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# options = webdriver.ChromeOptions()
# options.add_argument('--headless')

driver = webdriver.Chrome()
driver.maximize_window()

url = "https://news.ycombinator.com/"

driver.get(url)

time.sleep(5)

titles = []
links = []
scores = []
i = 5
while i > 0:
    elements = driver.find_elements(by=By.XPATH, value="//tr[@class='athing']/td[3]/span/a")
    points = driver.find_elements(by=By.CLASS_NAME, value="score")

    for element, point in zip(elements, points):
        titles.append(element.text)
        links.append(element.get_attribute("href"))
        scores.append(point.text)
    
    go_to_next_page = driver.find_elements(by=By.CLASS_NAME, value='morelink')
    
    if go_to_next_page:
        go_to_next_page[0].click()
        i -= 1
    else:
        break
        
data = {
    "title": titles,
    "link": links,
    "score": scores,
}

df = pd.DataFrame(data)
df.to_csv("data.csv")

driver.close()
