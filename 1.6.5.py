from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/find_link_text")
    link = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link.click()
    input1 = browser.find_element_by_name("first_name")
    input1.send_keys("zhan")

    input2 = browser.find_element_by_name("last_name")
    input2.send_keys('Akhmetkhan')

    input3 = browser.find_element_by_class_name("form-control.city")
    input3.send_keys('Astana')

    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russian")

    button = browser.find_element_by_class_name("btn.btn-default")
    button.click()
finally:
    time.sleep(5)
    browser.quit()