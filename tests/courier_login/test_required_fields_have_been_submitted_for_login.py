import requests

from data.urls import URL

class TestRequiredFieldsHaveBeenSubmittedForLogin:
    def test_required_fields_have_been_submitted_for_login(self, courier_data):
        payload = {
            "login": courier_data["login"],
            "password": courier_data["password"]
        }

        response = requests.post(f"{URL}/api/v1/courier/login", json=payload)

        assert response.status_code == 200, (
            f"Ожидался 200, но получен {response.status_code}. Ответ: {response.text}"
        )

        body = response.json()
        assert "id" in body, (
            f"В ответе отсутствует 'id' курьера. Получено: {body}"
        )