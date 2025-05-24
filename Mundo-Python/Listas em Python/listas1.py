# Codigo simples de lista de notas

#notas = [8,7,3.5,6,8]
#for i in range(4):
    #print(notas[i])



# Codigo para fazer a media de notas

notas = [8,7,3.5,6,8]
soma = 0
for i in range(4):
    print(notas[i])
    soma = soma + notas[i]

media = soma/5
print("A media é {}".format(media))