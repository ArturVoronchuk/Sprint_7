import pytest
import requests

from data.urls import URL
from helper import Helper


@pytest.mark.parametrize(
        "scooter_color",
        [
            ["BLACK"],
            ["GREY"],
        ],
        ids=["BLACK", "GREY"]
    )

class TestChoosingScooterColor:
    def test_choosing_only_one_scooter_color(self,scooter_color):

        payload = {
            "firstName": Helper.random_string(),
            "lastName": Helper.random_string(),
            "address": "ул. Тестовая, д. 1",
            "metroStation": 4,
            "phone": "+79990000000",
            "rentTime": 5,
            "deliveryDate": "2024-12-10",
            "comment": "Тестовый комментарий",
            "color": scooter_color
        }

        create_order = requests.post(f"{URL}/api/v1/orders", json=payload)
        track = create_order.json()["track"]

        get_order = requests.get(f"{URL}/api/v1/orders/track", params={"t": track})
        order = get_order.json()["order"]

        assert order["color"] == scooter_color, (
            f"Ожидался color={scooter_color}, но получен: {order.get('color')}"
        )