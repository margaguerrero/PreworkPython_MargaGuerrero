"""Bucles y Funciones
1. Ejercicio: Define una función que utilice un bucle para imprimir los primeros n números de la serie de Fibonacci."""
print("Ejercicio 1:")
n = 10
def Fibonacci(n):
  if n < 2:
    return n
  else:
    return Fibonacci(n-1)+Fibonacci(n-2)
for x in range(n):
  print (Fibonacci(x))


"""2. Ejercicio: Define una función que tome un número y retorne una lista de sus divisores."""
x = 10
def divisores (x):
  return [i for i in range (1,x) if x % i ==0]
print (f"Ejercicio 2: Los divisores de {x} son{divisores(x)}")


"""3. Ejercicio: Define una función que tome una lista y retorne una nueva lista con los elementos únicos de la lista original."""
lista = [2,2,5,6,8,9,5,1,6]
lista_unicos = list(set(lista))
print(f"Ejercicio 3 :{lista_unicos}")


"""4. Ejercicio: Define una función que tome un número y retorne la suma de sus dígitos."""
a = 157
suma = 0
while a > 0:
  suma = suma + (a % 10)
  a = a // 10
print(f"Ejercicio 4: {suma}")


"""5. Ejercicio: Define una función que tome una cadena y cuente el número de vocales en la cadena."""
cadena = "¿Como te encuentras?"
def cuenta_vocales (cadena):
  conteo = 0
  for letra in cadena:
    if letra.lower() in "aeiou":
      conteo += 1
  return conteo
print (f"Ejercicio 5: En la cadena hay {cuenta_vocales(cadena)} vocales") 


"""6. Ejercicio: Define una función que tome una lista y un número n, y retorne los primeros n elementos de la lista."""
lista = [2,4,6,8,10,12,14,16,18,20]
n = 3
def primeros_n_numeros (lista, n):
  return lista [:n]
print (f"Ejercicio 6: {primeros_n_numeros(lista,n)}")


"""7. Ejercicio: Define una función que tome una cadena y retorne la cantidad de letras mayúsculas y minúsculas en la cadena."""
cadena = "Hola, ComO tE encUentrAS?"
def suma_mayusculas_minusculas (cadena):
  mayusculas = sum(1 for letra in cadena if letra.isupper())
  minusculas = sum(1 for letra in cadena if letra.islower())
  return (f"Ejercicio 7: Hay {mayusculas} mayúsculas, y {minusculas} minúsculas")
print(suma_mayusculas_minusculas(cadena))


"""8. Ejercicio: Define una función que tome un número y retorne True si es un número perfecto, False en caso contrario. Un número perfecto es aquel que es igual a la suma de sus divisores propios positivos. Por ejemplo, 6 es un número perfecto porque sus divisores son 1, 2 y 3, y 6 = 1 + 2 + 3."""
x = 28

def divisores (x):
  if x == sum([i for i in range (1,x) if x % i ==0]):
    return True 
  else:
    return False
print(f"Ejercicio 8: {divisores(x)}")


"""9. Ejercicio: Define una función que reciba un número y retorne su representación en binario."""
x = 28

def binario (x):
  binario = ""
  while x > 0:
    residuo = int(x % 2)
    x = int(x / 2)
    binario = str(residuo) + binario
  return binario
print(f"Ejercicio 9: El número {x} es {binario (x)} en binario")


"""10. Ejercicio: Define una función que reciba dos listas y retorne la intersección de ambas (los elementos que están en las dos listas)."""
lista1 = [1,3,5,7,6,8,9,2]
lista2 = [2,4,6,8,10]


def elementos_repetidos(lista1,lista2):
  return [a for a in lista1 for b in lista2 if a == b]
print (f"Ejercicio 10: {elementos_repetidos(lista1, lista2)}")


"""11. Ejercicio: Define una función que tome una cadena y determine si es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda)."""
palabra = "radar"
def es_palindromo (palabra):
  if palabra == palabra [::-1]:
    return (f"La palabra {palabra} es un palíndromo")
  else:
    return (f"La palabra {palabra} no es un palíndromo")
print (f"Ejercicio 11: {es_palindromo(palabra)}")


"""12. Ejercicio: Escribe un programa que imprima los números del 1 al 50, pero para múltiplos de tres imprima “Fizz” en lugar del número y para los múltiplos de cinco imprima “Buzz”. Para números que son múltiplos de tanto tres como cinco imprima “FizzBuzz”."""
print("Ejercicio 12:")
for i in range (1,51):
  if (i % 3 == 0) and (i % 5 ==0):
    print ("FizzBuzz", end=", ")
  elif i % 3 == 0:
    print ("Fizz", end=", ")
  elif i % 5 == 0:
    print ("Buzz", end=", ")
  else:
    print (i, end=", ") 


"""13. Ejercicio: Define una función que tome una lista y retorne la lista ordenada en orden ascendente."""
print("\n")
lista = [35,5,25,15,30,20,10,]
def lista_ordenada (lista):
  return sorted (lista)
print (f"Ejercicio 13: {lista_ordenada(lista)}")


"""14. Ejercicio: Define una función que reciba una lista de palabras y un entero n, y retorne la lista de palabras que son más largas que n."""
palabras = ["casas", "arbol", "coches", "autobús", "sol", "estrella"]
n = 5
def palabras_mas_largas(palabras, n):
  return [palabra for palabra in palabras if len(palabra) > n]
print (f"Ejercicio 14: {palabras_mas_largas(palabras, n)}")


"""15. Ejercicio: Define una función que tome un número y calcule su serie de Fibonacci."""
x = 10
def serie_Fibonacci(x):
  if x <= 0:
    return []
  elif x == 1:
    return [0]
  fib = [0, 1]
  while len(fib) < x:
    fib.append (fib[-1]+fib [-2])
  return (fib)
print(f"Ejercicio 15: {serie_Fibonacci(x)}")


"""16. Ejercicio: Define una función que tome una lista de números y retorne el número más grande de la lista."""
lista = [5,8,2,4,9]
def numero_mayor (lista):
  return max(lista)
print (f"Ejercicio 16: El número más grande es el {numero_mayor(lista)}")


"""17. Ejercicio: Define una función que reciba un número y retorne la suma de sus dígitos al cubo."""
x = 123
def suma_digitos_cubo(x):
  return sum(int(digit)**3 for digit in str(x))
print (f"Ejercicio 17: La suma de los dígitos al cubo de {x} es {suma_digitos_cubo(x)}")


"""18. Ejercicio: Define una función que reciba una lista de números y retorne el segundo número más grande de la lista."""
lista = [1,3,5,7,9]
def segundo_mas_grande (lista):
  return sorted (set(lista), reverse = True)[1]
print (f"Ejercicio 18: El segundo número más grande es {segundo_mas_grande(lista)}")
  

"""19. Ejercicio: Define una función que tome dos listas y retorne True si tienen al menos un miembro en común, de lo contrario, retorne False."""
lista1 = [1,3,5,7,9]
lista2 = [2,3,4,6,8]

def comun_listas (lista1, lista2):
  return bool (set(lista1)&set(lista2))
print (f"Ejercicio 19: {comun_listas(lista1, lista2)}")


"""20. Ejercicio: Define una función que tome una lista y retorne una nueva lista con los elementos de la lista original en orden inverso."""
lista = [1,2,3,4,5]

def lista_inversa(lista):
  return lista[::-1]
print(f"Ejercicio 20: La lista en orden inverso es {lista_inversa(lista)}")


"""21. Ejercicio: Define una función que reciba una cadena y cuente el número de dígitos y letras que contiene."""
cadena = "Feliz 18 cumpleaños"

def digitos_letras(cadena):
  digitos = 0
  letras = 0
  for c in cadena:
    if c.isdigit():
      digitos +=1
    elif c.isalpha():
      letras +=1
    else:
      pass
  return digitos, letras
print(f"Ejercicio 21:{digitos_letras(cadena)}")


"""22. Ejercicio: Define una función que reciba una lista de números y retorne la suma acumulada de los números"""
lista = [1,2,3,4,5]

def suma_acumulada (lista):
  total = 0
  suma_acumulada = []
  for numero in lista:
    total += numero
    suma_acumulada.append(total)
  return suma_acumulada
print (f"Ejercicio 22: {suma_acumulada(lista)}")


"""23. Ejercicio: Define una función que encuentre el elemento más común en una lista."""
lista = [1,2,3,4,5,5,3,1,5]
from collections import Counter
def mas_comun (lista):
  return Counter(lista).most_common(1)[0][0]
print (f"Ejercicio 23: El elemento más repetido es el {mas_comun(lista)}")


"""24. Ejercicio: Define una función que tome un número y retorne un diccionario con la tabla de multiplicar de ese número del 1 al 10."""
numero = 5

def tabla_multiplicar (numero):
  return {i:numero * i for i in range (1,11)}
print(f"Ejercicio 24: {tabla_multiplicar(numero)}")

"""25. Ejercicio: Define una función que tome una cadena y retorne un diccionario con la cantidad de apariciones de cada caracter en la cadena."""

print ("Ejercicio 25: ???")

"""26. Ejercicio: Define una función que tome dos listas y retorne la lista de elementos que no están en ambas listas."""
lista1= [1,3,5,7,9]
lista2 =[1,2,3,4,5,6,7,9]

def elementos_diferentes(lista1, lista2):
  return (set (lista1) ^ set(lista2))
print(f"Ejercicio 26: Los elementos que no están en ambas listas son {elementos_diferentes(lista1, lista2)}")


"""27. Ejercicio: Define una función que tome una lista y retorne la lista sin duplicados."""
lista = [1,2,4,6,8,10,2,4,10]

def lista_unicos(lista):
  return(set(lista))
print (f"Ejercicio 27: La lista sin duplicados es: {lista_unicos(lista)}") 


"""28. Ejercicio: Define una función que reciba un número entero positivo y retorne la suma de los cuadrados de todos los números pares menores o iguales a ese número."""
x = 10
def suma_cuadrados_pares (x):
  return sum(pow(i,2) for i in range (1,x) if i%2 == 0)
print (f"Ejercicio 28: La suma de los cuadrados de los números pares inferiores a {x} es {suma_cuadrados_pares(x)}" )


"""29. Ejercicio: Define una función que reciba una lista de números y retorne el promedio de los números en la lista."""
lista = [1,2,3,4,5]

def promedio (lista):
  return sum(lista)/len(lista)
print (f"Ejercicio 29: El promedio de la lista {lista} es {promedio (lista)}")

"""30. Ejercicio: Define una función que reciba una lista de cadenas y retorne la cadena más larga en la lista."""
lista = ["pato", "canguro", "delfin", "ave"]

def cadena_larga(lista):
  return max (lista, key=len)
print (f"Ejercicio 30: La palabra más larga es {cadena_larga(lista)}")


"""31. Ejercicio: Define una función que reciba un número entero n y retorne una lista con los n primeros números primos."""
n = 10

def es_primo(n):
  if n < 2:
    return False
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return False
  return True
def primeros_n_primos(n):
  primos = []
  numero = 2
  while len(primos) < n:
    if es_primo(numero):
      primos.append(numero)
    numero += 1
  return primos
print(f"Ejercicio 31: Los primeros {n} números primos son {primeros_n_primos(n)}")


"""32. Ejercicio: Define una función que reciba una cadena y retorne la misma cadena pero con las palabras en orden inverso."""
lista = ["casa", "perro", "sol", "estrella"]

def lista_inversa (lista):
 return lista[::-1]
print (f"Ejercicio 32: {lista_inversa(lista)}")

"""33. Ejercicio: Escribe una función que reciba una lista de tuplas y retorne una lista ordenada basada en el último elemento de cada tupla."""
tuplas = [(3,5), (1,9), (9,4)]

def ordenar_ultimo_elemento (tuplas):
  return sorted(tuplas, key=lambda x: x[-1])
print (f"Ejercicio 33: {ordenar_ultimo_elemento(tuplas)}")

"""34. Ejercicio: Define una función que reciba una cadena y retorne la cantidad de letras vocales en la cadena."""
cadena = "¿Como te encuentras?"
def cuenta_vocales (cadena):
  conteo = 0
  for letra in cadena:
    if letra.lower() in "aeiou":
      conteo += 1
  return conteo
print (f"Ejercicio 34: En la cadena hay {cuenta_vocales(cadena)} vocales") 

"""35. Ejercicio: Define una función que reciba un número entero y retorne True si es un número primo, de lo contrario retorne False"""
n = 10
def primo (n):
  if n < 2:
    return False
  for i in range (2, n):
    if n % i == 0:
      return False 
  return True
print (f"Ejercicio 35: {primo(n)}")