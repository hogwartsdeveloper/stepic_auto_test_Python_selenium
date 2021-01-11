from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.implicitly_wait(5)

try:
    link = 'http://suninjuly.github.io/wait1.html'
    browser.get(link)
    btn = browser.find_element(By.ID, 'verify')
    btn.click()

    message = browser.find_element(By.ID, 'verify_message')

    assert 'successful' in message.text
finally:
    browser.quit()