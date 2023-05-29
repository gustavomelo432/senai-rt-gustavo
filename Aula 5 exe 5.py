def somar(n1,n2):
    return n1 + n2
def mutiplicar(n1,n2):
    return n1 * n2
def maior(n1,n2):
    if n1 > n2:
        return n1
    else:
        return n2
def menor(n1,n2):
    if n1>n2:
        return n1
    else:
        return n2
Valor1=float(input("Insira o primerio valor: ") )
Valor2=float(input("Insira o segundo valor:  ") )
opçao = input("Selecione uma opçao: ")
if opçao =="A":
    Resultado=somar(Valor1,Valor2)
    print("A soma dos valores da:",Resultado)
if opçao =="B":
    Resultado=mutiplicar(Valor1,Valor2)
    print("A mutiplicaçao dos valores",Resultado)
if opçao=="C":
    Resultado=maior(Valor1,Valor2)
    print("O maior numero e",Resultado)
if opçao=="D":
    Resultado=menor(Valor1,Valor2)
    print("O menor numero e",Resultado)




      

