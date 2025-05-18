def CalcularImc(peso,altura):
    calculo = peso / (altura *altura)
    return calculo

a = float(input("Por favor, informe o peso: "))
b = float(input("Por favor, informe a altura: "))

c = CalcularImc(a,b)
print(CalcularImc(a,b))