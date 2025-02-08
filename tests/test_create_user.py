import requests
import pytest
import allure

from aps.endpoints import Urls, Endpoints
from aps.data_user import User
from aps.data_response import StatusCode, ResponseText


@allure.epic("Stellar Burgers")
@allure.feature("Регистрация пользователя")
class TestCreateUser:

    @allure.story("Успешная регистрация нового пользователя")
    @allure.title("Регистрация нового пользователя")
    @allure.description("Тест проверяет успешную регистрацию нового пользователя.")
    @allure.severity(allure.severity_level.CRITICAL)

    def test_new_user_registration(self):
        with allure.step("Генерация данных нового пользователя"):
            user_data = User.registration_new_user()

        with allure.step("Отправка запроса на регистрацию"):
            response = requests.post(f'{Urls.BASE_URL}{Endpoints.CREATE_USER}', json=user_data)

        with allure.step("Проверка ответа"):
            assert response.status_code == StatusCode.OK, f"Ожидался статус 200, получен {response.status_code}"
            assert response.json()["success"] is True, "Регистрация не удалась"

    @allure.story("Регистрация уже существующего пользователя")
    @allure.title("Попытка регистрации существующего пользователя")
    @allure.description("Тест проверяет, что нельзя зарегистрировать пользователя с уже существующим email.")
    @allure.severity(allure.severity_level.NORMAL)

    def test_double_user_registration(self):
        with allure.step("Подготовка данных уже существующего пользователя"):
            user_data = User.double_user

        with allure.step("Отправка запроса на регистрацию"):
            response = requests.post(f'{Urls.BASE_URL}{Endpoints.CREATE_USER}', json=user_data)

        with allure.step("Проверка ответа"):
            assert response.status_code == StatusCode.FORBIDDEN, f"Ожидался статус 403, получен {response.status_code}"
            assert ResponseText.CREATE_DOUBLE_USER in response.text, "Сообщение об ошибке не содержит 'User already exists'"

    @allure.story("Регистрация с некорректными данными")
    @allure.title("Попытка регистрации с некорректными данными")
    @allure.description("Тест проверяет, что нельзя зарегистрировать пользователя без email, пароля или имени.")
    @allure.severity(allure.severity_level.NORMAL)

    @pytest.mark.parametrize("data_user", [User.reg_without_email, User.reg_without_password, User.reg_without_name])
    def test_new_user_invalid_registration(self, data_user):
        with allure.step("Подготовка данных с некорректными полями"):
            user_data = data_user

        with allure.step("Отправка запроса на регистрацию"):
            response = requests.post(f'{Urls.BASE_URL}{Endpoints.CREATE_USER}', json=user_data)

        with allure.step("Проверка ответа"):
            assert response.status_code == StatusCode.FORBIDDEN, f"Ожидался статус 403, получен {response.status_code}"
            assert 'Email, password and name are required fields' in response.text, "Сообщение об ошибке не содержит 'Email, password and name are required fields'"
