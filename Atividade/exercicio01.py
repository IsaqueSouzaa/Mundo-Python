# Crie um programa que imprima os ímpares de 1 até N e faça a somatória, sendo N solicitado ao usuário

num = int(input("Digite um valor: "))

soma = 0 

for i in range(1, num + 1 ):

    if i % 2 != 0:
        print(i)
        soma += i 

print("A soma dos números impares entre 1 até {} é {}".format(num,soma))