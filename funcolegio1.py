import os
os.system("cls")
lista_estudiantes=[]
def menu_principal():
    print("1.Registrar estudiante:\n2.Buscar estudiante:\n3.Imprimir certificados:\n4.Salir")
    
def id_alumno(contador_ids):
    curso_estudiante=input("Nivel a ingresar Media o Basica:\n")
    while curso_estudiante != "media" and curso_estudiante != "basica":
       curso_estudiante=input("Nivel a ingresar Media o Basica:\n")
    if curso_estudiante == "media":
        curso_estudiante="AM"
    elif curso_estudiante=="basica":
        curso_estudiante="AB"
    id_estudiante=str(contador_ids).zfill(2)+"|"+curso_estudiante
    contador_ids+=1
    return id_estudiante
    
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
    contador_ids=1
    while True:
        id_estudiante = id_alumno(contador_ids)
        contador_ids+=1
        nombre = val_nombre()
        edad = val_edad ()
        dato_estudiante=[id_estudiante,nombre, edad]
        lista_estudiantes.append(dato_estudiante)
        print(dato_estudiante)
        print (lista_estudiantes)
        input("Enter para continuar")
        try:
            opcion_reg=int(input("Agregar otro estudiante? 1.Si 2.No:\n"))
            if opcion_reg==1:
                continue
            else:
                break
        except:
            print("Ingresar opcion valida")
            input("Enter para continuar")
    return dato_estudiante

def buscar_estudiante(dato_estudiante):
    id_buscar=input("Ingresar id a buscar:\n")
    for dato_estudiante in lista_estudiantes:
        if id_buscar == dato_estudiante[0]:
            print(f"Estudiante encontrado\nID: {dato_estudiante[0]}\nNombre: {dato_estudiante[1]}\nEdad: {dato_estudiante[2]}")
            input("Enter para continuar")
        else:
            print("Estudiante no encontrado")
            input("Enter para continuar")
    return
            