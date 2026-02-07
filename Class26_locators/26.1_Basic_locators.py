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

#locate by id
# search_box=driver.find_element(By.ID, "search_query_top")
# search_box.send_keys("T-SHIRTS")
# time.sleep(5)
# # LOCATE BY NAME
# search_button=driver.find_element(By.NAME,"submit_search")
# search_button.click()
# time.sleep(5)
# #LOCATE BY LINK-TEXT
# # LINK= driver.find_element(By.LINK_TEXT, "Printed Chiffon Dress")
# # LINK.click()
#
# #LOCATE BY PARTIAL LINK-TEXT
# LINK= driver.find_element(By.PARTIAL_LINK_TEXT, "Chiffon Dress")
# LINK.click()
#
# Locate by multiple elements by 'Tagname'
# tag=driver.find_elements(By.TAG_NAME, "img")
# print(len(tag))

#locate by multiple elements by 'classname'

sliders=driver.find_elements(By.CLASS_NAME,"homeslider-container")
print(len(sliders))


driver.quit()