import selenium.common.exceptions
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.ui import Select
import time
from locators import *
from data import *


"""Оформление заказа"""
def test_purchase(auth):
    """Оформление заказа используя корректные данные"""
    auth.find_element(By.ID, 'item_3_img_link').click()
    auth.find_element(By.ID, 'add-to-cart').click()
    auth.find_element(By.ID, 'shopping_cart_container').click()
    auth.find_element(By.ID, 'checkout').click()
    auth.find_element(By.ID, 'first-name').send_keys('James')
    auth.find_element(By.ID, 'last-name').send_keys('Smith')
    auth.find_element(By.ID, 'postal-code').send_keys('901234')
    auth.find_element(By.ID, 'continue').click()
    assert auth.find_element(By.ID, 'item_3_title_link').is_displayed()
    assert auth.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[1]').text == '1'
    auth.find_element(By.ID, 'finish').click()
    assert auth.current_url == 'https://www.saucedemo.com/checkout-complete.html', 'Покупка не совершена'
    assert auth.find_element(By.ID, 'checkout_complete_container').is_displayed()

"""Фильтр"""

def test_filter_A_Z(auth):
    """Проверка работоспособности фильтра (A to Z)"""
    auth.find_element(By.CLASS_NAME, 'product_sort_container').click()
    n = auth.find_elements(By.XPATH, '//*[@class="inventory_list"]/div')
    x = ''
    for i in range(1, len(n)+1):
        path = f'//*[@class="inventory_list"]/div[{i}]/div[@class="inventory_item_description"]/div[@class="inventory_item_label"]/a/div'
        assert auth.find_element(By.XPATH, path).text > x, 'Неверная работа фильтра'
        x = auth.find_element(By.XPATH, path).text
        print(x)


def test_filter_Z_A(auth):
    """Проверка работоспособности фильтра (Z to A)"""
    select = Select(auth.find_element(By.CLASS_NAME, 'product_sort_container'))
    select.select_by_value("za")
    n = auth.find_elements(By.XPATH, '//*[@class="inventory_list"]/div')
    print()
    for i in range(1, len(n)+1):
        path = f'//*[@class="inventory_list"]/div[{i}]/div[@class="inventory_item_description"]/div[@class="inventory_item_label"]/a/div'
        print(auth.find_element(By.XPATH, path).text)
    print('**********************************')
    x = ''
    for i in range(len(n), 0, -1):
        path = f'//*[@class="inventory_list"]/div[{i}]/div[@class="inventory_item_description"]/div[@class="inventory_item_label"]/a/div'
        assert auth.find_element(By.XPATH, path).text > x, 'Неверная работа фильтра'
        x = auth.find_element(By.XPATH, path).text
        print(x)

def test_filter_low_to_high(auth):
    """Проверка работоспособности фильтра (low to high)"""
    select = Select(auth.find_element(By.CLASS_NAME, 'product_sort_container'))
    select.select_by_value("lohi")
    n = auth.find_elements(By.XPATH, '//*[@class="inventory_list"]/div')
    print()
    x = 0
    for i in range(1, len(n) + 1):
        path = f'//*[@class="inventory_list"]/div[{i}]/div[@class="inventory_item_description"]/div[@class="pricebar"]/div'
        n = float(auth.find_element(By.XPATH, path).text[1:])
        assert n >= x, 'Неверная работа фильтра'
        x = n
        print(x)


def test_filter_hith_to_low(auth):
    """Проверка работоспособности фильтра (high to low)"""
    select = Select(auth.find_element(By.CLASS_NAME, 'product_sort_container'))
    select.select_by_value("hilo")
    n = auth.find_elements(By.XPATH, '//*[@class="inventory_list"]/div')
    print()
    x = 0
    for i in range(len(n), 0, -1):
        path = f'//*[@class="inventory_list"]/div[{i}]/div[@class="inventory_item_description"]/div[@class="pricebar"]/div'
        n = float(auth.find_element(By.XPATH, path).text[1:])
        assert n >= x, 'Неверная работа фильтра'
        x = n
        print(x)


"""Бургер меню"""
def test_burger_exit(auth):
    """Выход из системы"""
    auth.find_element(By.ID, 'react-burger-menu-btn').click()
    time.sleep(3)
    auth.find_element(By.XPATH, '//a[@id="logout_sidebar_link"]').click()
    assert auth.current_url == 'https://www.saucedemo.com/', 'Logout failed'

def test_burger_about(auth):
    """Проверка работоспособности кнопки "About" в меню"""
    auth.find_element(By.ID, 'react-burger-menu-btn').click()
    time.sleep(2)
    auth.find_element(By.XPATH, '//*[@id="about_sidebar_link"]').click()
    assert auth.current_url == 'https://saucelabs.com/', 'About failed'


def test_burger_reset(auth):
    """Проверка работоспособности кнопки "Reset App State". """
    auth.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
    assert auth.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
    auth.find_element(By.ID, 'react-burger-menu-btn').click()
    time.sleep(2)
    auth.find_element(By.XPATH, '//*[@id="reset_sidebar_link"]').click()
    time.sleep(1)
    try:
        with pytest.raises(selenium.common.exceptions.NoSuchElementException):
            auth.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
            pytest.fail("Не должно быть товара в корзине")
    finally:
        auth.quit()


