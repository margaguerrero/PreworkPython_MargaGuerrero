"""Funciones
1. Ejercicio: Define una función que tome dos números y retorne su suma."""

a = 5
b = 3
def total(a,b):
  return (a + b)
print(total(a,b))

"""2. Ejercicio: Define una función que tome un número y retorne su factorial."""
x = 7
def factorial (x):
  if x == 0:
    return 1
  else:
    return x * factorial (x-1)
print(factorial(x))

"""3. Ejercicio: Define una función que tome un número y determine si es primo."""
n = 10
def primo (n):
  if n < 2:
    return "No es primo"
  for i in range (2, n):
    if n % i == 0:
      return "No es primo"
  return "Es primo"
print (primo(n))

"""4. Ejercicio: Define una función que reciba una lista de números y retorne la suma de ellos."""
lista = [4,5,7,8,22,45,78]
def suma_lista (numeros):
  suma = 0
  for numero in numeros:
    suma += numero
  return suma
print (suma_lista(lista))

"""5. Ejercicio: Define una función que reciba una cadena de texto y retorne la cadena en reversa."""
cadena = "hello"
cadena_inversa = cadena[::-1]
print (cadena_inversa)


