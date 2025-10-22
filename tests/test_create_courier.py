import allure
import pytest
import requests
from faker import Faker
from data import Data, ResponseMessage
from urls import Url

fake = Faker()

class TestCreateCourier:
    @allure.title('Проверяем создание курьера с обязательными полями')
    def test_success_create_new_courier(self, create_courier):
        with allure.step("Проверка успешного создания курьера"):
            assert create_courier.status_code == 201 and create_courier.json()["ok"] == True

    @allure.title('Проверяем что упадет ошибка при попытки создания курьера который уже есть в системе')
    def test_check_create_identical_couriers(self, create_courier):
        with allure.step("Создание курьера"):    
            first_response = create_courier 
            with allure.step("Проверка успешного создания курьера"):
                assert first_response.status_code == 201 and first_response.json()["ok"] == True
            with allure.step("Проверка создания курьера с теми же данными"):
                response = requests.post(url = f"{Url.MAIN_URL}{Url.COURIER_URL}", json=first_response.request.body.decode("utf-8"))
                assert response.status_code == 409 and response.json()["message"] == ResponseMessage.USERNAME_ALREADY_USE


    @allure.title('Проверяем что упадет ошибка при попытки создания курьера без обязательных полей')
    @pytest.mark.parametrize("field_to_remove", ["login", "password"])
    def test_create_courier_without_required_field(field_to_remove):
        with allure.step("Создание копии данных"):
            incomplete_data = Data.new_courier.copy()
        
            with allure.step("Удаляем нужное поле"):
                del incomplete_data[field_to_remove]
        
                with allure.step("Попытка создать курьера без обязательного поля"):
                    response = requests.post(url=f"{Url.MAIN_URL}{Url.COURIER_URL}", json=incomplete_data)
                    with allure.step("Проверка результатов"):
                        assert response.status_code == 400
                        assert response.json()["message"] == ResponseMessage.INSUFFICIENT_DATA