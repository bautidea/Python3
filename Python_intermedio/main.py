from tkinter import *
import re
from tkinter.messagebox import askyesno, showinfo
from modelo import bdd
from objeto import funciones
from objeto import consultar_registros


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

        # Marcos adicionales edicion y eliminacion de datos
        self.frame_editar = LabelFrame(
            self.master,
            text="Editar Datos",
            pady=5,
            padx=5
        )
        self.frame_editar.grid(
            column=0,
            row=12,
            padx=10,
            pady=10
        )

        self.frame_borrar = LabelFrame(
            self.master,
            text="Borrar Datos",
            pady=5,
            padx=5
        )
        self.frame_borrar.grid(
            column=0,
            row=13,
            padx=10,
            pady=10
        )

        # Etiquetas
        self.nombre = Label(
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

        self.fi20 = Label(
            text="Ø25",
            justify=CENTER
        )
        self.fi20.grid(
            column=0,
            row=11,
            sticky="snew",
            padx=10,
            pady=5
        )

        self.total = Label(
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

        # Etiquetas del marco de edicion
        self.editar_obra = Label(
            self.frame_editar,
            text="Obra",
            justify=CENTER)
        self.editar_obra.grid(
            column=0,
            row=0,
            sticky="nsew",
            padx=5,
            pady=5
        )

        # Etiquetas del marco de borrar
        self.borrar_planta = Label(
            self.frame_borrar,
            text="Planta",
            justify=CENTER)
        self.borrar_planta.grid(
            column=0,
            row=0,
            sticky="nsew",
            padx=5,
            pady=5
        )

        # Entradas
        self.obra = Entry(
            self.master,
            justify=CENTER
        )
        self.obra.grid(
            column=1,
            row=0,
            sticky="nsew",
            pady=2.5
        )

        self.tot_hormigon = Entry(
            self.master,
            justify=CENTER,
            state="readonly"
        )
        self.tot_hormigon.grid(
            column=1,
            row=3,
            sticky="nsew"
        )

        self.tot_fi6 = Entry(
            self.master,
            justify=CENTER,
            state="readonly"
        )
        self.tot_fi6.grid(
            column=1,
            row=5,
            sticky="nsew"
        )

        self.tot_fi8 = Entry(
            self.master,
            justify=CENTER,
            state="readonly"
        )
        self.tot_fi8.grid(
            column=1,
            row=6,
            sticky="nsew"
        )

        self.tot_fi10 = Entry(
            self.master,
            justify=CENTER,
            state="readonly"
        )
        self.tot_fi10.grid(
            column=1,
            row=7,
            sticky="nsew"
        )

        self.tot_fi12 = Entry(
            self.master,
            justify=CENTER,
            state="readonly"
        )
        self.tot_fi12.grid(
            column=1,
            row=8,
            sticky="nsew"
        )

        self.tot_fi16 = Entry(
            self.master,
            justify=CENTER,
            state="readonly"
        )
        self.tot_fi16.grid(
            column=1,
            row=9,
            sticky="nsew"
        )

        self.tot_fi20 = Entry(
            self.master,
            justify=CENTER,
            state="readonly"
        )
        self.tot_fi20.grid(
            column=1,
            row=10,
            sticky="nsew"
        )

        self.tot_fi25 = Entry(
            self.master,
            justify=CENTER,
            state="readonly"
        )
        self.tot_fi25.grid(
            column=1,
            row=11,
            sticky="nsew"
        )

        # Entradas del marco de edicion
        self.entrada_editar = Entry(
            self.frame_editar,
            justify=CENTER
        )
        self.entrada_editar.grid(
            column=1,
            row=0,
            sticky="nsew",
            padx=5,
            pady=5
        )

        # Entradas del marco de borrar
        self.entrada_borrar = Entry(
            self.frame_borrar,
            justify=CENTER,
            state="readonly",
        )
        self.entrada_borrar.grid(
            column=1,
            row=0,
            sticky="nsew",
            padx=5,
            pady=5
        )

        # Botones
        self.imp_datos = Button(
            self.master,
            text="Imprimir datos",
            command=lambda: self.imprimir_datos(),
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
            self.master,
            text="Sumar",
            command=lambda: self.suma(),
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
            self.master,
            text="Agregar Planta",
            command=lambda: self.add_columna(),
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

        self.del_planta = Button(
            self.master,
            text="Eliminar Ultima",
            command=lambda: self.eliminar_ultima(),
            pady=5,
            padx=5,
            state=DISABLED
        )
        self.del_planta.grid(
            column=2,
            row=9,
            rowspan=3,
            sticky="nsew",
            padx=10,
            pady=5
        )

        # Botones del marco de edicion
        self.cargar_obra = Button(
            self.frame_editar,
            text="Cargar",
            command=lambda: self.exportar_obra(),
            justify=CENTER
        )
        self.cargar_obra.grid(
            column=0,
            row=1,
            columnspan=2,
            sticky="nsew",
            padx=5,
            pady=5
        )

        self.actualizar_registros = Button(
            self.frame_editar,
            text="Guardar Cambios",
            command=lambda: self.modif_reg(),
            justify=CENTER,
            state=DISABLED
        )
        self.actualizar_registros.grid(
            column=0,
            row=2,
            columnspan=2,
            sticky="nsew",
            padx=5,
            pady=5
        )

        # Botones marco de borrar
        self.borrar_planta = Button(
            self.frame_borrar,
            text="Borrar",
            justify=CENTER,
            state=DISABLED,
            command=lambda: self.eliminar_planta()
        )
        self.borrar_planta.grid(
            column=0,
            row=1,
            columnspan=2,
            sticky="nsew",
            padx=5,
            pady=5
        )

        self.borrar_obra = Button(
            self.frame_borrar,
            text="Borrar Obra",
            justify=CENTER,
            command=lambda: self.eliminar_obra(),
            state=DISABLED
        )
        self.borrar_obra.grid(
            column=0,
            row=2,
            columnspan=2,
            sticky="nsew",
            padx=5,
            pady=5
        )

        self.menubar = Menu(self.master)
        self.master.config(menu=self.menubar)

        self.archivo_menu = Menu(
            self.menubar,
            tearoff=0
        )

        self.archivo_menu.add_command(
            label="Importar registros a base de datos",
            command=lambda: self.importar_registros()
        )

        self.archivo_menu.add_command(
            label="Consultar Registros",
            command=lambda: self.consultar_registros()
        )

        self.archivo_menu.add_separator()

        self.archivo_menu.add_command(
            label="Salir",
            command=lambda: self.salir()
        )

        self.menubar.add_cascade(
            label="Archivo",
            menu=self.archivo_menu
        )
        self.master.protocol("WM_DELETE_WINDOW", self.salir)

        self.base_datos = bdd(ventana)
        self.func = funciones()

        self.base_datos.crear_tabla()

    def salir(self):
        """
        Esta Funcion se utiliza para confirmar la salida del programa
        """
        self.func.salir(self.master)

    def add_columna(self):
        """
        Se ejecuta el metodo "suma"
        Añade una columna a la grilla 
        Se habilita el boton "eliminar ultima"
        Si no se cargaron obras de la base de datos se deshabilita la opcion para cargar obras de la base de datos
        """
        self.suma()

        self.func.add_columna(
            self.master,
            self.add_planta,
            self.del_planta,
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
        )

        # Habilito la opcion para eliminar la ultima planta agregada
        self.del_planta.config(state=NORMAL)

        if not self.func.entradas_plantasid:  # En caso de que no haya alguna obra cargada, se deshabilita la opcion para cargar datos
            self.cargar_obra.config(state=DISABLED)
            self.entrada_editar.config(state="readonly")

    def imprimir_datos(self):
        """
        Se ejecuta el metodo "suma"
        Crea un archivo de texto que contiene los datos de la obra cargada
        """
        self.suma()

        self.func.imprimir_datos(
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

    def suma(self):
        """
        Suma todos los materiales de la obra para obtener un total de cada material
        """
        self.func.suma(
            self.tot_hormigon,
            self.tot_fi6,
            self.tot_fi8,
            self.tot_fi10,
            self.tot_fi12,
            self.tot_fi16,
            self.tot_fi20,
            self.tot_fi25
        )

    def importar_registros(self):
        """
        Antes de realizar la importacion ejecuta el metodo "suma"
        Importa la obra a la base de datos
        Al realizar la importacion con exito resetea la grilla e elimina los datos
        """

        self.suma()

        # Verificamos que el nombre de la obra este todo en minusculas y sin espacios, antes de importar losd datos a la tabla
        # Usamos regex para verificar que la obra sea escrita en minusucla, para recuperar datos de manera mas facil
        cadena = str(self.obra.get())
        patron = "[a-z_0-9]"

        self.base_datos.consultar_obra(self.obra)

        if not self.base_datos.obra_presente:
            if (re.match(patron, cadena)):
                # Mensaje para avisar si esta seguro de la importacion de registros
                if askyesno("Eliminacion de datos",
                            "Se eliminaran todos los campos actuales para realizar la accion, esta seguro?"):

                    self.base_datos.importar_registros(
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

                    self.func.limpiar_pantalla(
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
                        self.del_planta,
                        self.imp_datos,
                        self.suma_datos,
                        self.materiales,
                        self.entrada_editar,
                        self.cargar_obra,
                        self.actualizar_registros,
                        self.entrada_borrar,
                        self.borrar_planta,
                        self.borrar_obra,
                    )
            else:  # Si el nombre de la obra no esta escrito con los caracteres especificados me avisa de ello y no me deja importar los registros
                showinfo("Fallo en importacion",
                         "Fallo al subir los registros a la tabla, el nombre del edificio debe ser escrito todo en minuscula y sin espacios")
        else:
            showinfo("Error al importar obra",
                     "No se pudo importar la obra, ya hay una obra con el mismo nombre")

    def consultar_registros(self):
        """
        Abre una ventana en la cual se puede consultar los datos cargados en la base de datos
        """

        self.consulta = consultar_registros()
        resultado = self.base_datos.consultar_bdd()

        self.consulta.actualizar_datos(resultado)

        self.consulta.actualizar_consu.config(command=self.act_datos)

    def act_datos(self):
        """
        Actualiza los datos que se muestran en la ventana de consulta
        """

        resultado = self.base_datos.consultar_bdd()

        self.consulta.actualizar_datos(resultado)

    def exportar_obra(self):
        """
        Antes de  cargar la obra elimina los datos que estan en la grilla
        Carga en la grilla la obra solicitada por el usuario
        """

        # Mensaje para avisar si esta seguro de la accion a ejecutar
        if askyesno("Eliminacion de datos",
                    "Se eliminaran todos los campos actuales para realizar la accion, esta seguro?"):

            resultado = self.base_datos.consultar_bdd()

            self.func.limpiar_pantalla(
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
                self.del_planta,
                self.imp_datos,
                self.suma_datos,
                self.materiales,
                self.entrada_editar,
                self.cargar_obra,
                self.actualizar_registros,
                self.entrada_borrar,
                self.borrar_planta,
                self.borrar_obra,
            )

            self.func.exportar_obra(
                resultado,
                self.entrada_editar,
                self.master,
                self.add_planta,
                self.del_planta,
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
                self.cargar_obra,
                self.actualizar_registros,
                self.entrada_borrar,
                self.borrar_planta,
                self.borrar_obra,

            )

    def modif_reg(self):
        """
        Se modifican los datos de la obra cargada de la base de datos
        Permite editar y agregar columnas en una obra ya cargada
        Para luego guardarla de nuevo
        Al terminar la edicion se reseteara y eliminaran los datos de la grilla
        """

        # Mensaje para avisar si esta seguro de la accion a ejecutar
        if askyesno("Eliminacion de datos",
                    "Se eliminaran todos los campos actuales para realizar la accion, esta seguro?"):
            self.suma()

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

            self.base_datos.modificar_registros(
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

            self.func.limpiar_pantalla(
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
                self.del_planta,
                self.imp_datos,
                self.suma_datos,
                self.materiales,
                self.entrada_editar,
                self.cargar_obra,
                self.actualizar_registros,
                self.entrada_borrar,
                self.borrar_planta,
                self.borrar_obra
            )

    def eliminar_planta(self):
        """
        Elimina la planta especificada en el cuadro de entrada del marco de "Borrar Datos"
        """

        contador = 0
        # Si El cuadro de entrada esta vacio no se ejecutaria la funcion
        if self.entrada_borrar.get() != "" and self.obra.get() != self.entrada_borrar.get():
            for i in self.func.entradas_plantas:
                if i.get() == self.entrada_borrar.get():
                    elemento = self.func.elemento_eliminar(self.entrada_borrar)

                    self.base_datos.eliminar_planta(
                        elemento,
                        self.entrada_borrar,
                        self.obra
                    )

                    self.func.eliminar_planta(self.entrada_borrar)
                    contador += 1
                    self.suma()

            if contador == 0:
                showinfo("Fallo al eliminar planta",
                         "No se pudo encontrar el nombre de la planta solicitada")
                self.entrada_borrar.delete(0, END)
        else:
            showinfo("Fallo al eliminar planta",
                     "Usted no ingreso una planta valida de la obra " + self.obra.get())
            self.entrada_borrar.delete(0, END)

    def eliminar_obra(self):
        """
        Elimina la obra que se cargo previamente de la base de datos
        """

        if askyesno("Eliminar obra", "Esta seguro que desea remover la obra de la base de datos?"):
            self.base_datos.eliminar_obra(self.obra)
            self.func.limpiar_pantalla(
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
                self.del_planta,
                self.imp_datos,
                self.suma_datos,
                self.materiales,
                self.entrada_editar,
                self.cargar_obra,
                self.actualizar_registros,
                self.entrada_borrar,
                self.borrar_planta,
                self.borrar_obra
            )

    def eliminar_ultima(self):
        """
        Elimina la ultima columna de la grilla si esta no esta cargada en la base de datos
        No se puede eliminar la planta de una obra cargada en la base de datos
        Una vez eliminada ejecuta el metodo "suma" para actualizar el total
        """

        self.func.eliminar_ultima(
            self.entrada_editar,
            self.cargar_obra,
            self.add_planta,
            self.del_planta,
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
            self.entrada_borrar,
            self.borrar_planta,
            self.borrar_obra,
        )

        self.suma()


if __name__ == "__main__":

    master_tk = Tk()

    app = programa(master_tk)

    master_tk.mainloop()
