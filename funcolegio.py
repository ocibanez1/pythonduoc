import os
os.system("cls")
lista_estudiantes=[]

x=0
def menu_principal():
    print("1.Registrar estudiante:\n2.Buscar estudiante:\n3.Imprimir certificados:\n4.Salir")
    
def id_alumno():
    curso_estudiante=input("Nivel a ingresar Media o Basica:\n")
    while curso_estudiante != "media" and curso_estudiante != "basica":
       curso_estudiante=input("Nivel a ingresar Media o Basica:\n")
    if curso_estudiante == "media":
        curso_estudiante="AM"
    elif curso_estudiante=="basica":
        curso_estudiante="AB"
    for x in range(2):
        x+=1
        id=str(x).zfill(2)+"|"+curso_estudiante
    lista_estudiantes.append(id)
    return id
    
def val_nombre():
    nombre=input("Ingresar nombre:\n")
    while len(nombre) < 5:
        nombre=input("Ingresar nombre debe contener minimo 5 caracteres:\n")
    return nombre

def val_edad():
    try:
        edad = int(input("Ingresar edad:\n"))
        while edad > 17 or edad < 11:   
            edad = int(input("Ingresar edad debe estar entre el rango de edad 12 y 18:\n"))
    except:
        print("Ingresar edad valida")
        input("enter para continuar")
    return edad

def reg_estudiantes():
    while True:
        nombre = val_nombre()
        edad = val_edad ()
        id = id_alumno()
        dato_estudiante=[nombre, edad, id]
        lista_estudiantes.append(dato_estudiante)
        try:
            opcion_reg=int(input("Agregar otro estudiante? 1.Si 2.No:\n"))
            if opcion_reg==1:
                continue
            else:
                break
        except:
            print("Ingresar opcion valida")
            input("Enter para continuar")
            