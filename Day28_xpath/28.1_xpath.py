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
driver.get("https://demowebshop.tricentis.com/")
time.sleep(5)
driver.maximize_window()
actual_title=driver.title
expected_title="Demo Web Shop"

if actual_title==expected_title:
    print("title is correct")
else:
    print("title is not correct")
time.sleep(3)

#locate elemenet using absolute xpath
# search=driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[3]/form/input[1]')
# search.send_keys("Priyanka")
# time.sleep(10)

#locate element using relative xpath with single attribute
# search=driver.find_element(By.XPATH, "//input[@value='Search store']")
# search.send_keys("Priyanka")
# time.sleep(10)


#locate element using relative xpath with multiple attribute
# search=driver.find_element(By.XPATH, "//input[@value='Search store'][@autocomplete='off']")
# search.send_keys("Priyanka")
# time.sleep(10)
# driver.quit()

#locate element using relative xpath with multiple attribute
search=driver.find_element(By.XPATH, "//input[@value='Search store'][@autocomplete='off']")
print("search:", search.is_displayed())

driver.quit()