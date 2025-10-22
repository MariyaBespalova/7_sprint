import pytest
import requests
from faker import Faker
import random
import datetime
from data import Url

fake = Faker()

class Helpers:
    
    #  Функция для получения списка заказов
    def get_order_list():
        def _get_order_list():
            response = requests.get(url=f"{Url.MAIN_URL}{Url.ORDER_URL}")
            return response
        return _get_order_list