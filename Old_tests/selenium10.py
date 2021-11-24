from selenium import webdriver
import time
import os


try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    elements = browser.find_elements_by_css_selector('input.form-control')
    for element in elements:
        element.send_keys('kek')
    current_dir = os.path.abspath(os.path.dirname(__file__))   
    file_path = os.path.join(current_dir, 'file.txt')
    element = browser.find_element_by_id('file')
    element.send_keys(file_path)
    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()