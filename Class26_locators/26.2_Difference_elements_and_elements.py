#setup
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

opt = Options() #import webdriver_manager.chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opt)


#code for title verification
driver.get("http://www.automationpractice.pl/index.php")
time.sleep(5)
driver.maximize_window()
actual_title=driver.title
expected_title="My Shop"

if actual_title==expected_title:
    print("title is correct")
else:
    print("title is not correct")
time.sleep(3)

#scenario1: locator matches a single element
# single_element=driver.find_element(By.NAME,"search_query")
# print(single_element)

# single_element=driver.find_elements(By.NAME,"search_query")
# print(single_element)


#scenario2: locator matches a multiple element

# first_image=driver.find_element(By.TAG_NAME, "img")
# print("first menu item:",first_image)

# all_images=driver.find_elements(By.TAG_NAME, "img")
# print("first menu item:",all_images)

#scenario3: locator does not match a multiple element
# wrong_element=driver.find_element(By.NAME,"abc")
# print(wrong_element)


# wrong_element=driver.find_elements(By.NAME,"abc")
# print(wrong_element)




driver.quit()