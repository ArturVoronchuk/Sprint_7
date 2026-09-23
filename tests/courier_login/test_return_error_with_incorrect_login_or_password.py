import pytest
import requests

from data.urls import URL
from helper import Helper


@pytest.mark.parametrize(
    "field_to_break",
    ["login", "password"],
    ids=["неверный логин", "неверный пароль"]
)

class TestReturnErrorWithIncorrectLoginOrPassword:
    def test_return_error_with_incorrect_login_or_password(self, courier_data, field_to_break):

        payload = {
            "login": courier_data["login"],
            "password": courier_data["password"]
        }

        payload[field_to_break] = Helper.random_string()
        response = requests.post(f"{URL}/api/v1/courier/login", json=payload)

        assert response.status_code == 404 , (
            f"Ожидался 404 при некорректном '{payload}', "
            f"но получен {response.status_code}. Ответ: {response.text}"
        )

        body = response.json()
        message = body.get("message", "")

        assert "Учетная запись не найдена" in message, (
            f"Ожидалось 'Учетная запись не найдена', получено: {message}"
        )