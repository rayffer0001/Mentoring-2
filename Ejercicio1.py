#ejercicio 1
"""Algoritmo que lea dos números, calculando y escribiendo el valor de su suma, resta, producto y división."""


x = int(input('Ingrese un primer número: '))
y = int(input('Ingrese un segundo número: '))
suma = x + y
resta = x - y
multiplicacion = x * y
if y != 0:
    division = x / y
else:
    division = "¨No se puede dividir por 0¨"

print(f'la suma de los numero ingresados es:  {suma}')
print(f'la resta de los numero ingresados es:  {resta}')
print(f'la multiplicacion de los numero ingresados es:  {multiplicacion}')
print(f'la division de los numero ingresados es:  {division}')