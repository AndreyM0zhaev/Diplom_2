import pytest
import requests
import allure

from aps.endpoints import Urls, Endpoints
from aps.data_user import User
from aps.data_response import StatusCode, ResponseText


@allure.epic("Тесты для обновления данных пользователя")
@allure.feature("Обновление данных пользователя")
class TestUpdateDataUser:

    @allure.story("Обновление данных пользователя с авторизацией")
    @allure.title("Обновление данных пользователя с авторизацией")
    @allure.description("""
    Тест проверяет возможность обновления данных пользователя (имя, пароль, email) с использованием токена авторизации.
    Ожидаемый результат:
    - Статус код 200 (OK).
    - Ответ сервера содержит success=True.
    """)
    @pytest.mark.parametrize('user_data', [
        User.registration_new_user()["name"],
        User.registration_new_user()["password"],
        User.registration_new_user()["email"]
    ])
    def test_update_data_user_with_auth(self, create_user, user_data):
        with allure.step("Получение токена авторизации"):
            token = create_user[1].json()["accessToken"]
            assert token, "Не удалось получить токен авторизации"
            headers = {'Authorization': token}

        with allure.step("Отправка запроса на обновление данных пользователя"):
            response = requests.patch(
                url=Urls.BASE_URL + Endpoints.UPDATE_USER,
                headers=headers,
                data=user_data
            )

        with allure.step("Проверка статус кода и ответа сервера"):
            assert response.status_code == StatusCode.OK, f"Неверный статус код: {response.status_code}"
            assert response.json().get(ResponseText.SUCCESS) == True, "Ответ сервера не содержит success=True"

    @allure.story("Обновление данных пользователя без авторизации")
    @allure.title("Обновление данных пользователя без авторизации")
    @allure.description("""
    Тест проверяет попытку обновления данных пользователя (имя, пароль, email) без авторизации.
    Ожидаемый результат:
    - Статус код 401 (Unauthorized).
    - Ответ сервера содержит сообщение об ошибке авторизации.
    """)
    @pytest.mark.parametrize('user_data', [
        User.registration_new_user()["name"],
        User.registration_new_user()["password"],
        User.registration_new_user()["email"]
    ])
    def test_update_data_user_without_auth(self, user_data):
        with allure.step("Отправка запроса на обновление данных пользователя без авторизации"):
            response = requests.patch(
                url=Urls.BASE_URL + Endpoints.UPDATE_USER,
                data=user_data
            )

        with allure.step("Проверка статус кода и ответа сервера"):
            assert response.status_code == StatusCode.UNAUTHORIZED, f"Неверный статус код: {response.status_code}"
            assert response.json().get(ResponseText.MESSAGE) == ResponseText.UNAUTHORIZED, (
                "Ответ сервера не содержит ожидаемое сообщение об ошибке авторизации"
            )