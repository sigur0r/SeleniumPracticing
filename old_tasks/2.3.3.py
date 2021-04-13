from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    booking = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = browser.find_element_by_id("book")
    button.click()

    y = browser.find_element_by_id("input_value").text
    x = float(y)
    numba = str(math.log(abs(12 * math.sin(x))))

    input1 = browser.find_element_by_id('answer')
    input1.send_keys(numba)

    button_new = browser.find_element_by_id("solve")
    button_new.click()

finally:

    time.sleep(10)

    browser.quit()
