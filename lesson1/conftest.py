import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from data import *
from locators import *
import allure

@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.fixture
def auth(browser):
    auth = browser
    auth.get(main_page)
    auth.find_element(By.XPATH, username_field).send_keys(login)
    auth.find_element(By.XPATH, password_field).send_keys(password)
    auth.find_element(By.XPATH, login_button).click()
    yield auth

