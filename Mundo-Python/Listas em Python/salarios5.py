salario = []

for i in range(1,6):
    sal = float (input("Digite o salario: "))
    salario.append(sal)

    print(salario)

soma = 0

for i in range(0,5):
    soma = soma + salario[i]
    if salario < 850:
      print("Salarios baixo de R$850,00:{}".format(salario[i]))
    
print("Media = " + soma/5)
print(salario)
