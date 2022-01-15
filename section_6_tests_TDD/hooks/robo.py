class Robo():

    def __init__(self, nome, bateria=100, habilidades=[]) -> None:
        self._nome = nome
        self._bateria = bateria
        self._habilidades = habilidades
        pass
    
    @property
    def nome(self) -> str:
        return self._nome

    @property
    def bateria(self) -> int:
        return self._bateria

    @property
    def habilidades(self) -> list:
        return self._habilidades
    
    def carregar(self):
        self._bateria = 100
    
    def speak(self):
        if self._bateria <= 0:
            return 'Bateria Fraca. Por favor recarregue'
        self._bateria -= 1
        return f'Olá, eu sou {self._nome}'

