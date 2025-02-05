import pytest
import requests

from aps.endpoints import Urls, Endpoints
from aps.data_user import User


@pytest.fixture(scope="function")
def create_user():
    payload = User.registration_new_user()
    login_data = payload.copy()
    del login_data["name"]
    response = requests.post(f"{Urls.BASE_URL}{Endpoints.CREATE_USER}", data=payload)
    token = response.json()["accessToken"]
    yield response, payload, login_data, token
    requests.delete(f"{Urls.BASE_URL}{Endpoints.DELETE_USER}", headers={'Authorization': f'{token}'})