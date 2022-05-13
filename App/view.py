"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2-  5 estaciones desde donde se inician más viajes")
    print("3- Planear paseos turísticos por la ciudad")
    print("4- Reconocer los componentes fuertemente conectados del sistema")
    print("5- Planear una ruta rápida")
    print("6-Reportar rutas en un rango de fechas para los usuarios anuales")
    

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")

    elif int(inputs[0]) == 2:
        #estaciones=controller.getcincostatciones()
        pass
        
    
    elif int(inputs[0]) == 3:
        estin=input("Nombre de la estación de inicio: ")
        disponibilidad=input(" Disponibilidad del usuario pasa su paseo: ")
        minparadas=input(" número mínimo de estaciones de parada para la ruta (sin incluir la estación de inicio)")
        maxresp=input("máximo número de rutas de respuesta")
    
    elif int(inputs[0]) == 4:
        #controler.getfuertementeconectado
        pass

    elif int(inputs[0]) == 5:
        estor=input("Nombre de la estación origen: ")
        estdest=input("Nombre de la estación destino: ")

    elif int(inputs[0]) == 6:
        datein=input("Fecha inicial de consulta (formato “MM/DD/AAAA”): ")
        datefin=input("Fecha final de consulta (formato “MM/DD/AAAA”): ")

    else:
        sys.exit(0)
sys.exit(0)
