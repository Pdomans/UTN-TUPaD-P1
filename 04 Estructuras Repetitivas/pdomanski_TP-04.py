#1
for i in range(101):
    print(i)

#2
numero = input("Ingresa un número entero: ")
print("Cantidad de dígitos:", len(numero.strip()))

#4
total = 0
band=1

while band == 1 :
    n = int(input("Ingresa un número : "))        
    total += n
    print("Suma total:", total)
    band=int(input("ingrese 1 si quiere seguir"))

#5
import random

x= random.randint(0, 9)
intentos = 0
band = True 
while band:
    intento = int(input("Adivina el número (entre 0 y 9): "))
    intentos += 1
    if intento == x :
        print(f"¡Correcto! Lo adivinaste en {intentos} intentos.")
        band= False
#6
for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)

#7
#reveer

#8
cantidad = 3 
pares = impares = positivos = negativos = 0

for i in range(cantidad):
    n = int(input(f"Ingrese el número {i+1}: "))
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1
    if n > 0:
        positivos += 1
    elif n < 0:
        negativos = negativos + 1

print("Pares:", pares)
print("Impares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)

#9
cantidad = 100  
suma = 0

for i in range(cantidad):
    n = int(input(f"Ingrese el número {i+1}: "))
    suma += n

media = suma / cantidad
print("La media es:", media)