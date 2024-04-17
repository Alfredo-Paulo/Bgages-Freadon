# Aplicacion para crear musica 


import datetime
import time
import webbrowser  # Para abrir la galería en el navegador

# Definir la función del menú de reproducción
def menu_reproduccion():
    print("Menú de Reproducción:")
    print("1. Reproducir canción 1")
    print("2. Reproducir canción 2")
    print("3. Reproducir canción 3")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    return opcion

# Definir la función principal
def main():
    # Configurar la alarma
    hora_alarma = 7
    minuto_alarma = 0
    configurar_alarma(0,7, 0,0)

    # Ejecutar el menú de reproducción
    while True:
        opcion = menu_reproduccion()
        if opcion == "1":
            reproducir_musica("cancion1.mp3")
        elif opcion == "2":
            reproducir_musica("cancion2.mp3")
        elif opcion == "3":
            reproducir_musica("cancion3.mp3")
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Inténtelo de nuevo.")

    # Abrir galería en línea
    webbrowser.open("https://unsplash.com/")  # Ejemplo de Unsplash, puedes cambiar la URL según la galería que prefieras

if __name__ == "__main__":
    main()

# Definir la función de reproducción de música
def reproducir_musica(cancion):
    print("Reproduciendo:", cancion)

# Definir la función de alarma
def configurar_alarma(hora, minuto):
    while True:
        ahora = datetime.datetime.now()
        if ahora.hour == hora and ahora.minute == minuto:
            print("¡Es hora de despertar!")
            reproducir_musica("alarma.mp3")
            break
        time.sleep(60)  # Comprobar cada minuto

# Definir la función principal
def main():
    # Configurar la alarma
    hora_alarma = 7
    minuto_alarma = 0
    configurar_alarma(hora_alarma, minuto_alarma)

    # Ejemplo de reproducción de música
    cancion = "cancion.mp3"
    reproducir_musica(cancion)

    # Abrir galería en línea
    webbrowser.open("https://unsplash.com/")  # Ejemplo de Unsplash, puedes cambiar la URL según la galería que prefieras

if __name__ == "__main__":
    main()