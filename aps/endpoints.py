class Urls:
    BASE_URL = 'https://stellarburgers.nomoreparties.site'

class Endpoints:
    headers = {"Content-Type": "application/json"}
    CREATE_USER = '/api/auth/register'
    LOGIN = '/api/auth/login'
    UPDATE_USER = '/api/auth/user'
    DELETE_USER = '/api/auth/user'
    CREATE_ORDER = '/api/orders'
    GET_ORDERS = '/api/orders'