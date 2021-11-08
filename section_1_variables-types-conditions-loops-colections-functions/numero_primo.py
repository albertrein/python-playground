print("Digite um número:")
numero_entrada = int(input())

contador_divisoes = 0

for num_iterado in range(1, numero_entrada):
    if numero_entrada % num_iterado == 0:
        contador_divisoes += 1


if contador_divisoes == 1:
    print("É primo")
else:
    print("Não é primo")

