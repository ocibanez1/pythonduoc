import os
from funcolegio import *
os.system("cls")
flag_menu=True
while flag_menu:
    os.system("cls")
    menu_principal()
    try:
        opcion=int(input("Ingresar opcion:\n"))
        if opcion==1:
            os.system("cls")
            print("Registrar estudiante")
            reg_estudiantes()
        elif opcion==2:
            
             input("Enter para continuar")
        elif opcion==3:
            input("Enter para continuar")
        elif opcion==4:
            print("Salir")
            input("Enter para continuar")
            break  
    except:
        print("Ingresar valor numerio")
        input("Enter para continuar")   
