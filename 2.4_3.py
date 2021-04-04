from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.implicitly_wait(5)                             # говорим WebDriver искать каждый элемент в течение 5 секунд
browser.get("http://suninjuly.github.io/wait1.html")

button = browser.find_element_by_id("verify")
button.click()
message = browser.find_element_by_id("verify_message")
# print(message.text)
assert "successful" in message.text

browser.quit()
