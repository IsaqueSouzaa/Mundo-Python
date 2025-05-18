medias = []
nomes = []

x = int(input("Digite a quantidade de alunos: "))

for i in range(x):
    nome = input("Digite o nome do aluno: ")
    n1 = float(input("Digite a primeira nota ")) 
    n2 = float(input("Digite a segunda nota ")) 
    
    media = (n1 + n2) /2
    medias.append(media)
    nomes.append(nome)

n = int(input("Digite o numero do aluno que deseja exibir: "))

if medias[n] >= 6.0:
    print ( "O aluno %s foi aprovado com media ")
else:
    print("O aluno foi reprovado")    