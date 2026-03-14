from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

websites = [
    "https://www.nike.com",
    "https://www.ndtv.com/livetv-ndtv24x7",
    "https://www.python.org"
]

for s in websites:
    sleep(3)
    driver.get(s)
    print("Title:", driver.title)

driver.quit()