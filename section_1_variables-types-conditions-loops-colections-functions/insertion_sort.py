# Insertion Sort - Algoritmo de ordenamento O(n²)

lista = [5, 3, 6, 7, 2, 0, 4]
lista_copia = lista.copy()

lista_copia.sort()

for i in range(1, lista.__len__()):
    if lista[i] < lista[i-1]:
        for j in range(i, 0, -1):
            if lista[j] < lista[j-1]:
                lista[j-1], lista[j] = lista[j], lista[j-1]


print(f'Lista: {lista}')
print(f'Lista copia: {lista_copia}')

if lista == lista_copia:
    print('\U0001F609')
        
