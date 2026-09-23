import requests
from data.urls import URL
from helper import Helper

class TestSuccessfulRequestReturnsOk:
    def test_successful_request_returns_ok(self):

        payload = {
            "login": Helper.random_string(),
            "password": Helper.random_string(),
            "firstName": Helper.random_string()
        }

        response = requests.post(f"{URL}/api/v1/courier", json=payload)

        body = response.json()

        assert body.get("ok") is True