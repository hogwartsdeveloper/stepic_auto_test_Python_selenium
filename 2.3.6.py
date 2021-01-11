from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

browser = webdriver.Chrome()

try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser.get(link)
    btn_troll = browser.find_element(By.TAG_NAME, 'button')
    btn_troll.click()

    new_window = browser.window_handles[1]
    first_window = browser.window_handles[0]

    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.ID, 'input_value').text

    input1 = browser.find_element(By.TAG_NAME, 'input')
    input1.send_keys(str(math.log(abs(12 * math.sin(int(x_element))))))
    btn = browser.find_element(By.TAG_NAME, 'button')
    btn.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    alert.accept()
    print(alert_text)
finally:
    time.sleep(5)
    browser.quit()