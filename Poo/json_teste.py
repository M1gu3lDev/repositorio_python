import json

CAMINHO = 'json_class'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade



p1 = Pessoa('ricardo', 32)
bd = vars(p1)
with open(CAMINHO, 'w') as arquivo:
    json.dump(bd, arquivo)