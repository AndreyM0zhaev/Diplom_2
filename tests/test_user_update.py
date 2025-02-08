import pytest
import requests


from aps.endpoints import Urls, Endpoints
from aps.data_user import User
from aps.data_response import StatusCode, ResponseText

class TestUpdateDataUser:

    @pytest.mark.parametrize('user_data', [
        # Используем корректные данные для изменения: имя, пароль и email
        User.registration_new_user()["name"],
        User.registration_new_user()["password"],
        User.registration_new_user()["email"]
    ])
    def test_update_data_user_with_auth(self, create_user, user_data):
        # Получение токена авторизации из ответа на создание пользователя
        token = create_user[1].json()["accessToken"]
        assert token, "Не удалось получить токен авторизации"

        # Установка заголовков авторизации
        headers = {'Authorization': token}

        # Отправка запроса на изменение данных пользователя
        response = requests.patch(
            url=Urls.BASE_URL + Endpoints.UPDATE_USER,
            headers=headers,
            data=user_data
        )

        # Проверка успешного ответа сервера
        assert response.status_code == StatusCode.OK, f"Неверный статус код: {response.status_code}"
        assert response.json().get("success") == True, "Ответ сервера не содержит success=True"

    @pytest.mark.parametrize('user_data', [
        # Используем корректные данные для изменения: имя, пароль и email
        User.registration_new_user()["name"],
        User.registration_new_user()["password"],
        User.registration_new_user()["email"]
    ])
    def test_update_data_user_without_auth(self, user_data):
        # Отправка запроса на изменение данных без передачи заголовка авторизации
        response = requests.patch(
            url=Urls.BASE_URL + Endpoints.UPDATE_USER,
            data=user_data
        )

        # Проверка, что сервер возвращает ошибку авторизации
        assert response.status_code == StatusCode.UNAUTHORIZED, (
            f"Неверный статус код: {response.status_code}"
        )
        assert response.json().get("message") == ResponseText.UNAUTHORIZED, (
            "Ответ сервера не содержит ожидаемое сообщение об ошибке авторизации"
        )
