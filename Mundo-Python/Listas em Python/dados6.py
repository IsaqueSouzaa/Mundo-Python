num = []
numD = 0
soma = 0


while True:
  try:
    numeros = int(input("Digite um numero: "))
    num.append(numeros)
    soma += numeros
    numD += 1 
    print(num)

  except ValueError:
    print("Encerrando o programa!")  
    break
  
media = soma / numD

print("A soma dos numeros é: {}".format(soma))
print("A media é: {}".format(media))

cima_da_media = 0

for i in range(len(num)):
  if num[i] > media:
    cima_da_media += 1

print("Quantidade de numeros a cima da media: {}".format(cima_da_media))
  
  
