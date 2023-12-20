import json

FILE_PATH = 'convertJSON.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade=idade

p1 = Pessoa('João', 33)
p2 = Pessoa('Joanna', 23)
p3 = Pessoa('Rafael', 45)

bd=[vars(p1), vars(p2), vars(p3)]


with open(FILE_PATH, 'w', encoding='utf8') as arquivo:
    json.dump(bd, arquivo, ensure_ascii=False)