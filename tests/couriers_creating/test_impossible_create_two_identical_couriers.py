import requests
from data.urls import URL

class TestCantCreateTwoIdenticalCouriers:
    def test_cant_create_two_identical_couriers(self, courier_data):

        payload = {
            "login": courier_data["login"],
            "password": courier_data["password"],
            "firstName": courier_data["firstName"]
        }

        response = requests.post(f"{URL}/api/v1/courier", json=payload)

        assert response.status_code == 409, (
            f"Ожидался статус 409 (конфликт), но получен {response.status_code}. "
            f"Ответ: {response.text}"
        )

        body = response.json()
        message = body.get("message", "")

        assert "Этот логин уже используется" in message, (
            f"Ожидалось сообщение с фразой 'Этот логин уже используется', "
            f"но получено: {message}"
        )
