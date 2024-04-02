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
    auth.find_element(By.ID, 'add-to-cart').click()
    auth.find_element(By.ID, 'shopping_cart_container').click()
    auth.find_element(By.ID, 'checkout').click()
    auth.find_element(By.ID, 'first-name').send_keys(user.first_name)
    auth.find_element(By.ID, 'last-name').send_keys(user.last_name)
    auth.find_element(By.ID, 'postal-code').send_keys(user.postcode)
    auth.find_element(By.ID, 'continue').click()
    assert auth.find_element(By.ID, 'item_3_title_link').is_displayed()
    assert auth.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[1]').text == '1'
    auth.find_element(By.ID, 'finish').click()
    assert auth.current_url == 'https://www.saucedemo.com/checkout-complete.html', 'Покупка не совершена'
    assert auth.find_element(By.ID, 'checkout_complete_container').is_displayed()