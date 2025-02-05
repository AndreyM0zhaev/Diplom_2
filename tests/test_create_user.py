import requests

from aps.endpoints import Urls, Endpoints
from aps.data_user import User


class TestCreateUser:

    def test_new_user_registration(self):
        response = requests.post(f'{Urls.BASE_URL}{Endpoints.CREATE_USER}', data=User.registration_new_user())
        assert response.status_code == 200 and response.json()["success"] is True