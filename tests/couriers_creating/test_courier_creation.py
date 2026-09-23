
class TestCourierCreate:
    def test_can_create_courier(self, courier_data):

        assert len(courier_data) == 3, (
            f"Не удалось зарегистрировать курьера. Ожидалось 3 поля, получили {len(courier_data)}"
        )
