from tkinter import Tk
from vista import Ventanita


class Main:
    """
    Está es la clase principal
    """

    def __init__(self, root):
        self.objeto = Ventanita(root)
        self.objeto.actualizar()


if __name__ == "__main__":
    root_tk = Tk()
    
    application = Main(root_tk)
    
    root_tk.mainloop()
