import requests
from data.urls import URL
from helper import Helper

class TestCourierRequiredFields:
    def test_required_fields_validation(self):

        payload = {
            "login": Helper.random_string(),
            "password": Helper.random_string(),
            "firstName": Helper.random_string()
        }

        response = requests.post(f"{URL}/api/v1/courier", json=payload)

        assert response.status_code == 201, (
            f"Ожидался 201, но получен {response.status_code}. Ответ: {response.text}"
        )