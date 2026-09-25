import pytest
import requests

from data.urls import URL, COURIER_LOGIN_ENDPOINT, COURIER_CREATE_ENDPOINT
from data.user_generator import UserGenerator

@pytest.fixture(scope="function")
def courier_data(request):
    generator = UserGenerator()
    login, password, first_name = generator.register_new_courier_and_return_login_password()

    login_resp = requests.post(
        f"{URL}{COURIER_LOGIN_ENDPOINT}",
        json={"login": login, "password": password}
    )

    courier_id = login_resp.json()["id"]

    def delete_courier():
        requests.delete(f"{URL}{COURIER_CREATE_ENDPOINT}/{courier_id}")

    request.addfinalizer(delete_courier)

    return {
        "login": login,
        "password": password,
        "firstName": first_name,
        "id": courier_id
    }