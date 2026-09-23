import requests

from data.urls import URL
from helper import Helper

class TestBodyResponseContainsTrack:
    def test_body_response_contains_track(self):
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
        body = get_order.json()

        assert "track" in body["order"], (
            f"В теле ответа внутри 'order' отсутствует 'track'. "
            f"Получен ответ: {body}"
        )