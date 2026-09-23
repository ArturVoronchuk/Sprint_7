import pytest
import requests

from data.urls import URL

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

class TestChoosingBothScooterColors:
    def test_choosing_both_scooter_colors(self, color, address, delivery_date, phone):
        response = requests.get(f"{URL}/api/v1/orders")
        body = response.json()

        assert "orders" in body, (
            f"В теле ответа отсутствует ключ 'orders'. Получен: {body}"
        )

        assert isinstance(body["orders"], list), (
            f"'orders' должен быть списком. Получено: {type(body['orders'])}"
        )