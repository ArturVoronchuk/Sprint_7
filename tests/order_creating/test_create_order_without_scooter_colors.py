import requests

from data.urls import URL
from helper import Helper

class TestCreateOrderWithoutScooterColors():
    def test_order_creating_without_scooter_colors(self):
        payload = {
            "firstName": Helper.random_string(),
            "lastName": Helper.random_string(),
            "address": "ул. Тестовая, д. 1",
            "metroStation": 4,
            "phone": "+79990000000",
            "rentTime": 5,
            "deliveryDate": "2024-12-10",
            "comment": "Тестовый комментарий"
        }

        create_order = requests.post(f"{URL}/api/v1/orders", json=payload)
        track = create_order.json()["track"]

        get_order = requests.get(f"{URL}/api/v1/orders/track", params={"t": track})
        order = get_order.json()["order"]

        assert order.get("color") is None, (
            f"Ожидался color=None, но получен: {order.get('color')}"
        )