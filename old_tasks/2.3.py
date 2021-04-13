from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/execute_script.html")

    y = browser.find_element_by_id("input_value").text
    x = float(y)
    numba = str(math.log(abs(12*math.sin(x))))

    input1 = browser.find_element_by_id('answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
    input1.send_keys(numba)

    option1 = browser.find_element_by_id("robotCheckbox").click()

    option2 = browser.find_element_by_id("robotsRule").click()


    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:

    time.sleep(10)

    browser.quit()
