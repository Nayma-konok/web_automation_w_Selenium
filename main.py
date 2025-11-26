import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

load_dotenv()

username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
chrome_driver_path = os.getenv("CHROME_DRIVER_PATH")
login_url = os.getenv("LOGIN_URL")
useremail=os.getenv("Email")
currentaddress=os.getenv("Currentaddress")
permanentaddress=os.getenv("Permanentaddress")
download_path=os.getcwd()

chrome_options=Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")

prefs={'download.default_directory': download_path }
chrome_options.add_experimental_option('prefs', prefs)

service=Service(chrome_driver_path)
driver=webdriver.Chrome(options=chrome_options,service=service)
driver.get(login_url)


#locate username,password and click the button
username_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "userName"))
)
username_field.send_keys(username)

password_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "password"))
)
password_field.send_keys(password)

login_button=driver.find_element(By.ID, "login")
driver.execute_script("arguments[0].click();", login_button)

#locate the elements dropdown and Textbox
elements=WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div'))
)
elements.click()

text_box=WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'item-0'))
)
text_box.click()


#locate the form fields and submit button
fullname_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "userName"))
)
fullname_field.send_keys(username)

email_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "userEmail"))
)
email_field.send_keys(useremail)

current_address_field= WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "currentAddress"))
)
current_address_field.send_keys(currentaddress)
permanent_address_field= WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "permanentAddress"))
)
permanent_address_field.send_keys(permanentaddress)

submit_button=driver.find_element(By.ID, "submit")
driver.execute_script("arguments[0].click();", submit_button)

#locate the upload and download section and download button
upload_and_download = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "item-7"))
)
upload_and_download.click()
download_butoon=driver.find_element(By.ID, "downloadButton")
driver.execute_script("arguments[0].click();", download_butoon)



input("press enter to closs the browser")
driver.quit()