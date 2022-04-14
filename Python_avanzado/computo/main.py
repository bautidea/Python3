from ast import NotIn
from tkinter import *
import re
from tkinter.messagebox import askyesno, showinfo
from tkinter.ttk import Labelframe, Treeview
from modelo import bdd
from objeto import Funciones


class programa():
    """
    Esta Clasee contiene a los demas modulos
    Es la clase principal encargada de ejecutar todos los metodos
    """

    def __init__(self, ventana):
        """
        El metodo init se ejecuta al iniciar la aplicacion
        Crea la grilla inicial y todos los elementos de la aplicacion
        """
        self.master = ventana

        self.master.title("Trabajo Final")

        # Marco de la app
        self.frame = Frame(self.master, padx = 5,pady = 5)
        self.frame.grid(column = 0, row = 0, padx = 5, pady = 5, columnspan= 2, sticky= 'nsw')
        
        # Marcos adicionales edicion y eliminacion de datos
        self.frame_editar = LabelFrame(
            self.master,
            text="Editar Datos",
            pady=5,
            padx=5
        )
        self.frame_editar.grid(
            column=0,
            row=1,
            padx=10,
            pady=10,
        )

        self.frame_borrar = LabelFrame(
            self.master,
            text="Borrar Datos",
            pady=5,
            padx=5
        )
        self.frame_borrar.grid(
            column=1,
            row=1,
            padx=10,
            pady=10
        )
        
        # Marco del treeview
        self.frame_treev = Frame(self.master, pady=5, padx=5)
        self.frame_treev.grid(column = 0, row = 2, columnspan= 3, pady = 5, padx = 5)

        # Etiquetas
        self.nombre = Label(
            self.frame,
            text="Nombre del edificio",
            anchor=W,
            justify=LEFT
        )
        self.nombre.grid(
            column=0,
            row=0,
            sticky="nsew",
            padx=10,
            pady=5
        )

        self.plantas = Label(
            self.frame,
            text="Plantas",
            anchor=W,
            justify=LEFT
        )
        self.plantas.grid(
            column=0,
            row=1,
            sticky="nsew",
            padx=10,
            pady=5
        )

        self.materiales = Label(
            self.frame,
            text="Materiales",
            justify=CENTER,
            borderwidth=2,
            relief="solid"
        )
        self.materiales.grid(
            column=0,
            row=2,
            sticky="nsew",
            padx=10,
            pady=5
        )

        self.hormigon = Label(
            self.frame,
            text="Hormigon",
            justify=CENTER
        )
        self.hormigon.grid(
            column=0,
            row=3,
            sticky="nsew",
            padx=10,
            pady=5
        )

        self.barras = Label(
            self.frame,
            text="Barras",
            anchor=W,
            justify=LEFT
        )
        self.barras.grid(
            column=0,
            row=4,
            columnspan=3,
            sticky="nsew",
            padx=10,
            pady=5
        )

        self.fi6 = Label(
            self.frame,
            text="Ø6",
            justify=CENTER
        )
        self.fi6.grid(
            column=0,
            row=5,
            sticky="snew",
            padx=10,
            pady=5
        )

        self.fi8 = Label(
            self.frame,
            text="Ø8",
            justify=CENTER
        )
        self.fi8.grid(
            column=0,
            row=6,
            sticky="snew",
            padx=10,
            pady=5
        )

        self.fi10 = Label(
            self.frame,
            text="Ø10",
            justify=CENTER
        )
        self.fi10.grid(
            column=0,
            row=7,
            sticky="snew",
            padx=10,
            pady=5
        )

        self.fi12 = Label(
            self.frame,
            text="Ø12",
            justify=CENTER
        )
        self.fi12.grid(
            column=0,
            row=8,
            sticky="snew",
            padx=10,
            pady=5
        )

        self.fi16 = Label(
            self.frame,
            text="Ø16",
            justify=CENTER
        )
        self.fi16.grid(
            column=0,
            row=9,
            sticky="snew",
            padx=10,
            pady=5
        )

        self.fi20 = Label(
            self.frame,
            text="Ø20",
            justify=CENTER
        )
        self.fi20.grid(
            column=0,
            row=10,
            sticky="snew",
            padx=10,
            pady=5
        )

        self.fi25 = Label(
            self.frame,
            text="Ø25",
            justify=CENTER
        )
        self.fi25.grid(
            column=0,
            row=11,
            sticky="snew",
            padx=10,
            pady=5
        )

        self.total = Label(
            self.frame,
            text="TOTAL",
            justify=CENTER
        )
        self.total.grid(
            column=1,
            row=2,
            sticky="nsew",
            padx=10,
            pady=5
        )

        # Entradas
        self.obra = Entry(
            self.frame,
            justify=CENTER
        )
        self.obra.grid(
            column=1,
            row=0,
            sticky="nsew",
            pady=2.5
        )

        self.tot_hormigon = Entry(
            self.frame,
            justify=CENTER,
            state="readonly"
        )
        self.tot_hormigon.grid(
            column=1,
            row=3,
            sticky="nsew"
        )

        self.tot_fi6 = Entry(
            self.frame,
            justify=CENTER,
            state="readonly"
        )
        self.tot_fi6.grid(
            column=1,
            row=5,
            sticky="nsew"
        )

        self.tot_fi8 = Entry(
            self.frame,
            justify=CENTER,
            state="readonly"
        )
        self.tot_fi8.grid(
            column=1,
            row=6,
            sticky="nsew"
        )

        self.tot_fi10 = Entry(
            self.frame,
            justify=CENTER,
            state="readonly"
        )
        self.tot_fi10.grid(
            column=1,
            row=7,
            sticky="nsew"
        )

        self.tot_fi12 = Entry(
            self.frame,
            justify=CENTER,
            state="readonly"
        )
        self.tot_fi12.grid(
            column=1,
            row=8,
            sticky="nsew"
        )

        self.tot_fi16 = Entry(
            self.frame,
            justify=CENTER,
            state="readonly"
        )
        self.tot_fi16.grid(
            column=1,
            row=9,
            sticky="nsew"
        )

        self.tot_fi20 = Entry(
            self.frame,
            justify=CENTER,
            state="readonly"
        )
        self.tot_fi20.grid(
            column=1,
            row=10,
            sticky="nsew"
        )

        self.tot_fi25 = Entry(
            self.frame,
            justify=CENTER,
            state="readonly"
        )
        self.tot_fi25.grid(
            column=1,
            row=11,
            sticky="nsew"
        )

        # Botones
        self.imp_datos = Button(
            self.frame,
            text="Imprimir datos",
            command=lambda: self.Imprimir_datos(),
            pady=5,
            padx=5
        )
        self.imp_datos.grid(
            column=2,
            row=0,
            rowspan=2,
            sticky="nsew",
            padx=10,
            pady=5
        )

        self.suma_datos = Button(
            self.frame,
            text="Sumar",
            command=lambda: self.Suma(),
            pady=5,
            padx=5
        )
        self.suma_datos.grid(
            column=2,
            row=2,
            rowspan=3,
            sticky="nsew",
            padx=10,
            pady=5
        )

        self.add_planta = Button(
            self.frame,
            text="Agregar Planta",
            command=lambda: self.Add_columna(),
            pady=5,
            padx=5
        )
        self.add_planta.grid(
            column=2,
            row=5,
            rowspan=4,
            sticky="nsew",
            padx=10,
            pady=5
        )

        # Botones del marco de edicion
        self.alta_datos = Button(
            self.frame_editar,
            text="Alta de datos",
            command=lambda: self.Alta(),
            justify=CENTER
        )
        self.alta_datos.grid(
            column=0,
            row=0,
            sticky="nsew",
            padx=5,
            pady=5
        )

        self.actualizar_registros = Button(
            self.frame_editar,
            text="Guardar Cambios",
            command=lambda: self.Modificacion(),
            justify=CENTER,
            state=DISABLED
        )
        self.actualizar_registros.grid(
            column=0,
            row=1,
            sticky="nsew",
            padx=5,
            pady=5
        )

        # Botones marco de borrar
        self.borrar_seleccion = Button(
            self.frame_borrar,
            text="Borrar seleccion",
            justify=CENTER,
            state=DISABLED,
            command=lambda: self.Eliminar_seleccion()
        )
        self.borrar_seleccion.grid(
            column=0,
            row=0,
            sticky="nsew",
            padx=5,
            pady=5
        )

        self.borrar_obra = Button(
            self.frame_borrar,
            text="Borrar Obra",
            justify=CENTER,
            command=lambda: self.Eliminar_obra(),
            state=DISABLED
        )
        self.borrar_obra.grid(
            column=0,
            row=1,
            sticky="nsew",
            padx=5,
            pady=5
        )

        # Treeview
        columnas = ('col_obra', 'col_plantas', 'col_info')
        
        self.tree = Treeview(self.frame_treev, columns= columnas, show= 'headings')
        self.tree.grid(column=0, row=0, columnspan=2)
        
        self.tree.heading('col_obra', text= 'Obra')
        self.tree.column('col_obra', anchor=CENTER)
        
        self.tree.heading('col_plantas', text= 'Nro de plantas')
        self.tree.column('col_plantas', anchor=CENTER)
        
        self.tree.heading('col_info', text= 'Informacion')
        self.tree.column('col_info', anchor=CENTER)
        
        tree_scrollbar = Scrollbar(self.frame_treev, orient = VERTICAL, command = self.tree.yview)
        self.tree.configure(yscrollcommand= tree_scrollbar.set)
        tree_scrollbar.grid(column = 2, row = 0, padx = 5, pady = 5,sticky = 'nse')
        
        # Al hacer doble click en algun elemento del treeview me carga los datos
        # corresponientes a la obra
        self.tree.bind('<Double-1>', self.Cargar_obra)
        
        # Al pusar la X para cerrar, llama a la funcion 'salir'
        self.master.protocol("WM_DELETE_WINDOW", self.Salir)
        
        # instanciaciones de las clases
        self.base_datos = bdd()
        self.func = Funciones()
        self.Actualizar_tree()

    def Salir(self):
        """
        Esta Funcion se utiliza para confirmar la salida del programa
        """
        self.func.Salir(self.master)

    def Add_columna(self):
        """
        Se ejecuta el metodo "suma"
        Añade una columna a la grilla 
        Se habilita el boton "eliminar ultima"
        Si no se cargaron obras de la base de datos se deshabilita la opcion para cargar obras de la base de datos
        """
        self.Suma()

        self.func.Add_columna(
            self.frame,
            self.add_planta,
            self.imp_datos,
            self.suma_datos,
            self.total,
            self.tot_hormigon,
            self.tot_fi6,
            self.tot_fi8,
            self.tot_fi10,
            self.tot_fi12,
            self.tot_fi16,
            self.tot_fi20,
            self.tot_fi25,
            self.materiales,
            self.borrar_seleccion
        )

    def Imprimir_datos(self):
        """
        Se ejecuta el metodo "suma"
        Crea un archivo de texto que contiene los datos de la obra cargada
        """
        self.Suma()

        self.func.Imprimir_datos(
            self.obra,
            self.tot_hormigon,
            self.tot_fi6,
            self.tot_fi8,
            self.tot_fi10,
            self.tot_fi12,
            self.tot_fi16,
            self.tot_fi20,
            self.tot_fi25
        )

    def Suma(self):
        """
        Suma todos los materiales de la obra para obtener un total de cada material
        """
        self.func.Suma(
            self.tot_hormigon,
            self.tot_fi6,
            self.tot_fi8,
            self.tot_fi10,
            self.tot_fi12,
            self.tot_fi16,
            self.tot_fi20,
            self.tot_fi25
        )

    def Alta(self):
        """
        Antes de realizar la importacion ejecuta el metodo "suma"
        Importa la obra a la base de datos
        Al realizar la importacion con exito resetea la grilla e elimina los datos
        """

        self.Suma()

        # Verificamos que el nombre de la obra este todo en minusculas y sin espacios, antes de importar losd datos a la tabla
        # Usamos regex para verificar que la obra sea escrita en minusucla, para recuperar datos de manera mas facil
        cadena = str(self.obra.get())
        patron = "[a-z_0-9]"

        obra_presente = self.base_datos.Consultar_obra()

        if cadena not in obra_presente:
            if (re.match(patron, cadena)):
                # Mensaje para avisar si esta seguro de la importacion de registros
                if askyesno("Eliminacion de datos",
                            "Se eliminaran todos los campos actuales para realizar la accion, esta seguro?"):

                    self.base_datos.Alta(
                        self.obra,
                        self.tot_hormigon,
                        self.tot_fi6,
                        self.tot_fi8,
                        self.tot_fi10,
                        self.tot_fi12,
                        self.tot_fi16,
                        self.tot_fi20,
                        self.tot_fi25,
                        self.func.entradas_plantas,
                        self.func.entradas_hormigon,
                        self.func.entradas_fi6,
                        self.func.entradas_fi8,
                        self.func.entradas_fi10,
                        self.func.entradas_fi12,
                        self.func.entradas_fi16,
                        self.func.entradas_fi20,
                        self.func.entradas_fi25
                    )

                    self.func.Limpiar_pantalla(
                        self.obra,
                        self.tot_hormigon,
                        self.tot_fi6,
                        self.tot_fi8,
                        self.tot_fi10,
                        self.tot_fi12,
                        self.tot_fi16,
                        self.tot_fi20,
                        self.tot_fi25,
                        self.total,
                        self.add_planta,
                        self.imp_datos,
                        self.suma_datos,
                        self.materiales,
                        self.actualizar_registros,
                        self.borrar_obra,
                        self.borrar_seleccion
                    )
                    
                    self.Actualizar_tree()
                    
            else:  # Si el nombre de la obra no esta escrito con los caracteres especificados me avisa de ello y no me deja importar los registros
                showinfo("Fallo en importacion",
                         "Fallo al subir los registros a la tabla, el nombre del edificio debe ser escrito todo en minuscula y sin espacios")
        else:
            showinfo("Error al importar obra",
                     "No se pudo importar la obra, ya hay una obra con el mismo nombre")

    def Actualizar_tree(self):
        """
        Actualiza el treeview para poder visualizar las obras cargadas
        """

        resultado = self.base_datos.Consultar_obra()
        self.func.Actualizar_tree(self.tree, resultado)

    def Cargar_obra(self, event):
        """
        Antes de  cargar la obra elimina los datos que estan en la grilla
        Carga en la grilla la obra solicitada por el usuario
        """

        # Mensaje para avisar si esta seguro de la accion a ejecutar
        if askyesno("Eliminacion de datos",
                    "Se eliminaran todos los campos actuales para realizar la accion, esta seguro?"):

            resultado = self.base_datos.Consultar_bdd()
            
            valores_tree = self.tree.item(self.tree.focus(),'values')
            obra_acargar = valores_tree[0]

            self.func.Limpiar_pantalla(
                self.obra,
                self.tot_hormigon,
                self.tot_fi6,
                self.tot_fi8,
                self.tot_fi10,
                self.tot_fi12,
                self.tot_fi16,
                self.tot_fi20,
                self.tot_fi25,
                self.total,
                self.add_planta,
                self.imp_datos,
                self.suma_datos,
                self.materiales,
                self.actualizar_registros,
                self.borrar_obra,
                self.borrar_seleccion
            )

            self.func.Cargar_obra(
                resultado,
                obra_acargar,                
                self.frame,
                self.add_planta,
                self.imp_datos,
                self.suma_datos,
                self.total,
                self.tot_hormigon,
                self.tot_fi6,
                self.tot_fi8,
                self.tot_fi10,
                self.tot_fi12,
                self.tot_fi16,
                self.tot_fi20,
                self.tot_fi25,
                self.materiales,
                self.obra,
                self.actualizar_registros,
                self.borrar_obra,
                self.alta_datos,
                self.borrar_seleccion
            )
            self.Actualizar_tree()

    def Modificacion(self):
        """
        Se modifican los datos de la obra cargada de la base de datos
        Permite editar y agregar columnas en una obra ya cargada
        Para luego guardarla de nuevo
        Al terminar la edicion se reseteara y eliminaran los datos de la grilla
        """

        # Mensaje para avisar si esta seguro de la accion a ejecutar
        if askyesno("Eliminacion de datos",
                    "Se eliminaran todos los campos actuales para realizar la accion, esta seguro?"):
            self.Suma()

            ep = self.func.entradas_plantas
            eh = self.func.entradas_hormigon
            e6 = self.func.entradas_fi6
            e8 = self.func.entradas_fi8
            e10 = self.func.entradas_fi10
            e12 = self.func.entradas_fi12
            e16 = self.func.entradas_fi16
            e20 = self.func.entradas_fi20
            e25 = self.func.entradas_fi25
            epid = self.func.entradas_plantasid
            etid = self.func.entradas_totalid

            self.base_datos.Modificacion(
                self.obra,
                ep,
                eh,
                e6,
                e8,
                e10,
                e12,
                e16,
                e20,
                e25,
                epid,
                self.tot_hormigon,
                self.tot_fi6,
                self.tot_fi8,
                self.tot_fi10,
                self.tot_fi12,
                self.tot_fi16,
                self.tot_fi20,
                self.tot_fi25,
                etid
            )

            self.func.Limpiar_pantalla(
                self.obra,
                self.tot_hormigon,
                self.tot_fi6,
                self.tot_fi8,
                self.tot_fi10,
                self.tot_fi12,
                self.tot_fi16,
                self.tot_fi20,
                self.tot_fi25,
                self.total,
                self.add_planta,
                self.imp_datos,
                self.suma_datos,
                self.materiales,
                self.actualizar_registros,
                self.borrar_obra,
                self.borrar_seleccion
            )
            self.Actualizar_tree()
            
            # Habilito el boton de alta de datos
            self.alta_datos.config(state = NORMAL)

    def Eliminar_obra(self):
        """
        Elimina la obra que se cargo previamente de la base de datos
        """

        if askyesno("Eliminar obra", "Esta seguro que desea remover la obra de la base de datos?"):
            self.base_datos.Eliminar_obra(self.obra)
            
            self.func.Limpiar_pantalla(
                self.obra,
                self.tot_hormigon,
                self.tot_fi6,
                self.tot_fi8,
                self.tot_fi10,
                self.tot_fi12,
                self.tot_fi16,
                self.tot_fi20,
                self.tot_fi25,
                self.total,
                self.add_planta,
                self.imp_datos,
                self.suma_datos,
                self.materiales,
                self.actualizar_registros,
                self.borrar_obra,
                self.borrar_seleccion
            )
            self.Actualizar_tree()
            self.alta_datos.config(state=NORMAL)
    
    def Eliminar_seleccion(self):
        
        if askyesno("Eliminar seleccion", "Los elementos seleccionados tambien seran eliminados de la base de datos, proceder de igual manera?"):
            id_a_eliminar = self.func.Eliminar_seleccion(
                            self.add_planta,
                            self.imp_datos,
                            self.suma_datos,
                            self.total,
                            self.tot_hormigon,
                            self.tot_fi6,
                            self.tot_fi8,
                            self.tot_fi10,
                            self.tot_fi12,
                            self.tot_fi16,
                            self.tot_fi20,
                            self.tot_fi25,
                            self.materiales
                        )
            
            self.base_datos.Eliminar_seleccion(id_a_eliminar)
            
            self.Actualizar_tree()
            self.Suma()


if __name__ == "__main__":

    master_tk = Tk()

    app = programa(master_tk)

    master_tk.mainloop()
