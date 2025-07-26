import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome ()
driver.get("https://the-internet.herokuapp.com/login")
print("Navigated to the login page")


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
wait = WebDriverWait(driver, 10)
success_message_element = wait.until(EC.visibility_of_element_located((By.ID, "flash")))
assert "You logged into a secure area!" in success_message_element.text
print ("Assertion Passed: Success message is correcy.")
print("Script finished")
driver.quit()