import requests
import allure

from aps.endpoints import Urls, Endpoints
from aps.data_response import StatusCode, ResponseText
from aps.data_order import Ingredient


@allure.epic("Тесты для создания заказа")
@allure.feature("Создание заказа")
class TestCreateOrder:

    @allure.story("Создание заказа авторизованным пользователем")
    @allure.title("Создание заказа с валидными ингредиентами (авторизованный пользователь)")
    @allure.description("""
    Тест проверяет создание заказа авторизованным пользователем с валидными ингредиентами.
    Ожидаемый результат:
    - Статус код 200 (OK).
    - Ответ сервера содержит success=True.
    """)
    def test_create_order_auth_user(self, create_user):
        with allure.step("Получение токена авторизации"):
            token = create_user[1].json().get("accessToken")
            assert token, "Токен авторизации не получен"
            headers = {'Authorization': token}

        with allure.step("Отправка запроса на создание заказа"):
            response = requests.post(
                f"{Urls.BASE_URL}{Endpoints.CREATE_ORDER}",
                headers=headers,
                data=Ingredient.valid_ingredients
            )

        with allure.step("Проверка статус кода и ответа сервера"):
            assert response.status_code == StatusCode.OK, f"Ожидался статус код 200, но получен {response.status_code}"
            assert response.json().get(ResponseText.SUCCESS) is True, "Запрос не был выполнен успешно"

    @allure.story("Создание заказа неавторизованным пользователем")
    @allure.title("Создание заказа с валидными ингредиентами (неавторизованный пользователь)")
    @allure.description("""
    Тест проверяет создание заказа неавторизованным пользователем с валидными ингредиентами.
    Ожидаемый результат:
    - Статус код 200 (OK).
    - Ответ сервера содержит success=True, имя и номер заказа.
    """)
    def test_create_order_not_auth_user(self):
        with allure.step("Отправка запроса на создание заказа без авторизации"):
            response = requests.post(
                f"{Urls.BASE_URL}{Endpoints.CREATE_ORDER}",
                data=Ingredient.valid_ingredients
            )

        with allure.step("Проверка статус кода и ответа сервера"):
            name = response.json()['name']
            order_number = response.json()["order"]["number"]
            assert response.status_code == StatusCode.OK, f"Ожидался статус код 200, но получен {response.status_code}"
            assert response.text == f'{{"success":true,"name":"{name}","order":{{"number":{order_number}}}}}'

    @allure.story("Создание заказа авторизованным пользователем без ингредиентов")
    @allure.title("Создание заказа без ингредиентов (авторизованный пользователь)")
    @allure.description("""
    Тест проверяет попытку создания заказа авторизованным пользователем без указания ингредиентов.
    Ожидаемый результат:
    - Статус код 400 (Bad Request).
    - Ответ сервера содержит сообщение об ошибке.
    """)
    def test_create_order_auth_user_without_ingredients(self, create_user):
        with allure.step("Получение токена авторизации"):
            token = create_user[1].json().get("accessToken")
            assert token, "Токен авторизации не получен"
            headers = {'Authorization': token}

        with allure.step("Отправка запроса на создание заказа без ингредиентов"):
            response = requests.post(
                f"{Urls.BASE_URL}{Endpoints.CREATE_ORDER}",
                headers=headers,
                data=Ingredient.empty_ingredients
            )

        with allure.step("Проверка статус кода и ответа сервера"):
            assert response.status_code == StatusCode.BAD_REQUEST, f"Неверный код ответа: {response.status_code}"
            assert response.text == '{"success":false,"message":"Ingredient ids must be provided"}'

    @allure.story("Создание заказа неавторизованным пользователем без ингредиентов")
    @allure.title("Создание заказа без ингредиентов (неавторизованный пользователь)")
    @allure.description("""
    Тест проверяет попытку создания заказа неавторизованным пользователем без указания ингредиентов.
    Ожидаемый результат:
    - Статус код 400 (Bad Request).
    - Ответ сервера содержит сообщение об ошибке.
    """)
    def test_create_order_not_auth_user_without_ingredients(self):
        with allure.step("Отправка запроса на создание заказа без ингредиентов и авторизации"):
            response = requests.post(
                f"{Urls.BASE_URL}{Endpoints.CREATE_ORDER}",
                data=Ingredient.empty_ingredients
            )

        with allure.step("Проверка статус кода и ответа сервера"):
            assert response.status_code == StatusCode.BAD_REQUEST, f"Неверный код ответа: {response.status_code}"
            assert response.text == '{"success":false,"message":"Ingredient ids must be provided"}'

    @allure.story("Создание заказа авторизованным пользователем с невалидным хэшем ингредиентов")
    @allure.title("Создание заказа с невалидным хэшем ингредиентов (авторизованный пользователь)")
    @allure.description("""
    Тест проверяет попытку создания заказа авторизованным пользователем с невалидным хэшем ингредиентов.
    Ожидаемый результат:
    - Статус код 500 (Internal Server Error).
    - Ответ сервера содержит сообщение об ошибке.
    """)
    def test_create_order_auth_user_with_invalid_hash(self, create_user):
        with allure.step("Получение токена авторизации"):
            token = create_user[1].json().get("accessToken")
            assert token, "Токен авторизации не получен"
            headers = {'Authorization': token}

        with allure.step("Отправка запроса на создание заказа с невалидным хэшем ингредиентов"):
            response = requests.post(
                f"{Urls.BASE_URL}{Endpoints.CREATE_ORDER}",
                headers=headers,
                data=Ingredient.invalid_ingredients
            )

        with allure.step("Проверка статус кода и ответа сервера"):
            assert response.status_code == StatusCode.INTERNAL_SERVER_ERROR, f"Неверный код ответа: {response.status_code}"
            assert ResponseText.SERVER_ERROR in response.text, "Текст ошибки сервера не соответствует ожидаемому"