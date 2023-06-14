import os
import msvcrt
def total_año():
    lista = []
    datos = open('datos.csv', 'r')
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
    
def total():
    lista = []
    datos = open('datos.csv', 'r')
    _ = datos.readline()
    total=0
    for linea in datos.readlines():
        
        datos_separados = linea.split(";")
        total = (
            total
            + int(datos_separados[1])
            + int(datos_separados[2])
            + int(datos_separados[3])
            + int(datos_separados[4])
        )
    print("El total de ventas es de ",total)

    datos.close()
    
def promedio():
    lista = []
    contador=1
    datos = open('datos.csv', 'r')
    _ = datos.readline()
    total=0
    for linea in datos.readlines():
        
        datos_separados = linea.split(";")
        total = (
            total
            + int(datos_separados[1])
            + int(datos_separados[2])
            + int(datos_separados[3])
            + int(datos_separados[4])
        )
        contador=contador+1
    print("El promedio de ventas es de ",total%contador)

    datos.close()
    
respuesta=""
while respuesta!="4":
    respuesta=input("Ingrese una opción:\n1:Ver total de ventas por año\nv2:Ver total de ventas\n3:Ver promedio de ventas\n4: Salir\n"   )
    if respuesta=="1":
        total_año()
    if respuesta=="2":
        total()
    if respuesta=="3":
        promedio()