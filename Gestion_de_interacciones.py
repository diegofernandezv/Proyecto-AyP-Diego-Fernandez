from modulos.Gestion_Perfil import Gestion_Perfil
from modulos.Gestion_de_musical import Gestion_De_Musical


class Gestion_De_Interacciones:
    def __init__(self, gestion_Perfil: Gestion_Perfil, gestion_Musical: Gestion_De_Musical) -> None:
        self.gestion_Perfil = gestion_Perfil
        self.gestion_Musical = gestion_Musical

    def menu(self):
        while True:
            try:
                print("****🎧❤️BIENVENIDO A LA Gestión de Interacciones❤️🎧****\n")

                print("1.Dar like al perfil de un músico")
                print("2.Dar like al perfil de un álbum")
                print("3.Dar like a una canción")
                print("4.Dar like a una playlist")
                print("5.Salir")
                opcion = int(input("-->"))

                if opcion == 1:
                    self.like_musico()
                elif opcion == 2:
                    self.like_album()
                elif opcion == 3:
                    self.like_cancion()
                elif opcion == 4:
                    self.like_playlist()
                elif opcion == 5:
                    break
                else:
                    raise Exception

            except:
                print("Ha ingresado un valor erroneo, vuélvalo a intentar")

    def like_musico(self):
        print("Ingrese el usuario que quiere dar un like:")
        usuario =  self.gestion_Perfil.buscar_perfil_por_nombre()
        if usuario == None:
            print("El usuario no existe")
            return
        
        print("Ingrese el músico al que le quiere dar un like:")
        musico =  self.gestion_Perfil.buscar_perfil_por_nombre("musicos")
        if musico == None:
            print("El músico no existe")
            return
        
        musico.recibir_Like(usuario)

    def like_album(self):
        print("Ingrese el usuario que quiere dar un like:")
        usuario =  self.gestion_Perfil.buscar_perfil_por_nombre()
        if usuario == None:
            print("El usuario no existe")
            return

        print("Ingrese el álbum al que le quiere dar un like:")
        album =  self.gestion_Musical.buscar_Album()
        if album == None:
            print("El álbum no existe")
            return
        album.recibir_Like(usuario)

    def like_cancion (self):
        print("Ingrese el usuario que quiere dar un like:")
        usuario =  self.gestion_Perfil.buscar_perfil_por_nombre()
        if usuario == None:
            print("El usuario no existe")
            return

        print("Ingrese la canción al que le quiere dar un like:")
        cancion =  self.gestion_Musical.buscar_Cancion()
        if cancion == None:
            print("La canción no existe")
            return
        cancion.recibir_Like(usuario)

    def like_playlist(self):
        print("Ingrese el usuario que quiere dar un like:")
        usuario =  self.gestion_Perfil.buscar_perfil_por_nombre()
        if usuario == None:
            print("El usuario no existe")
            return

        print("Ingrese la playlist al que le quiere dar un like:")
        playlist =  self.gestion_Musical.buscar_Playlist_Por_Nombre()
        if playlist == None:
            print("La playlist no existe")
            return
        playlist.recibir_Like(usuario) 