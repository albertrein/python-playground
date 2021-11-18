"""
Self faz a referencia para o objeto instanciado.

construtor __init__
    atributos criados dentro de init são atributos de instancia

atributto privado  = __<nome_atributo>


"""
class Produto:
    preco_produto = 0#atibuto de classe

    def __init__(self, id_prod):
        self.id_prod = id_prod #atributo de instancia


prod = Produto(1)

print(prod.id_prod)

prod.tamanho = 1.99 #atributo dinamico

print(prod.tamanho)

print(prod.__dict__)