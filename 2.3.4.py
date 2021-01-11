from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()

try:
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser.get(link)
    btn = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    btn.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element(By.ID, 'input_value').text
    input1 = browser.find_element(By.TAG_NAME, 'input')
    input1.send_keys(str(math.log(abs(12 * math.sin(int(x_element))))))

    btn2 = browser.find_element(By.TAG_NAME, 'button')
    btn2.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    alert.accept()
    print(alert_text)

finally:
    time.sleep(5)
    browser.quit()