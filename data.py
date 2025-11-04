import pytest
from faker import Faker

fake = Faker()


class Data:
    new_courier = {
            "login": fake.user_name(),
            "password": fake.password(),
            "firstName": fake.first_name()
        }
    
    courier = {
            "login": "gomezamy",
            "password": "7%j2Vigvqf",
            "firstName": "Christina"
        }
    non_existent_courier = {
        "login": fake.user_name(),
        "password": fake.password()
        }
    courier_entrance = {
            "login": "gomezamy",
            "password": "7%j2Vigvqf"
        }
    
class ResponseMessage:
    SUCCESSFULLY_CREATED = "ok: true"
    USERNAME_ALREADY_USE = "Этот логин уже используется"
    INSUFFICIENT_DATA = "Недостаточно данных для создания учетной записи"
    INSUFFICIENT_LOGIN_INFORMATION = "Недостаточно данных для входа"
    ACCOUNT_NOT_FOUND = "Учетная запись не найдена"

