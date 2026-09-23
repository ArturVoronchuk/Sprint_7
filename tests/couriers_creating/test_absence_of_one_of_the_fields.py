import pytest
import requests
from data.urls import URL
from helper import Helper

@pytest.mark.parametrize(
    "missing_field",
    ["login", "password"],
    ids=["без логина", "без пароля"]
)
class TestAbsenceOfOneOfTheFields:
    def test_absence_of_one_of_the_fields_returns_an_error(self, missing_field):

        payload = {
            "login": Helper.random_string(),
            "password": Helper.random_string(),
            "firstName": Helper.random_string()
        }

        bad_payload = {k: v for k, v in payload.items() if k != missing_field}
        response = requests.post(f"{URL}/api/v1/courier", json=bad_payload)

        assert response.status_code == 400, (
            f"Ожидался 400 при отсутствии поля '{missing_field}', "
            f"но получен {response.status_code}. Ответ: {response.text}"
        )

        body = response.json()
        message = body.get("message", "")

        assert "Недостаточно данных" in message, (
            f"Ожидалось сообщение 'Недостаточно данных', получено: {message}"
        )