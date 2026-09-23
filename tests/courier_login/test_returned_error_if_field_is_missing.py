import pytest
import requests

from data.urls import URL
from helper import Helper

@pytest.mark.parametrize(
    "missing_field, expected_status",
    [
        ("login", 400),
        ("password", 504)
    ],
    ids=["без логина", "без пароля"]
)

class TestReturnedErrorIfFieldIsMissing:
    def test_returned_error_if_field_is_missing(self, missing_field, expected_status):

        payload = {
            "login": Helper.random_string(),
            "password": Helper.random_string()
        }

        bad_payload = {k: v for k, v in payload.items() if k != missing_field}
        response = requests.post(f"{URL}/api/v1/courier/login", json=bad_payload)

        assert response.status_code == expected_status, (
            f"Ожидался {expected_status} при отсутствии поля '{missing_field}'"
            f"но получен {response.status_code}. Ответ: {response.text}"
        )

        if expected_status == 400:
            body = response.json()
            message = body.get("message", "")
            assert "Недостаточно данных для входа" in message, (
                f"Ожидалось сообщение 'Недостаточно данных для входа', получено: {message}"
            )