from typing import Literal
import allure
import pytest
import requests
import random
import datetime
from data import Url, Data
from faker import Faker

fake = Faker()

class TestCreateOrder:
    @allure.title('Проверка создания заказа')
    @pytest.mark.parametrize("color", [("BLACK",), ("GREY",), ("BLACK", "GREY"), ("",)])
    def test_create_order_with_(self, color: Literal['BLACK'] | Literal['GREY'] | Literal['']):
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

        response = requests.post(url = f"{Url.MAIN_URL}{Url.ORDER_URL}", json=order_data)

        assert response.status_code == 201 and 'track' in response.json()

        order_id = response.json()['track']
        #   удаляем заказ после его успешного создания
        delete_response = requests.put(url=f"{Url.MAIN_URL}{Url.CANCEL_ORDER}", json = order_id)
        assert delete_response.status_code == 200, f"Заказ с ID={order_id} не удался удалить"







