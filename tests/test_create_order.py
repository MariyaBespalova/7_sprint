from typing import Literal
import allure
import pytest
import requests
import random
import datetime
from urls import Url
from faker import Faker


fake = Faker()

class TestCreateOrder:
    @allure.title('Проверка создания заказа')
    @pytest.mark.parametrize("color", [("BLACK",), ("GREY",), ("BLACK", "GREY"), ("",)])
    def test_create_order_with_(self, delete_order, color: Literal['BLACK'] | Literal['GREY'] | Literal['']):
        with allure.step("Создаем набор данных для заказа самоката"):
            order_data = {
                "firstName": fake.first_name(),
                "lastName": fake.last_name(),
                "address": fake.address(),
                "metroStation": random.randint(0, 100),
                "phone": fake.phone_number(),
                "rentTime": random.randint(0, 100),
                "deliveryDate": (datetime.datetime.now() + datetime.timedelta(days=random.randint(0, 10))).strftime("%Y-%m-%d"),
                "comment": fake.text(),
                "colors": list(color)
            }
            with allure.step("Отправляем запрос"):
                response = requests.post(url = f"{Url.MAIN_URL}{Url.ORDER_URL}", json=order_data)
                with allure.step("Проверка результатов"):
                    assert response.status_code == 201 and 'track' in response.json()

                    with allure.step("Получаем id заказа"):
                        order_id = response.json()['track']
                        with allure.step("Отменяем заказ после его успешного создания и проверяем результат"):
                            delete_response = delete_order(order_id)
                            assert delete_response.status_code == 200, f"Заказ с ID={order_id} не удался удалить"







