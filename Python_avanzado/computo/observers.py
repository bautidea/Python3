import os 
import datetime

class Tema():
    # Clase encargada de notificar a los observers de que se ejecuto
    # determinado metodo.
    
    # Creo lista vacia en donde se agregaran los observers.
    observadores = []
    
    def Add(self, obj):
        # Metodo de calse, agrega a los observers a la lista vacia,
        # para que estos puedan ser notificados.
        
        self.observadores.append(obj)
    
    def Notify_inicio(self, *args):
        # Metodo de clase, avisa al observador que la aplicacion se inicio.
  
        self.observadores[0].Update(*args)
        
    def Notify_alta(self, *args):
        # Metodo de clase, avisa al observador que hubo un alta de datos.
  
        self.observadores[1].Update(*args)
    
    def Notify_baja_seleccion(self, *args):
        # Metodo de clase, avisa al observador que se elimino los datos
        # seleccionados.
  
        self.observadores[2].Update(*args)
    
    def Notify_baja_obra(self, *args):
        # Metodo de clase, avisa al observador que se elimino una obra
        # de la base de datos.
  
        self.observadores[3].Update(*args)

    def Notify_modificar(self, *args):
        # Metodo de clase, avisa al abserver que hubo una modificacion de datos.
        
        self.observadores[4].Update(*args)
    
    def Notify_consulta(self, *args):
        # Metodo de clase, avisa al abserver que hubo una consulta
        # de la base de datos.
        
        self.observadores[5].Update(*args)
        
    def Notify_fin(self, *args):
        # Metodo de clase, avisa al abserver que se cerro la aplicacion
        
        self.observadores[6].Update(*args)
    
    def Notify_imprimir(self, *args):
        # Metodo de clase, avisa al abserver que se genero una impresion de
        # una obra.
        
        self.observadores[7].Update(*args)
        

class Observers():
    # Clase padre de los observers.
    
    # Obtengo la ruta desde donde se esta ejecutando la app.
    ruta = os.path.dirname(os.path.abspath(__file__)) + "\\computos_log.txt"
        
    # En caso de que no este encuentre a un observador al cual notoficar
    # me levanta el siguiente error.
    def Update(self):
        raise NotImplementedError('Delegacion de actualizacion')

class Inicio_observer (Observers):
    # Clase observadora, recibe la notificacion de la clase 'Temas'
    # de que se inicio la aplicacion
    
    def __init__(self, obj):
        # Metodo de instancia, al instanciarse esta clase en el modulo 'main.py',
        # ejeccuta metodo de la clase padre 'Tema'.
        
        # Instancio la clase 'Abmc', hija de 'Tema'
        # me permite ejecutar el metodo 'Add' de la clase padre.
        self.obs_inicio = obj
        self.obs_inicio.Add(self)
    
    def Update(self, *args):
        # Metodo de clase, es llamado por la clase padre 'Tema'.
        
        # Crea o abre el archivo de texto especificado en la clase padre 'Observers'
        # en modo append.
        log = open(self.ruta, 'a+')
        
        # Obtengo la fecha y hora, cuando se lama al atributo 'time'.
        time = datetime.datetime.now().strftime("%d/%m/%y %H:%M")
        
        # Imprimo en archivo creado, Tiempo - Titulo - estado.
        print('*'*25, 'APLICACION INICIADA -', time, '*'*25, file= log)

class Alta_observer (Observers):
    # Clase observadora, recibe la notificacion de la clase 'Temas'
    # de que se realizo un alta de datos.
    
    def __init__(self, obj):
        # Metodo de instancia, al instanciarse esta clase en el modulo 'main.py',
        # ejeccuta metodo de la clase padre 'Tema'.
        
        # Instancio la clase 'Abmc', hija de 'Tema'
        # me permite ejecutar el metodo 'Add' de la clase padre.
        self.obs_alta = obj
        self.obs_alta.Add(self)

    def Update(self, *args):
        # Metodo de clase, es llamado por la clase padre 'Tema'.
        
        # Crea o abre el archivo de texto especificado en la clase padre 'Observers'
        # en modo append.
        log = open(self.ruta, 'a+')
        
        # Obtengo la fecha y hora, cuando se lama al atributo 'time'.
        time = datetime.datetime.now().strftime("%d/%m/%y %H:%M")
        
        # Imprimo en archivo creado, Tiempo - Titulo - estado.
        print(time, '-', 'Obra', args[0], 'creada', file= log)


class Baja_seleccion_observer(Observers):
    # Clase observadora, recibe la notificacion de la clase 'Temas'
    # de que se realizo una baja de datos.
    
    def __init__(self, obj):
        # Metodo de instancia, al instanciarse esta clase en el modulo 'main.py',
        # ejecuta los metodos de la clase padre 'Tema'
        
        # Instancia la clase 'Abmc', hija de 'Tema'
        # me permite ejecutar el metodo 'Add' de la clase padre.
        self.obs_baja_seleccion = obj
        self.obs_baja_seleccion.Add(self)

    def Update(self, *args):
        # Metodo de clase, es llamado por la clase padre 'Tema'.
        
        # Crea o abre el archivo de especificado en la clase padre 'Observers'
        # en modo append.
        log = open(self.ruta, 'a+')
        
        # Obtengo la fecha y hora, cuando se lama al atributo 'time'.
        time = datetime.datetime.now().strftime("%d/%m/%y %H:%M")
        
        # Imprimo en archivo creado, Tiempo - Titulo - estado.
        print(time, '-', 'Se eliminaron',args[0], 'plantas de la base de datos - obra:', args[1], file= log)


class Baja_obra_observer(Observers):
    # Clase observadora, recibe la notificacion de la clase 'Temas'
    # de que se realizo una baja de datos.
    
    def __init__(self, obj):
        # Metodo de instancia, al instanciarse esta clase en el modulo 'main.py',
        # ejecuta los metodos de la clase padre 'Tema'
        
        # Instancia la clase 'Abmc', hija de 'Tema'
        # me permite ejecutar el metodo 'Add' de la clase padre.
        self.obs_baja_obra = obj
        self.obs_baja_obra.Add(self)
    
    def Update(self, *args):
        # Metodo de clase, es llamado por la clase padre 'Tema'.
        
        # Crea o abre el archivo de especificado en la clase padre 'Observers'
        # en modo append.
        log = open(self.ruta, 'a+')
        
        # Obtengo la fecha y hora, cuando se lama al atributo 'time'.
        time = datetime.datetime.now().strftime("%d/%m/%y %H:%M")
        
        # Imprimo en archivo creado, Tiempo - Titulo - estado.
        print(time, '-', 'Obra',args[0], 'eliminada', file= log)        


class Modificar_observer(Observers):
    # Clase observadora, recibe la notificacion de la clase 'Temas'
    # de que se realizo una baja de datos.
    
    def __init__(self, obj):
        # Metodo de instancia, al instanciarse esta clase en el modulo 'main.py',
        # ejecuta los metodos de la clase padre 'Tema'
        
        # Instancia la clase 'Abmc', hija de 'Tema'
        # me permite ejecutar el metodo 'Add' de la clase padre.
        self.obs_modificar = obj
        self.obs_modificar.Add(self)
    
    def Update(self, *args):
        # Metodo de clase, es llamado por la clase padre 'Tema'.
        
        # Crea o abre el archivo de especificado en la clase padre 'Observers'
        # en modo append.
        log = open(self.ruta, 'a+')
        
        # Obtengo la fecha y hora, cuando se lama al atributo 'time'.
        time = datetime.datetime.now().strftime("%d/%m/%y %H:%M")
        
        if args[0] != args[1]:
            print(time, '- Nombre de obra modificado (nombre anterior:', args[1], '-', 'nombre nuevo:', args[0], file= log) 
        
        if args[2] > 0:
            print(time, '- Se agregaron', args[2], 'plantas a la base de datos - obra:', args[0], file= log) 
        
        print(time, '- Obra', args[0], 'consulta finalizada', file= log)       
        
                
class Consulta_observer(Observers):
    # Clase observadora, recibe la notificacion de la clase 'Temas'
    # de que se realizo una consulta de la base de datos.
    
    def __init__(self, obj):
        # Metodo de instancia, al instanciarse esta clase en el modulo 'main.py',
        # ejeccuta metodo de la clase padre 'Tema'.
        
        # Instancio la clase 'Abmc', hija de 'Tema'
        # me permite ejecutar el metodo 'Add' de la clase padre.
        self.obs_consulta = obj
        self.obs_consulta.Add(self)

    def Update(self, *args):
        # Metodo de clase, es llamado por la clase padre 'Tema'.
        
        # Crea o abre el archivo de texto especificado en la clase padre 'Observers'
        # en modo append.
        log = open(self.ruta, 'a+')
        
        # Obtengo la fecha y hora, cuando se lama al atributo 'time'.
        time = datetime.datetime.now().strftime("%d/%m/%y %H:%M")
        
        # Imprimo en archivo creado, Tiempo - Titulo - estado.
        print(time, '- Obra', args[0], 'consultada', file= log)


class Fin_observer (Observers):
    # Clase observadora, recibe la notificacion de la clase 'Temas'
    # de que se finalizo la aplicacion
    
    def __init__(self, obj):
        # Metodo de instancia, al instanciarse esta clase en el modulo 'main.py',
        # ejeccuta metodo de la clase padre 'Tema'.
        
        # Instancio la clase 'Abmc', hija de 'Tema'
        # me permite ejecutar el metodo 'Add' de la clase padre.
        self.obs_fin = obj
        self.obs_fin.Add(self)
    
    def Update(self, *args):
        # Metodo de clase, es llamado por la clase padre 'Tema'.
        
        # Crea o abre el archivo de texto especificado en la clase padre 'Observers'
        # en modo append.
        log = open(self.ruta, 'a+')
        
        # Obtengo la fecha y hora, cuando se lama al atributo 'time'.
        time = datetime.datetime.now().strftime("%d/%m/%y %H:%M")
        
        # Imprimo en archivo creado, Tiempo - Titulo - estado.
        print('*'*25, 'APLICACION FINALIZADA -', time, '*'*23, file= log)

class Imprimir_observer(Observers):
    # Clase observadora, recibe la notificacion de la clase 'Temas'
    # de que se genero una impresion de la grilla
    
    def __init__(self, obj):
        # Metodo de instancia, al instanciarse esta clase en el modulo 'main.py',
        # ejeccuta metodo de la clase padre 'Tema'.
        
        # Instancio la clase 'Abmc', hija de 'Tema'
        # me permite ejecutar el metodo 'Add' de la clase padre.
        self.obs_imprimir = obj
        self.obs_imprimir.Add(self)
    
    def Update(self, *args):
        # Metodo de clase, es llamado por la clase padre 'Tema'.
        
        # Crea o abre el archivo de texto especificado en la clase padre 'Observers'
        # en modo append.
        log = open(self.ruta, 'a+')
        
        # Obtengo la fecha y hora, cuando se lama al atributo 'time'.
        time = datetime.datetime.now().strftime("%d/%m/%y %H:%M")
        
        # Imprimo en archivo creado, Tiempo - Titulo - estado.
        print(time, '- Archivo "Computos_' + str(args[0]) + '"', 'creado', file= log)