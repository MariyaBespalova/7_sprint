import allure
import pytest
import requests
from faker import Faker
from data import Url, Data, ResponseMessage

fake = Faker()

class TestLoginCourier:
    @allure.title('Проверяем что упадет ошибка при попытки ввода логина курьера без обязательных полей')
    @pytest.mark.parametrize("login, password", [
        ("", "password"),
        ("username", "")])
    def test_login_courier_without_required_fields(self, login, password):
        courier = {
            "login": login,
            "password": password
        }

        response = requests.post(url=f"{Url.MAIN_URL}{Url.COURIER_LOGIN}", json=courier)
        assert response.status_code == 400 and response.json()["message"] == ResponseMessage.INSUFFICIENT_LOGIN_INFORMATION

    @allure.title('Проверяем что упадет ошибка при попытки логина несуществующего курьера')
    def test_login_courier(self):
        response = requests.post(url = f"{Url.MAIN_URL}{Url.COURIER_LOGIN}", json=Data.non_existent_courier)
        assert response.status_code == 404 and response.json()["message"] == ResponseMessage.ACCOUNT_NOT_FOUND


    @allure.title('Проверяем логин курьера')
    def test_login_courier_(self):
        courier = {
            "login": "gomezamy",
            "password": "7%j2Vigvqf"
        }

        response = requests.post(url = f"{Url.MAIN_URL}{Url.COURIER_LOGIN}", json=Data.courier_entrance)
        assert response.status_code == 200 and 'id' in response.json()