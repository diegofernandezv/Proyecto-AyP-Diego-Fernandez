import uuid


class User:
    def __init__(self, id, name, email, username, type,
                likes_Musico = [], likes_Album = [], likes_Canciones = [] ,likes_Playlist = []):
        if id == None: 
            self.id = str(uuid.uuid4()) #UUID es una libreria , para crear randoms ID.
        else:
            self.id = id 
        self.name = name 
        self.email = email
        self.username = username
        self.type = type

        self.likes_Musico = set(likes_Musico)
        self.likes_Album = set(likes_Album)
        self.likes_Canciones = set(likes_Canciones)
        self.likes_Playlist = set(likes_Playlist)

    def mostrar_atributos(self):
        print(f"{self.id}\nNombre: {self.name}\nCorreo: {self.email}\nUsername: {self.username}\nTipo: {self.type}\n ")

    """
    Muestra los atributos del usuario en el sistema.
    """