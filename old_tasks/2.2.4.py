from selenium import webdriver
import time
import os

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name('lastname')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("ivan.petrov@gmail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'uploaddoc.txt')
    element = browser.find_element_by_id("file")
    element.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:

    time.sleep(10)

    browser.quit()
