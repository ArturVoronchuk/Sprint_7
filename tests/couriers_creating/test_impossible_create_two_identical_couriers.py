import allure
import requests

from data.urls import URL, COURIER_CREATE_ENDPOINT

class TestCantCreateTwoIdenticalCouriers:

    @allure.title("Нельзя создать двух курьеров с одинаковым логином: 409 Conflict")
    def test_cant_create_two_identical_couriers(self, courier_data):

        payload = {
            "login": courier_data["login"],
            "password": courier_data["password"],
            "firstName": courier_data["firstName"]
        }

        with allure.step("Пытаемся создать второго курьера с тем же логином"):
            response_second = requests.post(f"{URL}{COURIER_CREATE_ENDPOINT}", json=payload)

        assert response_second.status_code == 409, (
            f"Ожидался 409 (Conflict), но получен {response_second.status_code}. "
            f"Ответ: {response_second.text}"
        )

        body = response_second.json()
        message = body.get("message", "")

        assert "Этот логин уже используется" in message, (
            f"Ожидалось сообщение 'Этот логин уже используется', но получено: {message}"
        )
