#fun analisis
import os, random, csv
from statistics import geometric_mean
lista_productos=["Televisor","Lavadora","Refrigerador","Microondas","Computadora","Celular","Impresora","Cafetera","Licuadora","Ventilador"]
precios=[]
precios_prod=[]
lista_imprimir=[]

def limpiar_pantalla():
    os.system("cls")

def asignar_precio():
    limpiar_pantalla()
    if not precios:   
        for producto in lista_productos:
            precio=random.randint(300000,2500000)
            precios.append((producto,precio))
            precios_prod.append(precio)
        print(precios)
        input("Enter para continuar...")  
    else:
        print("Precios ya creados")
        print(precios)
        input("Enter para continuar...")  
        return

def clasificar_precio():
    limpiar_pantalla()
    men800=[]
    may2m=[]
    entre8ky2m=[]
    if not precios:
        print("No existen precios en los productos")
        input("Enter para continuar...")          
        return
    for producto in precios:
        if producto[1]<800000:
            men800.append(producto) 
        elif producto[1]>2000000:
            may2m.append(producto)
        else:
            entre8ky2m.append(producto)
    print(f"Productos menores a 800.000 {men800}\nProductos entre 800.000 y 2.000.000 {entre8ky2m}\nProductos mayores a 2.000.000 {may2m}")
    input("Enter para continuar...")  

def ver_estadistica():
    limpiar_pantalla()
    if not precios:
        print("No existen precios en los productos")
        input("Enter para continuar...")          
        return
    promedio=sum(precios_prod)/len(precios_prod)
    print("Precio mayor ",max(precios))
    print("Precio menor ",min(precios))
    print("Promedio de precios ",promedio)
    print("Media geometrica ",geometric_mean(precios_prod))
    input("Enter para continuar...")  

def reporte_precios():
    limpiar_pantalla()
    dscto10=[]
    dscto5=[]
    if not precios:
        print("No existen precios en los productos")
        input("Enter para continuar...")          
        return
    i=0
    for producto in precios:
        dcto10=round(producto[1]*0.9,1)
        dcto5=round(producto[1]*0.95,1)
        dscto10.append((dcto10))
        dscto5.append((dcto5))
        pfinal=round(producto[1]-(producto[1]*0.05)-(producto[1]*0.1),1)
        lista_imprimir.append((lista_productos[i], precios_prod[i], dcto5, dcto10, pfinal))
        i+=1
    with open ('reporte_de_precios.csv', mode='w',newline='')as file:
        writer = csv.writer(file)
        writer.writerow(["PRODUCTO", "PRECIO", "DESCUENTOMEMBRESIA", "DESCUENTOPROMOCION", "PRECIOFINAL"])
        for producto_imprimir in lista_imprimir:
            writer.writerow(producto_imprimir)
            print (producto_imprimir)
                
    print(lista_imprimir)
    print(dscto10)
    print(dscto5)
    input("Enter para continuar...")