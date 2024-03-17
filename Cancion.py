import uuid

from User import User


class Cancion:
    def __init__(self, id :str, name:str , duration:str , link: str, 
                 likes = [], reproducciones = []):
        if id == None:
            id = str(uuid.uuid4())
        self.id = id
        self.name = name
        self.duration = duration
        self.link = link 
        self.likes = set(likes)
        self.reproducciones = reproducciones.copy()

    def recibir_Like(self, usuario: User):
        """
    Maneja la recepción de un "like" por parte de una canción de un usuario específico.

    Args:
        usuario (User): El usuario que ha dado el "like" a la canción.
    """
        if usuario.id in self.likes:
            self.likes.remove(usuario.id)
            usuario.likes_Canciones.remove(self.id)

            print(f"Like removido por el usuario {usuario.name} -> {len(self.likes)}")

        else:
            self.likes.add(usuario.id)
            usuario.likes_Canciones.add(self.id)

            print(f"Like recibido por el usuario {usuario.name} -> {len(self.likes)}")


    def escuchar(self, idUser: str):
        """
    Registra la reproducción de la canción por un usuario específico.

    Args:
        idUser (str): El ID del usuario que está reproduciendo la canción.
    """
        self.reproducciones.append(idUser)
        print("Escuchando...")
        print(f"Cancion escuchada: {self.name} -> {len(self.reproducciones)}") 

