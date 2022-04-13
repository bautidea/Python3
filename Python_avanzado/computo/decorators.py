import re
from modelo import bdd

class Decorator():
    def Main(self, method):
        def wrap(self, *args):
            if method.__name__ == 'Actualizar_tree':
                resultado = bdd.consultar_bdd()
                print(args)
                args[1] = resultado
                print(args)
                method(self, *args)
        return wrap