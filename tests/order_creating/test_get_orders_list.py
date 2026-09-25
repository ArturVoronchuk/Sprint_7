import allure
import pytest
import requests

from data.data import ORDER_PAYLOAD
from data.urls import URL, ORDERS_CREATE_ENDPOINT


@pytest.mark.parametrize(
    "color, address, delivery_date, phone",
    [
        (["BLACK"],            "ул. Тестовая, д. 1",   "2024-12-10", "+79990000001"),
        (["GREY"],             "пр-т Ленина, д. 5",    "2024-12-11", "+79990000002"),
        (["BLACK", "GREY"],    "ул. Пушкина, д. 10",   "2024-12-12", "+79990000003"),
        ([],                   "ул. Гагарина, д. 3",   "2024-12-13", "+79990000004"),
    ],
    ids=["black", "grey", "both_colors", "no_color"]
)

class TestGetOrdersList:
    @allure.title("Проверяем, что в тело ответа возвращается список заказов")
    def test_response_returns_orders_list(self, color, address, delivery_date, phone):
        payload = ORDER_PAYLOAD.copy()

        with allure.step("Создаём несколько заказов"):
            requests.post(f"{URL}{ORDERS_CREATE_ENDPOINT}", json=payload)

        with allure.step("Получаем список заказов"):
            response = requests.get(f"{URL}{ORDERS_CREATE_ENDPOINT}")
            body = response.json()

        assert "orders" in body, (
            f"В теле ответа отсутствует ключ 'orders'. Получен: {body}"
        )
        assert isinstance(body["orders"], list), (
            f"'orders' должен быть списком. Получено: {type(body['orders'])}"
        )