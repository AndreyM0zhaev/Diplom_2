import requests

from aps.endpoints import Urls, Endpoints
from aps.data_response import StatusCode, ResponseText
from aps.data_order import Ingredient


class TestGetUserOrder:

    def test_get_order_auth_user(self, create_user):
        token = create_user[1].json().get("accessToken")
        assert token, "Токен авторизации не получен"
        headers = {'Authorization': token}
        response = requests.get(
            f"{Urls.BASE_URL}{Endpoints.GET_ORDERS}",
            headers=headers,
            data=Ingredient.valid_ingredients
        )
        assert response.status_code == 200, f"Ожидался статус код 200, но получен {response.status_code}"
        response_data = response.json()
        orders = response_data.get('orders')
        total = response_data.get('total')
        total_today = response_data.get('totalToday')
        assert orders is not None, "Ключ 'orders' отсутствует в ответе"
        assert total is not None, "Ключ 'total' отсутствует в ответе"
        assert total_today is not None, "Ключ 'totalToday' отсутствует в ответе"
        expected_response = {
            "success": True,
            "orders": orders,
            "total": total,
            "totalToday": total_today
        }
        assert response.json() == expected_response, "Тело ответа не соответствует ожидаемому"


    def test_get_order_not_auth_user(self):
        response = requests.get(f'{Urls.BASE_URL}{Endpoints.GET_ORDERS}')
        assert response.status_code == 401, f"Ожидался статус код 401, но получен {response.status_code}"
        assert response.text == '{"success":false,"message":"You should be authorised"}'
