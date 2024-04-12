from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
 
# Initialize the Chrome WebDriver
driver = webdriver.Chrome()
 
# Open the Instagram login page
driver.get("https://www.instagram.com/accounts/login/")
 
# Wait for the username field to be loaded
username_field = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.NAME, "username"))
)

password_field = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.NAME, "password"))
)

# username_field = WebDriverWait(driver, 20).until(
#     EC.presence_of_element_located((By.NAME, "username"))
# )


 
# You can now interact with the username field, for example, send some text
username_field.send_keys("nittesh")
password_field.send_keys("password1234")
time.sleep(10)

button = WebDriverWait(driver, 20).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
)

button.click()
time.sleep(30)
 
# Continue with other actions, like locating the password field or clicking the login button
# ...
 
# Remember to close the browser after your script finishes
driver.close()
