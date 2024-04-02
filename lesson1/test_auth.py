from selenium.webdriver.common.by import By
from locators import *
from data import *


"""Авторизация"""
def test_auth_positive(auth):
    """Авторизация используя корректные данные (standard_user, secret_sauce)"""

    assert auth.current_url == catalogue, 'url не соответствует ожидаемому'



def test_auth_negative(browser):
    """Авторизация используя некорректные данные (user, user)"""

    browser.get(main_page)
    browser.find_element(By.XPATH, username_field).send_keys('user')
    browser.find_element(By.XPATH, password_field).send_keys('user')
    browser.find_element(By.XPATH, login_button).click()
    assert browser.find_element(By.XPATH, login_button).is_displayed()
    # '//*[@id="login_button_container"]/div/form/div[3]/h3'
    assert browser.current_url != catalogue, 'url не соответствует ожидаемому'