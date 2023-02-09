"""
Programa que arroje mayor de edad,
si la edad es mayor o igual que 18,
de lo contrario muestre menor de edad
"""

"""
edad = int (input("Ingrese edad: "))
if edad >= 18:
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad")
"""

"""
Programa que arroje mayor de edad,
si la edad es mayor o igual que 18, si edad mayor que 65,
muestre usted pertenece a la tercera edad, de lo contrario muestre menor de edad
"""

edad = int (input("Ingrese edad: "))
if edad >= 18 and edad <= 64:
    print("Usted es mayor de edad")

elif edad >= 65:
    print("Usted pertenece a la tercera edad")

else:
    print("Usted es menor de edad")