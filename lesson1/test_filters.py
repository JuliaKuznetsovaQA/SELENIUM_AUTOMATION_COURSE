from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from locators import *


"""Фильтр"""
def test_filter_A_Z(auth):
    """Проверка работоспособности фильтра (A to Z)"""
    select = Select(auth.find_element(By.CLASS_NAME, filter_class))
    select.select_by_value("az")
    n = auth.find_elements(By.XPATH, elements)
    x = ''
    for i in range(1, len(n)+1):
        path = item_label_start + str(i) + item_label_end
        assert auth.find_element(By.XPATH, path).text > x, 'Неверная работа фильтра'
        x = auth.find_element(By.XPATH, path).text
        print(x)


def test_filter_Z_A(auth):
    """Проверка работоспособности фильтра (Z to A)"""
    select = Select(auth.find_element(By.CLASS_NAME, filter_class))
    select.select_by_value("za")
    n = auth.find_elements(By.XPATH, elements)
    print()
    for i in range(1, len(n)+1):
        path = item_label_start + str(i) + item_label_end
        print(auth.find_element(By.XPATH, path).text)
    print('**********************************')
    x = ''
    for i in range(len(n), 0, -1):
        path = item_label_start + str(i) + item_label_end
        assert auth.find_element(By.XPATH, path).text > x, 'Неверная работа фильтра'
        x = auth.find_element(By.XPATH, path).text
        print(x)


def test_filter_low_to_high(auth):
    """Проверка работоспособности фильтра (low to high)"""
    select = Select(auth.find_element(By.CLASS_NAME, filter_class))
    select.select_by_value("lohi")
    n = auth.find_elements(By.XPATH, elements)
    print()
    x = 0
    for i in range(1, len(n) + 1):
        path = item_pricebar_start + str(i) + item_pricebar_end
        n = float(auth.find_element(By.XPATH, path).text[1:])
        assert n >= x, 'Неверная работа фильтра'
        x = n
        print(x)


def test_filter_high_to_low(auth):
    """Проверка работоспособности фильтра (high to low)"""
    select = Select(auth.find_element(By.CLASS_NAME, filter_class))
    select.select_by_value("hilo")
    n = auth.find_elements(By.XPATH, elements)
    print()
    x = 0
    for i in range(len(n), 0, -1):
        path = item_pricebar_start + str(i) + item_pricebar_end
        n = float(auth.find_element(By.XPATH, path).text[1:])
        assert n >= x, 'Неверная работа фильтра'
        x = n
        print(x)
