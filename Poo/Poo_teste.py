# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.

"""class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('miguel', 'angelo')
p1.nome = 'luiz'
p1.sobrenome = 'otávio'
print(p1.nome)
print(p1.sobrenome)"""

class Carro:
    def __init__(self, nome) -> None:
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando')


fusca = Carro('fusca')
fusca.acelerar()
celta = Carro('celta')
celta.acelerar()

Carro.acelerar(fusca)