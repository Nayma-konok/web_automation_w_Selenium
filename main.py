from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options=Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")
service=Service('chromedriver-win64\chromedriver.exe')
driver=webdriver.Chrome(options=chrome_options,service=service)
driver.get("http://demoqa.com/login")

input("press enter to closs the browser")
driver.quit()