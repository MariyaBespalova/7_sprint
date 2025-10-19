import allure
import pytest
import requests
from faker import Faker
from data import Url, Data, ResponseMessage



fake = Faker()

class TestCreateCourier:
    @allure.title('Проверяем создание курьера с обязательными полями')
    def test_success_create_new_courier(self):
        
        response = requests.post(url = f"{Url.MAIN_URL}{Url.COURIER_URL}", json=Data.new_courier)
        assert response.status_code == 201 and response.json()["ok"] == True

    @allure.title('Проверяем что упадет ошибка при попытки создания курьера который уже есть в системе')
    def test_check_create_identical_couriers(self):

        response = requests.post(url = f"{Url.MAIN_URL}{Url.COURIER_URL}", json=Data.courier)
        assert response.status_code == 409 and response.json()["message"] == ResponseMessage.USERNAME_ALREADY_USE


    @allure.title('Проверяем что упадет ошибка при попытки создания курьера без обязательных полей')
    def test_create_courier_without_required_field(self):
        incomplete_data = Data.new_courier.copy()
        del incomplete_data['login']
        
        response = requests.post(url = f'{Url.MAIN_URL}{Url.COURIER_URL}',json = incomplete_data)

        assert response.status_code == 400 and response.json()["message"] == ResponseMessage.INSUFFICIENT_DATA

     