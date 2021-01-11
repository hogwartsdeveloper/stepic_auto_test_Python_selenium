from selenium import webdriver

browser = webdriver.Chrome()

try:
    link = 'http://suninjuly.github.io/cats.html'
    browser.get(link)

    button = browser.find_element_by_id('button')
except Exception as ex:
    print(ex)
finally:
    browser.quit()