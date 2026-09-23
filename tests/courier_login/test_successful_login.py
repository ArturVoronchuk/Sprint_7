import requests
from data.urls import URL

class TestSuccessfulLogin:
    def test_successful_login(self, courier_data):

        payload = {
            "login": courier_data["login"],
            "password": courier_data["password"]
        }

        response = requests.post(f"{URL}/api/v1/courier/login", json=payload)

        assert response.status_code == 200, (
            f"Ожидался 200, но получен {response.status_code}. Ответ: {response.text}"
        )