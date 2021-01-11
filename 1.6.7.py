from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
try:
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.TAG_NAME, 'input')

    for element in elements:
        element.send_keys('Мой ответ')

    button = browser.find_element(By.CLASS_NAME, 'btn.btn-default')
    button.click()
finally:
    time.sleep(6)
    browser.quit()