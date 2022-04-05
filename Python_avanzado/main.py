from tkinter import Tk
from vista import Ventanita
import observers


class Main:
    """
    Está es la clase principal
    """

    def __init__(self, root):
        self.objeto = Ventanita(root)
        self.objeto.actualizar()
        self.obs_a = observers.Alta_observer(self.objeto.objeto_base)
        self.obs_b = observers.Borrar_observer(self.objeto.objeto_base)
        self.obs_c = observers.Modificar_observer(self.objeto.objeto_base)


if __name__ == "__main__":
    root_tk = Tk()
    
    application = Main(root_tk)
    
    root_tk.mainloop()
