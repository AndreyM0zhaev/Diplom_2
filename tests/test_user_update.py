import pytest
import requests

from aps.endpoints import Urls, Endpoints
from aps.data_user import User
from aps.data_response import StatusCode, ResponseText



class TestUpdateDataUser:


    @pytest.mark.parametrize('user_data', [
        User.registration_new_user()["name"],
        User.registration_new_user()["password"],
        User.registration_new_user()["email"]
    ])
    def test_update_data_user_with_auth(self, create_user, user_data):
        token = create_user[1].json()["accessToken"]
        assert token, "Не удалось получить токен авторизации"
        headers = {'Authorization': token}
        response = requests.patch(
            url=Urls.BASE_URL + Endpoints.UPDATE_USER,
            headers=headers,
            data=user_data
        )
        assert response.status_code == StatusCode.OK, f"Неверный статус код: {response.status_code}"
        assert response.json().get("success") == True, "Ответ сервера не содержит success=True"


    @pytest.mark.parametrize('user_data', [
        User.registration_new_user()["name"],
        User.registration_new_user()["password"],
        User.registration_new_user()["email"]
    ])
    def test_update_data_user_without_auth(self, user_data):
        response = requests.patch(
            url=Urls.BASE_URL + Endpoints.UPDATE_USER,
            data=user_data
        )
        assert response.status_code == StatusCode.UNAUTHORIZED, (
            f"Неверный статус код: {response.status_code}"
        )
        assert response.json().get("message") == ResponseText.UNAUTHORIZED, (
            "Ответ сервера не содержит ожидаемое сообщение об ошибке авторизации"
        )
