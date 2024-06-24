import os, random
os.system("cls")
lista_estudiantes=[]

def menu_principal():
    os.system("cls")
    print("1.Registrar estudiante:\n2.Buscar estudiante:\n3.Imprimir certificados:\n4.Salir")

def id_alumno(contador_ids):
    os.system("cls")
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
    os.system("cls")
    nombre=input("Ingresar nombre:\n")
    while len(nombre) < 5:
        nombre=input("Ingresar nombre debe contener minimo 5 caracteres:\n")
    return nombre

def val_edad():
    os.system("cls")
    while True:
        try:
            os.system("cls")
            edad = int(input("Ingresar edad:\n"))
            while edad is not None:
                if edad < 11 or edad > 17:
                    os.system("cls")
                    edad = int(input("Ingresar edad minima 12 maxima 17:\n"))
                else:
                    return edad
        except:
            os.system("cls")
            print("Ingresar edad valida")
            input("enter para continuar")

def reg_estudiantes():
    os.system("cls")
    contador_ids=1
    while True:
        id_estudiante = id_alumno(contador_ids)
        contador_ids+=1
        nombre = val_nombre()
        edad = val_edad ()
        dato_estudiante=[id_estudiante,nombre, edad]
        lista_estudiantes.append(dato_estudiante)
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

def buscar_estudiante():
    os.system("cls")
    num_id=None
    id_buscar=None
    flagID=True
    if not lista_estudiantes:
        print("Lista de estudiantes vacia...Crear registro de datos.")
        input("Presiona Enter para continuar...")
        return
    curso_buscar=input("Nivel a buscar Media o Basica:\n")
    while curso_buscar != "media" and curso_buscar != "basica":
       curso_buscar=input("Nivel a buscar Media o Basica:\n")
    if curso_buscar == "media":
        curso_buscar="AM"
        curso_nom="Enseñanza Media"
    elif curso_buscar=="basica":
        curso_buscar="AB"
        curso_nom="Enseñanza Basica"
    try:
        num_id=int(input("Ingresar numero de id:\n"))
        id_buscar=str(num_id).zfill(2)+"|"+curso_buscar
        for dato_estudiante in lista_estudiantes:
            if id_buscar == dato_estudiante[0]:
                print(f"Nombre: {dato_estudiante[1]}\nEdad: {dato_estudiante[2]}\nCurso: {curso_nom}")
                input("Enter para continuar")
                estudiante_encontrado = True
                break
        if not estudiante_encontrado:
            print("estudiante no existente")
            input("Enter para continuar")             
    except:
        print("Error de ingreso")
        input("Enter para continuar")

def certificado_asistencia():
    os.system("cls")
    num_id=None
    id_buscar=None
    flagID=True
    if not lista_estudiantes:
        print("Lista de estudiantes vacia...Crear registro de datos.")
        input("Presiona Enter para continuar...")
        return
    curso_buscar=input("Nivel a buscar Media o Basica:\n")
    while curso_buscar != "media" and curso_buscar != "basica":
       curso_buscar=input("Nivel a buscar Media o Basica:\n")
    if curso_buscar == "media":
        curso_buscar="AM"
        curso_nom="Enseñanza Media"
    elif curso_buscar=="basica":
        curso_buscar="AB"
        curso_nom="Enseñanza Basica"
    try:
        num_id=int(input("Ingresar numero de id:\n"))
        id_buscar=str(num_id).zfill(2)+"|"+curso_buscar
        for dato_estudiante in lista_estudiantes:
            if id_buscar == dato_estudiante[0]:
                asistencia=random.randint(1,100)
                os.system("cls")
                print(f"ID: {dato_estudiante[0]}\nNombre: {dato_estudiante[1]}\nEdad: {dato_estudiante[2]}\nCurso: {curso_nom}\nAsistencia: {asistencia}%")
                input("Enter para continuar")
                estudiante_encontrado = True
                break
        if not estudiante_encontrado:
            print("estudiante no existente")
            input("Enter para continuar")             
    except: 
        print("Error de ingreso")
        input("Enter para continuar")  
        os.system("cls")

def certificado_notas():
    os.system("cls")
    num_id=None
    id_buscar=None
    flagID=True
    if not lista_estudiantes:
        print("Lista de estudiantes vacia...Crear registro de datos.")
        input("Presiona Enter para continuar...")
        return
    curso_buscar=input("Nivel a buscar Media o Basica:\n")
    while curso_buscar != "media" and curso_buscar != "basica":
       curso_buscar=input("Nivel a buscar Media o Basica:\n")
    if curso_buscar == "media":
        curso_buscar="AM"
        curso_nom="Enseñanza Media"
    elif curso_buscar=="basica":
        curso_buscar="AB"
        curso_nom="Enseñanza Basica"
    try:
        num_id=int(input("Ingresar numero de id:\n"))
        id_buscar=str(num_id).zfill(2)+"|"+curso_buscar
        notas=[]
        for dato_estudiante in lista_estudiantes:
            if id_buscar == dato_estudiante[0]:
                for x in range(5):
                    while True:
                        try:
                            nota=float(input(f"Ingresar nota {x+1}\n"))
                            if 1.0 <= nota <= 7.0:
                                notas.append(nota)
                                break
                            else:
                                print("Nota fuera de rango ")
                        except:
                            print("Valor invalido")
                            input("Enter para continuar")
                promedio=round(sum(notas)/x,1)
                os.system("cls")
                print(f"ID: {dato_estudiante[0]}\nNombre: {dato_estudiante[1]}\nEdad: {dato_estudiante[2]}\nCurso: {curso_nom}\nNotas: {notas}\nPromedio: {promedio}")
                input("Enter para continuar")
                estudiante_encontrado = True
                break
        if not estudiante_encontrado:
            print("estudiante no existente")
            input("Enter para continuar")             
    except: 
        print("Error de ingreso")
        input("Enter para continuar")  
        os.system("cls")

def certificado_conducta():
    os.system("cls")
    num_id=None
    id_buscar=None
    if not lista_estudiantes:
        print("Lista de estudiantes vacia...Crear registro de datos.")
        input("Presiona Enter para continuar...")
        return
    curso_buscar=input("Nivel a buscar Media o Basica:\n")
    while curso_buscar != "media" and curso_buscar != "basica":
       curso_buscar=input("Nivel a buscar Media o Basica:\n")
    if curso_buscar == "media":
        curso_buscar="AM"
        curso_nom="Enseñanza Media"
    elif curso_buscar=="basica":
        curso_buscar="AB"
        curso_nom="Enseñanza Basica"
    try:
        num_id=int(input("Ingresar numero de id:\n"))
        id_buscar=str(num_id).zfill(2)+"|"+curso_buscar
        for dato_estudiante in lista_estudiantes:
            if id_buscar == dato_estudiante[0]:
                conducta_nivel=random.randint(1,3)
                if conducta_nivel==1:
                    conducta="A"
                elif conducta_nivel==2:
                    conducta="B"
                elif conducta_nivel==3:
                    conducta="C"
                print(f"Nombre: {dato_estudiante[1]}\nEdad: {dato_estudiante[2]}\nCurso: {curso_nom}\nConducta: {conducta}")
                input("Enter para continuar")
                estudiante_encontrado = True
                break
        if not estudiante_encontrado:
            print("estudiante no existente")
            input("Enter para continuar")             
    except:
        print("Error de ingreso")
        input("Enter para continuar")

def menu_certificados():
    os.system("cls")
    flag_menuc=True
    while flag_menuc:
        os.system("cls")
        print("1.Certificado de asistencia:\n2.Certificado de notas:\n3.Certificado de conducta:\n4.Salir")
        try:
            opcion_certificado=int(input("Ingresar opcion:\n"))
            if opcion_certificado==1:
                os.system("cls")
                print("Imprimir certificado de asistencia")
                certificado_asistencia()
            elif opcion_certificado==2:
                os.system("cls")
                certificado_notas()
            elif opcion_certificado==3:
                os.system("cls")
                certificado_conducta()
            elif opcion_certificado==4:
                os.system("cls")
                print("Saliendo...")
                flag_menuc=False
                input("Enter para continuar")
        except:
            input("Enter para continuar")