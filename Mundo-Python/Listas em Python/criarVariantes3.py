#Cria variantes e arrays
numeros = []
num = int(input("Digite um numero: "))
soma = 0
#Cria um loop aonde é adicionado um item no array e faz a soma entre os itens
while (num != 0):
    numeros.append(num)
    soma = soma + num
    
    num = int(input("Digite um numero: "))
#Exibe a media e a lista    
n = len(numeros)
print ("Media=",soma/n)
print(numeros)
