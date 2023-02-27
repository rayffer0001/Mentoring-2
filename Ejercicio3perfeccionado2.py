#ejercicio3 perfeccionado
import sys

num = input('Ingresa un numero entero aleatorio: ')
is_string = True



suma = 0
promedio = 0.0
min = 0
max = 0
cont = 0


while num != 0:
    
    
    while is_string:
        
        
        if num.isdigit():
            num = int(num)
            is_string = False
            if min == 0 and max == 0:
                min = num
                max = num
                
            
        else:
            
            print('ingresa solo numeros enteros')
            is_string = True
            num = input('Ingresa un numero entero aleatorio: ')
            continue
    
        
    cont += 1
    if num !=0:
        suma = suma + num
        promedio = suma / cont
        if num < min:
            min = num
        if num > max:
            max = num
        num = input('Ingresa un numero entero aleatorio: ')
        
        if ~(num.isdigit()):
            is_string = True
        else:
            num = int(num)
            
        
        
        
        
print(f'ingresastes {cont} numeros, la suma de los numeros es {suma}')
print(f'el promedio es {promedio}')
print(f'el numero minimo ingresado es {min}')
print(f'el numero mayor ingresado es {max}')

