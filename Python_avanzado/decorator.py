import os
import datetime


def Decorator(method):
    # Funcion decoradora, intercepta el metodo y los parametros para agregar
    # logica extra al codigo, cuando se llama al metodo decorado.
    
    def txt(*args):
        # Funcion que envuelve al metodo que estamos ejecutando, agregandole
        # la logica de crear un archivo Log.
        
        # Obtenemos la ruta donde se esta ejecutando la app.
        ruta = os.path.dirname(os.path.abspath(__file__))+"\\decorator_log.txt"
        
        # Abrimos o creamos el archivo especificado, en formato append.
        log = open(ruta, 'a+')
        
        # Obtenemos el tiempo en el que se ejecut el decorador
        time = datetime.datetime.now().strftime("%d/%m/%y %H:%M")
        
        # De los argumentos interceptados obenemos el tiulo.
        titulo = args[1].get()
        
        # Me fijo que el nombre del metodo interceptado coincida con los 
        # siguientes nombres, para darle un estado.
        if method.__name__ == 'alta':
            estado = 'creado'
        
        if method.__name__ == 'baja':
            estado = 'eliminado'
        
        if method.__name__ == 'modificar':
            
            # Si en la modificacion se cambio el titulo lo informo en el log.
            if titulo != args[5]: 
                estado = 'nombre modificado' + ' - (Nombre anterior: ' + str(args[5]) + ')'
            else:
                estado = 'modificado'

        # Imprimo en archivo creado, Tiempo - Titulo - estado.
        print(time, '-', 'Titulo', titulo, estado, file= log)  
        log.close()  
        
        # Una vez ejecutada la logica extra, ejecuto el metodo, con sus
        # con sus respectivos argumentos  
        method(*args)
    return txt