class Fibonacci:

    def get_number_positional_fibonacci(self, posicao_elemento_buscado):
        somador_fibo = 0
        somador_fibo_antes = 1
        somador_fibo_depois = 1
        for i in range(posicao_elemento_buscado-1):
            somador_fibo = somador_fibo_antes + somador_fibo_depois
            somador_fibo_antes = somador_fibo_depois
            somador_fibo_depois = somador_fibo
        
        return somador_fibo_depois

if __name__ == '__main__':
    fibi = Fibonacci()
    print(fibi.get_number_positional_fibonacci(-10))
