from selenium.webdriver.common.by import By
from locators import *
from data import *


"""Карточка товара"""

def test_item_card_from_image(auth):
    """Успешный переход к карточке товара после клика на картинку товара"""
    auth.find_element(By.XPATH, t_shirt_image).click()
    assert auth.current_url == t_shirt_card, 'Url не соответствует ожидаемому'


def test_item_card_from_title(auth):
    """Успешный переход к карточке товара после клика на название товара"""
    auth.find_element(By.XPATH, bike_light_title).click()
    assert auth.current_url == bike_light_card, 'Url не соответствует ожидаемому'
