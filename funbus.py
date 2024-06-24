import os
os.system("cls")
lista_asientos=[]
reservar={}
asiento_reservados=[]
def pausar():
    input("Enter para continuar")

def limpiar_pantalla():
    os.system("cls")

def mostrar_asientos():
    for i in range(1,40+1):
        asiento=str(i).zfill(2)
        lista_asientos.append(asiento)      
    for i in range(0,40,4):
        print(f"{lista_asientos[i]} {lista_asientos[i+1]} | {lista_asientos[i+2]} {lista_asientos[i+3]}")

def val_nombre():
    nombre=None
    while not nombre:
        nombre=input("Ingresar nombre:\n")
        if len(nombre)>=4:
            nombre_val=nombre
            reservar["Nombre"]=nombre_val
            break
        else:
            print("El nombre debe contener 4 caracteres como minimo")
            pausar()
    return nombre_val

def val_rut():
    rut=None
    while not rut:
        rut=int(input("Ingresar rut sin digito verificador:\n"))
        rut_val=str(rut)
        if len(rut_val) > 0 or len(rut_val) < 9 :
            print(f"Rut ingresado {rut_val}")
            reservar["Rut"]=rut_val
            pausar()
            break
        else:
            print("Rut invalido")

def val_destinohora():
    destino=None
    hora=None
    while not destino:
        destino=input("Ingresar destino:\n")
        if len(destino)>=4:
            destino_val=destino
            reservar["Destino"]=destino_val
            continue
        else:
            print("El destino debe contener 4 caracteres como minimo")
            pausar()
    while not hora:
        try:
            hora=int(input("Ingresar hora:\n Ejemplo formato:'1300\n'"))
            if hora > 0 or hora < 2359:
                hora_val= hora
                reservar["Hora"]=hora_val
                break
            else:
                print("Horario no existente")
        except:
            print("Hora no valida")
            pausar()
    
def reservar_asiento():
    limpiar_pantalla()
    mostrar_asientos()
    while True:
        try:
            selec_asiento=int(input("Seleccionar asiento disponible para comprar:\n"))
            if 0 < selec_asiento < 41:
                asiento_selec=str(selec_asiento).zfill(2)
                flag_asiento=True
                while flag_asiento:#romper al no querer comprar mas asientos
                    if asiento_selec in lista_asientos:
                        limpiar_pantalla
                        print("Asiento disponible")
                        pausar()
                        val_nombre()
                        val_rut()
                        val_destinohora()
                        print (reservar)
                        pausar()
                        asiento_reservados.append(asiento_selec)
                        lista_asientos[selec_asiento]="X"
                        flag_asiento=False
                break

            else:
                print("Asientos fuera de rango")
                limpiar_pantalla()

        except:
             print("Error de seleccion de asiento")
             pausar()

def mostrar_reservas():
    if not asiento_reservados:
        print("No existen asientos reservados")
    else:
        print (asiento_reservados)



    





        
