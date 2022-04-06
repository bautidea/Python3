import os
import datetime


class Tema():
    observadores = []
    
    def Add(self, obj):
        self.observadores.append(obj)
            
    def Notify_alta(self, *args):
        self.observadores[0].Update(*args)
    
    def Notify_borrar(self, *args):
        self.observadores[1].Update(*args)
    
    def Notify_modificar(self, *args):
        self.observadores[2].Update(*args)

class Observer():
    ruta = os.path.dirname(os.path.abspath(__file__))+"\\observer_log.txt" 
    time = datetime.datetime.now().strftime("%d/%m/%y %H:%M")
    
    def Update(self):
        raise NotImplementedError('Delegacion de actualizacion')

class Alta_observer(Observer):
    def __init__(self, obj):
        self.obs_a = obj
        self.obs_a.Add(self)
        
    def Update(self, *args):
        log = open(self.ruta, 'a+')
        print(self.time, '-', 'Titulo', args[0], 'creado', file= log)
     
class Borrar_observer(Observer):
    def __init__(self, obj):
        self.obs_b = obj
        self.obs_b.Add(self)
    
    def Update(self, *args):
        log = open(self.ruta, 'a+')
        print(self.time, '-', 'Titulo',args[0], 'eliminado', file= log)

class Modificar_observer(Observer):
    def __init__(self, obj):
        self.obs_c = obj
        self.obs_c.Add(self)
    
    def Update(self, *args):
        log = open(self.ruta, 'a+')
        
        if args[0] != args[1]:
            estado = 'nombre modificado' + ' - (Nombre anterior: ' + str(args[1]) + ')'
        else:
            estado = 'modificado'
        
        print(self.time, '-', 'Titulo', args[0], estado, file= log)