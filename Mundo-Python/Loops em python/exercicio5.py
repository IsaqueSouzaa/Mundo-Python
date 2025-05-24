#5- Temos um grupo de pessoas. Escreva um programa em Python que leia o sexo e a altura de cada pessoa, 
#calcule e mostre a altura média das mulheres e dos homens separadamente. Utilize o comando de repetição que desejar

mulheres = 0
alturaMulheres = 0.0

homens = 0
alturaHomens = 0.0

while True:
    try:
        sexo = input("Informe o sexo da pessoa (M/F) ou digite (S) para sair: ").strip().upper()
        
        if sexo == "S":
            break  
        
        if sexo not in ["M", "F"]:
            print("Sexo inválido. Digite apenas M ou F.")
            continue

        altura = float(input("Informe a altura da pessoa (em metros): "))

        if sexo == "M":
            homens += 1
            alturaHomens += altura
        elif sexo == "F":
            mulheres += 1
            alturaMulheres += altura

    except ValueError:
        print("Erro: altura deve ser um número válido.")
        continue


if homens > 0:
    mediaHomens = alturaHomens / homens
else:
    mediaHomens = 0

if mulheres > 0:
    mediaMulheres = alturaMulheres / mulheres
else:
    mediaMulheres = 0


print("\n--- RESULTADOS ---")
print(f"Total de homens: {homens}")
print(f"Média da altura dos homens: {mediaHomens:.2f} m")

print(f"Total de mulheres: {mulheres}")
print(f"Média da altura das mulheres: {mediaMulheres:.2f} m")
    
