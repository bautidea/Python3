from tkinter import *


class temas:
    def tema1(self, root, titulo, descripcion, boton_t1, boton_t2, boton_t3):
        tema_1 = "light slate gray"
        root.configure(background=tema_1)
        titulo.configure(background=tema_1, fg="white")
        descripcion.configure(background=tema_1, fg="white")
        boton_t1.configure(background=tema_1, fg="white")
        boton_t2.configure(background=tema_1, fg="white")
        boton_t3.configure(background=tema_1, fg="white")

    def tema2(self, root, titulo, descripcion, boton_t1, boton_t2, boton_t3):
        tema_2 = "sienna1"
        root.configure(background=tema_2)
        titulo.configure(background=tema_2, fg="black")
        descripcion.configure(background=tema_2, fg="black")
        boton_t1.configure(background=tema_2, fg="black")
        boton_t2.configure(background=tema_2, fg="black")
        boton_t3.configure(background=tema_2, fg="black")

    def tema3(self, root, titulo, descripcion, boton_t1, boton_t2, boton_t3):
        tema_3 = "sky blue"
        root.configure(background=tema_3)
        titulo.configure(background=tema_3, fg="black")
        descripcion.configure(background=tema_3, fg="black")
        boton_t1.configure(background=tema_3, fg="black")
        boton_t2.configure(background=tema_3, fg="black")
        boton_t3.configure(background=tema_3, fg="black")
