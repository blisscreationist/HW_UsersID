class User:
    def __init__(self, user_id, name, access_level='user'):
        self._user_id = user_id
        self._name = name
        self._access_level = access_level

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    def set_name(self, name):
        self._name = name
        print("Имя пользователя изменено.")

    def set_access_level(self, access_level):
        if access_level in ['user', 'admin']:
            self._access_level = access_level
        else:
            print("Неправильный уровень доступа.")

    def set_user_id(self, user_id):
        self._user_id = user_id

class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, 'admin')
        self.users = []

    def add_user(self, user):
        if user not in self.users:
            self.users.append(user)
            print(f"Пользователь {user.get_name()} добавлен в список.")
        else:
            print("Такой пользователь уже существует.")

    def remove_user(self, user):
        if user in self.users:
            self.users.remove(user)
            print(f"Пользователь {user.get_name()} удален из списка.")
        else:
            print("Такой пользователь не найден в списке.")

    def list_users(self):
        print("Список пользователей:")
        for user in self.users:
            print(f"- ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}")

    def change_user_name(self, user, new_name):
        if user in self.users:
            user.set_name(new_name)
            print(f"Имя пользователя {user.get_user_id()} изменено на {new_name}.")
        else:
            print("Такой пользователь не найден в списке.")


admin = Admin("1", "Админ Петр Сергеевич")
user1 = User("2", "Владимир")
user2 = User("3", "Сергей")

admin.add_user(user1)
admin.add_user(user2)
admin.list_users()

admin.change_user_name(user2, "Алексей")
admin.list_users()

admin.remove_user(user1)
admin.list_users()