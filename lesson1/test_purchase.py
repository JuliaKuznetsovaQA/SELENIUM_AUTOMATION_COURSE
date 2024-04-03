from selenium.webdriver.common.by import By
from locators import *
from data import *
from generator import generated_user


"""Оформление заказа"""


def test_purchase(auth):
    """Оформление заказа используя корректные данные"""
    """генерация данных пользователя"""
    user = next(generated_user())
    auth.find_element(By.XPATH, t_shirt_red_image).click()
    auth.find_element(By.XPATH, add_to_cart).click()
    auth.find_element(By.XPATH, shopping_cart).click()
    auth.find_element(By.XPATH, checkout).click()
    auth.find_element(By.XPATH, first_name).send_keys(user.first_name)
    auth.find_element(By.XPATH, last_name).send_keys(user.last_name)
    auth.find_element(By.XPATH, postal_code).send_keys(user.postcode)
    auth.find_element(By.XPATH, purchase_continue).click()
    assert auth.find_element(By.XPATH, t_shirt_red_title).is_displayed()
    assert auth.find_element(By.XPATH, checkout_summary).text == '1'
    auth.find_element(By.XPATH, finish).click()
    assert auth.current_url == checkout_complete, 'Покупка не совершена'
    assert auth.find_element(By.ID, 'checkout_complete_container').is_displayed()
    