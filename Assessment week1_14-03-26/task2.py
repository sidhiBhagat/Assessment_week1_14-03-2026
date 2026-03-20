# 1. Write a Python script using Selenium.
# 2. Navigate to https://www.wikipedia.org/
#  3. Find the search input field.
#  4. Find the "English" language.
# 5. Find the main Wikipedia logo image.
# 6. Count how many language links are present in the central block (Hint: inspect the common container and look for tags within it).Use find_elements and print the count.
#  7. Navigate back to the previous page
#  8. Navigate forward.
# 9. Refresh the page.
# 10. Print the final page title.
# 11. Quit the browser.

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.wikipedia.org/")
driver.maximize_window()
sleep(2)

search=driver.find_element(By.ID, "searchInput")
print(search)
eng=driver.find_element(By.ID, "js-link-box-en")
print(eng)
logo=driver.find_element(By.CSS_SELECTOR, ".central-featured-logo")
print(logo)
languages=driver.find_elements(By.CSS_SELECTOR,".central-featured-lang")
print(languages)
print("Total languages :",len(languages))
driver.back()
sleep(2)
driver.forward()
sleep(2)
driver.refresh()
sleep(2)
print("Title:",driver.title)
driver.quit()
print("Working successfully")