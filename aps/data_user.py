from faker import Faker

faker = Faker()

class User:

    @staticmethod
    def registration_new_user():
        name = faker.name()
        email = faker.email()
        password = faker.password()
        user_data = {"login": email, "password": password, "name": name}
        return user_data


    current_user = {
        "login": "Andre",
        "password": "1234"
    }
    not_reg_user = {
        "login": "зло не дремлет",
        "password": "666"
    }
    auth_without_login = {
        "login": "",
        "password": "1234"
    }
    auth_without_password = {
        "login": "Andre",
        "password": ""
    }