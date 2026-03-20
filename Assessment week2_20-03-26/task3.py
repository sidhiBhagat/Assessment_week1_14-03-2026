# Open Google
# Enter "Selenium Python"
# Use explicit wait for suggestions
# Capture all suggestions using find_elements
# Print them
# Click one suggestion

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()

# Open Google
driver.get("https://www.google.com")

wait = WebDriverWait(driver, 10)

search_box = wait.until(EC.presence_of_element_located((By.XPATH, "//textarea[@id='APjFqb']")))
search_box.send_keys("Selenium Python")
sleep(3)
sug = driver.find_elements(By.XPATH, "//ul[@role='listbox']/descendant::li/descendant::span")
print("Suggestion:")
for s in sug:
    print(s.text)
select=driver.find_element(By.XPATH, "//ul[@role='listbox']/descendant::li[2]")
select.click()

# driver.quit()