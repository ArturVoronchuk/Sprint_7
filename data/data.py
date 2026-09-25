from conftest import courier_data
from helper import Helper

ORDER_PAYLOAD = {
    "firstName": Helper.random_string(),
    "lastName": Helper.random_string(),
    "address": "ул. Тестовая, д. 1",
    "metroStation": 4,
    "phone": "+79990000000",
    "rentTime": 5,
    "deliveryDate": "2024-12-10",
    "comment": "Тестовый комментарий",
}

COURIER_PAYLOAD = {
    "login": Helper.random_string(),
    "password": Helper.random_string(),
    "firstName": Helper.random_string()
}
