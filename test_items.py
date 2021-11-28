from selenium import webdriver
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_item(browser):
    browser.get(link)
    time.sleep(10)
    button = browser.find_elements_by_css_selector("button.btn-primary")
    assert button, "Кнопки добавления в корзину нет"