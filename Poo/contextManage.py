# Context Manager com classes - Criando e Usando gerenciadores de contexto
# Você pode implementar seus próprios protocolos
# apenas implementando os dunder methods que o
# Python vai usar.
# Isso é chamado de Duck typing. Um conceito
# relacionado com tipagem dinâmica onde o Python não
# está interessado no tipo, mas se alguns métodos existem
# no seu objeto para que ele funcione de forma adequada.
# Duck Typing:
# Quando vejo um pássaro que caminha como um pato, nada como
# um pato e grasna como um pato, eu chamo aquele pássaro de pato.
# Para criar um context manager, os métodos __enter__ e __exit__
# devem ser implementados.
# O método __exit__ receberá a classe de exceção, a exceção e o
# traceback. Se ele retornar True, exceção no with será
# suprimidas.



class MyContextManager:
    def __init__(self, caminho, modo):
        self.caminho = caminho
        self.modo = modo
        self._arquivo = None


    def __enter__(self):
        print("abrindo")
         
        self._arquivo = open(self.caminho, self.modo, encoding='utf8')
        return self._arquivo

    def __exit__(self, class_exception, exception_, traceback_):
        print("fechando")
        self._arquivo.close()

        raise class_exception("minha msg")

        print(class_exception)
        print(exception_)
        print(traceback_)

        return True # tratei da exceção




with MyContextManager('contextManage','w') as arquivo:
    arquivo.write('linha 1\n')
    arquivo.write('linha 2\n', 123)
    arquivo.write('linha 3\n')
    print("WITH", arquivo)



