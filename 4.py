n = int(input('informe n: '))
Qtdnumero = 0
soma = 0

while Qtdnumero < 5:
    x = int(input(f"insira o valor de x{Qtdnumero}): "))
    if x < 10:
        print("informe novamente")
    else:
        soma += x
        Qtdnumero+=1
    
print(f"o somatório para n = {5} fica: {soma}")