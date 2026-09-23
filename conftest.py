import pytest

from data.urls import URL
from data.user_generator import UserGenerator

@pytest.fixture(scope="function")
def courier_data():
    generator = UserGenerator()
    result = generator.register_new_courier_and_return_login_password()

    login, password, first_name = result

    yield {
        "login": login,
        "password": password,
        "firstName": first_name
    }

