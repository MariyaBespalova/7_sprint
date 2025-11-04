from helpers import Helpers
import allure

class TestOrderList:
    @allure.title('Проверка получения списка заказа')
    def test_order_list(self):
        with allure.step("Получаем список заказов"):
            response = Helpers.get_order_list()

        with allure.step("Проверяем статус-код и наличие хотя бы одного заказа"):
            assert response.status_code == 200
            orders = response.json().get('orders', [])
            assert len(orders) > 0, "Список заказов пуст!"
            for order in orders:
                assert 'id' in order, f"Поле 'id' отсутствует в заказе: {order}"