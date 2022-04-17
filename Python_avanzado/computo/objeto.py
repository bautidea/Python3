from tkinter import *
import tkinter as tk
from tkinter.messagebox import *
import os
import observers


class Funciones(observers.Tema):
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
        self.entradas_plantasid = []
        self.entradas_totalid = []
        self.checkbox = []
        self.checkbox_var = []

        self.contador_columnas = 0
    
    def Inicio(self):
        self.Notify_inicio()    

    def Salir(self, salida):
        """
        Modulo que se encarga de preguntar si desea finalizar la ejecucion del programa
        """

        if askyesno("Finalizar Ejecucion", "desea salir del programa?"):
            salida.destroy()
            
            self.Notify_fin()

    def Add_columna(self, app, ap, imd, sd, t, th, t6, t8, t10, t12, t16, t20, t25, mat, bs):
        """
        Agrega una columna a la grilla, agregando los datos a las listas creadas
        """

        # Al pulsar el boton de agregar planta se añadiran una fila de columnas
        # Creamos entrys en la columna siguente
        col_ent = self.contador_columnas + 1
        
        self.ent_planta = Entry(app, justify=CENTER)
        self.ent_planta.grid(row=1, sticky="nsew")
        
        self.ent_hormigon = Entry(app, justify=CENTER)
        self.ent_hormigon.grid(row=3, sticky="nsew")
        
        self.ent_fi6 = Entry(app, justify=CENTER)
        self.ent_fi6.grid(row=5, sticky="nsew")
        
        self.ent_fi8 = Entry(app, justify=CENTER)
        self.ent_fi8.grid(row=6, sticky="nsew")

        self.ent_fi10 = Entry(app, justify=CENTER)
        self.ent_fi10.grid(row=7, sticky="nsew")
        
        self.ent_fi12 = Entry(app, justify=CENTER)
        self.ent_fi12.grid(row=8, sticky="nsew")
        
        self.ent_fi16 = Entry(app, justify=CENTER)
        self.ent_fi16.grid(row=9, sticky="nsew")
        
        self.ent_fi20 = Entry(app, justify=CENTER)
        self.ent_fi20.grid(row=10, sticky="nsew")
        
        self.ent_fi25 = Entry(app, justify=CENTER)
        self.ent_fi25.grid(row=11, sticky="nsew")
        
        self.var = IntVar()
        
        self.check = Checkbutton(app, variable= self.var)
        self.check.grid(row = 12)
        
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
        self.checkbox.append(self.check)
        self.checkbox_var.append(self.var)
        
        self.contador_columnas += 1
        
        # Configuramos la grilla
        self.Configurar_grilla(ap, imd, sd, t, th, t6, t8, t10, t12, t16, t20, t25, mat)
       
        # Habilitamos el boton para borrar seleccionados
        bs.config(state=NORMAL)
        
    def Configurar_grilla(self,ap, imd, sd, t, th, t6, t8, t10, t12, t16, t20, t25, mat):
        '''
        Luego de Ejecutar algun metodo me acomoda nuevamente los botones y los 
        entrys de la columna Total.
        '''
        
        pos = 0
        for i in range(0, self.contador_columnas):
            col_ent = i + 1
            
            self.entradas_plantas[pos].grid(column = col_ent)
            
            self.entradas_hormigon[pos].grid(column = col_ent)
            
            self.entradas_fi6[pos].grid(column = col_ent)
            
            self.entradas_fi8[pos].grid(column = col_ent)
            
            self.entradas_fi10[pos].grid(column = col_ent)
            
            self.entradas_fi12[pos].grid(column = col_ent)
            
            self.entradas_fi16[pos].grid(column = col_ent)
            
            self.entradas_fi20[pos].grid(column = col_ent)
            
            self.entradas_fi25[pos].grid(column = col_ent)
            
            self.checkbox[pos].grid(column = col_ent)

            pos += 1
            
        # Configuramos la ubicacion de los botones
        col_bot = self.contador_columnas + 3
        
        ap.grid(column= col_bot)
        imd.grid(column= col_bot)
        sd.grid(column= col_bot)

        # Configuramos la ubicacion de la columna 'Total'
        col_tot = self.contador_columnas + 2
        
        t.grid(column= col_tot)
        th.grid(column= col_tot)
        t6.grid(column= col_tot)
        t8.grid(column= col_tot)
        t10.grid(column= col_tot)
        t12.grid(column= col_tot)
        t16.grid(column= col_tot)
        t20.grid(column= col_tot)
        t25.grid(column= col_tot)

        mat.grid(columnspan= col_tot)
        
    def Imprimir_datos(self, obra, th, t6, t8, t10, t12, t16, t20, t25):
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

        self.Notify_imprimir(obra.get())

    def Suma(self, th, t6, t8, t10, t12, t16, t20, t25):
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
    
    def Actualizar_tree(self, tree, resultados):
        '''
        Agrega los nombres de las obras y la cantidad de plantas que tiene cada una
        al treeview para su visualizacion
        '''

        obras = []
        tupla_obras = []
        
        # Eliminamos los datos cargados en el treeview.
        for item in tree.get_children():
            tree.delete(item)
        
        # Agregamos los nombres de obras, sin tener en cuenta repetidos.     
        for i in resultados:
            if i not in obras:
                obras.append(i)
        
        # Contamos la cantidad de veces que la obra aparece y le restamos 1,
        # para no tener en cuenta la columna 'Totales'.
        for j in obras:
            plantas = resultados.count(j)-1
            tupla_obras.append((j,plantas))
        
        # Insertamos al treeview.
        for item in tupla_obras:
            tree.insert('', 0, values = item)   

    def Cargar_obra(self, resultado, obra_acargar, app, ap, imd, sd, t, th, t6, t8, t10, t12, t16, t20, t25, mat, obra, ar, bo, aa, bs):
        """
        Cuando se carga una obra de la base de datos este modulo se encarga de generar la grilla para esa obra
        Creando las columnas que tenia la obra y asignandole los datos
        """

        for i in resultado:  # Recorremos las tuplas dentro de la lista "resultado"

            # Filtramos los nombres de las obras y solamente obtenemos el nombre buscado
            if obra_acargar == i[1]:
                # Cargamos todos los valores de las plantas a excepcion de la planta de "TOTALES"
                if i[2] != "Total":
                    self.Add_columna(app, ap, imd, sd, t,
                                     th, t6, t8, t10, t12, t16, t20, t25, mat, bs)

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

                # Para el caso de la planta de "TOTALES" obtenemos sus datos de manera separada
                elif i[2] == "Total":
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

        # El nombre de la obra cargada se mueve de lugar
        obra.insert(END, obra_acargar)

        # Habilito el boton para modificar los registros de la base de datos
        ar.config(state=NORMAL)
        bo.config(state=NORMAL)

        # Desabilito el boton de alta de datos
        aa.config(state=DISABLED)

        # Guardo en una variable el nombre de la obra cargada, por si se modifica
        # el mismo
        self.nombre_obra_original = obra_acargar
        
        self.Notify_consulta(obra_acargar)
        

    def Limpiar_pantalla(self, obra, th, t6, t8, t10, t12, t16, t20, t25, t, ap, imd, sd, mat, ar, bo, bs):
        """
        Se limpia la pantalla y resetea la grilla luego de realizar determinada accion
        """
        
        # Creamos una lista de tuplas que contenga las demas listas,
        # para luego iterarla y borrar todo con menos utilizacion de codigo
        entradas_totales = []
        entradas_totales.append(self.entradas_plantas) 
        entradas_totales.append(self.entradas_hormigon)
        entradas_totales.append(self.entradas_fi6)
        entradas_totales.append(self.entradas_fi8)
        entradas_totales.append(self.entradas_fi10)
        entradas_totales.append(self.entradas_fi12)
        entradas_totales.append(self.entradas_fi16)
        entradas_totales.append(self.entradas_fi20)
        entradas_totales.append(self.entradas_fi25)
        entradas_totales.append(self.checkbox)

        # Destruimos los entrys
        for lista in entradas_totales:
            for elemento in lista:
                elemento.destroy()
        
        # Borramos las variables asociadas a los checkbox
        for variable in self.checkbox_var:
            del variable          

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

        # Deshabilito el boton para actualizar registros
        ar.config(state=DISABLED)
        # Deshabilito el boton para borrar obra
        bo.config(state=DISABLED)   
        # Deshabilito el boton para borrar seleccion
        bs.config(state=DISABLED)           
       
        self.entradas_plantas.clear()
        self.entradas_hormigon.clear()
        self.entradas_fi6.clear()
        self.entradas_fi8.clear()
        self.entradas_fi10.clear()
        self.entradas_fi12.clear()
        self.entradas_fi16.clear()
        self.entradas_fi20.clear()
        self.entradas_fi25.clear()
        self.entradas_plantasid.clear()
        self.entradas_totalid.clear()
        self.checkbox.clear()
        self.checkbox_var.clear()
        
        self.contador_columnas = 0
        
        # Movemos junto con la eliminacion de los entrys los botones y labels
        ap.grid(column=2)
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
    
    def Eliminar_seleccion(self, ap, imd, sd, t, th, t6, t8, t10, t12, t16, t20, t25, mat):
        '''
        Elimina los elementos seleccionados de la grilla, y si los mismos estan cargados
        en la base de datos, pasa dichos valores para que sean removidos de la misma.
        '''
        
        # Listas que recibiran la posicion de los elementos a eliminar
        seleccion_plantas = []
        seleccion_id = []
        
        # Lista que recibira los numeros de id a eliminar de la base de datos
        id_a_eliminar = []
        
        # Recorremos todos los checkboxes.
        for pos in self.checkbox_var:
            # Nos fijamos cuales estan seleccionados.
            if pos.get() == 1:
                # Añiadimos la posicion de los checkboxes seleccionados, dicha posicion
                # se corresponde con la posicion de los elementos a elimiar.
                seleccion_plantas.append(self.checkbox_var.index(pos))
        
        # Corroboramos si hay alguna obra cargada de la base de datos.     
        if self.entradas_plantasid:
            # Obtengo la cantidad de elementos cargados.
            cantidad_ids = len(self.entradas_plantasid)
            
            # Recorremos la lista de checkboxes sin pasarnos de la cantidad
            # de elementos cargados.
            for pos_id in self.checkbox_var[0: cantidad_ids]:
                # Nos fijamos cuales ids estan seleccionados.   
                if pos_id.get() == 1:
                    # Añiadimos la posicion de los checkboxes seleccionados, la cual se
                    # correponde con la posicion de ids a elimninar.
                    seleccion_id.append(self.checkbox_var.index(pos_id)) 
        
        # Recorremos la lista de posiciones, cada elemento se corresponde con la 
        # posicion a eliminar.       
        for i in seleccion_plantas[::-1]:            
            # Eliminamos los entrys correspondientes, y eliminamos el elemento de
            # la lista.
            self.entradas_plantas[i].destroy()
            self.entradas_plantas.pop(i)
            
            self.entradas_hormigon[i].destroy()
            self.entradas_hormigon.pop(i)
            
            self.entradas_fi6[i].destroy()
            self.entradas_fi6.pop(i)
            
            self.entradas_fi8[i].destroy()
            self.entradas_fi8.pop(i)
            
            self.entradas_fi10[i].destroy()
            self.entradas_fi10.pop(i)
            
            self.entradas_fi12[i].destroy()
            self.entradas_fi12.pop(i)
            
            self.entradas_fi16[i].destroy()
            self.entradas_fi16.pop(i)
            
            self.entradas_fi20[i].destroy()
            self.entradas_fi20.pop(i)
            
            self.entradas_fi25[i].destroy()
            self.entradas_fi25.pop(i)
            
            self.checkbox[i].destroy()
            self.checkbox.pop(i)
            
            self.checkbox_var.pop(i)
         
        # Recorremos la lista de posiciones de ids a eliminar.    
        for j in seleccion_id[::-1]:
            # Obtenemos los valores de los ids que vamos a elimnar de la base de datos.
            # y los agregamos a una lista que se lo pasaremos al ORM, el cual
            # los eliminara de la base de datos.
            id_a_eliminar.append(self.entradas_plantasid[j])
            
            # Eliminamos el elemento seleccionado de la lista.
            self.entradas_plantasid.pop(j)      
        
        # Obtenemos la cantidad de columnas en la grilla para poder configurar la misma.
        self.contador_columnas = self.contador_columnas - len(seleccion_plantas)

        # Configuramos la grilla
        self.Configurar_grilla(ap, imd, sd, t, th, t6, t8, t10, t12, t16, t20, t25, mat)
        
        # Devolvemos los valores de ids a eliminar
        return id_a_eliminar