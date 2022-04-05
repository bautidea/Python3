import os
import datetime


def Decorator(method):
    def txt(self, *args):
        ruta = os.path.dirname(os.path.abspath(__file__))+"\\decorator_log.txt"
        log = open(ruta, 'a+')
        
        time = datetime.datetime.now().strftime("%d/%m/%y %H:%M")
        titulo = args[0].get()
        
        if method.__name__ == 'alta':
            estado = 'Creado'
        
        if method.__name__ == 'baja':
            estado = 'Eliminado'
        
        if method.__name__ == 'modificar':
            if titulo != args[4]: 
                estado = 'Nombre modificado' + ' - (Nombre anterior: ' + str(args[4]) + ')'
            else:
                estado = 'Modificado'

        print(time, '-', 'Titulo', titulo, estado, file= log)  
        log.close()    
        method(self,*args)
    return txt