# Задание 2: API

## Проект по автоматизации тестирования API сайта Stellar Burgers

### Структура проекта

- `API_desc` - директория, содержащая документацию API

- `aps/` - папка вспомогательных функций:
  - `aps/data_order.py`     - данные для работы с заказами
  - `aps/data_response.py` - используемые статус коды
  - `aps/data_user.py`        - данные для работы с пользователями
  - `aps/endpoints.py`  - тестируемые ендпойнты

- `tests/` - папка с файлами тестов:
  - `tests/test_create_user.py`     - проверки создания пользователя
  - `tests/test_login_user.py`      - проверки аутентификации пользователя
  - `tests/test_update_user.py`     - проверки обновления данных пользователя
  - `tests/test_create_order.py`    - проверки создания заказа
  - `tests/test_get_user_orders.py` - проверки получения заказов пользователя


- `conftest.py` - фикстуры


- `README.md` - файл с описанием проекта
- `requirements.txt` - файл с внешними зависимостями
- `.gitignore` - перечень игнорируемых объектов


- `allure_results/` - папка с отчетами Allure


### Для запуска тестов должны быть установлены пакеты:
- `Pytest`
- `Requests`
- `Allure-pytest`

**Запуск всех тестов выполняется командой:**

>  `$ pytest -v ./tests`

**Запуск тестов с генерацией отчета Allure выполняется командой:**

>  `$ pytest tests/ --alluredir=allure-results`

**Генерация отчета выполняется командой:**

>  `$ allure serve allure-results`

**Установка зависимостей из файла requirements.txt выполняется командой:**

>  `$ pip install -r requirements.txt`
