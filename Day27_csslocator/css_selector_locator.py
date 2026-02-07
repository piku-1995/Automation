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

#locate by css selector: tag & id
# search=driver.find_element(By.CSS_SELECTOR, "input#small-searchterms")
# search.send_keys("Priyanka")
# time.sleep(3)
#locate by css selector: tag & class
# search=driver.find_element(By.CSS_SELECTOR, "input.search-box-text")
# search=driver.find_element(By.CSS_SELECTOR,".search-box-text")
# search.send_keys("Priyanka")
# time.sleep(3)
#locate by css selector: tag & attribute
# search=driver.find_element(By.CSS_SELECTOR, "input[type='text']")
search=driver.find_element(By.CSS_SELECTOR, "[type='text']")
search.send_keys("Priyanka")
time.sleep(3)


#locate by css selector: tag, class & attribute
# search=driver.find_element(By.CSS_SELECTOR, "input.search-box-text[type='text']")
# search.send_keys("Priyanka")
# time.sleep(3)

driver.quit()