import requests
import allure

from aps.endpoints import Urls, Endpoints
from aps.data_order import Ingredient
from aps.data_response import StatusCode, ResponseText

@allure.epic("Тесты для получения заказов пользователя")
@allure.feature("Получение заказов пользователя")
class TestGetUserOrder:

    @allure.story("Получение заказов авторизованным пользователем")
    @allure.title("Получение заказов с валидными данными (авторизованный пользователь)")
    @allure.description("""
    Тест проверяет получение заказов авторизованным пользователем.
    Ожидаемый результат:
    - Статус код 200 (OK).
    - Ответ сервера содержит ключи 'orders', 'total', 'totalToday'.
    - Тело ответа соответствует ожидаемому формату.
    """)
    def test_get_order_auth_user(self, create_user):
        with allure.step("Получение токена авторизации"):
            token = create_user[1].json().get("accessToken")
            assert token, "Токен авторизации не получен"
            headers = {'Authorization': token}

        with allure.step("Отправка запроса на получение заказов"):
            response = requests.get(
                f"{Urls.BASE_URL}{Endpoints.GET_ORDERS}",
                headers=headers,
                data=Ingredient.valid_ingredients
            )

        with allure.step("Проверка статус кода"):
            assert response.status_code == StatusCode.OK, f"Ожидался статус код 200, но получен {response.status_code}"

        with allure.step("Проверка наличия ключей в ответе"):
            response_data = response.json()
            orders = response_data.get('orders')
            total = response_data.get('total')
            total_today = response_data.get('totalToday')
            assert orders is not None, "Ключ 'orders' отсутствует в ответе"
            assert total is not None, "Ключ 'total' отсутствует в ответе"
            assert total_today is not None, "Ключ 'totalToday' отсутствует в ответе"

        with allure.step("Проверка тела ответа"):
            expected_response = {
                ResponseText.SUCCESS: True,
                ResponseText.ORDERS: orders,
                ResponseText.TOTAL: total,
                ResponseText.TOTAL_TODAY: total_today
            }
            assert response.json() == expected_response, "Тело ответа не соответствует ожидаемому"

    @allure.story("Получение заказов неавторизованным пользователем")
    @allure.title("Получение заказов (неавторизованный пользователь)")
    @allure.description("""
    Тест проверяет попытку получения заказов неавторизованным пользователем.
    Ожидаемый результат:
    - Статус код 401 (Unauthorized).
    - Ответ сервера содержит сообщение об ошибке.
    """)
    def test_get_order_not_auth_user(self):
        with allure.step("Отправка запроса на получение заказов без авторизации"):
            response = requests.get(f'{Urls.BASE_URL}{Endpoints.GET_ORDERS}')

        with allure.step("Проверка статус кода и ответа сервера"):
            assert response.status_code == StatusCode.UNAUTHORIZED, f"Ожидался статус код 401, но получен {response.status_code}"
            assert ResponseText.UNAUTHORIZED in response.text, "Текст ошибки не соответствует ожидаемому"