#3-  Faça um programa em Python que leia um valor n, inteiro e positivo, calcule e mostre a seguinte soma:​

# 0S = 1 + 1/2 + 1/3 + 1/4 +...+ 1/n​


numero = int(input("Por favor informe um numero positivo: "))


soma = 0


for i in range(1, numero + 1):
    soma += 1/i


print(f"A soma é: {soma:.2f}")