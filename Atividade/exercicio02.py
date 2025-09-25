#Crie um programa onde o usuário ira informar dois números, o
#menor e maior, faça a somatório dos números impares e pares desse
#intervalo.

num1 = int(input("Informe o primeiro número:"))

num2 = int(input("Informe o segundo número: "))

total_pares = 0

total_impares = 0

num_par = {}

num_impar = {}

for i in range(num1 , num2 ):

    if i % 2 == 0:
        num_par = i 
        total_pares += i 

    elif i % 2 != 0:
        num_impar = i
        total_impares +=i

print("O total de num par é {}".format(num_par))
print("O total de num impar é {}".format(num_impar))

print("A soma dos números pares é {} a soma dos números impares é {}".format(total_pares,total_impares))