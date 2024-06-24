import os
from funcolegio1 import *
os.system("cls")
flag_menu=True
while flag_menu:
    os.system("cls")
    menu_principal()
    opcion=int(input("Ingresar opcion:\n"))
    if opcion==1:
            os.system("cls")
            print("Registrar estudiante")
            reg_estudiantes()
    elif opcion==2:
            os.system("cls")
            print("Buscar Estudiante")
            buscar_estudiante()
    elif opcion==3:
            os.system("cls")
            menu_certificados()
    elif opcion==4:
            os.system("cls")
            print("Saliendo")
            input("Enter para continuar")
            flag_menu=False

