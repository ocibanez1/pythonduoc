import os
from funbus import *
os.system("cls")
flag_menu=True
while flag_menu:
    limpiar_pantalla()
    print("Menu principal")
    print("1.Mostrar asientos\n2.Reservar asientos:\n3.Mostrar reservas:\n4.Salir")
    try:
        opcion=int(input("Ingresar opcion:\n"))
        if opcion==1:
            limpiar_pantalla()
            mostrar_asientos()
            pausar()
        elif opcion==2:
            limpiar_pantalla()
            reservar_asiento()
            pausar()
        elif opcion==3:
            limpiar_pantalla()
            mostrar_reservas()
            pausar()
        elif opcion==4:
            limpiar_pantalla()
            print("Saliendo")
            pausar()
            break
    except:
         limpiar_pantalla()
         print("Ingresar un valor valido para el menu")
         pausar()
