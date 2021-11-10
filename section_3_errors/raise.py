def maior_de_18(idade):
    if idade is not int:
        raise ValueError('Um inteiro é esperado.')
    if idade < 18:
        raise ValueError('Menor de idade')
    return True

#maior_de_18('33')

def validar_estados_habilitados(usuario_estado):
    lista_estados = ['RS', 'SC', 'PR']
    
    if type(usuario_estado) is not str:
        raise ValueError('Digite um estado')
    
    if usuario_estado not in lista_estados:
        raise ValueError('Estado não reconhecido')

validar_estados_habilitados('SP')