import requests

from data.urls import URL


class TestSuccessfulRequestReturnsId:
    def test_successful_request_returns_id(self, courier_data):

        payload = {
            "login": courier_data["login"],
            "password": courier_data["password"]
        }

        response = requests.post(f"{URL}/api/v1/courier/login", json=payload)
        body = response.json()

        assert 'id' in body, (
            f"В ответе отсутствует обязательное поле - 'id' курьера"
            f"Получен ответ {body}"
        )