import os
from funbus import *
os.system("cls")
flag_menu=True
while flag_menu:
    os.system("cls")
    menu_principal()
    try:
        opcion=int(input("Ingresar opcion:\n"))
        if opcion==1:
            os.system("cls")
            mostrar_asientos()
        elif opcion==2:
            # reservar_asientos()
             input("Enter para continuar")
        elif opcion==3:
            input("Enter para continuar")
        elif opcion==4:
            input("Enter para continuar")        
    except:
        os.system("cls")
        print("Ingresar valor dentro del rango de opciones")
        input("Enter para continuar")