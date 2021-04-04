from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 12 секунд, пока цена не станет $100
    price = browser.find_element_by_id("price")
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
    # как только цена стала $100 кликаем забукать
    button = browser.find_element_by_id("book")
    button.click()

    # теперь надо проскролить страницу вниз, чтобы стало видно математическую задачу и кнопку submit
    # задачи 2.2_5, 2.2_6
    browser.execute_script("window.scrollBy(0, 200);")

    # находим элемент x по старой схеме из предыдущих задач
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    submit = browser.find_element_by_id('solve')
    submit.click()


finally:
    time.sleep(30)
    browser.quit()
