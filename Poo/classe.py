class Pessoa:
    ano_atual = 2025

    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

        def get_ano_nascimento(self):
            return Pessoa.ano_atual - self.idade
        
        @classmethod # métodos de classe + factorys

        def criar_com_50(cls, nome):
            return cls(nome, 50)
        
        @staticmethod
        def funcao_que_esta_na_classe():
            print('oi')

        @property
        def nome(self):
            return self._nome
        
        @nome.setter
        def nome(self, valor):
            self._nome = valor