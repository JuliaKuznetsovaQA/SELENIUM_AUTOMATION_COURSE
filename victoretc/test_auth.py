from selenium.webdriver.common.by import By
from data import *
from locators import *
from generator import generated_user, generated_password


def test_auth_positive(browser):
    """Позитивный"""
    browser.get(main_page)
    user = next(generated_user())
    print(user.first_name)
    genpas = generated_password()
    print(genpas)
    browser.find_element(By.XPATH, name).send_keys(user.first_name)
    browser.find_element(By.XPATH, password).send_keys(genpas)
    browser.find_element(By.XPATH, checkbox).click()
    assert browser.find_element(By.XPATH, register_button).is_enabled()


def test_auth_negative_no_name(browser):
    """Негативный: не введено имя"""
    browser.get(main_page)
    genpas = generated_password()
    browser.find_element(By.XPATH, password).send_keys(genpas)
    browser.find_element(By.XPATH, checkbox).click()
    assert browser.find_element(By.XPATH, register_button).is_enabled() == False


def test_auth_negative_no_pass(browser):
    """Негативный: не введен пароль"""
    browser.get(main_page)
    user = next(generated_user())
    print(user.first_name)
    browser.find_element(By.XPATH, name).send_keys(user.first_name)
    browser.find_element(By.XPATH, checkbox).click()
    assert browser.find_element(By.XPATH, register_button).is_enabled() == False


def test_auth_negative_no_checkbox(browser):
    """Негативный: не отмечен чек-бокс"""
    browser.get(main_page)
    user = next(generated_user())
    print(user.first_name)
    genpas = generated_password()
    print(genpas)
    browser.find_element(By.XPATH, name).send_keys(user.first_name)
    browser.find_element(By.XPATH, password).send_keys(genpas)
    assert browser.find_element(By.XPATH, register_button).is_enabled() == False


