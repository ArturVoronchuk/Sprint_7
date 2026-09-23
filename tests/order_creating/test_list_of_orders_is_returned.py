import requests

from data.urls import URL


class TestOrderCreating:
    def test_order_creating_is_returned(self):
        response = requests.get(f"{URL}/api/v1/orders", timeout=10)

        assert response.status_code == 200, (
            f"Ожидался 200, но получен {response.status_code}. Ответ: {response.text}"
        )

        body = response.json()

        assert "orders" in body, (
            f"В ответе отсутствует ключ 'orders'. Получен: {body}"
        )

        assert isinstance(body["orders"], list), (
            f"Ожидался список заказов, но получен {type(body['orders'])}. "
            f"Значение: {body['orders']}"
        )