#mainanalisis
import os, time, random
from funanalisis import *
from statistics import geometric_mean
flagmenu=True
while flagmenu:
        limpiar_pantalla()
        try:
                print("Menu principal")
                print("1.Asignar precios aleatorios\n2.Clasificar precios\n3.Ver estadistica\n4.Reporte precios\n5.Salir del programa")
                opcion=int(input("Ingresar opcion\n"))
                if opcion==1:
                        asignar_precio()
                elif opcion==2:
                        clasificar_precio()
                elif opcion==3:
                        ver_estadistica()
                elif opcion==4:
                        reporte_precios()
                elif opcion==5:
                        print("Cerrando programa")
                        flagmenu=False
        except:
                print("Debe ingresar valor numerico")
                input("Enter para continuar...")




