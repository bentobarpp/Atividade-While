Par = 0
Impar = 0
imparSoma = 0 

while Par <5 and imparSoma <= 30:
    numero= int(input("Informe um numero inteiro: "))

    if numero <0:
        print ("O numero deve ser maior que 0")
    else:
        if numero % 2 == 0:
            Par += 1
        else:
            imparSoma+= numero
            Impar += 1

        if Par == 5:
            print ("5 numeros pares")
            print(f"os numeros impares foram de: {Impar}")
        elif imparSoma > 30:
            print (f"A quantidade de numeros impares é de: {Par}")
            print(f"A soma passou de 30 ({imparSoma})")