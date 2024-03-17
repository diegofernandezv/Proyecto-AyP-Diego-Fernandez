from User import User


class Playlist:
    def __init__(self, id:str, name: str, description: str, tracks: list, creator: str , likes = []) -> None:
        self.id = id
        self.name = name
        self.description = description
        self.tracks = tracks
        self.creator = creator
        self.likes = set(likes)


    def recibir_Like(self, usuario:User):
        """
    Maneja la recepción de likes por parte de un usuario en la playlist.

    Args:
        usuario (User): El usuario que está dando like.

    """
        if usuario.id in self.likes:
            self.likes.remove(usuario.id)
            usuario.likes_Playlist.remove(self.id)

            print(f"Like removido del usuario {usuario.name} -> {len(self.likes)}")

        else:
            self.likes.add(usuario.id)
            usuario.likes_Playlist.add(self.id)

            print(f"Like recibido del usuario {usuario.name} -> {len(self.likes)}")
