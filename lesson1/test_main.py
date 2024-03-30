import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome()

@pytest.fixture
def auth():
    auth = webdriver.Chrome()
    auth.get("https://www.saucedemo.com/")
    auth.find_element('id', 'user-name').send_keys('standard_user')
    auth.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    auth.find_element(By.XPATH, '//*[@id="login-button"]').click()
    yield auth
    auth.quit()

"""Авторизация"""
def test_auth_positive():
    """Авторизация используя корректные данные (standard_user, secret_sauce)"""
    browser.get("https://www.saucedemo.com/")

    browser.find_element('id', 'user-name').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    assert browser.current_url == 'https://www.saucedemo.com/inventory.html', 'url не соответствует ожидаемому'

    browser.quit()


def test_auth_negative():
    """Авторизация используя некорректные данные (user, user)"""

    browser.get("https://www.saucedemo.com/")

    browser.find_element('id', 'user-name').send_keys('user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('user')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    assert browser.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3').is_displayed()
    assert browser.current_url != 'https://www.saucedemo.com/inventory.html', 'url не соответствует ожидаемому'

    browser.quit()

"""Корзина"""
def test_add_to_cart():
    """Добавление товара в корзину через каталог"""

    browser.get("https://www.saucedemo.com/")
    browser.find_element('id', 'user-name').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    browser.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
    browser.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
    assert browser.find_element(By.XPATH, '//*[text()="Sauce Labs Backpack"]').is_displayed()
    browser.quit()


def test_remove_from_cart():
    try:
        browser.get("https://www.saucedemo.com/")
        browser.find_element('id', 'user-name').send_keys('standard_user')
        browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
        browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
        browser.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
        browser.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
        browser.find_element(By.XPATH, '//*[@id="remove-sauce-labs-backpack"]').click()
        with pytest.raises(selenium.common.exceptions.NoSuchElementException):
            browser.find_element(By.XPATH, '//*[text()="Sauce Labs Backpack"]')
            pytest.fail("Не должно быть товара в корзине")
    finally:
        browser.quit()


def test_add_to_cart_from_item_card(auth):
    """Добавление товара в корзину из карточки товара"""
    auth.find_element(By.XPATH, '// *[text() = "Sauce Labs Fleece Jacket"]').click()
    auth.find_element(By.ID, 'add-to-cart').click()
    auth.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
    assert auth.find_element(By.XPATH, '// *[text() = "Sauce Labs Fleece Jacket"]').is_displayed()


def test_remove_from_item_card(auth):
    """Удаление товара из корзины через карточку товара"""
    auth.find_element(By.XPATH, '// *[text() = "Sauce Labs Fleece Jacket"]').click()
    auth.find_element(By.ID, 'add-to-cart').click()
    auth.find_element(By.ID, 'remove').click()
    auth.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
    try:
        with pytest.raises(selenium.common.exceptions.NoSuchElementException):
            auth.find_element(By.XPATH, '//*[text()="Sauce Labs Fleece Jacket"]')
            pytest.fail("Не должно быть товара в корзине")
    finally:
        auth.quit()


"""Карточка товара"""

def test_item_card_from_image(auth):
    """Успешный переход к карточке товара после клика на картинку товара"""
    auth.find_element(By.ID, 'item_1_img_link').click()
    assert auth.current_url == 'https://www.saucedemo.com/inventory-item.html?id=1', 'Url не соответствует ожидаемому'


def test_item_card_from_title(auth):
    """Успешный переход к карточке товара после клика на название товара"""
    auth.find_element(By.ID, 'item_0_title_link').click()
    assert auth.current_url == 'https://www.saucedemo.com/inventory-item.html?id=0', 'Url не соответствует ожидаемому'

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


