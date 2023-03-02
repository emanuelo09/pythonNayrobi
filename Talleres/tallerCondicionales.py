
#Punto 1
"""
weight_clown = 95
weight_doll = 70
clowns = int(input("Introduce el número de payasos a enviar: "))
dolls = int(input("Introduce el número de muñecas a enviar: "))
total_weights = weight_clown * clowns + weight_doll* dolls
print("El peso total del paquete es " + str(total_weights))
"""

#Punto 2
"""
number = int(input("Ingresa un número entero: "))
if number % 2 == 0:
    print("El numero " + str(number) + " es par")
else:
    print("El numero " + str(number) + " es impar")
"""

#Punto 3
"""
age = int(input("Cuál es tu edad? "))
income = float(input("Cuales son tus ingresos mensuales?"))
if age <= 18 and income <= 2500000:
    print("No tienes que tributar")
else:
    print("Tienes que tributar")
"""

#Punto 4
"""
noteD = float(input("Cuál es tu nota en la clase de Desarrollo de Software? "))
noteM = float(input("Cuál es tu nota en la clase de Matematicas? "))
noteL = float(input("Cuál es tu nota en la clase de Logica de Programacion? "))
sumNote = noteD + noteM + noteL
average = sumNote / 3
if average >= 3:
    print("Aprobaste con un promedio de: ", round(average,1))
else:
    print("A repetir año porque no aprobó")
"""

#punto 5
"""
age = int(input("Ingresa tu edad"))

if age < 10:
    price = 0
elif age >= 11 and age <= 18:
    price = 24660
else:
    price = 48000

print("El precio de su entrada es de", "$",price)
"""
