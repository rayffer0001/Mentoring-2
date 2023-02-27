#ejercicio3 perfeccionado

num = 9
suma = 0
promedio = 0.0
min = 99999999999
max = 0
cont = 0

while num != 0:
    num = input('Ingresa un numero entero aleatorio: ')
    
    if num.isdigit():
        num = int(num)
        
    else:
        print('ingresa solo numeros enteros')
        continue
        
    cont += 1
    if num !=0:
        suma = suma + num
        promedio = suma / cont
        if num < min:
            min = num
        if num > max:
            max = num
        
print(f'ingresastes {cont} numeros, la suma de los numeros es {suma}')
print(f'el promedio es {promedio}')
print(f'el numero minimo ingresado es {min}')
print(f'el numero mayor ingresado es {max}')
