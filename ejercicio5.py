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
lista2 = [2,3,4,6,8,9]

def comun_listas (lista1, lista2):
  repetido = [n for n in lista1 if n in lista2]
print (comun_listas(lista1, lista2))



"""20. Ejercicio: Define una función que tome una lista y retorne una nueva lista con los elementos de la lista original en orden inverso."""
"""21. Ejercicio: Define una función que reciba una cadena y cuente el número de dígitos y letras que contiene."""
"""22. Ejercicio: Define una función que reciba una lista de números y retorne la suma acumulada de los números"""
"""23. Ejercicio: Define una función que encuentre el elemento más común en una lista."""
"""24. Ejercicio: Define una función que tome un número y retorne un diccionario con la tabla de multiplicar de ese número del 1 al 10."""
"""25. Ejercicio: Define una función que tome una cadena y retorne un diccionario con la cantidad de apariciones de cada caracter en la cadena."""
"""26. Ejercicio: Define una función que tome dos listas y retorne la lista de elementos que no están en ambas listas."""
"""27. Ejercicio: Define una función que tome una lista y retorne la lista sin duplicados."""
"""28. Ejercicio: Define una función que reciba un número entero positivo y retorne la suma de los cuadrados de todos los números pares menores o iguales a ese número."""
"""29. Ejercicio: Define una función que reciba una lista de números y retorne el promedio de los números en la lista."""
"""30. Ejercicio: Define una función que reciba una lista de cadenas y retorne la cadena más larga en la lista."""
"""31. Ejercicio: Define una función que reciba un número entero n y retorne una lista con los n primeros números primos."""
"""32. Ejercicio: Define una función que reciba una cadena y retorne la misma cadena pero con las palabras en orden inverso."""
"""33. Ejercicio: Escribe una función que reciba una lista de tuplas y retorne una lista ordenada basada en el último elemento de cada tupla."""
"""34. Ejercicio: Define una función que reciba una cadena y retorne la cantidad de letras vocales en la cadena."""
"""35. Ejercicio: Define una función que reciba un número entero y retorne True si es un número primo, de lo contrario retorne False"""