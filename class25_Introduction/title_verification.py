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
    print("title is totally correct")
else:
    print("title is not correct")
time.sleep(3)

driver.quit()