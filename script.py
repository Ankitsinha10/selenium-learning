import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome ()
driver.get("https://the-internet.herokuapp.com/login")
print("Navigated to the login page")
time.sleep(2)

# Find and fill the Username field
username_field = driver.find_element(By.ID , "username")
username_field.send_keys("tomsmith")

#Find and fill the password field 
password_field = driver.find_element(By.ID, "password")
password_field.send_keys ("SuperSecretPassword!")
print("Found and filled the password field")

#Find and click the login button using a CSS SELECTOR

login_button = driver.find_element(By.CSS_SELECTOR, "button[type = 'submit']")
login_button.click()
print("Found and clicked the login button.")

#Quiting process
print("Waiting to see the result...")
time.sleep(3) 
print("Script finished")
driver.quit()