from faker import Faker

faker = Faker('ru_RU')

class User:

    @staticmethod
    def registration_new_user():
        user_name = faker.name()
        user_email = faker.email()
        user_password = faker.password()
        user_data = {"email": user_email, "password": user_password, "name": user_name}
        return user_data

    current_user = {
        "email": "Mozhaev.Andrey.v@yandex.ru",
        "password": "asdfgh123456!"
    }

    not_reg_user = {
        "email": "funky@punky.net",
        "password": "777"
    }

    double_user = {
        "email": "Mozhaev.Andrey.v@yandex.ru",
        "password": "asdfgh123456!",
        "name": "Andrey"
    }

    reg_without_email = {
        "email": "",
        "password": "asdfgh123456!",
        "name": "Andrey"
    }
    reg_without_password = {
        "email": "Mozhaev.Andrey.v@yandex.ru",
        "password": "",
        "name": "Andrey"
    }

    reg_without_name = {
        "email": "Mozhaev.Andrey.v@yandex.ru",
        "password": "asdfgh123456!",
        "name": ""
    }

    auth_with_update = {
        "email": "Mozhaev.Andrey.v@yandex.ru",
        "password": "asdfgh123456!",
        "name": "Rndex"
    }

