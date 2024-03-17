from Musico import Musico
from Oyente import Oyente



class Gestion_Perfil:
    def __init__(self, musicos: list[Musico], oyentes: list[Oyente]) -> None:
        self.musicos = musicos
        self.oyentes = oyentes

    def menu(self):
        """
    Muestra el menú de gestión de perfil y permite al 
    usuario elegir entre diferentes opciones para administrar su perfil.

    """
        while True:
            try:
                print("****👤📋BIENVENIDO A LA Gestión de Perfil📋👤****\n")

                print("1.Registrar nuevo usuario")
                print("2.Buscar perfiles por nombre")
                print("3.Cambiar información personal de la cuenta")
                print("4.Borrar los datos de la cuenta")
                print("5.Mostrar información del usuario")
                print("6. Salir")

                opcion = int(input("-->"))

                if opcion == 1:
                    self.registrar_usuario()
                elif opcion == 2:
                    usuario = self.buscar_perfil_por_nombre()
                    if usuario == None:
                        print("Usuario no encontrado")
                        return
                elif opcion == 3:
                    self.cambiar_informacion_personal()
                elif opcion == 4:
                    self.borrar_cuenta()
                elif opcion == 5:
                    self.mostrar_informacion()
                elif opcion == 6:
                    break


            except Exception as e:
                print(e)
                print("Ha ingresado un valor erroneo, vuelvalo a intentar")


    def pedir_Tipo(self):
        """
    Solicita al usuario que seleccione el tipo de usuario entre Músico y Escucha.

    Returns:
        str: "musico" si el usuario selecciona 1, "escucha" si selecciona 2.
    """
        while True:
            try:
                tipo_usuario = int(input("Seleccione tipo de usuario (1 para Músico, 2 para Escucha): "))
            
                if tipo_usuario == 1:
                    return "musico"
                elif tipo_usuario == 2:
                    return "escucha"
                else:
                   raise Exception #crear una excepcion artificial
            except:
                print("Opción inválida, por favor seleccione 1 para Músico o 2 para Escucha.") 

    def registrar_usuario(self):
        """
    Registra un nuevo usuario solicitando su nombre, correo electrónico, nombre de usuario y tipo de usuario.
    Luego, crea un objeto Musico u Oyente dependiendo del tipo de usuario y lo agrega a la lista correspondiente.

    """    
        nombre = input ("Ingrese su nombre o nombre artístico:")
        correo = input ("Ingrese su correo electrónico:")
        username = input ("Ingresa su nombre de usuario:")
        tipo_usuario = self.pedir_Tipo()

        print("Se ha creado el siguiente usuario: ")
        if tipo_usuario == "musico":
            musico = Musico(None, nombre, correo, username)
            self.musicos.append(musico)
            musico.mostrar_atributos()
        else:
            oyente = Oyente(None, nombre, correo, username)
            self.oyentes.append(oyente)
            oyente.mostrar_atributos()

    def buscar_perfil_por_nombre(self, filtro = "todos"):
        """
    Busca un perfil (musico u oyente) por su nombre.

    Args:
        filtro (str): Indica si se debe buscar en "todos" los usuarios, 
        solo en "musicos" o solo en "oyentes". Por defecto, es "todos".

    Returns:
        obj or None: El objeto del usuario encontrado si se encuentra, None si no se encuentra.
    """
        
        if filtro == "todos":
            usuarios = self.oyentes + self.musicos
            sustantivo = "usuario"
        elif filtro == "musicos":
            usuarios = self.musicos
            sustantivo = "musico"
        elif filtro == "oyentes":
            usuarios = self.oyentes
            sustantivo = "oyente"
        else:
            usuarios = self.oyentes + self.musicos
            sustantivo = "usuario" 

            
        nombre = input(f"Ingrese el nombre del {sustantivo} que desea buscar:").strip().title()
        for usuario in usuarios:
            if usuario.name.strip() == nombre:
                return usuario
        return None

    def cambiar_informacion_personal(self):
        """
    Permite al usuario cambiar la información personal de su perfil (nombre, correo electrónico, username).

    """  
        usuario = self.buscar_perfil_por_nombre()
        if usuario == None:
            print("No se puede modificar el usuario, porque no se encontró")
        else:
            usuario.mostrar_atributos()

            while True:
                opcion = input("¿Qué información desea cambiar? (nombre/correo/username/salir): ").strip().lower()

                if opcion == "nombre":
                    nuevo_nombre = input("Ingrese el nuevo nombre: ")
                    print(f"Nombre actualizado correctamente. {usuario.name} -> {nuevo_nombre}")
                    usuario.name = nuevo_nombre

                elif opcion == "correo":
                    nuevo_correo = input("Ingrese el nuevo correo electrónico: ")
                    print(f"Correo electrónico actualizado correctamente. {usuario.email} -> {nuevo_correo}")
                    usuario.email = nuevo_correo

                elif opcion == "username":
                    username = input("Ingrese el nuevo username: ")
                    print(f"Username actualizado correctamente. {usuario.username} -> {username}")
                    usuario.username = username
                elif opcion == "salir":
                    print("Saliendo de cambiar información \n")
                    break
                else:
                    print("Opción no válida, inténtelo de nuevo")

    def borrar_cuenta(self):
            """
    Permite al usuario eliminar su cuenta. Busca el perfil del usuario 
    por nombre y lo elimina de la lista correspondiente (musicos u oyentes).

    """
            usuarioEncontrado = self.buscar_perfil_por_nombre()

            for index, musico in enumerate(self.musicos):
                if musico.name == usuarioEncontrado.name:
                    self.musicos.pop(index) #Uso de .pop para remover por indice en vez de por valor.
                    print("La cuenta de", musico.name, "ha sido eliminada correctamente.")
                    return
           
            for index, oyente in enumerate(self.oyentes):
                if oyente.name == usuarioEncontrado.name:
                    self.oyentes.pop(index) 
                    print("La cuenta de", oyente.name, "ha sido eliminada correctamente.")
                    return
         
    def mostrar_informacion(self):
        """
    Muestra la información de un usuario dado su nombre.
    Muestra el nombre, correo electrónico y tipo de usuario (Músico o Escucha).
    Si el usuario es un Músico, también muestra los álbumes de música y su tracklist.
    Si el usuario es un Escucha, también muestra los álbumes y canciones 
    gustadas, así como las playlists creadas y/o guardadas.

    """
        nombre = input("Ingrese el nombre del usuario cuya información desea mostrar: ")
        encontrado = False
        for usuario in self.oyentes + self.musicos:
            if usuario.name.lower() == nombre.lower():
                encontrado = True
                print("Información del usuario:")
                print("Nombre:", usuario.name)
                print("Correo electrónico:", usuario.email)
                print("Tipo de usuario:", "Músico" if isinstance(usuario, Musico) else "Escucha")
                if isinstance(usuario, Oyente, album):
                    print("Álbumes gustados:", usuario.albumes)
                    print("Canciones gustadas:", usuario.canciones)
                    print("Playlists creadas y/o guardadas:", usuario.playlists)
                else:
                    print("Álbumes de música:", usuario.albumes)
                    for album in usuario.albumes:
                        print("Tracklist de", album, ":", usuario.albumes[album])
        if not encontrado:
            print("Usuario no encontrado.")



    

                            
