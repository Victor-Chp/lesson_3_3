# !/usr/bin/env python3
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_check_button_add_to_basket(browser):
    browser.get(link)
    button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((
        By.XPATH, '//form[@id="add_to_basket_form"]//button[@type="submit"]')))
    time.sleep(5)
    assert button is not None
