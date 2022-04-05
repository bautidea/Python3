class Tema():
    observadores = []
    
    def Notify_alta(self):
        pass
    
    def Notify_Borrar(self):
        pass
    
    def Notify_modificar(self):
        pass

class Alta_observer():
    def __init__(self, obj):
        self.obs_a = obj

class Borrar_observer():
    def __init__(self, obj):
        self.obs_b = obj

class Modificar_observer():
    def __init__(self, obj):
        self.obs_c = obj