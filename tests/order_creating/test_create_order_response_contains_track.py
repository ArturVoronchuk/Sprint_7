import allure
import requests

from data.data import ORDER_PAYLOAD
from data.urls import URL, ORDERS_CREATE_ENDPOINT, ORDERS_TRACK_ENDPOINT

class TestCreateOrderResponseContainsTrack:
    @allure.title("Проверяем, что тело ответа на запрос получения списка заказов содержит track")
    def test_create_order_response_contains_track(self):
        payload = ORDER_PAYLOAD.copy()

        with allure.step("Создаём заказ"):
            create_order = requests.post(f"{URL}{ORDERS_CREATE_ENDPOINT}", json=payload)
            track = create_order.json()["track"]

        with allure.step("Получаем по его номеру (track)"):
            get_order = requests.get(f"{URL}{ORDERS_TRACK_ENDPOINT}", params={"t": track})
            body = get_order.json()

        assert "track" in body["order"], (
            f"В теле ответа внутри 'order' отсутствует 'track'. "
            f"Получен ответ: {body}"
        )