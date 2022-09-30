from tkinter import CENTER, DISABLED, END, VERTICAL, Entry, Label, Button, Radiobutton, ttk
from tkinter.font import NORMAL
from modelo import Abmc
from tktemas import temas
from tkinter.messagebox import *
import datetime

    
class Mensaje(): 
    # Cuando se imprima la instancia de esta clase nos devolvera
    # la accion que se le pase por parametro.
    def __init__(self, accion):
        self.accion = accion

    def __str__(self):
        # Metodo de instancia que me devuelve una accion al imprimir la instancia de la clase
        return "Titulo " + self.accion + ": " + datetime.datetime.now().strftime("%d/%m/%y %H:%M")


class Ventanita():
    def __init__(self, window):
        # Inicializamos las instancias de las clases a utilizar
        # y creamos los elementos interactivos de la app.
        
        self.root = window
        self.objeto_base = Abmc()

        # Frame.
        self.root.title("Tarea Poo")
        self.root.resizable(False, False)
        self.root.configure(background="AntiqueWhite2")

        # Etiquetas.
        self.superior = Label(
            self.root,
            text="Ingrese sus datos",
            bg="orchid",
            fg="white",
            relief= "ridge",
            borderwidth=3
        )
        self.superior.grid(
            row=0,
            column=0,
            columnspan=4,
            padx=1,
            pady=1,
            sticky="nsew"
        )

        self.titulo = Label(
            self.root,
            text="Titulo",
            background="AntiqueWhite2"
        )
        self.titulo.grid(
            row=1,
            column=2,
            sticky="w"
        )

        self.descripcion = Label(
            self.root,
            text="Descripcion",
            background="AntiqueWhite2"
        )
        self.descripcion.grid(
            row=2,
            column=2,
            sticky="w"
        )

        Label(
            self.root,
            background="goldenrod1"
        ).grid(
            row=1,
            column=0,
            columnspan=2,
            rowspan=2,
            sticky="nsew"
        )

        self.registros = Label(
            self.root,
            text="Registros existentes",
            bg="orchid",
            fg="white",
            relief= "ridge",
            borderwidth=3
        )
        self.registros.grid(
            row=3,
            column=0,
            columnspan=4,
            padx=1,
            pady=1,
            sticky="nsew"
        )

        self.temas = Label(
            self.root,
            text="Temas",
            bg= "orchid",
            fg="white",
            relief="ridge",
            borderwidth=3,
        )
        self.temas.grid(
            row=6,
            column=0,
            columnspan=4,
            padx=1,
            pady=1,
            sticky="nsew"
        )

        # Entradas.
        self.tit = Entry(self.root)
        self.tit.grid(row=1, column=3, sticky="nsew")
        self.tit.focus_set()
        self.des = Entry(self.root)
        self.des.grid(row=2, column=3, sticky="nsew")

        # Botones.
        self.boton_alta = Button(
            self.root,
            text="Alta",
            command=lambda: self.alta(),
            width=10
        )
        self.boton_alta.grid(row=4, column=1, sticky="w")

        self.boton_editar = Button(
            self.root,
            text="Actualizar",
            command=lambda: self.modificar(),
            state=DISABLED,
            width=10
        )
        self.boton_editar.grid(row=4, column=1, columnspan=2)

        self.boton_borrar = Button(
            self.root,
            text="Borrar",
            command=lambda: self.borrar(),
            state=DISABLED,
            width=10
        )
        self.boton_borrar.grid(row=4, column=2, sticky="e")

        # Radiobutton.
        self.boton_tema1 = Radiobutton(
            self.root,
            text="Tema 1",
            value="1",
            fg="red",
            command=lambda: temas.tema1(
                self,
                self.root,
                self.titulo,
                self.descripcion,
                self.boton_tema1,
                self.boton_tema2,
                self.boton_tema3
            ),
            background="AntiqueWhite2"
        )
        self.boton_tema1.grid(column=0, row=7, columnspan=4, sticky="nsew")

        self.boton_tema2 = Radiobutton(
            self.root,
            text="Tema 2",
            value="2",
            fg="red",
            command=lambda: temas.tema2(
                self,
                self.root,
                self.titulo,
                self.descripcion,
                self.boton_tema1,
                self.boton_tema2,
                self.boton_tema3
            ),
            background="AntiqueWhite2"
        )

        self.boton_tema2.grid(column=0, row=8, columnspan=4, sticky="nsew")

        self.boton_tema3 = Radiobutton(
            self.root,
            text="Tema 3",
            value="3",
            fg="red",
            command=lambda: temas.tema3(
                self,
                self.root,
                self.titulo,
                self.descripcion,
                self.boton_tema1,
                self.boton_tema2,
                self.boton_tema3
            ),
            background="AntiqueWhite2"
        )
        self.boton_tema3.grid(column=0, row=9, columnspan=4, sticky="nsew")

        # Treeview.
        columnas = ("col_1", "col_2", "col_3", "col_4")
        self.tree = ttk.Treeview(self.root, columns=columnas, show="headings")

        self.tree.column("col_1", anchor=CENTER)
        self.tree.heading("col_1", text="ID")

        self.tree.column("col_2", anchor=CENTER)
        self.tree.heading("col_2", text="Título")

        self.tree.column("col_3", anchor=CENTER)
        self.tree.heading("col_3", text="Descripción")

        self.tree.column("col_4", anchor=CENTER)
        self.tree.heading("col_4", text="Mensaje")

        self.tree.grid(row=5, column=0, columnspan=4)

        scrollbar = ttk.Scrollbar(
            self.root,
            orient=VERTICAL,
            command=self.tree.yview
        )

        self.tree.configure(yscrollcommand=scrollbar.set)

        scrollbar.grid(row=5, column=5, sticky="ns")

        self.tree.bind("<Double-1>", self.on_tree_2click)
        self.tree.bind("<1>", self.on_tree_1click)

    def alta(self): 
        # Metodo de clase encargado de subir informacion a la base de datos.
        
        # Instancio a la clase mensaje para obtener estado.
        accion = Mensaje("Creado") 
        
        self.objeto_base.alta(
            self.tit,
            self.des,
            self.tree,
            accion
        )

        # Formateo los entrys.
        self.tit.delete(0, END)
        self.des.delete(0, END)

    def borrar(self): 
        # Metodo de clase encargado de eliminar informacion de la base de datos.
        
        self.objeto_base.baja(self.tit, self.tree)

        # Se formatea la app, se bloquean ('editar' y 'borrar')
        # y activan ('alta') botones, formatean entrys, borran labels.
        self.boton_alta.configure(state=NORMAL)
        self.boton_editar.configure(state=DISABLED)
        self.boton_borrar.configure(state=DISABLED)
        self.etiqueta_id.destroy()
        self.carga_id.destroy()
        self.tit.delete(0, END)
        self.des.delete(0, END)

    def modificar(self):
        # Metodo de clase encargado de modificar informacion de la base de datos.
        
        # Instancio a la clase mensaje para obtener estado.
        accion = Mensaje("Modificado")
        
        self.objeto_base.modificar(
            self.tit,
            self.des,
            self.tree,
            accion,
            self.tit_anterior
        )

        # Se formatea la app, se bloquean ('editar' y 'borrar')
        # y activan ('alta') botones, formatean entrys, borran labels.
        self.boton_alta.configure(state=NORMAL)
        self.boton_editar.configure(state=DISABLED)
        self.boton_borrar.configure(state=DISABLED)
        self.etiqueta_id.destroy()
        self.carga_id.destroy()
        self.tit.delete(0, END)
        self.des.delete(0, END)

    def actualizar(self):
        # Metodo de clase que me actualiza la vista del treeview cuando se abre la app
        # mostrandome todos los datos cargados en la base de datos.
        
        self.objeto_base.actualizar_treeview(self.tree)

    def on_tree_2click(self, event):
        # Metodo de clase, cuando se clickea dos veces en algun elemento del treview.
        try:
            item_seleccionado = self.tree.focus()
            valor_id = self.tree.item(item_seleccionado, "values")

            # Se crean etiquetas que referencian el ID del elemento seleccionado.
            self.etiqueta_id = Label(
                self.root,
                text="ID",
                relief="solid",
                borderwidth=2,
                width=5,
                font=10
            )
            self.etiqueta_id.grid(
                row=1,
                column=1,
                sticky="ns",
                rowspan=2
            )

            self.carga_id = Label(
                self.root,
                text=valor_id[0],
                relief="solid",
                borderwidth=2,
                width=5,
                font=10,
                fg="red"
            )
            self.carga_id.grid(
                row=1,
                column=1,
                sticky="nse",
                rowspan=2
            )

            # Se insertan en los entrys los datos del elemento.
            self.tit.insert(END, str(valor_id[1]))
            self.tit.focus_set()
            self.des.insert(END, str(valor_id[2]))
            
            # Obtenemos el nombre del titulo, previo a su modificacion.
            self.tit_anterior = self.tit.get()

            # Habilitamos los botones de 'borrar' y 'editar'
            # dehabilitamos el boton de 'alta'.
            self.boton_editar.configure(state=NORMAL)
            self.boton_borrar.configure(state=NORMAL)
            self.boton_alta.configure(state=DISABLED)
            
        except:
            showinfo("Seleccion incorrecta",
                     "Seleccione una noticia valida")

    def on_tree_1click(self, event):
        # Metodo de clase, cuando se clickea una vez en alguna parte del treeview
        # seformatea la app.
        
        try:
            self.boton_alta.configure(state=NORMAL)
            self.boton_editar.configure(state=DISABLED)
            self.boton_borrar.configure(state=DISABLED)
            self.etiqueta_id.destroy()
            self.carga_id.destroy()
            self.tit.delete(0, END)
            self.des.delete(0, END)
        except:
            pass
