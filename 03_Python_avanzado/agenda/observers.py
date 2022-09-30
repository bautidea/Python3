import os
import datetime


class Tema():
    # Clase encargada de notificar a los observers de que se ejectuto
    # determinado metodo.
    
    # Creo lista vacia en donde se agregaran los observers.
    observadores = []
    
    def Add(self, obj):
        # Metodo de clase, agrega a los observers a la lista vacia,
        # para que estos puedan ser notificados.
        
        self.observadores.append(obj)
            
    def Notify_alta(self, *args):
        # Metodo de clase, avisa al observador que hubo un alta de datos.
  
        self.observadores[0].Update(*args)
    
    def Notify_borrar(self, *args):
        # Metodo de clase, avisa al observer que hubo una baja de datos.
        
        self.observadores[1].Update(*args)
    
    def Notify_modificar(self, *args):
        # Metodo de clase, avisa al abserver que hubo una modificacion de datos.
        
        self.observadores[2].Update(*args)

class Observers():
    # Clase padre de los observers
    
    # Obtengo la ruta desde donde se esta ejectuando la app.
    ruta = os.path.dirname(os.path.abspath(__file__))+"\\observer_log.txt" 
    
    # Obtengo la fecha y hora, cuando se llama al atributo 'time'.
    time = datetime.datetime.now().strftime("%d/%m/%y %H:%M")
    
    def Update(self):
        raise NotImplementedError('Delegacion de actualizacion')

class Alta_observer(Observers):
    # Clase observadora, recibe la notificacion de la clase 'Temas'
    # de que se realizo un alta de datos.
    
    def __init__(self, obj):
        # Metodo de instancia, al instanciarse esta clase en el modulo 'main.py',
        # ejeccuta metodo de la clase padre 'Tema'.
        
        # Instancio la clase 'Abmc', hija de 'Tema'
        # me permite ejecutar el metodo 'Add' de la clase padre.
        self.obs_a = obj
        self.obs_a.Add(self)
        
    def Update(self, *args):
        # Metodo de clase, es llamado por la clase padre 'Tema'.
        
        # Crea o abre el archivo de texto especificado en la clase padre 'Observers'
        # en modo append.
        log = open(self.ruta, 'a+')
        
        # Imprimo en archivo creado, Tiempo - Titulo - estado.
        print(self.time, '-', 'Titulo', args[0], 'creado', file= log)
     
class Borrar_observer(Observers):
    # Clase observadora, recibe la notificacion de la clase 'Temas'
    # de que se realizo una baja de datos.
    
    def __init__(self, obj):
        # Metodo de instancia, al instanciarse esta clase en el modulo 'main.py',
        # ejecuta los metodos de la clase padre 'Tema'
        
        # Instancia la clase 'Abmc', hija de 'Tema'
        # me permite ejecutar el metodo 'Add' de la clase padre.
        self.obs_b = obj
        self.obs_b.Add(self)
    
    def Update(self, *args):
        # Metodo de clase, es llamado por la clase padre 'Tema'.
        
        # Crea o abre el archivo de especificado en la clase padre 'Observers'
        # en modo append.
        log = open(self.ruta, 'a+')
        
        # Imprimo en archivo creado, Tiempo - Titulo - estado.
        print(self.time, '-', 'Titulo',args[0], 'eliminado', file= log)

class Modificar_observer(Observers):
    # Clase observadora, recibe la notificacion de la clase 'Temas'
    # de que se realizo una modificacion de datos.
    
    def __init__(self, obj):
        # Metodo de instancia, al instanciarse esta clase en el modulo 'main.py',
        # ejecuta los metodos de la clase padre 'Tema'
        
        # Instancia la clase 'Abmc', hija de 'Tema'
        # me permite ejecutar el metodo 'Add' de la clase padre.
        self.obs_c = obj
        self.obs_c.Add(self)
    
    def Update(self, *args):
        # Metodo de clase, es llamado por la clase padre 'Tema'.
        
        # crea o abre el archivo de especificado en la clase padre 'Observers'
        # en modo append.
        log = open(self.ruta, 'a+')
        
        # Comparo si el titulo no se modifico al editar los datos.
        if args[0] != args[1]:
            # Si el titulo se modifico lo informo en el log
            estado = 'nombre modificado' + ' - (Nombre anterior: ' + str(args[1]) + ')'
        else:
            # Si el titulo no fue modificado, solo informo que se modificaron los datos
            estado = 'modificado'
        
        # Imprimo en archivo creado, Tiempo - Titulo - estado.
        print(self.time, '-', 'Titulo', args[0], estado, file= log)