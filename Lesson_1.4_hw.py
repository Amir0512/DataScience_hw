class User:
    count = 0

    def __init__(self, name, login, password):
        User.count += 1
        self.name = name
        self.__password = password
        self._login = login

    @property
    def password(self):
        return 'Password cannot be shown to the user'

    @password.setter
    def password(self, value):
        self.__password = value

    @property
    def login(self):
        return self._login

    def show_info(self):
        print("Name: {}".format(self.name))
        print("Login: {}".format(self._login))


class SuperUser(User):
    count = 0

    def __init__(self, name, login, password, role):
        super(SuperUser, self).__init__(name, login, password)
        self.role = role
        SuperUser.count += 1

    def show_info(self):
        print("Role: {}".format(self.role))
        print("Name: {}".format(self.name))
        print("Login: {}".format(self._login))


User1 = User(name="Amir", login="amir", password="123456")
User2 = User(name="Adilya", login="adilya", password="123456")
SuperUser1 = SuperUser(name='Dad', login='dad', password='123456', role='admin')
SuperUser2 = SuperUser(name='Mum', login='mum', password='123456', role='admin')
