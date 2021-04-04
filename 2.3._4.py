from selenium import webdriver
import time
import math

link = 'http://suninjuly.github.io/alert_accept.html'


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_tag_name('button')
    button.click()
    alert = browser.switch_to.alert
    alert.accept()
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    submit = browser.find_element_by_tag_name('button')
    submit.click()
    alert2 = browser.switch_to.alert
    alert2_text = alert2.text
    print(alert2_text)
finally:
    time.sleep(30)
    browser.quit()
