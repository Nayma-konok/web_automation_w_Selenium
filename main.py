import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
chrome_driver_path = os.getenv("CHROME_DRIVER_PATH")
login_url = os.getenv("LOGIN_URL")


chrome_options=Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")
service=Service(chrome_driver_path)
driver=webdriver.Chrome(options=chrome_options,service=service)
driver.get(login_url)

username_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "userName"))
)
username_field.send_keys(username)

password_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "password"))
)
password_field.send_keys(password)

login_button=username_field = driver.find_element(By.ID, "login")
driver.execute_script("arguments[0].click();", login_button)


input("press enter to closs the browser")
driver.quit()