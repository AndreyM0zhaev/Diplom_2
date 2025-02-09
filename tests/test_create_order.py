import requests

from aps.endpoints import Urls, Endpoints
from aps.data_response import StatusCode, ResponseText
from aps.data_order import Ingredient

class TestCreateOrder:


    def test_create_order_auth_user(self, create_user):
        token = create_user[1].json().get("accessToken")
        assert token, "Токен авторизации не получен"
        headers = {'Authorization': token}
        response = requests.post(
            f"{Urls.BASE_URL}{Endpoints.CREATE_ORDER}",
            headers=headers,
            data=Ingredient.valid_ingredients
        )
        assert response.status_code == 200, f"Ожидался статус код 200, но получен {response.status_code}"
        assert response.json().get("success") is True, "Запрос не был выполнен успешно"


    def test_create_order_not_auth_user(self):
        response = requests.post(
            f"{Urls.BASE_URL}{Endpoints.CREATE_ORDER}",
            data=Ingredient.valid_ingredients
        )
        name = response.json()['name']
        order_number = response.json()["order"]["number"]
        assert response.status_code == 200, f"Ожидался статус код 200, но получен {response.status_code}"
        assert response.text == f'{{"success":true,"name":"{name}","order":{{"number":{order_number}}}}}'


    def test_create_order_auth_user_without_ingredients(self, create_user):
        token = create_user[1].json().get("accessToken")
        assert token, "Токен авторизации не получен"
        headers = {'Authorization': token}
        response = requests.post(
            f"{Urls.BASE_URL}{Endpoints.CREATE_ORDER}",
            headers=headers,
            data=Ingredient.empty_ingredients
        )
        assert response.status_code == StatusCode.BAD_REQUEST, f"Неверный код ответа: {response.status_code}"
        assert response.text == '{"success":false,"message":"Ingredient ids must be provided"}'


    def test_create_order_not_auth_user_without_ingredients(self):
        response = requests.post(
            f"{Urls.BASE_URL}{Endpoints.CREATE_ORDER}",
            data=Ingredient.empty_ingredients
        )
        assert response.status_code == StatusCode.BAD_REQUEST, f"Неверный код ответа: {response.status_code}"
        assert response.text == '{"success":false,"message":"Ingredient ids must be provided"}'


    def test_create_order_auth_user_with_invalid_hash(self, create_user):
        token = create_user[1].json().get("accessToken")
        assert token, "Токен авторизации не получен"
        headers = {'Authorization': token}
        response = requests.post(
            f"{Urls.BASE_URL}{Endpoints.CREATE_ORDER}",
            headers=headers,
            data=Ingredient.invalid_ingredients
        )
        assert response.status_code == StatusCode.INTERNAL_SERVER_ERROR, f"Неверный код ответа: {response.status_code}"
        assert ResponseText.SERVER_ERROR in response.text, "Текст ошибки сервера не соответствует ожидаемому"