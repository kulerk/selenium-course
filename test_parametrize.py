import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import driver_firefox

LINKS = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
]


@pytest.mark.parametrize('link', LINKS)
def test_parametrize_stepik(driver, link):
    driver.get(link)
    input_field = WebDriverWait(driver, 30).until(
                   EC.visibility_of_element_located((
                   By.CLASS_NAME, "textarea")))

    answer = math.log(int(time.time()))
    input_field.send_keys(str(answer))
    submit_button = driver.find_element_by_css_selector('.submit-submission')
    submit_button.click()
    confirmation = WebDriverWait(driver, 30).until(
                   EC.visibility_of_element_located((
                   By.CLASS_NAME, "smart-hints__hint"))).text

    assert confirmation == "Correct!"


