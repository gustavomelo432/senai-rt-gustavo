km=float( input("Informe quantos km: ")  )
if km > 80 :
    kmexcetidos= km - 80
    multa= kmexcetidos * 7
    print ("multado")
    print("velocidade excetida",kmexcetidos,"km/h")
    print("valor a ser pago da multa sera",multa)
else:
    print("voce esta no limite continue dirigindo com segurança ")
    
