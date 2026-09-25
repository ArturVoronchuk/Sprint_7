import allure
import pytest
import requests

from data.data import COURIER_PAYLOAD
from data.urls import URL, COURIER_CREATE_ENDPOINT


class TestCourierCanBeCreated:
    @allure.title("Курьера можно создать: запрос возвращает код 201 и ok=true в теле ответа")
    def test_courier_can_be_created(self):
        payload = COURIER_PAYLOAD.copy()

        with allure.step("Создаем курьера"):
            response = requests.post(f"{URL}{COURIER_CREATE_ENDPOINT}", json=payload)

        assert response.status_code == 201, (
            f"Ожидался 201 Created, но получен {response.status_code}. "
            f"Ответ: {response.text}"
        )

        body = response.json()
        assert body.get("ok") is True, (
            f"Ожидается ok: true, но получено: {body}"
        )

    @pytest.mark.parametrize(
        "missing_field",
        ["login", "password"],
        ids=["без логина", "без пароля"]
    )

    @allure.title("Если одного из обязательных полей нет - запрос возвращает ошибку")
    def test_absence_of_one_of_the_fields_returns_an_error(self, missing_field):
        payload = COURIER_PAYLOAD.copy()

        bad_payload = {k: v for k, v in payload.items() if k != missing_field}

        with allure.step("Создаем курьера, передав обязательные поля."):
            response = requests.post(f"{URL}{COURIER_CREATE_ENDPOINT}", json=bad_payload)

        assert response.status_code == 400, (
            f"Ожидался 400 при отсутствии поля '{missing_field}', "
            f"но получен {response.status_code}. Ответ: {response.text}"
        )

        body = response.json()
        message = body.get("message", "")

        assert "Недостаточно данных" in message, (
            f"Ожидалось сообщение 'Недостаточно данных', получено: {message}"
        )