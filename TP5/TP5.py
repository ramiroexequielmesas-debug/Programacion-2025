#tp- listas

#ejercicio 1
lista= []
for i in range(1,101):
    if i %4==0:
        lista.append(i)
print(lista)

#ejercicio 2
mi_lista=["me","encanta","ir al","GYM"," :)"]
penultima=mi_lista[-2]
print(penultima)

#ejercicio 3
lista_vacia=[]
for i in range(3):
    palabra:str=input(f"Ingrese {i+1} palabra : ")
    palabra=palabra.upper()
    lista_vacia.append(str(palabra))
print(f"La lista creada contiene {lista_vacia}")

#ejercicio 4
animales=["perro", "gato", "conejo", "pez"]
animales[1]="loro"
animales[3]="oso"
print(animales)

#ejercicio 5
#explicar lo que realiza el siguiente programa
numeros=[8,15,3,22,7] #arma una lista con los siguientes numeros
numeros.remove(max(numeros)) #con la funcion remove y max remueve el valor maximo de la lista
print(numeros)# y aqui imprime la lista sin el valor mas grande

#ejercicio 6
lista= list(range(10,31,5))
print(lista[:2])

#ejercicio 7
autos = ["sedan", "polo", "suran", "gol"]
autos[1]="mercedes"
autos[2]="audi"
print(autos)

#ejercicio 8
dobles=[]
valores=[5,10,15]

for valor in valores:
    dobles.append(valor*2)
print(dobles)

#ejercicio 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
compras[2].append("jugo")
compras[1][1]="tallarines"
compras[0].remove("pan")
print(compras)

#ejercicio 10
lista_anidada=[[15],[True],[25.5, 57.9, 30.6],[False]]
print(lista_anidada)
