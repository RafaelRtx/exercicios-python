from functools import singledispatch
from random import randint

def sorteia(func):
    def wrapper(*args, **kwargs):
        lista = [randint(0, 10) for _ in range(5)]
        return func(lista, *args, **kwargs)
    return wrapper

@singledispatch
@sorteia
def SomaPar(x):
    print(sum(filter(lambda x: x % 2 == 0, x)))

SomaPar.register(list, lambda x: sum(filter(lambda x: x % 2 == 0, x)))

# chamar a função sem argumentos
SomaPar()