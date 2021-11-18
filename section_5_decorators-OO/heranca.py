
class Animal:
    def __init__(self, vertebrado):
        self.__vertebrado = vertebrado
    
    def mostra_vertebra(self):
        print(f"Eh vertebrado: {self.__vertebrado}")

    def get_vertebrado(self):
        return self.__vertebrado

class Felino(Animal):
    def __init__(self, possui_vertebras, qtdPatas, pelo, nome):
        super().__init__(possui_vertebras)
        self.qtdPatas = qtdPatas
        self.pelo = pelo
        self.nome = nome
    
    def to_string(self):
        print(f"Nome {self.nome}")
        print(f"Pelo {self.pelo}")
        print(f"Patas {self.qtdPatas}")
        super().mostra_vertebra()
    
    def mostra_vertebra(self):
        if self.get_vertebrado():
            print("Eh Sim!")
            return True
        print("Eh Não")
        return False

gato = Felino(True, 4, True, 'Cat')
print(gato.__dict__)
gato.mostra_vertebra()
gato.to_string()
