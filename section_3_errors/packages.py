import random

print(random.random())

##
from random import random as rand, randint as randit

from meu_pacote import meu_modulo

print(meu_modulo.get_hello())

from meu_pacote.meu_modulo import get_hello

print(get_hello())