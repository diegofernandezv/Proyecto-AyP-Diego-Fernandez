from datetime import datetime
from Album import Album
from Cancion import Cancion
from Playlists import Playlist
from modulos.Gestion_Perfil import Gestion_Perfil


class Gestion_De_Musical:
    def __init__(self, albumes: list[Album], gestion_Perfil: Gestion_Perfil, playlists: list[Playlist]) -> None:
        self.albumes = albumes
        self.gestion_Perfil = gestion_Perfil
        self.playlists = playlists

    def menu(self):
        """
    Muestra el menú de gestión musical y permite al usuario elegir una opción.

    """ 
        while True:
            try:
                print("****🎵✨BIENVENIDO A LA Gestión de Musical✨🎵****\n")

                print("1. Crear un album musical")
                print("2. Escuchar Música")
                print("3. Crear Playlist")
                print("4. Salir")
                opcion = int(input("-->"))

                if opcion == 1:
                    self.crear_Album()
                elif opcion == 2:
                    self.manera_Escuchar()
                elif opcion == 3:
                    self.crear_playlist()
                elif opcion == 4:
                    break

            except Exception as e:
                print(e)
                print("Ha ingresado un valor erroneo, vuelvalo a intentar")
    
    def crear_Album(self):
        """
    Permite al usuario crear un álbum musical, solicitando información como el nombre, la descripción, la portada,
    la fecha de publicación, el género y la lista de canciones del álbum.

    Returns:
        tuple: Una tupla que contiene el objeto del álbum creado y la lista de canciones del álbum.
    """
        nombre = input("Ingresa el nombre del álbum que quieres crear:").strip().title()
        descripcion = input("Ingresa la descripcion del álbum:")
        link = input("Ingresa el link de la portada del álbum: ") 
        fecha = datetime.today().strftime('%Y-%m-%dT%H:%M:%SZ') #Datetime es una libreria usada para ver la fecha publicada
        genero = self.pedir_Genero()
        artist = self.gestion_Perfil.buscar_perfil_por_nombre("musicos")

        tracklist = []
        
        while True:
            try:
                print("\nIngresa los datos de la canción que quieres agregar al álbum:")
                cancion_Creada = self.crear_Cancion()

                tracklist.append(cancion_Creada) 

                respuesta = input("¿Deseas agregar otra canción? (y/n): ").lower() 
                if respuesta != 'y':
                    break
            except ValueError:
                print("Ha ingresado un valor erróneo, vuelva a intentarlo")

        album = Album(None, nombre, descripcion, link ,fecha,genero, artist, tracklist)#artist, #cambiar en caso de que artist si sea necesario.
        self.albumes.append(album)
        
        return album ,tracklist 

    def pedir_Genero(self):
        """
    Solicita al usuario seleccionar un género para el álbum que está siendo creado.

    Returns:
        str: El género seleccionado por el usuario.
    """
        generos = set()

        for album in self.albumes:
            generos.add(album.genre)

        print("Estos son los generos disponibles: ")
        generosLista = list(generos)
        for index, genero in enumerate(generosLista):
            print(f"{index +1}. {genero}")
        

        while True:
            try:
                opcion = int(input("")) -1
                if opcion < 0:
                    raise Exception

                return generosLista[opcion]
            except:
                print("Ha ingresado un valor erroneo, vuelvalo a intentar")

    def crear_Cancion(self):
        """
    Permite al usuario ingresar información para crear una nueva canción.

    Returns:
        Cancion: El objeto de la canción creada.
    """

        nombre_cancion = input("Ingrese el nombre de la canción:")
        duracion = self.pedir_Duracion()
        link = input("Ingresa el link de la canción:") 

        return Cancion(None, nombre_cancion, duracion, link)
        
    def pedir_Duracion(self):
        """
    Solicita al usuario ingresar la duración de una canción en minutos y segundos.

    Returns:
        str: La duración de la canción en formato "minutos:segundos".
    """
        while True:
            try:
                minutos = int(input("Ingrese los minutos que dura la canción: "))

                if minutos < 0:
                    print("Ingrese una duración positiva")
                    continue
                break
            except:
                print("Ha ingresado un valor erroneo, inténtalo de nuevo")

        while True:
            try:
                segundos = int(input("Ingrese los segundos que dura la canción: "))

                if segundos < 0:
                    print("Ingrese una duración positiva")
                    continue
                elif segundos > 60:
                    print("Los segundos no pueden ser mayores a 60")
                    continue
                break
            except:
                print("Ha ingresado un valor erroneo, inténtalo de nuevo")

        return f"{minutos}:{segundos}"
    
    def manera_Escuchar(self):
        """
    Permite al usuario escuchar música de diferentes formas: buscando por nombre de álbum o canción,
    por perfil de músico o a través de una playlist.
    """
        usuario = self.gestion_Perfil.buscar_perfil_por_nombre()
        if usuario == None:
            print("No existe ningún usuario con ese nombre")
            return

        while True:
            try:
                opcion = int(input("1. Escuchar a través de nombre de álbum o canción \n 2. Escuchar a través de un perfil de músico \n 3. Escuchar a través de playlist \n 4. Salir \n -->"))
            

                if opcion == 1:
                    self.escuchar_Por_Nombre(usuario.id)
                    
                elif opcion == 2:
                    musico = self.gestion_Perfil.buscar_perfil_por_nombre("musicos")
                    if musico == None:
                        print("El musico no existe")
                        return
                    cancion = musico.seleccionar_Cancion(self.albumes)
                    cancion.escuchar(usuario.id)
                    
                elif opcion == 3:
                    self.escuchar_Por_Playlist(usuario.id)
                elif opcion == 4:
                    break
                else:
                    raise Exception

            except:
                print("Ha ingresado un valor erroneo , inténtalo de nuevo")
        pass
    
    def escuchar_Por_Playlist(self, idUsuario: str):
        """
    Permite al usuario escuchar las canciones de una playlist específica.

    Args:
        idUsuario (str): El ID del usuario que está escuchando la playlist.
    """
        playlist = self.buscar_Playlist_Por_Nombre()

        for cancionId in playlist.tracks:
            cancion = self.buscar_Cancion_Por_Id(cancionId)

            if not cancion:
                print(f"La canción con el id {cancionId} no existe")
                continue
            cancion.escuchar(idUsuario)
    
    def buscar_Cancion_Por_Id(self, id: str):
        """
    Busca una canción por su ID en la lista de canciones de todos los álbumes.

    Args:
        id (str): El ID de la canción que se está buscando.

    Returns:
        Cancion or None: La canción encontrada, o None si no se encuentra.
    """
        for album in self.albumes:
            for track in album.tracklist: 
                if id == track.id:
                    return track

    def buscar_Playlist_Por_Nombre(self):
        """
    Permite al usuario seleccionar una playlist por su nombre entre las playlists existentes.

    Returns:
        Playlist: La playlist seleccionada.
    """
        listaNombres = []
        for index, playlist in enumerate(self.playlists):
            nombre = playlist.name.strip().title()
            print(f"{index + 1}. {nombre}")
            listaNombres.append(nombre)

        while True:
            try:
                nombre = input("Escoja un nombre de las playlists mostradas: ").strip().title()

                playlistIndice = listaNombres.index(nombre)
                return self.playlists[playlistIndice]
            except ValueError:
                print("El nombre no existe, verifique si lo está escribiendo bien:")
        
    def escuchar_Por_Nombre(self, idUsuario: str):
        """
    Permite al usuario escuchar una canción o álbum específico mediante su nombre.

    Args:
        idUsuario (str): El ID del usuario que está escuchando la canción o álbum.
    """
        resultado = self.buscar_Album_O_Cancion_Por_Nombre()
        resultado.escuchar(idUsuario)

    def buscar_Album_O_Cancion_Por_Nombre(self):
        """
    Permite al usuario seleccionar un álbum o una canción por su nombre entre los álbumes y canciones disponibles.

    Returns:
        Album or Cancion: El álbum o la canción seleccionada.
    """
        listaNombres = {}

        for index, album in enumerate(self.albumes):
            count = index + 1
            print(f"{count}. {album.name}")

            listaNombres[album.name] = []

            for index2, track in enumerate(album.tracklist):
                print(f"    {count}.{index2 + 1}. {track.name}")
                listaNombres[album.name].append(track.name)

        while True:
            nombre = input("Escoja un nombre de los albumes o canciones mostradas: ").strip().title()

            indexAlbum = 0
            for nombreAlbum, nombresCanciones in listaNombres.items():
                if nombreAlbum == nombre:
                    return self.albumes[indexAlbum]
                
                for indexCancion, nombreCancion in enumerate(nombresCanciones):
                    if nombreCancion == nombre:
                        return self.albumes[indexAlbum].tracklist[indexCancion]
                indexAlbum += 1
            
            print("El nombre no existe, verifique si lo está escribiendo bien:")

    def crear_playlist(self):
        """
    Permite al usuario crear una nueva playlist.
    """

        titulo = input ("Inserta el título de tu playlist:")
        descripcion = input ("Inserta la descripción de la playlist:")
        canciones_playlist = []

        while True:
            cancion = self.buscar_Cancion()
            canciones_playlist.append(cancion.id)

            nombre_cancion = input("Desea terminar de agregar canciones (y/n): ").strip().lower()
            if nombre_cancion.lower() == 'y':
                break
            else:
                print("Se interepretará que desea seguir agregando")

        creator = None
        while creator == None:
            creator = self.gestion_Perfil.buscar_perfil_por_nombre()
            if creator == None:
                print("El usuario no existe, por favor ingrese otro nombre")
                continue
            break
        nuevo_playlist = Playlist(None, titulo, descripcion, canciones_playlist, creator)

        self.playlists.append(nuevo_playlist)
        print("Playlist creado con éxito!")

    def buscar_Cancion(self):
        
        resultado = self.buscar_Album_O_Cancion_Por_Nombre() 
        if isinstance(resultado, Cancion):
            return resultado
        else:
            return resultado.escoger_Cancion()   

    def buscar_Album(self):
        """
    Permite al usuario buscar un álbum por su nombre.

    Returns:
        Album: El álbum encontrado, o None si no se encuentra.
    """
        nombre = input("Ingrese el nombre del álbum que desea buscar").strip().title()
        for album in self.albumes:
            if album.name.strip().title() == album:
                return album



    def buscar(self, criterio_busqueda):
        """
    Busca elementos en un contexto específico según el criterio de búsqueda proporcionado.

    Args:
        criterio_busqueda (str): El criterio de búsqueda utilizado para buscar elementos.

    Returns:
        list: Una lista de resultados que coinciden con el criterio de búsqueda.
    """
        resultados = []
        criterio = criterio_busqueda.lower()

        
        for album in self.albumes:
            if criterio in album.nombre.lower() or criterio in album.artista.lower():
                resultados.append(album)

        
        for album in self.albumes:
            for cancion in album.canciones:
                if criterio in cancion.titulo.lower() or criterio in cancion.artista.lower():
                    resultados.append(cancion)

        
        for playlist in self.playlists:
            if criterio in playlist.titulo.lower() or criterio in playlist.creador.lower():
                resultados.append(playlist)

        return resultados





