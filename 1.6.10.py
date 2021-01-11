from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

try:
    browser.get('http://suninjuly.github.io/registration1.html')
    input1 = browser.find_element(By.NAME, "first_name")
    input1.send_keys("Zhang")

    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys('Akhmatova')

    input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
    input3.send_keys("Astana")

    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Kazakhstan")

    btn = browser.find_element(By.XPATH, '//button[text() = "Submit"]')
    btn.click()
