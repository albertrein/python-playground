nome_user = "guilherme"

#Validando o conjunto DEPOIS iteração
lista_nome = [ nome.upper() if nome is "l" or nome is "h" else nome for nome in nome_user]

print(lista_nome)

#Printing Falses checks with bool
print( [bool(elemento) for elemento in ['', [], 0]] )

numeros = list(range(0,20))

#Validando o conjunto ANTES iteração
pares = [numero for numero in numeros if not numero % 2]
impares = [numero for numero in numeros if numero % 2 == 1]
impares = [numero for numero in numeros if numero % 2]
