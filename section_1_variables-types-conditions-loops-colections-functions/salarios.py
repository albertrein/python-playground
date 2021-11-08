import math

print("Digite o seu salário:")
salario_trabalhador = float(input())

if salario_trabalhador > 10000:
    print("Você é Senior!")
elif salario_trabalhador >= 5000:
    print("Você é Pleno")
elif salario_trabalhador >= 1500:
    print("Voce é Junior")
else:
    print("Você é Estagiário")

salario_trabalhador = math.sqrt(salario_trabalhador)
salario_trabalhador = salario_trabalhador**3
print(salario_trabalhador)

print(math.floor(salario_trabalhador))

