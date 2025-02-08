import pytest
import requests

from aps.endpoints import Urls, Endpoints
from aps.data_user import User


@pytest.fixture
def create_user():
    payload = User.registration_new_user()
    response = requests.post(Urls.BASE_URL + Endpoints.CREATE_USER, data=payload)
    yield payload, response
    token = response.json()["accessToken"]
    requests.delete(Urls.BASE_URL + Endpoints.DELETE_USER, headers={"Authorization": token})