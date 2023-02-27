##ejercicio 3 

"""Algoritmo que lea números enteros hasta teclear 0, y nos muestre el máximo, 
el mínimo y la media de todos ellos. Piensa como debemos inicializar las variables."""

x = 1 # 5
suma = 0 
contador = 0
min = 999999999999999999999999999999999999999999999999999999999999  # 5 (2) (1)
max = 0  # 5 

while x != 0:
    x = int(input('ingrese un numero: ')) # (5) (2) (1) (6)
   
    if x != 0:
        suma = suma + x # 0 + 5  (2 + 5) (7 + 1) (8 + 6)
        print(suma) # 5 (7) (8) (14)
        contador = contador + 1 # 1 (2) (3) (4)
        print(contador) # 1 (2) (3) (4)

        if max == x: 
            print('ambos numeros son iguales, no hay maximo')
            if x < max:
                print(f'{max} es el valor maximo')
        
        if max < x:
            max = x
            print(f'{max} es el numero maximo')


        if min == x:
            print('ambos numeros son iguales, no hay minimo')
            if x > min: # x = 2 > 5
                print(f'{min} es el valor minimo') 
        
        if  x < min: 
            print(f'{x} es el valor minimo')
            min = x # 2 # 1    

else:
    x == 0
    print('Has parado el programa al presionar 0')

print(f'suma es {suma}')
if contador > 0:
    promedio = suma / contador
    print(f'promedio es {promedio}') 
    print(f'numero minimo es {min} y numero maximo es {max}')   

 
print(x)