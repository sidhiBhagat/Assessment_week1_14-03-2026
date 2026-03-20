# Open Amazon
# Verify page title and current URL
# Locate the category dropdown (next to search bar)
# Select "Books" using Select class
# Enter "Harry Potter" in search and press Enter
# Use explicit wait to wait until results are visible
# Get all product titles using find_elements
# Print first 5 product names
# Click on the first product

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 10)

driver.get("https://www.amazon.in/")


# assert "Amazon" in driver.title, "Title does not contain Amazon"
# print("Title verified successfully")
assert 'amazon.in' in driver.current_url, "Url does not contain Amazon"
print("Url verified successfully")

dropdown = wait.until(EC.presence_of_element_located((By.ID, "searchDropdownBox")))
# print(dropdown.text)
select = Select(dropdown)

select.select_by_visible_text("Books")

search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys("Harry Potter",Keys.ENTER)

res = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//h2//span")))
# print(res)

titles = driver.find_elements(By.XPATH, "//a[@class='a-link-normal s-line-clamp-2 puis-line-clamp-3-for-col-4-and-8 s-link-style a-text-normal']//h2//span")
print("Top 5 Products:")
for i in range(5):
    print(titles[i].text)

titles[0].click()
print('First product selected')

# driver.quit()