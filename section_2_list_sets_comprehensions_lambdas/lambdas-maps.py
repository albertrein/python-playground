duplicador = lambda x: x *2

print(duplicador(3))

# MAPS

def calcula_area(x):
    return x[0] * x[1]

calcula_area_lambda = lambda entrada: entrada[0] * entrada[1]

lista_area_objetos = [[4,4], [5,6], [3,3]]

objeto_iteravel = map(calcula_area, lista_area_objetos)
objeto_iteravel = map(calcula_area_lambda, lista_area_objetos)

print(list(objeto_iteravel)) # tranformando um objeto em lista e imprimindo


#Filter
graus_celsius = [10, 20, 30, 39, 40]
objeto_filter = filter(lambda grau_atual: grau_atual>30, graus_celsius)

print(list(objeto_filter))

string_nome = ["Guilherme", "", "Alberto"]
x = filter(None, string_nome) #filtra itens em branco
print(list(x))
