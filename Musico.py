from Album import Album
from Cancion import Cancion
from User import User

class Musico(User):
    def __init__(self, id, name, email, username, likes = []):
        super().__init__(id, name, email, username, "musician")
        self.albumes = []
        self.canciones = []
        self.playlists = []

        self.likes = set(likes)

    def mostrar_atributos(self):
        """
    Muestra los atributos del usuario, así como los álbumes, canciones y playlists asociadas.
    """
        super().mostrar_atributos()
        print(f"Albumes {self.albumes} \n Canciones {self.canciones} \n Playlists {self.playlists}")

    def seleccionar_Cancion(self, albumes: list[Album]):
        """
    Permite al usuario seleccionar una canción de entre los álbumes asociados.

    Args:
        albumes (list[Album]): Lista de álbumes asociados al usuario.

    Returns:
        Cancion: La canción seleccionada por el usuario.
    """
        mis_Canciones: list[Cancion] = []
        for album in albumes:
            if album.artist == self.id:
                for cancion in album.tracklist:
                    mis_Canciones.append(cancion)

        for index, cancion in enumerate(mis_Canciones):
            print(f"{index + 1} {cancion.name}")

        while True:
            try:
                opcion = int(input("Ingrese el número de la canción que desea: ")) -1
                if opcion < 0:
                    print("Por favor no ingrese números negativos")
                    continue

                return mis_Canciones[opcion]
            except:
                print("Ingrese una opción válida")

    def recibir_Like(self, usuario:User):
        """
    Maneja la recepción de likes por parte de un usuario.

    Args:
        usuario (User): El usuario que está dando like.
    """
        if usuario.id in self.likes:
            self.likes.remove(usuario.id)
            usuario.likes_Musico.remove(self.id)

            print(f"Like removido del usuario {usuario.name} -> {len(self.likes)}")

        else:
            self.likes.add(usuario.id)
            usuario.likes_Musico.add(self.id)

            print(f"Like recibido del usuario {usuario.name} -> {len(self.likes)}")
