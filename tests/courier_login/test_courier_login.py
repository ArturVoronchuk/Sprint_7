import allure
import requests

from data.data import COURIER_PAYLOAD
from data.urls import URL, COURIER_LOGIN_ENDPOINT
from helper import Helper


@allure.story("Авторизация курьера")
class TestCourierLogin:

    @allure.title("Курьер может авторизоваться: 200 и id в ответе")
    def test_courier_can_login_returns_id(self, courier_data):
        payload = {
            "login": courier_data["login"],
            "password": courier_data["password"]
        }

        with allure.step("Логинимся валидными данными"):
            response = requests.post(f"{URL}{COURIER_LOGIN_ENDPOINT}", json=payload)

        assert response.status_code == 200, (
            f"Ожидался 200, получен {response.status_code}. Ответ: {response.text}"
        )

        body = response.json()
        assert "id" in body, f"В ответе нет 'id'. Получено: {body}"

    @allure.title("Авторизация без логина возвращает ошибку 400")
    def test_login_without_login_returns_error(self):
        payload = COURIER_PAYLOAD.copy()
        payload.pop("login")

        with allure.step("Логинимся без поля login"):
            response = requests.post(f"{URL}{COURIER_LOGIN_ENDPOINT}", json=payload)

        assert response.status_code == 400, (
            f"Ожидался 400 при отсутствии login, "
            f"получен {response.status_code}. Ответ: {response.text}"
        )

        body = response.json()
        assert "Недостаточно данных для входа" in body.get("message", ""), (
            f"Ожидалось 'Недостаточно данных для входа', получено: {body}"
        )

    @allure.title("Авторизация без пароля возвращает ошибку 504 (фактический код стенда)")
    def test_login_without_password_returns_error(self):
        payload = COURIER_PAYLOAD.copy()
        payload.pop("password")

        with allure.step("Логинимся без поля password"):
            response = requests.post(f"{URL}{COURIER_LOGIN_ENDPOINT}", json=payload)

        assert response.status_code == 504, (
            f"Ожидался 504 при отсутствии password, "
            f"получен {response.status_code}. Ответ: {response.text}"
        )

    @allure.title("Авторизация с неверным паролем возвращает ошибку")
    def test_login_with_wrong_password_returns_error(self, courier_data):

        payload = {
            "login": courier_data["login"],
            "password": Helper.random_string()
        }

        with allure.step("Логинимся с неверным паролем"):
            response = requests.post(f"{URL}{COURIER_LOGIN_ENDPOINT}", json=payload)

        assert response.status_code == 404, (
            f"Ожидался 404, получен {response.status_code}. Ответ: {response.text}"
        )

        body = response.json()
        assert "Учетная запись не найдена" in body.get("message", ""), (
            f"Ожидалось 'Учетная запись не найдена', получено: {body}"
        )

    @allure.title("Авторизация под несуществующим пользователем возвращает ошибку")
    def test_login_with_non_existent_user_returns_error(self):
        payload = COURIER_PAYLOAD.copy()

        with allure.step("Логинимся под несуществующим пользователем"):
            response = requests.post(f"{URL}{COURIER_LOGIN_ENDPOINT}", json=payload)

        assert response.status_code == 404, (
            f"Ожидался 404, получен {response.status_code}. Ответ: {response.text}"
        )

        body = response.json()
        assert "Учетная запись не найдена" in body.get("message", ""), (
            f"Ожидалось 'Учетная запись не найдена', получено: {body}"
        )
