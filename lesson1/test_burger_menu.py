import selenium.common.exceptions
from selenium.webdriver.common.by import By
import pytest
import time
from locators import *
from data import *


"""Бургер меню"""
def test_burger_exit(auth):
    """Выход из системы"""
    auth.find_element(By.XPATH, burger_menu).click()
    time.sleep(1)
    auth.find_element(By.XPATH, burger_logout).click()
    assert auth.current_url == main_page, 'Logout failed'


def test_burger_about(auth):
    """Проверка работоспособности кнопки "About" в меню"""
    auth.find_element(By.XPATH, burger_menu).click()
    time.sleep(1)
    auth.find_element(By.XPATH, burger_about).click()
    assert auth.current_url == about, 'About failed'


def test_burger_reset(auth):
    """Проверка работоспособности кнопки "Reset App State". """
    auth.find_element(By.XPATH, backpack_add_to_cart).click()
    assert auth.find_element(By.XPATH, shopping_badge).is_displayed()
    auth.find_element(By.XPATH, burger_menu).click()
    time.sleep(1)
    auth.find_element(By.XPATH, burger_reset).click()
    try:
        with pytest.raises(selenium.common.exceptions.NoSuchElementException):
            auth.find_element(By.XPATH, shopping_badge)
            pytest.fail("Не должно быть товара в корзине")
    finally:
        pass
    auth.find_element(By.XPATH, shopping_cart).click()
    assert len(auth.find_elements(By.XPATH, card_item_price)) == 0



