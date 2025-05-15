class MeuError(Exception):
    ...
    
    
def levantar():
    exception_ = MeuError('a','b','c')
    raise exception_

try:
    levantar()
except(MeuError, ZeroDivisionError) as error:
    print(error.args)
    print(error.__class__.__name__)