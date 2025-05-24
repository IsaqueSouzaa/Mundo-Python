kmI = int(input("Informe o Km inicial: "))
kmF = int(input("Informe o Km final: "))
consumo = int(input("Informe litros gastos: "))
preco = int(input("Informe o preço da gasolina: "))

def calculo(kmI,kmF, consumo,preco):
    distancia = kmF - kmI
    gasto = distancia / consumo
    valor = consumo * preco

    print("Distancia: " , distancia)
    print("Listros Gastos: ", gasto)
    print("Valor Gasto: ", valor )

calculo(kmI,kmF, consumo,preco)