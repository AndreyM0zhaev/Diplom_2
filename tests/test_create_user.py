import requests
import pytest

from aps.endpoints import Urls, Endpoints
from aps.data_user import User


class TestCreateUser:

    def test_new_user_registration(self):
        response = requests.post(f'{Urls.BASE_URL}{Endpoints.CREATE_USER}', data=User.registration_new_user())
        assert response.status_code == 200 and response.json()["success"] is True


    def test_double_user_registration(self):
        response = requests.post(f'{Urls.BASE_URL}{Endpoints.CREATE_USER}', data=User.double_user)
        assert response.status_code == 403 and 'User already exists' in response.text


    @pytest.mark.parametrize("data_user", [User.auth_without_email, User.auth_without_password, User.auth_without_name])
    def test_new_user_invalid_registration(self, data_user):
        response = requests.post(f'{Urls.BASE_URL}{Endpoints.CREATE_USER}', data=data_user)
        assert response.status_code == 403 and 'Email, password and name are required fields' in response.text