import os
os.system ("cls")

# def suma (num1,num2):
#     resultado=num1+num2
#     return resultado

# a=int(input("numero1:\n"))
# b=int(input("numero2:\n"))
# print (f"el total{suma(a,b)}")

# def es_par(a):
#     flag=False
#     if a%2==0:
#         flag=True
#     return flag

# numero=int(input("numero1:\n"))
# print(es_par(numero))

# def celsius_fahrenheit(celsius):
#     formula= (celsius*9/5)+32
#     return formula

# temperatura=int(input("ingrese temp a transformar:\n"))
# print(f"la temp en fahrenheit es {celsius_fahrenheit(temperatura)} ")

# def max_de_tres(a,b,c):
#     numeros= a,b,c
#     numero_mayor=0
#     for i in numeros:
#         if i>numero_mayor:
#             numero_mayor=i
#     return numero_mayor


# num1=int(input("ingresar num1:\n"))
# num2=int(input("ingresar num2:\n"))
# num3=int(input("ingresar num3:\n"))
# numero_grande=max_de_tres(num1,num2,num3)
# print(f"el numero mas grande entre {num1}, {num2}, {num3} es: {numero_grande}")

def validar_nombre(nombre):
    while nombre=="" or nombre==" ":
        nombre=input("el campo del nombre no puede venir vacio.\n Ingresar nombre:\n")
    return nombre

nombre=input("ingresar nombre:\n")
validar_nombre(nombre)
