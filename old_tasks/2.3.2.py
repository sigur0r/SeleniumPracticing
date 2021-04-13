from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    y = browser.find_element_by_id("input_value").text
    x = float(y)
    numba = str(math.log(abs(12 * math.sin(x))))

    input1 = browser.find_element_by_id('answer')
    input1.send_keys(numba)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:

    time.sleep(10)

    browser.quit()
