from tkinter import *
import tkinter as tk
from tkinter.messagebox import *
import os


class funciones():
    """
    Esta clase esta encargada del funcionamiento de la aplicacion 
    Y las tareas que realiza cada boton
    """

    def __init__(self):
        """
        Al instanciarse esta clase se crean las listas que contendran los entrys de la aplicacion
        Estos entrys contendran los datos de cada obra
        """

        self.entradas_plantas = []
        self.entradas_hormigon = []
        self.entradas_fi6 = []
        self.entradas_fi8 = []
        self.entradas_fi10 = []
        self.entradas_fi12 = []
        self.entradas_fi16 = []
        self.entradas_fi20 = []
        self.entradas_fi25 = []
        self.entradas_totales = []
        self.entradas_plantasid = []
        self.entradas_totalid = []

        self.contador_columnas = 0

    def salir(self, salida):
        """
        Modulo que se encarga de preguntar si desea finalizar la ejecucion del programa
        """

        if askyesno("Finalizar Ejecucion", "desea salir del programa?"):
            salida.destroy()

    def add_columna(self, app, ap, dp, imd, sd, t, th, t6, t8, t10, t12, t16, t20, t25, mat):
        """
        Agrega una columna a la grilla, agregando los datos a las listas creadas
        """

        # Al pulsar el boton de agregar planta se añadiran una fila de columnas
        # Creamos entrys en la columna siguente
        self.ent_planta = Entry(
            app,
            justify=CENTER,
        )
        self.ent_planta.grid(
            column=(self.contador_columnas + 1),
            row=1,
            sticky="nsew"
        )

        self.ent_hormigon = Entry(
            app,
            justify=CENTER
        )
        self.ent_hormigon.grid(
            column=(self.contador_columnas + 1),
            row=3,
            sticky="nsew"
        )

        self.ent_fi6 = Entry(
            app,
            justify=CENTER
        )
        self.ent_fi6.grid(
            column=(self.contador_columnas + 1),
            row=5,
            sticky="nsew"
        )

        self.ent_fi8 = Entry(
            app,
            justify=CENTER
        )
        self.ent_fi8.grid(
            column=(self.contador_columnas + 1),
            row=6,
            sticky="nsew"
        )

        self.ent_fi10 = Entry(
            app,
            justify=CENTER
        )
        self.ent_fi10.grid(
            column=(self.contador_columnas + 1),
            row=7,
            sticky="nsew"
        )

        self.ent_fi12 = Entry(
            app,
            justify=CENTER
        )
        self.ent_fi12.grid(
            column=(self.contador_columnas + 1),
            row=8,
            sticky="nsew"
        )

        self.ent_fi16 = Entry(
            app,
            justify=CENTER
        )
        self.ent_fi16.grid(
            column=(self.contador_columnas + 1),
            row=9,
            sticky="nsew"
        )

        self.ent_fi20 = Entry(
            app,
            justify=CENTER
        )
        self.ent_fi20.grid(
            column=(self.contador_columnas + 1),
            row=10,
            sticky="nsew"
        )

        self.ent_fi25 = Entry(
            app,
            justify=CENTER
        )
        self.ent_fi25.grid(
            column=(self.contador_columnas + 1),
            row=11,
            sticky="nsew"
        )

        # Movemos junto con la creacion de los entrys los botones y labels
        ap.grid(column=self.contador_columnas+3)
        dp.grid(column=self.contador_columnas+3)
        imd.grid(column=self.contador_columnas+3)
        sd.grid(column=self.contador_columnas+3)

        t.grid(column=self.contador_columnas+2)
        th.grid(column=self.contador_columnas+2)
        t6.grid(column=self.contador_columnas+2)
        t8.grid(column=self.contador_columnas+2)
        t10.grid(column=self.contador_columnas+2)
        t12.grid(column=self.contador_columnas+2)
        t16.grid(column=self.contador_columnas+2)
        t20.grid(column=self.contador_columnas+2)
        t25.grid(column=self.contador_columnas+2)

        mat.grid(columnspan=self.contador_columnas+2)

        # Aniadimos los datos de las entradas a las listas, asi de esa manera luego podremos recuperar la informacion
        self.entradas_plantas.append(self.ent_planta)
        self.entradas_hormigon.append(self.ent_hormigon)
        self.entradas_fi6.append(self.ent_fi6)
        self.entradas_fi8.append(self.ent_fi8)
        self.entradas_fi10.append(self.ent_fi10)
        self.entradas_fi12.append(self.ent_fi12)
        self.entradas_fi16.append(self.ent_fi16)
        self.entradas_fi20.append(self.ent_fi20)
        self.entradas_fi25.append(self.ent_fi25)

        self.entradas_totales.extend([
            self.ent_planta,
            self.ent_hormigon,
            self.ent_fi6,
            self.ent_fi8,
            self.ent_fi10,
            self.ent_fi12,
            self.ent_fi16,
            self.ent_fi20,
            self.ent_fi25
        ])

        self.contador_columnas += 1

    def imprimir_datos(self, obra, th, t6, t8, t10, t12, t16, t20, t25):
        """
        Imprime en un archivo de texto los datos de la obra cargada en la planilla
        Crea el archivo de texto con el nombre de la obra e imprime la informacion en el
        """

        # Con esta funcion imprimiremos las datos en un archivo de texto
        nom = ("\\Computos_" + str(obra.get()) + ".txt")
        ruta = os.path.dirname(os.path.abspath(__file__))+nom
        log = open(ruta, "w")

        print(
            "####################################################################", file=log)
        print("NOMBRE DEL EDIFICIO: " + str(obra.get()), file=log)

        pos = 0
        # Ya que todas las listas tienen la misma longitud obtenemos el rango de la entrada de plantas, para que vaya iterando
        for i in range(0, len(self.entradas_plantas)):
            # print("####################################################################")
            print(
                "PLANTA: ",
                str(self.entradas_plantas[pos].get()),
                " - ",
                "HORMIGON [m3]: ",
                str(self.entradas_hormigon[pos].get()),
                " - ",
                "BARRAS Ø6 [m]: ",
                str(self.entradas_fi6[pos].get()),
                " - ",
                "BARRAS Ø8 [m]: ",
                str(self.entradas_fi8[pos].get()),
                " - ",
                "BARRAS Ø10 [m]: ",
                str(self.entradas_fi10[pos].get()),
                " - ",
                "BARRAS Ø12 [m]: ",
                str(self.entradas_fi12[pos].get()),
                " - ",
                "BARRAS Ø16 [m]: ",
                str(self.entradas_fi16[pos].get()),
                " - ",
                "BARRAS Ø20 [m]: ",
                str(self.entradas_fi20[pos].get()),
                " - ",
                "BARRAS Ø25 [m]: ",
                str(self.entradas_fi25[pos].get()),
                file=log
            )

            pos += 1

        print(
            "TOTAL: ",
            " - ",
            "HORMIGON [m3]: ",
            str(th.get()),
            " - ",
            "BARRAS Ø6 [m]: ",
            str(t6.get()),
            " - ",
            "BARRAS Ø8 [m]: ",
            str(t8.get()),
            " - ",
            "BARRAS Ø10 [m]: ",
            str(t10.get()),
            " - ",
            "BARRAS Ø12 [m]: ",
            str(t12.get()),
            " - ",
            "BARRAS Ø16 [m]: ",
            str(t16.get()),
            " - ",
            "BARRAS Ø20 [m]: ",
            str(t20.get()),
            " - ",
            "BARRAS Ø25 [m]: ",
            str(t25.get()),
            file=log
        )

        print(
            "####################################################################", file=log)

        showinfo("REGISTRO CREADO",
                 "Se creo un archivo llamado Computos_" + str(obra.get()))

    def suma(self, th, t6, t8, t10, t12, t16, t20, t25):
        """
        Suma los datos de la planilla para obtener un total de cada material
        """

        total_hormigon = 0
        total_fi6 = 0
        total_fi8 = 0
        total_fi10 = 0
        total_fi12 = 0
        total_fi16 = 0
        total_fi20 = 0
        total_fi25 = 0

        for hormigon in self.entradas_hormigon:
            if hormigon.get() != "":
                total_hormigon = total_hormigon + float(hormigon.get())

        for fi6 in self.entradas_fi6:
            if fi6.get() != "":
                total_fi6 = total_fi6 + float(fi6.get())

        for fi8 in self.entradas_fi8:
            if fi8.get() != "":
                total_fi8 = total_fi8 + float(fi8.get())

        for fi10 in self.entradas_fi10:
            if fi10.get() != "":
                total_fi10 = total_fi10 + float(fi10.get())

        for fi12 in self.entradas_fi12:
            if fi12.get() != "":
                total_fi12 = total_fi12 + float(fi12.get())

        for fi16 in self.entradas_fi16:
            if fi16.get() != "":
                total_fi16 = total_fi16 + float(fi16.get())

        for fi20 in self.entradas_fi20:
            if fi20.get() != "":
                total_fi20 = total_fi20 + float(fi20.get())

        for fi25 in self.entradas_fi25:
            if fi25.get() != "":
                total_fi25 = total_fi25 + float(fi25.get())

        var_horm = tk.StringVar()
        th.config(textvariable=var_horm)
        var_horm.set(total_hormigon)

        var_fi6 = tk.StringVar()
        t6.config(textvariable=var_fi6)
        var_fi6.set(total_fi6)

        var_fi8 = tk.StringVar()
        t8.config(textvariable=var_fi8)
        var_fi8.set(total_fi8)

        var_fi10 = tk.StringVar()
        t10.config(textvariable=var_fi10)
        var_fi10.set(total_fi10)

        var_fi12 = tk.StringVar()
        t12.config(textvariable=var_fi12)
        var_fi12.set(total_fi12)

        var_fi16 = tk.StringVar()
        t16.config(textvariable=var_fi16)
        var_fi16.set(total_fi16)

        var_fi20 = tk.StringVar()
        t20.config(textvariable=var_fi20)
        var_fi20.set(total_fi20)

        var_fi25 = tk.StringVar()
        t25.config(textvariable=var_fi25)
        var_fi25.set(total_fi25)

    def limpiar_pantalla(self, obra, th, t6, t8, t10, t12, t16, t20, t25, t, ap, dp, imd, sd, mat, ed, co, ar, eb, bp, bo):
        """
        Se limpia la pantalla y resetea la grilla luego de realizar determinada accion
        """

        # Limpiamos y borramos los registros luego de su importacion
        for entradas in self.entradas_totales:
            entradas.delete(0, END)

        obra.delete(0, END)

        th.config(state=NORMAL)
        th.delete(0, END)
        th.config(state="readonly")

        t6.config(state=NORMAL)
        t6.delete(0, END)
        t6.config(state="readonly")

        t8.config(state=NORMAL)
        t8.delete(0, END)
        t8.config(state="readonly")

        t10.config(state=NORMAL)
        t10.delete(0, END)
        t10.config(state="readonly")

        t12.config(state=NORMAL)
        t12.delete(0, END)
        t12.config(state="readonly")

        t16.config(state=NORMAL)
        t16.delete(0, END)
        t16.config(state="readonly")

        t20.config(state=NORMAL)
        t20.delete(0, END)
        t20.config(state="readonly")

        t25.config(state=NORMAL)
        t25.delete(0, END)
        t25.config(state="readonly")

        ed.config(state="normal")  # Desbloqueo el cuadro de busqueda
        # Vuelvo a activar el boton para cargar una obra nueva
        co.config(state=NORMAL)
        # Deshabilito el boton para actualizar registros
        ar.config(state=DISABLED)
        # Imposibilito la escritura en el entry de "borrar obra"
        eb.config(state="readonly")
        bp.config(state=DISABLED)  # Deshabilito el boton para borrar planta
        bo.config(state=DISABLED)  # Deshabilito el boton para borrar obra

        dp.config(state=DISABLED)

        for entradas in self.entradas_totales:
            entradas.destroy()

        # Movemos junto con la eliminacion de los entrys los botones y labels
        self.entradas_plantas = []
        self.entradas_hormigon = []
        self.entradas_fi6 = []
        self.entradas_fi8 = []
        self.entradas_fi10 = []
        self.entradas_fi12 = []
        self.entradas_fi16 = []
        self.entradas_fi20 = []
        self.entradas_fi25 = []
        self.entradas_totales = []
        self.entradas_plantasid = []
        self.entradas_totalid = []
        self.contador_columnas = 0

        ap.grid(column=2)
        dp.grid(column=2)
        imd.grid(column=2)
        sd.grid(column=2)

        t.grid(column=1)
        th.grid(column=1)
        t6.grid(column=1)
        t8.grid(column=1)
        t10.grid(column=1)
        t12.grid(column=1)
        t16.grid(column=1)
        t20.grid(column=1)
        t25.grid(column=1)

        mat.grid(columnspan=1)

    def exportar_obra(self, resultado, entrada_editar, app, ap, dp, imd, sd, t, th, t6, t8, t10, t12, t16, t20, t25, mat, obra, co, ar, eb, bp, bo):
        """
        Cuando se carga una obra de la base de datos este modulo se encarga de generar la grilla para esa obra
        Creando las columnas que tenia la obra y asignandole los datos
        """

        obra_acargar = str(entrada_editar.get())

        # Creo un contador para determinar si una obra tiene datos cargados
        contador_plantas = 0

        for i in resultado:  # Recorremos las tuplas dentro de la lista "resultado"

            # Filtramos los nombres de las obras y solamente obtenemos el nombre buscado
            if obra_acargar == i[1]:
                # Cargamos todos los valores de las plantas a excepcion de la planta de "TOTALES"
                if i[2] != "total":
                    self.add_columna(app, ap, dp, imd, sd, t,
                                     th, t6, t8, t10, t12, t16, t20, t25, mat)

                    self.ent_planta.insert(END, str(i[2]))
                    self.ent_hormigon.insert(END, str(i[3]))
                    self.ent_fi6.insert(END, str(i[4]))
                    self.ent_fi8.insert(END, str(i[5]))
                    self.ent_fi10.insert(END, str(i[6]))
                    self.ent_fi12.insert(END, str(i[7]))
                    self.ent_fi16.insert(END, str(i[8]))
                    self.ent_fi20.insert(END, str(i[9]))
                    self.ent_fi25.insert(END, str(i[10]))

                    self.entradas_plantasid.append(i[0])

                    self.contador_columnas += 1

                # Para el caso de la planta de "TOTALES" obtenemos sus datos de manera separada
                elif i[2] == "total":
                    th.config(state=NORMAL)
                    th.insert(END, str(i[3]))
                    th.config(state="readonly")

                    t6.config(state=NORMAL)
                    t6.insert(END, str(i[4]))
                    t6.config(state="readonly")

                    t8.config(state=NORMAL)
                    t8.insert(END, str(i[5]))
                    t8.config(state="readonly")

                    t10.config(state=NORMAL)
                    t10.insert(END, str(i[6]))
                    t10.config(state="readonly")

                    t12.config(state=NORMAL)
                    t12.insert(END, str(i[7]))
                    t12.config(state="readonly")

                    t16.config(state=NORMAL)
                    t16.insert(END, str(i[8]))
                    t16.config(state="readonly")

                    t20.config(state=NORMAL)
                    t20.insert(END, str(i[9]))
                    t20.config(state="readonly")

                    t25.config(state=NORMAL)
                    t25.insert(END, str(i[10]))
                    t25.config(state="readonly")

                    self.entradas_totalid.append(i[0])

                # Si llegara a cargar algun dato el contador aumenta y de esa manera se si se cargo algun dato
                contador_plantas += 1

        if contador_plantas >= 1:  # Si el contador aumento significa que cargo datos

            # El nombre de la obra cargada se mueve de lugar
            obra.insert(END, obra_acargar)

            # bloqueo el boton para cargar obras, asi de esa manera no se cargan obras de mas
            co.config(state=DISABLED)

            # Borro el contenido del cuadro de busqueda
            entrada_editar.delete(0, END)

            # Bloqueo el cuadro de busqueda
            entrada_editar.config(state="readonly")

            # Habilito el boton para modificar los registros de la base de datos
            ar.config(state=NORMAL)
            eb.config(state=NORMAL)
            bp.config(state=NORMAL)
            bo.config(state=NORMAL)

            # desabilito el boton para eliminar la ultima planta agregada
            dp.config(state=DISABLED)

        else:  # Si el contador no aumento, significa que no se cargaron datos, puede ser que el nombre este mal escrito
            showinfo("Error al cargar obra",
                     "No se pudo cargar la obra ingresada, verifique si esta bien escrita o si esta ingresada")
            entrada_editar.delete(0, END)

    def elemento_eliminar(self, eb):
        """
        Este metodo se encarga de encontrar la planta que se quiere eliminar de determinada obra
        Recorre la lista que contiene los nombres de las plantas y se detiene cuando encuentra 
        Que el nombre del cuadro de entrada de "Borrar Datos" coincide con alguno de los nombres de las plantas cargadas
        Luego devuelve la posicion de dicho elemento en la lista
        """

        self.pos_elemento = 0  # Iniciamos un contador de posicion
        # Recorremos la lista de ids los cuales coinciden con mis elementos cargados
        for i in range(0, len(self.entradas_plantasid)):
            # cuando el elemento coincida con mi cuadro de busqueda ahi ingresa en la funcion para eliminalo
            if str(eb.get()) == str(self.entradas_plantas[self.pos_elemento].get()):
                elemento = str(self.entradas_plantasid[self.pos_elemento])

                return elemento
                # una vez detectado el elemento salgo del bucle asi de esa manera me queda guardada la posicion
                # De esa manera podre recuperar dicha posicion mas adelante
            self.pos_elemento += 1

    def eliminar_planta(self, eb):
        """
        Elimina el elemento que se borro de la base de datos de cada una de las listas que contienen datos
        Obtiene la posicion del elemento a eliminar de la lista del metodo "elemento_eliminar"
        """

        # Una vez recuperado el elemento, destuimos los cuadros de entrada y lo removemos de las listas
        for i in self.entradas_plantas:
            if str(eb.get()) == str(i.get()):
                for j in self.entradas_totales:
                    if j == self.entradas_plantas[self.pos_elemento]:
                        indice = self.entradas_totales.index(
                            self.entradas_plantas[self.pos_elemento])
                        self.entradas_totales.pop(indice)
                        j.destroy()

                for j in self.entradas_totales:
                    if j == self.entradas_hormigon[self.pos_elemento]:
                        indice = self.entradas_totales.index(
                            self.entradas_hormigon[self.pos_elemento])
                        self.entradas_totales.pop(indice)
                        j.destroy()

                for j in self.entradas_totales:
                    if j == self.entradas_fi6[self.pos_elemento]:
                        indice = self.entradas_totales.index(
                            self.entradas_fi6[self.pos_elemento])
                        self.entradas_totales.pop(indice)
                        j.destroy()

                for j in self.entradas_totales:
                    if j == self.entradas_fi8[self.pos_elemento]:
                        indice = self.entradas_totales.index(
                            self.entradas_fi8[self.pos_elemento])
                        self.entradas_totales.pop(indice)
                        j.destroy()

                for j in self.entradas_totales:
                    if j == self.entradas_fi10[self.pos_elemento]:
                        indice = self.entradas_totales.index(
                            self.entradas_fi10[self.pos_elemento])
                        self.entradas_totales.pop(indice)
                        j.destroy()

                for j in self.entradas_totales:
                    if j == self.entradas_fi12[self.pos_elemento]:
                        indice = self.entradas_totales.index(
                            self.entradas_fi12[self.pos_elemento])
                        self.entradas_totales.pop(indice)
                        j.destroy()

                for j in self.entradas_totales:
                    if j == self.entradas_fi16[self.pos_elemento]:
                        indice = self.entradas_totales.index(
                            self.entradas_fi16[self.pos_elemento])
                        self.entradas_totales.pop(indice)
                        j.destroy()

                for j in self.entradas_totales:
                    if j == self.entradas_fi20[self.pos_elemento]:
                        indice = self.entradas_totales.index(
                            self.entradas_fi20[self.pos_elemento])
                        self.entradas_totales.pop(indice)
                        j.destroy()

                for j in self.entradas_totales:
                    if j == self.entradas_fi25[self.pos_elemento]:
                        indice = self.entradas_totales.index(
                            self.entradas_fi25[self.pos_elemento])
                        self.entradas_totales.pop(indice)
                        j.destroy()

                # Una vez eliminados los entrys sacamos de las listas restantes los items eliminados
                indice = self.entradas_plantas.index(
                    self.entradas_plantas[self.pos_elemento])
                self.entradas_plantas.pop(indice)

                indice = self.entradas_hormigon.index(
                    self.entradas_hormigon[self.pos_elemento])
                self.entradas_hormigon.pop(indice)

                indice = self.entradas_fi6.index(
                    self.entradas_fi6[self.pos_elemento])
                self.entradas_fi6.pop(indice)

                indice = self.entradas_fi8.index(
                    self.entradas_fi8[self.pos_elemento])
                self.entradas_fi8.pop(indice)

                indice = self.entradas_fi10.index(
                    self.entradas_fi10[self.pos_elemento])
                self.entradas_fi10.pop(indice)

                indice = self.entradas_fi12.index(
                    self.entradas_fi12[self.pos_elemento])
                self.entradas_fi12.pop(indice)

                indice = self.entradas_fi16.index(
                    self.entradas_fi16[self.pos_elemento])
                self.entradas_fi16.pop(indice)

                indice = self.entradas_fi20.index(
                    self.entradas_fi20[self.pos_elemento])
                self.entradas_fi20.pop(indice)

                indice = self.entradas_fi25.index(
                    self.entradas_fi25[self.pos_elemento])
                self.entradas_fi25.pop(indice)

                indice = self.entradas_plantasid.index(
                    self.entradas_plantasid[self.pos_elemento])
                self.entradas_plantasid.pop(indice)

                eb.delete(0, END)

    def eliminar_ultima(self, ee, co, ap, dp, imd, sd, t,
                        th, t6, t8, t10, t12, t16, t20, t25, mat, obra, ar, eb, bp, bo):
        """
        Elimina la ultima planta que se agrego con el boton "agregar planta"
        """

        if askyesno("Borrar planta", "Se borrarar la ultima planta agregada, desea continuar?"):

            # Procedemos a eliminar los entrys de la ultima columna creada
            for i in self.entradas_totales:
                if i == self.entradas_plantas[-1]:
                    indice = self.entradas_totales.index(
                        self.entradas_plantas[-1])
                    self.entradas_totales.pop(indice)
                    i.destroy()

            for i in self.entradas_totales:
                if i == self.entradas_hormigon[-1]:
                    indice = self.entradas_totales.index(
                        self.entradas_hormigon[-1])
                    self.entradas_totales.pop(indice)
                    i.destroy()

            for i in self.entradas_totales:
                if i == self.entradas_fi6[-1]:
                    indice = self.entradas_totales.index(self.entradas_fi6[-1])
                    self.entradas_totales.pop(indice)
                    i.destroy()

            for i in self.entradas_totales:
                if i == self.entradas_fi8[-1]:
                    indice = self.entradas_totales.index(self.entradas_fi8[-1])
                    self.entradas_totales.pop(indice)
                    i.destroy()

            for i in self.entradas_totales:
                if i == self.entradas_fi10[-1]:
                    indice = self.entradas_totales.index(
                        self.entradas_fi10[-1])
                    self.entradas_totales.pop(indice)
                    i.destroy()

            for i in self.entradas_totales:
                if i == self.entradas_fi12[-1]:
                    indice = self.entradas_totales.index(
                        self.entradas_fi12[-1])
                    self.entradas_totales.pop(indice)
                    i.destroy()

            for i in self.entradas_totales:
                if i == self.entradas_fi16[-1]:
                    indice = self.entradas_totales.index(
                        self.entradas_fi16[-1])
                    self.entradas_totales.pop(indice)
                    i.destroy()

            for i in self.entradas_totales:
                if i == self.entradas_fi20[-1]:
                    indice = self.entradas_totales.index(
                        self.entradas_fi20[-1])
                    self.entradas_totales.pop(indice)
                    i.destroy()

            for i in self.entradas_totales:
                if i == self.entradas_fi25[-1]:
                    indice = self.entradas_totales.index(
                        self.entradas_fi25[-1])
                    self.entradas_totales.pop(indice)
                    i.destroy()

            # Una vez eliminados los entrys sacamos de las listas restantes los items eliminados

            self.entradas_plantas.pop(-1)

            self.entradas_hormigon.pop(-1)

            self.entradas_fi6.pop(-1)

            self.entradas_fi8.pop(-1)

            self.entradas_fi10.pop(-1)

            self.entradas_fi12.pop(-1)

            self.entradas_fi16.pop(-1)

            self.entradas_fi20.pop(-1)

            self.entradas_fi25.pop(-1)

            self.contador_columnas -= 1

            if self.contador_columnas == 0:  # En caso de no tener elementos cargados, configuro la grilla como al inicio
                self.limpiar_pantalla(
                    obra,
                    th,
                    t6,
                    t8,
                    t10,
                    t12,
                    t16,
                    t20,
                    t25,
                    t,
                    ap,
                    dp,
                    imd,
                    sd,
                    mat,
                    ee,
                    co,
                    ar,
                    eb,
                    bp,
                    bo
                )

            # Si llegara a tener cargada alguna obra de la base de datos no podria elimnar las columnas
            elif len(self.entradas_plantas) == len(self.entradas_plantasid):
                dp.config(state=DISABLED)

            else:  # si no llegara a entrar en las demas condiciones formateo la grilla
                # Movemos junto con la creacion de los entrys los botones y labels
                ap.grid(column=self.contador_columnas+3)
                dp.grid(column=self.contador_columnas+3)
                imd.grid(column=self.contador_columnas+3)
                sd.grid(column=self.contador_columnas+3)

                t.grid(column=self.contador_columnas+2)
                th.grid(column=self.contador_columnas+2)
                t6.grid(column=self.contador_columnas+2)
                t8.grid(column=self.contador_columnas+2)
                t10.grid(column=self.contador_columnas+2)
                t12.grid(column=self.contador_columnas+2)
                t16.grid(column=self.contador_columnas+2)
                t20.grid(column=self.contador_columnas+2)
                t25.grid(column=self.contador_columnas+2)

                mat.grid(columnspan=self.contador_columnas+2)


class consultar_registros():
    """
    Esta clase se encarga de crear una ventana para mostrar los datos que se encuentran en la base de datos
    """

    def __init__(self):
        """
        Al instanciarse crea la ventana con los labels necesarios y el boton "Actualizar Datos"
        """

        # Creamos la intefaz de la nueva ventana, generando las mismas columnas que la tabla de la base de datos
        self.consu = Toplevel()
        self.consu.title("Consulta de registro")
        self.contador_consu = 0
        self.entradas_consulta = []

        # Etiquetas
        self.cons_id = Label(
            self.consu,
            text="ID",
            justify=CENTER
        )
        self.cons_id.grid(
            column=0,
            row=0,
            sticky="nsew",
            padx=5,
            pady=5
        )

        self.cons_nombre = Label(
            self.consu,
            text="Nombre de obra",
            justify=CENTER
        )
        self.cons_nombre.grid(
            column=1,
            row=0,
            sticky="nsew",
            padx=5,
            pady=5
        )

        self.cons_planta = Label(
            self.consu,
            text="Plantas",
            justify=CENTER
        )
        self.cons_planta.grid(
            column=2,
            row=0,
            sticky="nsew",
            padx=5,
            pady=5
        )

        self.cons_hormigon = Label(
            self.consu,
            text="Hormigon",
            justify=CENTER
        )
        self.cons_hormigon.grid(
            column=3,
            row=0,
            sticky="nsew",
            padx=5,
            pady=5
        )

        self.cons_fi6 = Label(
            self.consu,
            text="Ø6",
            justify=CENTER
        )
        self.cons_fi6.grid(
            column=4,
            row=0,
            sticky="nsew",
            padx=5,
            pady=5
        )

        self.cons_fi8 = Label(
            self.consu,
            text="Ø8",
            justify=CENTER
        )
        self.cons_fi8.grid(
            column=5,
            row=0,
            sticky="nsew",
            padx=5,
            pady=5
        )

        self.cons_fi10 = Label(
            self.consu,
            text="Ø10",
            justify=CENTER
        )
        self.cons_fi10.grid(
            column=6,
            row=0,
            sticky="nsew",
            padx=5,
            pady=5
        )

        self.cons_fi12 = Label(
            self.consu,
            text="Ø12",
            justify=CENTER
        )
        self.cons_fi12.grid(
            column=7,
            row=0,
            sticky="nsew",
            padx=5,
            pady=5
        )

        self.cons_fi16 = Label(
            self.consu,
            text="Ø16",
            justify=CENTER
        )
        self.cons_fi16.grid(
            column=8,
            row=0,
            sticky="nsew",
            padx=5,
            pady=5
        )

        self.cons_fi20 = Label(
            self.consu,
            text="Ø20",
            justify=CENTER
        )
        self.cons_fi20.grid(
            column=9,
            row=0,
            sticky="nsew",
            padx=5,
            pady=5
        )

        self.cons_fi25 = Label(
            self.consu,
            text="Ø25",
            justify=CENTER
        )
        self.cons_fi25.grid(
            column=10,
            row=0,
            sticky="nsew",
            padx=5,
            pady=5
        )

        # Boton
        self.actualizar_consu = Button(
            self.consu,
            text="Actualizar Datos",
            padx=5,
            pady=5
        )
        self.actualizar_consu.grid(
            column=0,
            row=1,
            columnspan=11,
            sticky="nsew",
            padx=10,
            pady=5
        )

    def actualizar_datos(self, resultado):
        """
        A esta funcion se le pasan toods los datos de la base de datos y luego
        Los muestra en la ventana de consulta 
        """

        if self.entradas_consulta:
            for x in self.entradas_consulta:
                x.destroy()

        for i in resultado:

            l0 = Label(self.consu, text=str(i[0]))
            l0.grid(column=0, row=self.contador_consu+1, padx=5, pady=5)

            l1 = Label(self.consu, text=str(i[1]))
            l1.grid(column=1, row=self.contador_consu+1, padx=5, pady=5)

            l2 = Label(self.consu, text=str(i[2]))
            l2.grid(column=2, row=self.contador_consu+1, padx=5, pady=5)

            l3 = Label(self.consu, text=str(i[3]))
            l3.grid(column=3, row=self.contador_consu+1, padx=5, pady=5)

            l4 = Label(self.consu, text=str(i[4]))
            l4.grid(
                column=4, row=self.contador_consu+1, padx=5, pady=5)
            l5 = Label(self.consu, text=str(i[5]))
            l5.grid(column=5, row=self.contador_consu+1, padx=5, pady=5)

            l6 = Label(self.consu, text=str(i[6]))
            l6.grid(column=6, row=self.contador_consu+1, padx=5, pady=5)

            l7 = Label(self.consu, text=str(i[7]))
            l7.grid(column=7, row=self.contador_consu+1, padx=5, pady=5)

            l8 = Label(self.consu, text=str(i[8]))
            l8.grid(column=8, row=self.contador_consu+1)

            l9 = Label(self.consu, text=str(i[9]))
            l9.grid(column=9, row=self.contador_consu+1, padx=5, pady=5)

            l10 = Label(self.consu, text=str(i[10]))
            l10.grid(column=10, row=self.contador_consu+1, padx=5, pady=5)

            self.entradas_consulta.extend(
                [l0, l1, l2, l3, l4, l5, l6, l7, l8, l9, l10])

            self.actualizar_consu.grid(row=self.contador_consu+2)

            self.contador_consu += 1
