import selenium.common.exceptions
from selenium.webdriver.common.by import By
import pytest
from locators import *


"""Корзина"""
def test_add_to_cart(auth):
    """Добавление товара в корзину через каталог"""

    auth.find_element(By.XPATH, backpack_add_to_cart).click()
    auth.find_element(By.XPATH, shopping_cart).click()
    assert auth.find_element(By.XPATH, backpack_in_cart).is_displayed()


def test_remove_from_cart(auth):
    """Удаление товара из корзины"""
    try:
        auth.find_element(By.XPATH, backpack_add_to_cart).click()
        auth.find_element(By.XPATH, shopping_cart).click()
        assert auth.find_element(By.XPATH, backpack_in_cart).is_displayed()
        auth.find_element(By.XPATH, backpack_remove).click()
        with pytest.raises(selenium.common.exceptions.NoSuchElementException):
            auth.find_element(By.XPATH, backpack_in_cart)
            pytest.fail("Не должно быть товара в корзине")
    finally:
        auth.quit()


def test_add_to_cart_from_item_card(auth):
    """Добавление товара в корзину из карточки товара"""
    auth.find_element(By.XPATH, fleece_jacket).click()
    auth.find_element(By.XPATH, add_to_cart).click()
    auth.find_element(By.XPATH, shopping_cart).click()
    assert auth.find_element(By.XPATH, fleece_jacket).is_displayed()


def test_remove_from_item_card(auth):
    """Удаление товара из корзины через карточку товара"""
    auth.find_element(By.XPATH, fleece_jacket).click()
    auth.find_element(By.XPATH, add_to_cart).click()
    auth.find_element(By.XPATH, remove_from_cart).click()
    auth.find_element(By.XPATH, shopping_cart).click()
    try:
        with pytest.raises(selenium.common.exceptions.NoSuchElementException):
            auth.find_element(By.XPATH, fleece_jacket)
            pytest.fail("Не должно быть товара в корзине")
    finally:
        auth.quit()
