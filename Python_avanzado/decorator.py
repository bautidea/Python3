import os
import datetime


def Decorator(method):
    def txt(self, *args):
        ruta = os.path.dirname(os.path.abspath(__file__))+"\\decorator_log.txt"
        log = open(ruta, 'a+')
        
        time = datetime.datetime.now().strftime("%d/%m/%y %H:%M")
        titulo = args[0].get()
        
        if method.__name__ == 'alta':
            estado = 'creado'
        
        if method.__name__ == 'baja':
            estado = 'eliminado'
        
        if method.__name__ == 'modificar':
            if titulo != args[4]: 
                estado = 'nombre modificado' + ' - (Nombre anterior: ' + str(args[4]) + ')'
            else:
                estado = 'modificado'

        print(time, '-', 'Titulo', titulo, estado, file= log)  
        log.close()    
        method(*args)
    return txt