from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("http://www.google.com")

element = driver.find_element(By.XPATH, "//textarea[@name='q']")

element.send_keys("find selenium practising websites")

element.send_keys(Keys.ENTER)

time.sleep(10)
print("script ran successfully")

driver.close()