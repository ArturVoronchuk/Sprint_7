import allure
import pytest
import requests

from data.data import ORDER_PAYLOAD
from data.urls import URL, ORDERS_CREATE_ENDPOINT, ORDERS_TRACK_ENDPOINT


class TestOrderColorHandling:

    @allure.title("Можно указать один цвет: {payload_color}")
    @pytest.mark.parametrize(
        "payload_color",
        [["BLACK"], ["GREY"]],
        ids=["BLACK", "GREY"]
    )

    @allure.title("Можно указать один из цветов: BLACK или GREY")
    def test_can_set_single_color(self, payload_color):
        payload = ORDER_PAYLOAD.copy()
        payload["color"] = payload_color

        with allure.step(f"Создаём заказ с color={payload_color}"):
            create_order = requests.post(f"{URL}{ORDERS_CREATE_ENDPOINT}", json=payload)
            track = create_order.json()["track"]

        with allure.step(f"Получаем заказ по track={track}"):
            get_order = requests.get(f"{URL}{ORDERS_TRACK_ENDPOINT}", params={"t": track})
            order = get_order.json()["order"]

        assert order.get("color") == payload_color, (
            f"Ожидался color={payload_color}, но получен: {order.get('color')}"
        )

    @allure.title("Цвет можно не указывать: поле color равно None")
    def test_can_omit_color_field(self):
        payload = ORDER_PAYLOAD.copy()
        payload.pop("color", None)

        with allure.step("Создаём заказ без поля color"):
            create_order = requests.post(f"{URL}{ORDERS_CREATE_ENDPOINT}", json=payload)
            track = create_order.json()["track"]

        with allure.step(f"Получаем заказ по track={track}"):
            get_order = requests.get(f"{URL}{ORDERS_TRACK_ENDPOINT}", params={"t": track})
            order = get_order.json()["order"]

        assert order.get("color") is None, (
            f"Ожидалось, что color=None, но получено: {order.get('color')}"
        )

    @allure.title("Можно указать сразу оба цвета: BLACK и GREY")
    def test_can_set_both_colors_simultaneously(self):
        payload = ORDER_PAYLOAD.copy()
        payload["color"] = ["BLACK", "GREY"]

        with allure.step("Создаём заказ с обоими цветами"):
            create_order = requests.post(f"{URL}{ORDERS_CREATE_ENDPOINT}", json=payload)
            track = create_order.json()["track"]

        with allure.step(f"Получаем заказ по track={track}"):
            get_order = requests.get(f"{URL}{ORDERS_TRACK_ENDPOINT}", params={"t": track})
            order = get_order.json()["order"]

        received_colors = order.get("color")
        assert isinstance(received_colors, list), "Поле color должно быть списком"
        assert set(received_colors) == {"BLACK", "GREY"}, (
            f"Ожидались оба цвета BLACK и GREY, но получено: {received_colors}"
        )
