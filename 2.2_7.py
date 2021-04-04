from selenium import webdriver
import time
import os

link = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_name('firstname')
    input1.send_keys('Kate')
    input2 = browser.find_element_by_name('lastname')
    input2.send_keys('Romanova')
    input3 = browser.find_element_by_name('email')
    input3.send_keys('test@gmail.com')
    attach = browser.find_element_by_id('file')
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, '2.2_7.txt')  # добавляем к этому пути имя файла
    attach.send_keys(file_path)
    button = browser.find_element_by_tag_name('button')
    button.click()
    print(current_dir, '\n========\n', file_path)

finally:
    time.sleep(30)
    browser.quit()

