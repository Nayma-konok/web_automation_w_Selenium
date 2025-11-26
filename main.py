import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

load_dotenv()

class WebAutomation:
    def __init__(self):
        download_path = os.getcwd()
        chrome_driver_path = os.getenv("CHROME_DRIVER_PATH")

        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")

        prefs = {'download.default_directory': download_path}
        chrome_options.add_experimental_option('prefs', prefs)

        service = Service(chrome_driver_path)
        self.driver = webdriver.Chrome(options=chrome_options, service=service)
        
    def login(self):
        username = os.getenv("USERNAME")
        password = os.getenv("PASSWORD")
        login_url = os.getenv("LOGIN_URL")

        self.driver.get(login_url)
        username_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "userName"))
        )
        username_field.send_keys(username)

        password_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "password"))
        )
        password_field.send_keys(password)

        login_button = self.driver.find_element(By.ID, "login")
        self.driver.execute_script("arguments[0].click();", login_button)

    def fill_form(self):
        username = os.getenv("USERNAME")
        useremail = os.getenv("Email")
        currentaddress = os.getenv("Currentaddress")
        permanentaddress = os.getenv("Permanentaddress")

        elements = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div'))
        )
        elements.click()

        text_box = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'item-0'))
        )
        text_box.click()

        fullname_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "userName"))
        )
        fullname_field.send_keys(username)

        email_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "userEmail"))
        )
        email_field.send_keys(useremail)

        current_address_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "currentAddress"))
        )
        current_address_field.send_keys(currentaddress)

        permanent_address_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "permanentAddress"))
        )
        permanent_address_field.send_keys(permanentaddress)

        submit_button = self.driver.find_element(By.ID, "submit")
        self.driver.execute_script("arguments[0].click();", submit_button)

    def downloading(self):
        upload_and_download = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "item-7"))
        )
        upload_and_download.click()

        download_button = self.driver.find_element(By.ID, "downloadButton")
        self.driver.execute_script("arguments[0].click();", download_button)

    def close(self):
        self.driver.quit()

if __name__=="__main__":
    wa = WebAutomation()
    wa.login()
    wa.fill_form()
    wa.downloading()
    wa.close()
