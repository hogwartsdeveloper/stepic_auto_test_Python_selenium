from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import 

option = Options()
option.add_argument("--user-data-dir=C:/Users/zhah/AppData/Local/Google/Chrome/User Data/")
option.add_argument("--profile-directory=Default")

browser = webdriver.Chrome(options=option)
link = 'https://mail.google.com/'
browser.get(link)

