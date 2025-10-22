import allure
import pytest
import requests
from faker import Faker
from data import Data, ResponseMessage
from urls import Url

fake = Faker()

class TestLoginCourier:
    @allure.title('Проверяем что упадет ошибка при попытки ввода логина курьера без обязательных полей')
    @pytest.mark.parametrize("login, password", [
        ("", "password"),
        ("username", "")])
    def test_login_courier_without_required_fields(self, login, password):
        with allure.step("Создаем данные для курьера"):
            courier = {
                "login": login,
                "password": password
            }
            with allure.step("Отправляем запрос"):
                response = requests.post(url=f"{Url.MAIN_URL}{Url.COURIER_LOGIN}", json=courier)
                with allure.step("Проверка результатов"):
                    assert response.status_code == 400 and response.json()["message"] == ResponseMessage.INSUFFICIENT_LOGIN_INFORMATION

    @allure.title('Проверяем что упадет ошибка при попытки ввода логина несуществующего курьера')
    def test_login_courier(self):
        with allure.step("Отправляем запрос на создание курьера с несуществующим id"):
            response = requests.post(url = f"{Url.MAIN_URL}{Url.COURIER_LOGIN}", json=Data.non_existent_courier)
            with allure.step("Проверка результатов"):
                assert response.status_code == 404 and response.json()["message"] == ResponseMessage.ACCOUNT_NOT_FOUND


    @allure.title('Проверяем логин курьера')
    def test_login_courier_(self):
        with allure.step("Отправляем запрос на вход в систему"):
            response = requests.post(url = f"{Url.MAIN_URL}{Url.COURIER_LOGIN}", json=Data.courier_entrance)
            with allure.step("Проверка результатов"):
                assert response.status_code == 200 and 'id' in response.json()