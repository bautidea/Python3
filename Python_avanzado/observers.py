from ast import arg
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

class Log_observer():
    ruta = os.path.dirname(os.path.abspath(__file__))+"\\observer_log.txt" 
    time = datetime.datetime.now().strftime("%d/%m/%y %H:%M")

class Alta_observer(Log_observer):
    def __init__(self, obj):
        self.obs_a = obj
        self.obs_a.Add(self)
        
    def Update(self, *args):
        log = open(self.ruta, 'a+')
        print(args[0])
        print(self.time, '-', 'Titulo', args[0], 'creado', file= log)
     
class Borrar_observer(Log_observer):
    def __init__(self, obj):
        self.obs_b = obj
        self.obs_b.Add(self)
    
    def Update(self, *args):
        print(args)

class Modificar_observer(Log_observer):
    def __init__(self, obj):
        self.obs_c = obj
        self.obs_c.Add(self)
    
    def Update(self, *args):
        print(args)