#---------------Recursividad------------
#Mesas Ramiro
# Ejercicio 1
print("==== Ejercicio 1 ====")
numIngresado :str = validar_numero("Ingrese un valor para realizar un factorial: ")

print("==== Factoriales ====")
for i in range(numIngresado): 
    print(f"Factorial del numero {i + 1} = {factorial(i + 1)}")

# Ejercicio 2
print("==== Ejercicio 2 ====")
# Pedir al usuario una posición
pos = validar_numero("Ingresa la posición hasta donde quieres ver la serie: ")

print("==== Serie de Fibonacci ====")
for i in range(pos + 1):
    print(f"F({i}) = {fibonacci(i)}")

# Ejercicio 3
print("==== Ejercicio 3 ====")

b = validar_numero("Ingresa la base: ")
e = validar_numero("Ingresa el exponente: ")

print("==== Potencia ====")
print(f"{b} ^ {e} = {potencia(b, e)}")

# Ejercicio 4 
print("==== Ejercicio 4 ====")

num = validar_numero("Ingrese un numero decimal: ")
print(f"El número {num} en binario es {decimal_a_binario(num)}")

# Ejercicio 5
print("==== Ejercicio 5 ====")
palabra = input("Ingrese una palabra: ")

if es_palindromo(palabra):
    print("Es palíndromo")
else:
    print("No es palíndromo")

# Ejercicio 6
print("==== Ejercicio 6 ====")
num = validar_numero("Ingrese un numero decimal: ")
print("==== Suma de los digitos ====")
print(suma_digitos(num))

# Ejercicio 7 
print("==== Ejercicio 7 ====")
num = validar_numero("Ingrese un numero de bloques: ")

print("==== Numero de bloques que se necesitaron ====")
print(contar_bloques(num))

# Ejercicio 8
print("==== Ejercicio 7 ====")
num = validar_numero("Ingrese un numero: ")
dig = validar_digito("Ingrese un digito: ")

print(contar_digito(num, dig))