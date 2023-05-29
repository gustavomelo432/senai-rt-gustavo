def calculararea (largura ,comprimento):
    area=largura * comprimento
    return area
largura=float(input("Digite a largura de um terreno: ")  )
comprimento=float(input("Digite o comprimento de um terreno: ") )
resultado=calculararea(largura,comprimento)
print("area do terreno e: ",resultado)
