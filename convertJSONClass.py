import json
from Class import FILE_PATH, Pessoa

with open(FILE_PATH, 'r', encoding='utf8') as arquivo:
    pessoas = json.load(arquivo)
    print(pessoas)
    
    for pessoa in pessoas:
        p1 = Pessoa(**pessoas[1])
        print(p1.nome, p1.idade)