import os
import msvcrt


def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


def imprimir_menu():
    print("Agenda de ventas:")
    print("1. Ver total de ventas")
    print("2. Ver total de ventas por año")
    print("3. Ver promedio de ventas por año")
    print("4. Salir")


def obtener_opcion():
    opcion = input("Ingrese una opción: ")
    while opcion not in ["1", "2", "3", "4", "5"]:
        opcion = input("Opción inválida. Ingrese una opción nuevamente: ")
    return opcion


def ver_total_de_ventas():
    datos = open("datos.csv", "r")
    print("Ventas totales:")
    total = 0
    _ = datos.readline()
    for linea in datos.readlines():
        datos_separados = linea.split(";")
        total = (
            total
            + int(datos_separados[1])
            + int(datos_separados[2])
            + int(datos_separados[3])
            + int(datos_separados[4])
        )
    print(total)
    datos.close()
    datos = open("datos.csv", "r")
    for linea in datos.readlines():
        print(linea)
    datos.close()


def ver_total_de_ventas_por_año():
    datos = open("datos.csv", "r")
    _ = datos.readline()

    print("Ventas totales por año:")

    for linea in datos.readlines():
        total = 0
        datos_separados = linea.split(";")
        total = (
            total
            + int(datos_separados[1])
            + int(datos_separados[2])
            + int(datos_separados[3])
            + int(datos_separados[4])
        )
        print(f"{datos_separados[0]}: {total}")

    datos.close()


def ver_promedio_de_ventas_por_año():
    datos = open("datos.csv", "r")
    _ = datos.readline()

    print("Promedio de ventas por año:")

    for linea in datos.readlines():
        total = 0
        datos_separados = linea.split(";")
        total = (
            total
            + int(datos_separados[1])
            + int(datos_separados[2])
            + int(datos_separados[3])
            + int(datos_separados[4])
        )
        print(f"{datos_separados[0]}: {total/4}")

    datos.close()


while True:
    imprimir_menu()
    opcion = obtener_opcion()
    if opcion == "1":
        ver_total_de_ventas()
    elif opcion == "2":
        ver_total_de_ventas_por_año()
    elif opcion == "3":
        ver_promedio_de_ventas_por_año()
    elif opcion == "4":
        print("Programa finalizado")
        break
    print("1: Voler al menú \n2: Salir")
    respuesta = input()
    while respuesta not in ["1", "2"]:
        print("Opción no válida, reintente")
        respuesta = input()
    if respuesta == "2":
        print("Programa finalizado")
        break
    limpiar_pantalla()
