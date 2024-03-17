
import requests
from Cancion import Cancion
from Playlists import Playlist
from Album import Album
from Musico import Musico
from Oyente import Oyente
from modulos.Gestion_Perfil import Gestion_Perfil
from modulos.Gestion_de_interacciones import Gestion_De_Interacciones
from modulos.Gestion_de_musical import Gestion_De_Musical
from modulos.Indicadores_de_gestion import Indicadores_de_gestion



def get_api_Users():
    """
    Obtiene los usuarios desde una API y los organiza en listas separadas de músicos y oyentes.

    Returns:
        tuple: Una tupla que contiene dos listas: la primera lista contiene objetos de tipo Musico,
               la segunda lista contiene objetos de tipo Oyente.
    """
    response = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/users.json")
    usuariosJSON = response.json()
    
    musicos: list[Musico] = []
    oyentes: list[Oyente] = []

    for usuarioJSON in usuariosJSON:
        id = usuarioJSON["id"]
        name = usuarioJSON["name"].strip().title()
        email = usuarioJSON["email"]
        username = usuarioJSON["username"]
        type = usuarioJSON ["type"]

        if type == "musician":
            musico = Musico(id, name, email, username)
            musicos.append(musico)
        elif type == "listener":
            oyente = Oyente(id, name, email ,username)
            oyentes.append(oyente)
    
    return musicos, oyentes

def get_api_Albums():
    """
    Obtiene los álbumes desde una API y organiza la información en una lista de objetos de tipo Album.

    Returns:
        list: Una lista que contiene objetos de tipo Album, cada uno representando un álbum con su información completa.
    """
    response = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/albums.json")
    albumsJson = response.json()


    albums = []

    for albumJson in albumsJson:
        id = albumJson["id"]
        name = albumJson ["name"].strip().title()
        description = albumJson ["description"]
        cover = albumJson ["cover"]
        published = albumJson ["published"]
        genre = albumJson ["genre"]
        artist = albumJson ["artist"]
        tracklist = albumJson["tracklist"]

        tracks = []
    
        for track in tracklist:
            track_id = track["id"]
            track_name = track["name"].strip().title()
            track_duration = track["duration"]
            track_link = track["link"]
            track = Cancion(track_id, track_name, track_duration, track_link)
            tracks.append(track)

        album = Album(id, name, description, cover, published, genre, artist, tracks)
        albums.append(album)
    
    return albums


def get_Api_Playlist():
    """
    Obtiene las listas de reproducción desde una API y organiza la información en una lista de objetos de tipo Playlist.

    Returns:
        list: Una lista que contiene objetos de tipo Playlist, cada uno representando una lista de reproducción con su información completa.
    """
    response = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/playlists.json")
    playlistsJson= response.json()

    playlists = []

    for playlistJson in playlistsJson:
        id = playlistJson ["id"]
        name = playlistJson ["name"].strip().title()
        description = playlistJson ["description"]
        creator = playlistJson ["creator"]
        tracks = playlistJson ["tracks"]

        playlist = Playlist(id,name,description, tracks, creator)
        playlists.append(playlist)
    
    return playlists

url_playlists = requests.request("GET","https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/playlists.json")
url_users = requests.request("GET","https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/users.json")
url_albums = requests.request("GET","https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/albums.json")

directory = './archivos/'
def open_txt():
    """
    Abre archivos de texto y escribe datos obtenidos de diversas API en ellos.
    Esta función contiene subfunciones para abrir y escribir en archivos 
    de texto para usuarios, álbumes, canciones de álbumes, listas de reproducción y canciones de listas de reproducción.
    """
    
    def open_users():
        file_name = 'db_users'
        with open(directory + file_name, 'w')as file:
            for user in url_users.json():
                file.write(f'{user["id"]}, {user["name"]},{user["email"]},{user["username"]}, {user["type"]}, {0},{0}*\n')
    def open_albums():
        file_name = 'db_albums'
        with open(directory + file_name, 'w') as file:
            for album in url_albums.json():
                if "\n" in album["description"]:
                    description = album["description"].split("\n")[0] + album["description"].split("\n")[1]
                else:
                    description = album["description"]
                file.write(f'{album["id"]},{album["name"]},{description},')
                file. write(f'{album["cover"]},{album["published"]},{album["genre"]},{album["artist"]},{0},{0}*\n')
    def open_album_song():
        file_name = 'db_albums_songs'
        with open(directory + file_name, 'w') as file:
            for album in url_albums.json():
                for song in album["tracklist"]:
                    file.write(f'{album["id"]},{song["id"]},{song["name"]},{song["duration"]},{song["link"]},{0},{0}*\n')
    def open_playlist():
        file_name = 'db_playlist'
        with open(directory + file_name, 'w') as file:
            for playlist in url_playlists.json():
                if "\n" in playlist["description"]:
                    description = playlist["description"].split("\n")[0] + playlist["description"].split("\n")[1]
                else:
                    description = playlist["description"]
                file.write(f'{playlist["id"]},{playlist["name"]},{description},{playlist["creator"]},{0}*\n')
    def open_playlists_songs():
        file_name = 'db_playlist_songs'
        with open(directory + file_name, 'w') as file:
            for playlist in url_playlists.json():
                for song in playlist["tracks"]:
                    file.write(f'{playlist["id"]},{song}* \n')

    open_users()
    open_albums()
    open_album_song()
    open_playlist()
    open_playlists_songs()


class App: 
    def __init__(self):

        
        self.musicos, self.oyentes = get_api_Users()
        self.albums = get_api_Albums()
        self.playlists = get_Api_Playlist()

        self.gestion_Perfil = Gestion_Perfil(self.musicos, self.oyentes)
        self.gestion_De_Musical = Gestion_De_Musical(self.albums,  self.gestion_Perfil, self.playlists)
        self.gestion_De_Interacciones = Gestion_De_Interacciones(self.gestion_Perfil, self.gestion_De_Musical)
        self.estadisticas = Indicadores_de_gestion(self.musicos, self.oyentes, self.albums)
        


    def menu(self):
        """
    Muestra el menú principal del sistema y permite al usuario elegir una 
    opción para acceder a los diferentes módulos.

    """
        while True:
            try:
                print("****🎧BIENVENIDO A METROTIFY🎧.****")
                print("Escoja el modulo al que quiere acceder:")
                print("1. Gestión Perfil")
                print("2. Gestión de Musical")
                print("3. Gestión de Interacciones")
                print("4. Indicadores de Gestión")
                print("5. Crear txts")
                print("6. Salir")
                

                opcion = int(input("--->"))

                if opcion == 1:
                    self.gestion_Perfil.menu()
                elif opcion == 2:
                    self.gestion_De_Musical.menu()
                elif opcion ==3:
                    self.gestion_De_Interacciones.menu()
                elif opcion == 4:
                    self.estadisticas.menu()
                elif opcion == 5:
                    open_txt()
                if opcion == 6:
                    break
                else:
                    raise Exception

            except:
                print("Ha ingresado un error erroneo, vuelvalo a intentar")

    



def main():
    app = App()
    app.menu()

main()

