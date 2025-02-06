import requests
import allure

from aps.endpoints import Urls, Endpoints
from aps.data_user import User


@allure.epic("Stellar Burgers")
@allure.feature("Авторизация пользователя")
class TestLogin:

    @allure.story("Успешная авторизация пользователя")
    @allure.title("Авторизация зарегистрированного пользователя")
    @allure.description("Тест проверяет успешную авторизацию зарегистрированного пользователя.")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_log_in_user(self):

        with allure.step("Подготовка данных зарегистрированного пользователя"):
            user_data = User.current_user

        with allure.step("Отправка запроса на авторизацию"):
            response = requests.post(f'{Urls.BASE_URL}{Endpoints.LOGIN}', json=user_data)

        with allure.step("Проверка ответа"):
            assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"
            assert response.json().get('success') is True, "Авторизация не удалась"

    @allure.story("Неуспешная авторизация пользователя")
    @allure.title("Авторизация незарегистрированного пользователя")
    @allure.description("Тест проверяет, что незарегистрированный пользователь не может авторизоваться.")
    @allure.severity(allure.severity_level.NORMAL)
    def test_invalid_log_in_user(self):
        with allure.step("Подготовка данных незарегистрированного пользователя"):
            user_data = User.not_reg_user

        with allure.step("Отправка запроса на авторизацию"):
            response = requests.post(f'{Urls.BASE_URL}{Endpoints.LOGIN}', json=user_data)

        with allure.step("Проверка ответа"):
            assert response.status_code == 401, f"Ожидался статус 401, получен {response.status_code}"
            assert response.json().get('success') is False, "Авторизация прошла успешно, хотя не должна была"
