import requests
import pytest
import allure

from aps.endpoints import Urls, Endpoints
from aps.data_user import User

class TestLogin:

    def test_log_in_user(self):
        response = requests.post(f'{Urls.BASE_URL}{Endpoints.LOGIN}', data=User.current_user)
        assert response.status_code == 200 and response.json().get('success') == True

    def test_invalid_log_in_user(self):
        response = requests.post(f'{Urls.BASE_URL}{Endpoints.LOGIN}', data=User.not_reg_user)
        assert response.status_code == 401 and response.json().get('success') == False
