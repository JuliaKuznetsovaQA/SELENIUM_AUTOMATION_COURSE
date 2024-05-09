import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from lesson4.pages.auth_page import LoginPage
from selenium.webdriver.chrome.service import Service
from lesson4.urls import base_url

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
    yield driver
    driver.quit()

@pytest.fixture()
def login_page(driver):
    page = LoginPage(driver, base_url)
    return page