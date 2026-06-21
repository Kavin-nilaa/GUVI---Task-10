import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#code to launch the browser
driver = webdriver.Chrome()
driver.maximize_window()

#code to launch the url
driver.get("https://www.saucedemo.com/")

#code to log in into the url
driver.find_element(By.ID,"user-name").send_keys("standard_user")
time.sleep(4)
driver.find_element(By.ID,"password").send_keys("secret_sauce")
time.sleep(4)
driver.find_element(By.ID,"login-button").click()
time.sleep(5)

#code to fetch the title, current url and content of the webpage
print(driver.title)
print(driver.current_url)
print(driver.page_source)

# code to extract the content of the webpage in text file
file=open("Webpage_task_11.txt",'w')
file.write(driver.page_source)
file.close()





