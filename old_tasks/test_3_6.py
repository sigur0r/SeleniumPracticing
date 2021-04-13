import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('lesson', ["236895", "236896", "236898", "236899", "236903", "236904", "236905"])
def test_answer_should_be_correct(browser, lesson):
    link = f"https://stepik.org/lesson/{lesson}/step/1"
    browser.get(link)
    input1 = browser.find_element_by_tag_name("textarea")
    input1.send_keys(str(math.log(int(time.time()))))
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
    )
    button.click()
    expected_text = "Correct!"
    actual_text = browser.find_element_by_class_name("smart-hints__hint").text
    assert actual_text == expected_text
