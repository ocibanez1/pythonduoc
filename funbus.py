import os
os.system("cls")
lista_asientos=[]

def menu_principal():
    print("1.Mostrar asientos\n2.Reservar asientos\n3.Mostrar reservas\n4.Salir")

def mostrar_asientos():
    print("Mostrar asientos")
    total_asientos=40
    for i in range (1 , total_asientos +1):
        asiento = str(i).zfill(2)
        lista_asientos.append(asiento)
    for i in range(0,total_asientos,4):
        fila=lista_asientos[i:i+4]
        print(f"{fila[0]} {fila[1]} | {fila[2]} {fila[3]}")
    input("Enter para continuar")
    print(lista_asientos)
    input("Enter para continuar")

# def reservar_asientos():
    while True:
         try:
             asiento_elegir=int(input("Ingresar el asiento a reservar:\n"))
             if asiento_elegir not in lista_asientos:
                 os.system("cls")
                 print("Asiento no disponible")
                 input("Enter para continuar")
             else:
                 asiento_reserva = "X"
                 for i in lista_asientos:

                 os.system("cls")

         except:
             os.system("cls")
             print("Ingresar valor numerico")
             input("Enter para continuar")

                