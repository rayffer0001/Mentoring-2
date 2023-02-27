#ejercicio 2
"""Una tienda ofrece un descuento del 15% sobre el total de la compra durante el mes de octubre. 
Dado un mes y un importe, calcular cuál es la cantidad que se debe cobrar al cliente."""

mes = str(input('Ingrese el mes de compra: '))
valor = int(input('Ingrese el valor de la compra: '))
desc = valor * 0.15

if mes == 'octubre' or mes == 'Octubre' or mes == 'OCTUBRE':
    cobrar = valor - desc

else:
    cobrar = valor

print(f'Su valor a cobrar es: {cobrar}' )