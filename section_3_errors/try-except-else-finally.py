def divisao(x, y):
    return x / y

try:
    reposta_divisao = divisao(3,0)
except ZeroDivisionError:
    print('Erro')
else:
    print(reposta_divisao)
finally:
    print("Division ended")
