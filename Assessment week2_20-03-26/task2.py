# https://automationexercise.com/signup
# Open signup page
# Enter name & email
# Select Title (Mr/Mrs) → Radio button
# Select checkboxes:
# Newsletter
# Special offers
# # Use get_attribute("checked") to verify selection

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

# Open signup page
driver.get("https://automationexercise.com/signup")

wait = WebDriverWait(driver, 10)

name = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Name']")))
name.send_keys("Shikha")

email = driver.find_element(By.XPATH, "//input[@data-qa='signup-email']")
email.send_keys("shikhaa123@gmail.com")

signup_btn = driver.find_element(By.XPATH, "//button[@data-qa='signup-button']")
signup_btn.click()

title = wait.until(EC.element_to_be_clickable((By.ID, "id_gender1")))
title.click()

news = driver.find_element(By.ID, "newsletter")
offers = driver.find_element(By.ID, "optin")

news.click()
offers.click()

print("Newsletter :", news.get_attribute("checked"))
print("Special offers:", offers.get_attribute("checked"))

# driver.quit()