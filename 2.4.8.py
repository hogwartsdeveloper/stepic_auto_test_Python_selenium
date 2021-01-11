from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()

try:
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser.get(link)

    house_price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )
    button = browser.find_element(By.ID, 'book')
    button.click()

    x_element = browser.find_element(By.ID, 'input_value').text

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(str(math.log(abs(12 * math.sin(int(x_element))))))

    submit = browser.find_element(By.ID, 'solve')
    submit.click()
finally:
    alert = browser.switch_to.alert
    alert_text = alert.text
    alert.accept()
    print(alert_text)
    browser.quit()