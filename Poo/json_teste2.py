import json
from json_teste import CAMINHO

with open(CAMINHO, 'r') as arquivo:
    pessoas = json.load(arquivo)
    print(pessoas)
