import selenium.common.exceptions
from selenium.webdriver.common.by import By
import pytest
from locators import *
from data import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()

@pytest.fixture
def wait(auth):
    wait = WebDriverWait(auth, timeout=10)
    return wait

"""Бургер меню"""
def test_burger_exit(auth, wait):
    """Выход из системы"""
    auth.find_element(By.XPATH, burger_menu).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, burger_logout)))
    auth.find_element(By.XPATH, burger_logout).click()
    assert auth.current_url == main_page, 'Logout failed'


def test_burger_about(auth, wait):
    """Проверка работоспособности кнопки "About" в меню"""
    auth.find_element(By.XPATH, burger_menu).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, burger_about)))
    wait.until(EC.visibility_of_element_located((By.XPATH, burger_about)))
    auth.find_element(By.XPATH, burger_about).click()
    assert auth.current_url == about, 'About failed'


def test_burger_reset(auth, wait):
    """Проверка работоспособности кнопки "Reset App State". """
    auth.find_element(By.XPATH, backpack_add_to_cart).click()
    assert auth.find_element(By.XPATH, shopping_badge).is_displayed()
    auth.find_element(By.XPATH, burger_menu).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, burger_reset)))
    auth.find_element(By.XPATH, burger_reset).click()
    try:
        with pytest.raises(selenium.common.exceptions.NoSuchElementException):
            auth.find_element(By.XPATH, shopping_badge)
            pytest.fail("Не должно быть товара в корзине")
    finally:
        pass
    auth.find_element(By.XPATH, shopping_cart).click()
    assert len(auth.find_elements(By.XPATH, card_item_price)) == 0



