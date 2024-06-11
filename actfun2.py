# def total_factura(valor_neto):
#     valor_total=valor_neto*1.19
#     return valor_total
# valorneto=int(input("ingrese valor:\n"))
# print(f"el valor total es de {total_factura(valorneto)}")

# def area_circulo(radio):
#     aTotal=3.14*radio**2
#     return aTotal
# radio1=int(input("ingreses radio para calcular el area del circulo:\n"))
# print (f"{area_circulo(radio1)}")


# def media_numeros(numeros):
#     if len(numeros)==0:
#       cant = int(input("ingresar cantidad de numeros:\n"))  
#     for i in range(cant):
#         numero=int(input(f"ingresar numero {i+1}:\n"))
#         numeros.append(numero)

#     suma = sum(numeros)
#     cantidad = len(numeros)
#     media = suma/cantidad
#     return media
# numero=[]
# print (f"la media es {media_numeros(numero)}")

# def cuadrado_numeros(numeros,list_cuadrado):
#     if len(numeros)==0:
#         cant = int(input("ingresar cantidad de numeros:\n"))  
#     for i in range(cant):
#         numero=int(input(f"ingresar numero {i+1}:\n"))
#         numeros.append(numero)
#         list_cuadrado.append(numero**2)
#     return numeros, list_cuadrado
# numero=[]
# lista_cuadrados=[]
# numero, lista_cuadrados=cuadrado_numeros(numero, lista_cuadrados)
# print(f"{numero}\n{lista_cuadrados}")

def cant_palabras(palabras):
    cant = int(input("ingresar cantidad de numeros:\n"))
    for i in range(cant):
        palabra = input("ingresar palabra:\n").strip()
        palabras.append(palabra)
    return palabras, cant

palabra=[]
print(cant_palabras(palabra))




