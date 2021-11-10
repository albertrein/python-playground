lista_valores = [1,2,3,4,5,6]

print(max(lista_valores))
print(min(lista_valores))
# 6
# 1

print(max(int(input()), int(input())))
#_________________________________________________


lista_dict_musicas_duracao = [
    {"musica":"Kashmir", "duracao":8.37},
    {"musica":"Layla", "duracao":7.04},
    {"musica":"Faroeste Caboclo", "duracao":9.07}
]

larger_duration = max(lista_dict_musicas_duracao, key=lambda valor: valor['duracao'])

print(larger_duration)


print(min('a','b','c','d'))

