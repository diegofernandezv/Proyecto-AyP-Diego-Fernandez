
import uuid
from Cancion import Cancion
from User import User

class Album:

    def __init__(self, id: str, name: str, description: str, cover: str, published:str, 
                 genre: str, artist:str, tracklist: list[Cancion] , likes_Album = [] ):
        if id == None:
            id = str(uuid.uuid4())
        self.id = id
        self.name = name
        self.description = description
        self.cover = cover
        self.published = published
        self.genre = genre
        self.artist = artist
        self.tracklist = tracklist

        self.likes_Album = set(likes_Album)

    def recibir_Like(self, usuario:User):
        if usuario.id in self.likes:
            self.likes_Album.remove(usuario.id)
            usuario.likes_Album.remove(self.id)

            print(f"Like removido por el usuario {usuario.name} -> {len(self.likes_Album)}")

        else:
            self.likes_Album.add(id)
            usuario.likes_Album.add(self.id)

            print(f"Like recibido por el usuario {usuario.name} -> {len(self.likes_Album)}")

        
    def escuchar(self, idUsuario: str):
        """
    Registra la reproducción de la lista de reproducción, álbum o canción por el usuario especificado.

    Args:
        idUsuario (str): El ID del usuario que está reproduciendo la lista de reproducción, álbum o canción.
    """
        for track in self.tracklist:
            track.escuchar(idUsuario)
    
    def escoger_Cancion(self):
        """
    Permite al usuario seleccionar una canción de un álbum.

    Returns:
        Cancion: La canción seleccionada por el usuario.
    """
        print("Las canciones que están en el álbum son estas: ")
        for index, cancion in enumerate(self.tracklist):
            print(f"{index + 1} {cancion.name}") 
        
        while True:
            try:
                cancionIndex = int(input ("Dime el número de su canción:")) -1
                if cancionIndex < 0:
                    print("Por favor solo números positivos")
                    continue
                return self.tracklist[cancionIndex]
            except:
                print("Por favor ingrese un número")