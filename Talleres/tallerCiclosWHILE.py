
#Punto WHILE

number1 = int(input("Ingrese el primer numero: "))
number2 = int(input("Ingrese el segundo numero: "))
opt = 0

while opt != 8:
    print("""Ingrese la operación que quiere realizar:
    1.Suma
    2.Resta
    3.División
    4.Potenciación
    5.Multiplicación
    6.Raiz Cuadrada
    7.Cambiar los numeros ingresados
    8.Salir""")

    opt=int(input())

    if opt == 1:
        print(number1, "+", number2, "=", number1+number2)
    elif opt == 2:
        print(number1, "-", number2, "=", number1-number2)
    elif opt == 3:
        if number2 == 0:
            print("ERROR EN LA DIVISION")
        else:
            print(number1,"/",number2,"=",number1/number2)
    elif opt == 4:
        print(number1, "**", number2, "=", number1**number2)
    elif opt == 5:
        print(number1, "*", number2, "=", number1*number2)
    elif opt == 6:    
        raiz = pow(number1,1/2)
        raiz1 = pow (number2,0.5)
        print("El resultado de la raiz es:",round(raiz,3),round(raiz1,3))
    elif opt == 7:
        number1 = int(input("Ingrese el primer numero: "))
        number2 = int(input("Ingrese el segundo numero: "))
    elif opt == 8:
        break
    else:
        print("OPCION INCORRECTA")





        
