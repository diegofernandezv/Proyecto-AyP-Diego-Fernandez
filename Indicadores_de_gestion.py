
import matplotlib.pyplot as plt
from Album import Album
from Musico import Musico
from Oyente import Oyente

class Indicadores_de_gestion:
    def __init__(self, musicos: list[Musico], oyentes: list[Oyente], albumes: list[Album]):
        self.musicos = musicos
        self.oyentes = oyentes
        self.albumes = albumes

    def menu(self):
        """
    Muestra el menú de indicadores de gestión y permite al usuario elegir el informe que desea generar.

    """
        while True:
            try:
                print("****📈📊BIENVENIDO A LOS Indicadores de Gestión📊📈****\n")
                print("Elige el informe que quieres generar:")

                print("1.Top 5 músicos con mayor cantidad de streams")
                print("2.Top 5 de álbumes con mayor cantidad de streams")
                print("3.Top 5 de canciones con mayor cantidad de streams")
                print("4.Top 5 de escuchas con mayor cantidad de streams")
                print("5. Salir")
                opcion = int(input("-->"))

                if opcion == 1:
                    self.obtener_top_Musicos()
                elif opcion == 2:
                    self.obtener_top_Albumes()
                elif opcion == 3:
                    self.obtener_top_Canciones()
                elif opcion == 4:
                    self.obtener_top_Escuchas()
                elif opcion == 5:
                    break
            except Exception as e:
                print(e)
                print("Ha ingresado un valor erroneo, vuelvalo a intentar")
    
    def obtener_top_Musicos(self):
        """
    Genera un informe de los top 5 músicos con la mayor cantidad de streams.
    Calcula la cantidad total de streams de todas las canciones de cada álbum 
    de cada músico y muestra los top 5.

    """
        top_musicos = {}
        for album in self.albumes:
            musico = self.buscar_Usuario_Por_Id(album.artist)
            if musico == None:
                print("El artista del álbum ya no existe en la base de datos")
                continue

            top_musicos[musico.id] = {
                    "nombre": musico.name,
                    "streams": 0
            }

            for cancion in album.tracklist:
                top_musicos[musico.id]["streams"] += len(cancion.reproducciones)
       
        self.mostrar_top5(top_musicos, "musicos")

    def buscar_Usuario_Por_Id(self, idUser):
        """
    Busca un usuario por su ID en la lista combinada de oyentes y músicos.

    Args:
        idUser (int): El ID del usuario que se desea buscar.

    Returns:
        obj or None: El objeto del usuario si se encuentra, None si no se encuentra.
    """
        for usuario in (self.oyentes + self.musicos):
            if usuario.id == idUser:
                return usuario
        

    def obtener_top_Albumes(self):
        """
    Genera un informe de los top 5 álbumes con la mayor cantidad de streams.
    Calcula la cantidad total de streams de todas las canciones de cada álbum y muestra los top 5.

    """
        top_Albums = {}
        for album in self.albumes:
            top_Albums[album.id] = {
                    "nombre": album.name,
                    "streams": 0
            }

            for cancion in album.tracklist:
                top_Albums[album.id]["streams"] += len(cancion.reproducciones)
       
        self.mostrar_top5(top_Albums, "albums")

    def obtener_top_Canciones(self):
        """
    Genera un informe de las top 5 canciones con la mayor cantidad de streams.
    Calcula la cantidad total de streams de cada canción y muestra los top 5.

    """
        top_Canciones = {}
        for album in self.albumes:
            for cancion in album.tracklist:
                top_Canciones[cancion.id] = {
                    "nombre": cancion.name,
                    "streams": len(cancion.reproducciones)
                }

        
        self.mostrar_top5(top_Canciones, "canciones")

    def obtener_top_Escuchas(self):
        """
    Genera un informe de las top 5 escuchas con la mayor cantidad de streams.
    Calcula la cantidad total de streams de cada usuario (escucha) y muestra los top 5.

    """
        top_escucha = {}
        for album in self.albumes:
            for cancion in album.tracklist:
                for userId in cancion.reproducciones:
                    usuario = self.buscar_Usuario_Por_Id(userId)
                    if usuario == None:
                        print(f"El usuario que escuchó la canción {cancion.name} ya no existe en la base de datos")
                        continue
                    
                    if top_escucha.get(usuario.id) == None:
                        top_escucha[usuario.id] = {
                            "nombre": usuario.name,
                            "streams": 1
                        }
                    else:
                         top_escucha[usuario.id]["streams"] += 1
       
        self.mostrar_top5(top_escucha, "escuchas")

    def mostrar_top5(self, top_Objetos, title):
        """
    Muestra los top 5 objetos junto con su cantidad de streams y luego muestra un gráfico correspondiente.

    Args:
        top_Objetos (dict): Un diccionario de objetos donde las claves son los IDs de 
        los objetos y los valores son diccionarios que contienen información 
        sobre el objeto (nombre y cantidad de streams).
        title (str): El título del gráfico.

    """
        objetos_Ordenados = sorted(top_Objetos.items(), reverse=True, key= lambda item: item[1]["streams"] )

        valores = []
        nombres = []
        for index, top_Objeto in enumerate(objetos_Ordenados[:5]):
            cancion = top_Objeto[1]
            nombre = cancion["nombre"]
            streams = cancion["streams"]

            print(f"Posición {index + 1} {nombre}: {streams} streams")
            nombres.append(nombre)
            valores.append(streams)

        self.mostrar_graficos(nombres, valores, title)
        
    def mostrar_graficos(self, names,streams,title):
        """
    Muestra un gráfico de barras para visualizar los datos de los top 5 objetos más escuchados.

    Args:
        names (list): Una lista de nombres de objetos.
        streams (list): Una lista de la cantidad de streams correspondientes a cada objeto.
        title (str): El título del gráfico.
    """
        plt.figure(figsize=(10,5))
        plt.bar(names,streams,color = '#2C7070')
        plt.xlabel(title)
        plt.ylabel('Streams')
        plt.title(f'Top 5 de {title} Más escuchadas')
        plt.xticks(rotation=45)
        plt.show()



    





    