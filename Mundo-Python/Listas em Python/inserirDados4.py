# Programa para inserir dados em um array 
nomes = []
for i in range(5):
    n = input("Digite o nome: ")
    nomes.append(n)
# Faz a verificação do item pelo indice    
m = int(input("Digite o indice: "))
print(nomes[m])
