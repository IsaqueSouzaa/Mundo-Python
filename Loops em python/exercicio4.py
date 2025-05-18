#4- Escreva um algoritmo que leia um grupo de valores reais e determine quantos valores são positivos e quantos 
#são negativos. Determine, também, qual é o menor desses valores. Utilize o comando de repetição que desejar.

num = []
positivos = 0
negativos = 0

while True:
  try:

    n = float(input("Digite um numero real ( Ou digite qualquer outra coisa para encerrar):"))
    num.append(n)
    print(num)

    if n >= 0:
        positivos += 1
    elif n < 0:
        negativos += 1   
  except ValueError:
        print("Encerrando o programa!")
        break 

menor = min(num)
print("Numeros reais digitados: {}".format(num))
print("Numeros reais positivos digitados: {}".format(positivos))
print("Numeros reais negativos digitados: {}".format(negativos))
print("Menor numero digitado: {}".format(menor))


           
    


    