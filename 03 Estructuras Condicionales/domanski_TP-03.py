""" 1) Escribir un programa que solicite la edad del usuario.
 Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”."""


edad=int(input("ingrese edad "))

if edad > 18 :
    print("es mayor edad")


    """ 2) Escribir un programa que solicite su nota al usuario.
      Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”."""
    
    nota=int(input("ingrese la nota "))

    if nota >= 6 : 
            print ("aprobado")
    else :
          print ("desaprobado")



"""3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par,
 imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". 
Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar."""


numero = int(input("ingrese un numero "));

if numero % 2 !=0 : 
      print (f"el {numero} es impar por favor ingrese un numero par")
else : 
      print (f"el {numero} es par ") 


"""
4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: ● Niño/a: menor de 12 años.
 ● Adolescente: mayor o igual que 12 años y menor que 18 años. ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. ● Adulto/a: mayor o igual que 30 años.
"""


edad2=int(input("ingrese su edad"))

if edad2 < 12  :
      print("niño")
elif edad2 >=12 and edad2 <18 :
      print("adolecenete")

elif edad2 >=18 and edad2 <30 :
      print ("adulto/joven")

elif edad2>=30 :
      print ("adulto")


""" 
5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada,
 imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor,
 ingrese una contraseña de entre 8 y 14 caracteres".
 Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.


"""
password=input("ingrese contraseña")


if len(password) >=8 and len(password) <=14 :
 print ("Ha ingresado una contraseña correcta")
else :
 print("ingrese una contraseña de entre 8 y 14 caracteres") 




#6

 from statistics import mode, median,mean
import random
lista=[random.randint(1,100)for i in range(50)]

print(lista)


#sesgo positivo a la derecha 
mediana=median(lista)
moda=mode(lista)
media=mean(lista)

print (f" la media es {mediana}, la moda es {moda}  y la media es {media}")

if mediana == moda  and moda == media :
    print ("sin sesgo")

elif media<mediana and media < moda : 
    print("sesgo negato o a la izquierda") 

elif media> mediana and  mediana > moda :
    print ("sego positivo a la derecha")




#7

palabra = input("Ingresa una frase o palabra: ")

# Verifica si el último carácter es una vocal (mayúscula o minúscula)
if palabra[-1].lower() in "aeiou":
    palabra += "!"

# Imprime el resultado
print("Resultado:", palabra)


#8
nombre = input("Ingresa tu nombre: ")

print("elige una opción:")


print("1. nombre en MAYÚSCULAS")

print("2. nombre en minúsculas")

print("3. nombre con la Primera Letra en mayúscula")

opcion = input("ingresa 1, 2 o 3: ")


if opcion == "1":
    resultado = nombre.upper()
elif opcion == "2":
    resultado = nombre.lower()
elif opcion == "3":
    resultado = nombre.title()
else:
    resultado = "opción no válida"

print("Resultado:", resultado)


#9
magnitud = float(input("Ingresa la magnitud del terremoto: "))

# Clasifica según la escala de Richter
if magnitud < 3:
    print("Muy leve (imperceptible)")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif 6 <= magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")