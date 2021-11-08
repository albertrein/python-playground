def is_sigla_valida(**kwargs):
    if type(kwargs['sigla']) is str and kwargs['sigla'].__len__() == 2:
        return True
    return False

def is_ddd_valido(**kwargs):
    if type(kwargs['ddd']) is int:
        return True
    return False


def cadastra_ddd():
    print("Digite a sigla do estado")
    sigla_estado = str(input())
    if not is_sigla_valida(sigla=sigla_estado):
        return False
    print("Digite o DDD")
    ddd_estado = int(input())
    if not is_ddd_valido(ddd=ddd_estado):
        return False
    return {sigla_estado: ddd_estado}

def busca_ddd(lista_estados):
    print('Digite a sigla de busca')
    sigla_busca = input()
    if lista_estados.__contains__(sigla_busca):
        print(f"O DDD de {sigla_busca} eh {lista_estados[sigla_busca]}")
        return True
    print('Sigla não encontrada')
    return False

lista_estados_ddd = []

while True:
    print("Digite 'C' p/ Cadastrar um DDD")
    print("Digite 'B' p/ Buscar um DDD")
    print("Digite  qualquer outra coisa p/ Sair")

    escolha_acao = str(input())
    if escolha_acao.upper() == "C":
        novo_ddd = cadastra_ddd()
        lista_estados_ddd.update(novo_ddd) if novo_ddd is not False else False
    elif escolha_acao.upper() == "B":
        busca_ddd()
    else:
        break

