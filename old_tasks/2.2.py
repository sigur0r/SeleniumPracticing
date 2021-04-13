from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")

    x = browser.find_element_by_id("num1").text
    y = browser.find_element_by_id("num2").text

    sum1 = int(x)
    sum2 = int(y)
    overall = sum1 + sum2

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text('%s' % overall)

    browser.find_element_by_tag_name("button").click()

finally:

    time.sleep(10)

    browser.quit()
