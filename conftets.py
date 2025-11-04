import pytest
import requests
from faker import Faker
from data import Url, Data

fake = Faker()

#   фикстура для создания курьера
@pytest.fixture(scope="module")
def create_courier():
    response = requests.post(url = f"{Url.MAIN_URL}{Url.COURIER_URL}", json=Data.new_courier)
    return response

#   фикстура для отмены заказа
@pytest.fixture(scope="function")
def delete_order():
    def _delete(order_id):
        response = requests.put(url=f"{Url.MAIN_URL}{Url.CANCEL_ORDER}", json = order_id)
        return response
    
    yield _delete
