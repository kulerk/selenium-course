import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_cart_button_on_page(browser):
    browser.get(link)
    button = browser.find_elements_by_css_selector("button.btn-primary")
    assert button, "Кнопки добавления в корзину нет"