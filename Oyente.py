from User import User

class Oyente(User):
    def __init__(self, id, name, email, username):
        super().__init__(id, name, email, username, "listener")




