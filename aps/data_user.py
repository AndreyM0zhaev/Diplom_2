from faker import Faker

faker = Faker()

class User:

    @staticmethod
    def registration_new_user():
        user_name = faker.name()
        user_email = faker.email()
        user_password = faker.password()
        user_data = {"name": user_name, "email": user_email, "password": user_password}
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

    auth_without_email = {
        "email": "",
        "password": "asdfgh123456!",
        "name": "Andrey"
    }
    auth_without_password = {
        "email": "Mozhaev.Andrey.v@yandex.ru",
        "password": "",
        "name": "Andrey"
    }

    auth_without_name = {
        "email": "Mozhaev.Andrey.v@yandex.ru",
        "password": "asdfgh123456!",
        "name": ""
    }

    auth_with_update = {
        "email": "Mozhaev.Andrey.v@yandex.ru",
        "password": "asdfgh123456!",
        "name": "Rndex"
    }
