
def somar(x,y):
    soma = x + y
    return soma

def subtrair(x1,y1):
    sub = x1 - y1
    return sub

a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))

s = somar(a,b)
print(s)
print(somar(a,b))

s1 = subtrair (a,b)
print(s1)
