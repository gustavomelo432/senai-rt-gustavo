def verificar_par(numero):
    if numero % 2 ==0:
        return True
    else:
        return False
numero=int(input("Fale me um numero"))
if verificar_par(numero):
    print(numero,"O numero e par")
else:
    print(numero,"O numero e impar ")

