while True:
    num=int(input("Digite um numero:(Digite um valor negativo pra sair): ") )
    if num < 0:
        print("Programa encerrado.")
        break
    if num % 2 ==0:
        print(num,"Ele e um numero par. ")
    else:
        print(num,"Ele e um numero impar.")


