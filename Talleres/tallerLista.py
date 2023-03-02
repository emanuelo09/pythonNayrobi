
#Punto 1
"""
lista = [23, 45, 25, 53, 4, 8, 100]

print(lista[4])

lista.sort()
print("Lista ordenada: ", lista)

menor = None
mayor = None

for numero in lista:
    if menor == None and mayor == None:
        
        menor = numero
        mayor = numero

    else:
        if numero < menor:
            menor = numero
        
        if numero > mayor:
            mayor = numero

print(f'El numero mayor es {mayor}')
print(f'El numero menor es {menor}')"""

#Punto 2

#A
#Le falta el =
"""lista_colores ["rojo", "azul", "verde", 'amarillo']"""


#B
#print(lista_colores[0]) el 0 va entre []
"""
lista_colores = ["rojo", "verde", "azul", "amarillo"]
print(lista_colores(0))
"""


#C
#print(lista_colores[-4]) no existe [-4] es [-3]
"""
lista_colores = ["rojo", "azul", "verde" ]

print(lista_colores[-0])
print(lista_colores[-4])
"""


#Punto 3

"""
lista_colores = ["rojo", "azul", "verde", "amarillo"]
print(lista_colores[2][3])
"""


#Punto 4
"""
departamentosColombia = []

for i in range(int(input("Escriba cuantos departamentos de colombia quiere ingresar: "))):
    
    departamentos = (input("Escriba el departamento: "))
    departamentosColombia.append(departamentos)

print("Los ultimos departamentos ingresados fueron:", {departamentosColombia[-2]}, {departamentosColombia[-1]})

departamentosColombia.sort(reverse=True)
print(departamentosColombia)

#Punto 7
print("La longitud de la lista es de:", len(departamentosColombia))
"""



#Punto 5
"""

hardware = []

hardware.append("Teclado")
hardware.append("Monitor")
hardware.append("Mouse")

hardware.insert(2, "USB")
print(hardware)

#Punto 6

hardware.pop(2)
hardware.pop(0)

print(hardware)
"""



#Punto 8
"""
numeros = []

for i in range(int(input("Digite los numeros que desea ingresar: "))):
    numero = int(input("Digite numero: "))
    numeros.append(numero)
    numeros.sort()
    print(numeros)

for i in numeros:
    numeros.sort(reverse=True)
print(numeros)
"""
