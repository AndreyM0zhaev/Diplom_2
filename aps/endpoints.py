class Urls:
    BASE_URL = 'https://stellarburgers.nomoreparties.site/'

class Endpoints:
    headers = {"Content-Type": "application/json"}
    CREATE_USER = '/api/auth/register'
    LOGIN = '/api/auth/login'
    CHANGE_USER_DATA = '/api/auth/user'
    DELETE_USER = '/api/auth/user'