from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id('num1')
    y_element = browser.find_element_by_id('num2')
    sum1 = int(x_element.text) + int(y_element.text)
    print(sum1)
    select = Select(browser.find_element_by_tag_name('select'))
    select.select_by_value(str(sum1))
    browser.find_element_by_class_name('btn').click()

finally:
    time.sleep(10)
    browser.quit()