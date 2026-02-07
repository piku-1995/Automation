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
# search=driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[1]/div[3]/form/input[1]")
# search.send_keys("Priyanka")
# print("search presence", search.is_displayed())

#locate element using relative xpath with single attribute
# search=driver.find_element(By.XPATH, "//input[@value='Search']")
# search.send_keys("Priyanka")
# print("search presence", search.is_displayed())

#locate element using relative xpath with multiple attribute
# search=driver.find_element(By.XPATH, "//input[@value='Search'][@type='submit']")
# search.send_keys("Priyanka")
# print("search presence", search.is_displayed())

#locate element using relative xpath with and operator
# search=driver.find_element(By.XPATH, "//input[@value='Search'and @type='submit']")
# search.send_keys("Priyanka")
# print("search presence", search.is_displayed())

#locate element using relative xpath with or operator
# search=driver.find_element(By.XPATH, "//input[@value='Search'or @type='submit']")
# search.send_keys("Priyanka")
# print("search presence", search.is_displayed())

#locate element with contains
# computer_contains=driver.find_elements(By.XPATH, "//h2//a[contains(@href,'computer')]")
# print("item number", len(computer_contains))

#locate element with starts with
# computer_startswith=driver.find_elements(By.XPATH, "//h2//a[starts-with(@href,'/build')]")
# print("item number", len(computer_startswith))


#locate element with last()
# last = driver.find_element(By.XPATH, "(//h2//a[contains(@href,'computer')])[last()]")
# print(last.text)

# locate element with position()
# position = driver.find_element(By.XPATH, "(//h2//a[contains(@href,'computer')])[position()=2]")
# print(position.text)

#locate element with position()
# register_link = driver.find_element(By.XPATH, "//a[text()='Register']")
# print("register link presense",register_link.is_displayed())

#locate element with normalize-space()
# driver.find_element(By.XPATH,"//div[normalize-space(text())='Copyright © 2026 Tricentis Demo Web Shop. All rights reserved.']")






driver.quit()
