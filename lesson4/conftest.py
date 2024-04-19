import pytest
from selenium import webdriver
from lesson4.pages.auth_page import LoginPage
# from urls import base_url

base_url = 'https://victoretc.github.io/selenium_waits/'

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture()
def login_page(driver):
    page = LoginPage(driver, base_url)
    return page