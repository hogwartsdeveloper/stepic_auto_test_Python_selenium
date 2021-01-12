import unittest
from selenium import webdriver
import time

def registration(link):
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector('[placeholder="Input your first name"]')
    input1.send_keys('Conor')

    input2 = browser.find_element_by_css_selector('.form-control.second')
    input2.send_keys('McGregor')

    input3 = browser.find_element_by_css_selector('.form-control.third')
    input3.send_keys('mcgregor@gmail.com')

    button = browser.find_element_by_css_selector('.btn.btn-default')
    button.click()

    time.sleep(1)

    welcome_text = browser.find_element_by_tag_name('h1').text
    browser.quit()
    return welcome_text

class TestRegistration(unittest.TestCase):
    def test_reg1(self):
        self.assertEqual(registration('http://suninjuly.github.io/registration1.html'),
                         "Congratulations! You have successfully registered!", "req failed")

    def test_reg2(self):
        self.assertEqual(registration('http://suninjuly.github.io/registration2.html'),
                         "Congratulations! You have successfully registered!", "req failed")


if __name__ == "__main__":
    unittest.main()
