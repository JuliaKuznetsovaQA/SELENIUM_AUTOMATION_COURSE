from lesson5.pages import auth
import allure

url = 'https://victoretc.github.io/selenium_waits/'

@allure.title("Авторизация")
def test_login():
    auth.visit(url)
    auth.start().click()
    auth.login()
    auth.success_mesage_have_text('Вы успешно зарегистрированы!')


