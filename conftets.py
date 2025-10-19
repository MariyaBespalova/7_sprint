import pytest
import requests
from faker import Faker
import random
import datetime
from data import Url

fake = Faker()

#   Фикстура для создания заказа и возврата id трека.
@pytest.fixture(scope="module")
def create_order():
    
    def _create_order(order_data=None):
        if order_data is None:
            # Генерируем случайные данные заказа
            order_data = {
                "firstName": fake.first_name(),
                "lastName": fake.last_name(),
                "address": fake.address(),
                "metroStation": random.randint(0, 100),
                "phone": fake.phone_number(),
                "rentTime": random.randint(0, 100),
                "deliveryDate": (datetime.datetime.now() + datetime.timedelta(days=random.randint(0, 10))).strftime("%Y-%m-%d"),
                "comment": fake.text(),
                "colors": []
            }
            
        response = requests.post(url = f"{Url.MAIN_URL}{Url.ORDER_URL}", json=order_data)
        return response
    
    yield _create_order

#  фикстура для получения списка заказов
@pytest.fixture
def get_order_list():
    def _get_order_list():
        response = requests.get(url=f"{Url.MAIN_URL}{Url.ORDER_URL}")
        return response
    return _get_order_list