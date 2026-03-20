# 1. Go to https://the-internet.herokuapp.com/login.
# 2. Locate the username field using CSS Selector with Tag and name attribute.
# 3. Locate the password field using CSS Selector with Tag and id attribute.
#  4. Locate the "Login" button using CSS Selector with Tag and type attribute.
#  5. Locate the footer link ("Elemental Selenium") using CSS Selector(descendant).

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")
driver.maximize_window()
sleep(2)

username = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
print(username)
password = driver.find_element(By.CSS_SELECTOR, "input[id='password']")
print(password)
login_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
print(login_btn)
footer = driver.find_element(By.CSS_SELECTOR, "#page-footer a")
print(footer.text)
print("Working successfully")

sleep(2)
driver.quit()