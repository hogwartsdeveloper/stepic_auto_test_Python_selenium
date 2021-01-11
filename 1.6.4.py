from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'http://suninjuly.github.io/simple_form_find_task.html'
browser = webdriver.Chrome()
try:
    browser.get(link)
    input1 = browser.find_element(By.NAME, "first_name")
    input1.send_keys("Zhang")

    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys('Akhmatova')

    input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
    input3.send_keys("Astana")

    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Kazakhstan")

    button = browser.find_element(By.ID, "submit_button")
    button.click()
finally:
    time.sleep(30)
    browser.quit()