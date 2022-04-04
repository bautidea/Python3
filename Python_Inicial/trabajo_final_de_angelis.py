from tkinter import *
import tkinter as tk
from tkinter.messagebox import *
from types import CellType
import mysql.connector
import re

master = Tk()
master.title("Trabajo Final")
master.state("zoomed")

entradas_plantas = []
entradas_hormigon = []
entradas_fi6 = []
entradas_fi8 = []
entradas_fi10 = []
entradas_fi12 = []
entradas_fi16 = []
entradas_fi20 = []
entradas_fi25 = []
entradas_totales = []
entradas_consulta = []
entradas_plantasid = []
entradas_totalid = []


contador_columnas = 0
contador_consu = 0

# Definimos las funciones de los botones


def salir():  # Funcion para mostrar mensaje cuando se quiere terminar el programa
    if askyesno("Finalizar Ejecucion", "desea salir del programa?"):
        master.destroy()


def add_columna():  # Al pulsar el boton de agregar planta se añadiran una fila de columnas
    # Definimos las variables globales que se utilizaran en la funcion
    global entradas_plantas
    global entradas_hormigon
    global entradas_fi6
    global entradas_fi8
    global entradas_fi10
    global entradas_fi12
    global entradas_fi16
    global entradas_fi20
    global entradas_fi25
    global entradas_totales
    global contador_columnas

    # Creamos entrys en la columna siguente
    ent_planta = Entry(
        master,
        justify=CENTER,
    )
    ent_planta.grid(
        column=(contador_columnas + 1),
        row=1,
        sticky="nsew"
    )

    ent_hormigon = Entry(
        master,
        justify=CENTER
    )
    ent_hormigon.grid(
        column=(contador_columnas + 1),
        row=3,
        sticky="nsew"
    )

    ent_fi6 = Entry(
        master,
        justify=CENTER
    )
    ent_fi6.grid(
        column=(contador_columnas + 1),
        row=5,
        sticky="nsew"
    )

    ent_fi8 = Entry(
        master,
        justify=CENTER
    )
    ent_fi8.grid(
        column=(contador_columnas + 1),
        row=6,
        sticky="nsew"
    )

    ent_fi10 = Entry(
        master,
        justify=CENTER
    )
    ent_fi10.grid(
        column=(contador_columnas + 1),
        row=7,
        sticky="nsew"
    )

    ent_fi12 = Entry(
        master,
        justify=CENTER
    )
    ent_fi12.grid(
        column=(contador_columnas + 1),
        row=8,
        sticky="nsew"
    )

    ent_fi16 = Entry(
        master,
        justify=CENTER
    )
    ent_fi16.grid(
        column=(contador_columnas + 1),
        row=9,
        sticky="nsew"
    )

    ent_fi20 = Entry(
        master,
        justify=CENTER
    )
    ent_fi20.grid(
        column=(contador_columnas + 1),
        row=10,
        sticky="nsew"
    )

    ent_fi25 = Entry(
        master,
        justify=CENTER
    )
    ent_fi25.grid(
        column=(contador_columnas + 1),
        row=11,
        sticky="nsew"
    )

    # Movemos junto con la creacion de los entrys los botones y labels
    add_planta.grid(column=contador_columnas+3)
    del_planta.grid(column=contador_columnas+3)
    imp_datos.grid(column=contador_columnas+3)
    suma_datos.grid(column=contador_columnas+3)

    total.grid(column=contador_columnas+2)
    tot_hormigon.grid(column=contador_columnas+2)
    tot_fi6.grid(column=contador_columnas+2)
    tot_fi8.grid(column=contador_columnas+2)
    tot_fi10.grid(column=contador_columnas+2)
    tot_fi12.grid(column=contador_columnas+2)
    tot_fi16.grid(column=contador_columnas+2)
    tot_fi20.grid(column=contador_columnas+2)
    tot_fi25.grid(column=contador_columnas+2)

    materiales.grid(columnspan=contador_columnas+2)

    # Aniadimos los datos de las entradas a las listas, asi de esa manera luego podremos recuperar la informacion
    entradas_plantas.append(ent_planta)
    entradas_hormigon.append(ent_hormigon)
    entradas_fi6.append(ent_fi6)
    entradas_fi8.append(ent_fi8)
    entradas_fi10.append(ent_fi10)
    entradas_fi12.append(ent_fi12)
    entradas_fi16.append(ent_fi16)
    entradas_fi20.append(ent_fi20)
    entradas_fi25.append(ent_fi25)

    entradas_totales.extend([
        ent_planta,
        ent_hormigon,
        ent_fi6,
        ent_fi8,
        ent_fi10,
        ent_fi12,
        ent_fi16,
        ent_fi20,
        ent_fi25
    ])

    # Habilito la opcion para eliminar la ultima planta agregada
    del_planta.config(state=NORMAL)

    if not entradas_plantasid:  # En caso de que no haya alguna obra cargada, se deshabilita la opcion para cargar datos
        cargar_obra.config(state=DISABLED)
        entrada_editar.config(state="readonly")

    contador_columnas += 1


def imprimir_datos():  # Con esta funcion imprimiremos las datos en consola

    print("####################################################################")
    print("NOMBRE DEL EDIFICIO: ", str(obra.get()))

    pos = 0

    # Ya que todas las listas tienen la misma longitud obtenemos el rango de la entrada de plantas, para que vaya iterando
    for i in range(0, len(entradas_plantas)):
        print("####################################################################")
        print(
            "PLANTA: ",
            str(entradas_plantas[pos].get()),
            " - ",
            "HORMIGON [m3]: ",
            str(entradas_hormigon[pos].get()),
            " - ",
            "BARRAS Ø6 [m]: ",
            str(entradas_fi6[pos].get()),
            " - ",
            "BARRAS Ø8 [m]: ",
            str(entradas_fi8[pos].get()),
            " - ",
            "BARRAS Ø10 [m]: ",
            str(entradas_fi10[pos].get()),
            " - ",
            "BARRAS Ø12 [m]: ",
            str(entradas_fi12[pos].get()),
            " - ",
            "BARRAS Ø16 [m]: ",
            str(entradas_fi16[pos].get()),
            " - ",
            "BARRAS Ø20 [m]: ",
            str(entradas_fi20[pos].get()),
            " - ",
            "BARRAS Ø25 [m]: ",
            str(entradas_fi25[pos].get()),
        )

        pos += 1

    print("####################################################################")
    print(
        "TOTAL: ",
        " - ",
        "HORMIGON [m3]: ",
        str(tot_hormigon.get()),
        " - ",
        "BARRAS Ø6 [m]: ",
        str(tot_fi6.get()),
        " - ",
        "BARRAS Ø8 [m]: ",
        str(tot_fi8.get()),
        " - ",
        "BARRAS Ø10 [m]: ",
        str(tot_fi10.get()),
        " - ",
        "BARRAS Ø12 [m]: ",
        str(tot_fi12.get()),
        " - ",
        "BARRAS Ø16 [m]: ",
        str(tot_fi16.get()),
        " - ",
        "BARRAS Ø20 [m]: ",
        str(tot_fi20.get()),
        " - ",
        "BARRAS Ø25 [m]: ",
        str(tot_fi25.get()),
    )


def suma():  # Esta funcion suma todos las filas adyacentes para obtener un valor total de cada elemento computado

    total_hormigon = 0
    total_fi6 = 0
    total_fi8 = 0
    total_fi10 = 0
    total_fi12 = 0
    total_fi16 = 0
    total_fi20 = 0
    total_fi25 = 0

    for hormigon in entradas_hormigon:
        if hormigon.get() != "":
            total_hormigon = total_hormigon + float(hormigon.get())

    for fi6 in entradas_fi6:
        if fi6.get() != "":
            total_fi6 = total_fi6 + float(fi6.get())

    for fi8 in entradas_fi8:
        if fi8.get() != "":
            total_fi8 = total_fi8 + float(fi8.get())

    for fi10 in entradas_fi10:
        if fi10.get() != "":
            total_fi10 = total_fi10 + float(fi10.get())

    for fi12 in entradas_fi12:
        if fi12.get() != "":
            total_fi12 = total_fi12 + float(fi12.get())

    for fi16 in entradas_fi16:
        if fi16.get() != "":
            total_fi16 = total_fi16 + float(fi16.get())

    for fi20 in entradas_fi20:
        if fi20.get() != "":
            total_fi20 = total_fi20 + float(fi20.get())

    for fi25 in entradas_fi25:
        if fi25.get() != "":
            total_fi25 = total_fi25 + float(fi25.get())

    var_horm = tk.StringVar()
    tot_hormigon.config(textvariable=var_horm)
    var_horm.set(total_hormigon)

    var_fi6 = tk.StringVar()
    tot_fi6.config(textvariable=var_fi6)
    var_fi6.set(total_fi6)

    var_fi8 = tk.StringVar()
    tot_fi8.config(textvariable=var_fi8)
    var_fi8.set(total_fi8)

    var_fi12 = tk.StringVar()
    tot_fi12.config(textvariable=var_fi12)
    var_fi12.set(total_fi12)

    var_fi10 = tk.StringVar()
    tot_fi10.config(textvariable=var_fi10)
    var_fi10.set(total_fi10)

    var_fi16 = tk.StringVar()
    tot_fi16.config(textvariable=var_fi16)
    var_fi16.set(total_fi16)

    var_fi20 = tk.StringVar()
    tot_fi20.config(textvariable=var_fi20)
    var_fi20.set(total_fi20)

    var_fi25 = tk.StringVar()
    tot_fi25.config(textvariable=var_fi25)
    var_fi25.set(total_fi25)


def borrar_ultima():  # Esta funcion eliminara la ultima columna agregada que no se encuentra en tabla de la base de datos

    # Definimos las variables globales que se utilizaran en la funcion
    global entradas_plantas
    global entradas_hormigon
    global entradas_fi6
    global entradas_fi8
    global entradas_fi10
    global entradas_fi12
    global entradas_fi16
    global entradas_fi20
    global entradas_fi25
    global entradas_totales
    global contador_columnas
    global entradas_plantasid

    if askyesno("Borrar planta", "Se borrarar la ultima planta agregada, desea continuar?"):

        # Procedemos a eliminar los entrys de la ultima columna creada
        for i in entradas_totales:
            if i == entradas_plantas[-1]:
                indice = entradas_totales.index(
                    entradas_plantas[-1])
                entradas_totales.pop(indice)
                i.destroy()

        for i in entradas_totales:
            if i == entradas_hormigon[-1]:
                indice = entradas_totales.index(
                    entradas_hormigon[-1])
                entradas_totales.pop(indice)
                i.destroy()

        for i in entradas_totales:
            if i == entradas_fi6[-1]:
                indice = entradas_totales.index(entradas_fi6[-1])
                entradas_totales.pop(indice)
                i.destroy()

        for i in entradas_totales:
            if i == entradas_fi8[-1]:
                indice = entradas_totales.index(entradas_fi8[-1])
                entradas_totales.pop(indice)
                i.destroy()

        for i in entradas_totales:
            if i == entradas_fi10[-1]:
                indice = entradas_totales.index(entradas_fi10[-1])
                entradas_totales.pop(indice)
                i.destroy()

        for i in entradas_totales:
            if i == entradas_fi12[-1]:
                indice = entradas_totales.index(entradas_fi12[-1])
                entradas_totales.pop(indice)
                i.destroy()

        for i in entradas_totales:
            if i == entradas_fi16[-1]:
                indice = entradas_totales.index(entradas_fi16[-1])
                entradas_totales.pop(indice)
                i.destroy()

        for i in entradas_totales:
            if i == entradas_fi20[-1]:
                indice = entradas_totales.index(entradas_fi20[-1])
                entradas_totales.pop(indice)
                i.destroy()

        for i in entradas_totales:
            if i == entradas_fi25[-1]:
                indice = entradas_totales.index(entradas_fi25[-1])
                entradas_totales.pop(indice)
                i.destroy()

        # Una vez eliminados los entrys sacamos de las listas restantes los items eliminados

        entradas_plantas.pop(-1)

        entradas_hormigon.pop(-1)

        entradas_fi6.pop(-1)

        entradas_fi8.pop(-1)

        entradas_fi10.pop(-1)

        entradas_fi12.pop(-1)

        entradas_fi16.pop(-1)

        entradas_fi20.pop(-1)

        entradas_fi25.pop(-1)

        contador_columnas -= 1

        if contador_columnas == 0:  # En caso de no tener elementos cargados, configuro la grilla como al inicio

            add_planta.grid(column=2)
            del_planta.grid(column=2)
            imp_datos.grid(column=2)
            suma_datos.grid(column=2)

            total.grid(column=1)
            tot_hormigon.grid(column=1)
            tot_fi6.grid(column=1)
            tot_fi8.grid(column=1)
            tot_fi10.grid(column=1)
            tot_fi12.grid(column=1)
            tot_fi16.grid(column=1)
            tot_fi20.grid(column=1)
            tot_fi25.grid(column=1)

            materiales.grid(columnspan=1)

            # Desabilito el boton para elinar la utlima planta, ya que si no tengo columnas no tendria sentido
            del_planta.config(state=DISABLED)

            # Habilito la carga de datos para  edicion
            entrada_editar.config(state=NORMAL)
            cargar_obra.config(state=NORMAL)

        # Si llegara a tener cargada alguna obra de la base de datos no podria elimnar las columnas
        elif len(entradas_plantas) == len(entradas_plantasid):
            del_planta.config(state=DISABLED)

        else:  # si no llegara a entrar en las demas condiciones formateo la grilla
            # Movemos junto con la creacion de los entrys los botones y labels
            add_planta.grid(column=contador_columnas+3)
            del_planta.grid(column=contador_columnas+3)
            imp_datos.grid(column=contador_columnas+3)
            suma_datos.grid(column=contador_columnas+3)

            total.grid(column=contador_columnas+2)
            tot_hormigon.grid(column=contador_columnas+2)
            tot_fi6.grid(column=contador_columnas+2)
            tot_fi8.grid(column=contador_columnas+2)
            tot_fi10.grid(column=contador_columnas+2)
            tot_fi12.grid(column=contador_columnas+2)
            tot_fi16.grid(column=contador_columnas+2)
            tot_fi20.grid(column=contador_columnas+2)
            tot_fi25.grid(column=contador_columnas+2)

            materiales.grid(columnspan=contador_columnas+2)


def crear_bd():  # Funcion para crear la base de datos y la tabla, de una misma vez

    try:
        # Creamos un mensaje para avisar si esta seguro de la creacion de la base de datos
        if askyesno("Creacion de una base de datos",
                    "Esta a punto de crear una base de datos, esta seguro?"):

            # Nos conectamos al host
            jbda_bd = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd=""
            )

            # Creamos el cursor el cual se encargara de ejectutar las acciones
            micursor = jbda_bd.cursor()

            # Creamos la base de datos
            micursor.execute("CREATE DATABASE de_angelis_bd")

            # Cometemos los cambios
            jbda_bd.commit()

            # Cerramos la conexion a la base de datos
            jbda_bd.close()

            # Nos conectamos a la base de datos creada
            jbda_bd = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="de_angelis_bd"
            )

            # Nos conectamos al host
            micursor = jbda_bd.cursor()

            # Creamos las columnas de la base de datos
            micursor.execute("""CREATE TABLE computos (
                id int(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
                nombre_obra VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL,
                plantas VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL,
                hormigon VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL,
                fi_6 VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL,
                fi_8 VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL,
                fi_10 VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL,
                fi_12 VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL,
                fi_16 VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL,
                fi_20 VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL,
                fi_25 VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL
                )
            """)

            # Cometemos los cambios
            jbda_bd.commit()

            # Cerramos la conexion a la base de datos
            jbda_bd.close()

            # Si todo va bien se nos notifica de la creacion de la base de datos
            showinfo("Creacion Exitosa",
                     "Se Creo una base de datos con el nombre de_angelis_bd")
    except:  # En caso de que no se pueda crear la base de datos surgira el siguiente mensaje
        showinfo("Falla en Creacion",
                 "Fallo en la creacion de la base de datos, intente nuevamente o fijese si la misma ya esta creada")


def importar_registros():  # Funcion para agregar registos a la tabla de la base de datos

    # Definimos las variables globales que van a ser modificadas por la funcion
    global entradas_plantas
    global entradas_hormigon
    global entradas_fi6
    global entradas_fi8
    global entradas_fi10
    global entradas_fi12
    global entradas_fi16
    global entradas_fi20
    global entradas_fi25
    global entradas_totales
    global contador_columnas

    # Verificamos que el nombre de la obra este todo en minusculas y sin espacios, antes de importar losd datos a la tabla
    # Usamos regex para verificar que la obra sea escrita en minusucla, para recuperar datos de manera mas facil
    cadena = str(obra.get())
    patron = "[a-z_0-9]"

    if (re.match(patron, cadena)):
        try:
            # Mensaje para avisar si esta seguro de la importacion de registros
            if askyesno("Importar registros",
                        "Se eliminaran todos los registros cargados, esta seguro?"):

                # Nos conectamos a la base de datos creada
                jbda_bd = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="",
                    database="de_angelis_bd"
                )

                # Creamos el cursor el cual se encargara de ejectutar las acciones
                micursor = jbda_bd.cursor()

                # Insertamos los registros
                pos = 0
                for i in range(0, len(entradas_plantas)):
                    sql = """INSERT INTO computos (nombre_obra, plantas, hormigon, fi_6, fi_8, fi_10, fi_12, fi_16, fi_20, fi_25)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                    record = (
                        obra.get(),
                        entradas_plantas[pos].get(),
                        entradas_hormigon[pos].get(),
                        entradas_fi6[pos].get(),
                        entradas_fi8[pos].get(),
                        entradas_fi10[pos].get(),
                        entradas_fi12[pos].get(),
                        entradas_fi16[pos].get(),
                        entradas_fi20[pos].get(),
                        entradas_fi25[pos].get(),
                    )

                    micursor.execute(sql, record)

                    pos += 1

                sql_total = """INSERT INTO computos (nombre_obra, plantas, hormigon, fi_6, fi_8, fi_10, fi_12, fi_16, fi_20, fi_25)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                record_total = (
                    obra.get(),
                    "total",
                    tot_hormigon.get(),
                    tot_fi6.get(),
                    tot_fi8.get(),
                    tot_fi10.get(),
                    tot_fi12.get(),
                    tot_fi16.get(),
                    tot_fi20.get(),
                    tot_fi25.get(),
                )

                micursor.execute(sql_total, record_total)

                # Cometemos los cambios
                jbda_bd.commit()

                # Cerramos la conexion a la base de datos
                jbda_bd.close()

                # Una vez realizada la importacion si todo va bien, muestra un mensaje para avisarnos
                showinfo("Importacion Exitosa",
                         "Se han importado todos los registros a la tabla")

                # Limpiamos y borramos los registros luego de su importacion
                for entradas in entradas_totales:
                    entradas.delete(0, END)

                obra.delete(0, END)

                tot_hormigon.config(state=NORMAL)
                tot_hormigon.delete(0, END)
                tot_hormigon.config(state="readonly")

                tot_fi6.config(state=NORMAL)
                tot_fi6.delete(0, END)
                tot_fi6.config(state="readonly")

                tot_fi8.config(state=NORMAL)
                tot_fi8.delete(0, END)
                tot_fi8.config(state="readonly")

                tot_fi10.config(state=NORMAL)
                tot_fi10.delete(0, END)
                tot_fi10.config(state="readonly")

                tot_fi12.config(state=NORMAL)
                tot_fi12.delete(0, END)
                tot_fi12.config(state="readonly")

                tot_fi16.config(state=NORMAL)
                tot_fi16.delete(0, END)
                tot_fi16.config(state="readonly")

                tot_fi20.config(state=NORMAL)
                tot_fi20.delete(0, END)
                tot_fi20.config(state="readonly")

                tot_fi25.config(state=NORMAL)
                tot_fi25.delete(0, END)
                tot_fi25.config(state="readonly")

                for entradas in entradas_totales:
                    entradas.destroy()

                # Movemos junto con la eliminacion de los entrys los botones y labels
                entradas_plantas = []
                entradas_hormigon = []
                entradas_fi6 = []
                entradas_fi8 = []
                entradas_fi10 = []
                entradas_fi12 = []
                entradas_fi16 = []
                entradas_fi20 = []
                entradas_fi25 = []
                entradas_totales = []
                contador_columnas = 0

                add_planta.grid(column=2)
                del_planta.grid(column=2)
                imp_datos.grid(column=2)
                suma_datos.grid(column=2)

                total.grid(column=1)
                tot_hormigon.grid(column=1)
                tot_fi6.grid(column=1)
                tot_fi8.grid(column=1)
                tot_fi10.grid(column=1)
                tot_fi12.grid(column=1)
                tot_fi16.grid(column=1)
                tot_fi20.grid(column=1)
                tot_fi25.grid(column=1)

                materiales.grid(columnspan=1)

        except:  # En caso de que haya algun problema al importar los datos a la tabla me avisa del error
            showinfo("Falla en importacion",
                     "Fallo en subir los registros a la tabla, intente crear la base de datos primero")

    else:  # Si el nombre de la obra no esta escrito con los caracteres especificados me avisa de ello y no me deja importar los registros
        showinfo("Falla en importcion",
                 "Fallo al subir los registros a la tabla, el nombre del edificio debe ser escrito todo en minuscula y sin espacios")


def consultar_registros():  # Funcion la cual nos abre una ventana y nos importa todos los datos en la tabla
    # Definimos las variables globales a utilizar
    global contador_consu
    global consu
    global actualizar_consu
    global entradas_consulta

    # Creamos la intefaz de la nueva ventana, generando las mismas columnas que la tabla de la base de datos
    consu = Toplevel()
    consu.title("Consulta de registro")

    Label(
        consu,
        text="ID",
        justify=CENTER
    ).grid(
        column=0,
        row=0,
        sticky="nsew",
        padx=5,
        pady=5
    )

    Label(
        consu,
        text="Nombre de obra",
        justify=CENTER
    ).grid(
        column=1,
        row=0,
        sticky="nsew",
        padx=5,
        pady=5
    )

    Label(
        consu,
        text="Plantas",
        justify=CENTER
    ).grid(
        column=2,
        row=0,
        sticky="nsew",
        padx=5,
        pady=5
    )

    Label(
        consu,
        text="Hormigon",
        justify=CENTER
    ).grid(
        column=3,
        row=0,
        sticky="nsew",
        padx=5,
        pady=5
    )

    Label(
        consu,
        text="Ø6",
        justify=CENTER
    ).grid(
        column=4,
        row=0,
        sticky="nsew",
        padx=5,
        pady=5
    )

    Label(
        consu,
        text="Ø8",
        justify=CENTER
    ).grid(
        column=5,
        row=0,
        sticky="nsew",
        padx=5,
        pady=5
    )

    Label(
        consu,
        text="Ø10",
        justify=CENTER
    ).grid(
        column=6,
        row=0,
        sticky="nsew",
        padx=5,
        pady=5
    )

    Label(
        consu,
        text="Ø12",
        justify=CENTER
    ).grid(
        column=7,
        row=0,
        sticky="nsew",
        padx=5,
        pady=5
    )

    Label(
        consu,
        text="Ø16",
        justify=CENTER
    ).grid(
        column=8,
        row=0,
        sticky="nsew",
        padx=5,
        pady=5
    )

    Label(
        consu,
        text="Ø20",
        justify=CENTER
    ).grid(
        column=9,
        row=0,
        sticky="nsew",
        padx=5,
        pady=5
    )

    Label(
        consu,
        text="Ø25",
        justify=CENTER
    ).grid(
        column=10,
        row=0,
        sticky="nsew",
        padx=5,
        pady=5
    )

    # Este boton llama a la funcion actualizar (cumple la misma accion que esta funcion)
    actualizar_consu = Button(
        consu,
        text="Actualizar Datos",
        command=lambda: actualizar(),
        padx=5,
        pady=5
    )
    actualizar_consu.grid(
        column=0,
        row=1,
        columnspan=11,
        sticky="nsew",
        padx=10,
        pady=5
    )

    try:
        # Nos conectamos a nuestra base de datos
        jbda_bd = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="de_angelis_bd"
        )

        # creamos el cursor
        micursor = jbda_bd.cursor()

        # Seleccionamos todos los campos con sus registros para su importacion
        micursor.execute("SELECT * FROM computos")
        # Le decimos al cursor que nos importe todo, y lo asociamos a una variable
        resultado = micursor.fetchall()

        # ya que nos importa una tupla dentro de una lista, recorremos la lista, y de cada tupla obtenemos el dato que esta en la posicion correspondiente
        for i in resultado:

            l0 = Label(consu, text=str(i[0]))
            l0.grid(column=0, row=contador_consu+1, padx=5, pady=5)

            l1 = Label(consu, text=str(i[1]))
            l1.grid(column=1, row=contador_consu+1, padx=5, pady=5)

            l2 = Label(consu, text=str(i[2]))
            l2.grid(column=2, row=contador_consu+1, padx=5, pady=5)

            l3 = Label(consu, text=str(i[3]))
            l3.grid(column=3, row=contador_consu+1, padx=5, pady=5)

            l4 = Label(consu, text=str(i[4]))
            l4.grid(
                column=4, row=contador_consu+1, padx=5, pady=5)
            l5 = Label(consu, text=str(i[5]))
            l5.grid(column=5, row=contador_consu+1, padx=5, pady=5)

            l6 = Label(consu, text=str(i[6]))
            l6.grid(column=6, row=contador_consu+1, padx=5, pady=5)

            l7 = Label(consu, text=str(i[7]))
            l7.grid(column=7, row=contador_consu+1, padx=5, pady=5)

            l8 = Label(consu, text=str(i[8]))
            l8.grid(column=8, row=contador_consu+1)

            l9 = Label(consu, text=str(i[9]))
            l9.grid(column=9, row=contador_consu+1, padx=5, pady=5)

            l10 = Label(consu, text=str(i[10]))
            l10.grid(column=10, row=contador_consu+1, padx=5, pady=5)

            entradas_consulta.extend(
                [l0, l1, l2, l3, l4, l5, l6, l7, l8, l9, l10])

            actualizar_consu.grid(row=contador_consu+2)

            contador_consu += 1

        # Cometemos los cambios
        jbda_bd.commit()

        # Cerramos la conexion a la base de datos
        jbda_bd.close()

    except:  # En caso de que haya un error al consultar los datos, nos muestra el siguiente mensaje
        showinfo("Falla al consultar datos",
                 "No se pudo actualizar la informacion de la tabla, Verifique si la base de datos esta creada")


def actualizar():  # Esta funcion realiza la misma accion que "consultar_registros", es para actualizar los datos
    # Definimos las variables globales a utilizar en la funcion
    global contador_consu
    global entradas_consulta

    # Destruimos los labels creados aneriormente para que puedan ser sobreescribidos
    for x in entradas_consulta:
        x.destroy()

    try:
        # Nos conectamos a la base de datos
        jbda_bd = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="de_angelis_bd"
        )

        # creamos el cursor
        micursor = jbda_bd.cursor()

        # Seleccionamos todos los campos con sus registros para su importacion
        micursor.execute("SELECT * FROM computos")
        # Le decimos al cursor que nos importe todo, y lo asociamos a una variable
        resultado = micursor.fetchall()

        for i in resultado:

            l0 = Label(consu, text=str(i[0]))
            l0.grid(column=0, row=contador_consu+1, padx=5, pady=5)

            l1 = Label(consu, text=str(i[1]))
            l1.grid(column=1, row=contador_consu+1, padx=5, pady=5)

            l2 = Label(consu, text=str(i[2]))
            l2.grid(column=2, row=contador_consu+1, padx=5, pady=5)

            l3 = Label(consu, text=str(i[3]))
            l3.grid(column=3, row=contador_consu+1, padx=5, pady=5)

            l4 = Label(consu, text=str(i[4]))
            l4.grid(
                column=4, row=contador_consu+1, padx=5, pady=5)
            l5 = Label(consu, text=str(i[5]))
            l5.grid(column=5, row=contador_consu+1, padx=5, pady=5)

            l6 = Label(consu, text=str(i[6]))
            l6.grid(column=6, row=contador_consu+1, padx=5, pady=5)

            l7 = Label(consu, text=str(i[7]))
            l7.grid(column=7, row=contador_consu+1, padx=5, pady=5)

            l8 = Label(consu, text=str(i[8]))
            l8.grid(column=8, row=contador_consu+1)

            l9 = Label(consu, text=str(i[9]))
            l9.grid(column=9, row=contador_consu+1, padx=5, pady=5)

            l10 = Label(consu, text=str(i[10]))
            l10.grid(column=10, row=contador_consu+1, padx=5, pady=5)

            entradas_consulta.extend(
                [l0, l1, l2, l3, l4, l5, l6, l7, l8, l9, l10])

            actualizar_consu.grid(row=contador_consu+2)

            contador_consu += 1

        # Cometemos los cambios
        jbda_bd.commit()

        # Cerramos la conexion a la base de datos
        jbda_bd.close()

    except:  # En caso de no poder actualizara los datos nos avisa de ello
        showinfo("Falla al actualizar datos",
                 "No se pudo actualizar la informacion de la tabla")


def exportar_obra():  # Con esta funcion se exportaran a la grilla las obras que estan cargadas en nuestra base de datos

    # Definimos las variables globales que se utilizaran en la funcion
    global entradas_plantas
    global entradas_hormigon
    global entradas_fi6
    global entradas_fi8
    global entradas_fi10
    global entradas_fi12
    global entradas_fi16
    global entradas_fi20
    global entradas_fi25
    global entradas_totales
    global contador_columnas
    global entradas_totalid
    global entradas_plantasid

    # cambio de lugar el nombre de la obra
    obra_acargar = str(entrada_editar.get())

    # Creo un contador para determinar si una obra tiene datos cargados (linea 1149)
    contador_plantas = 0

    if askyesno("Carga de datos",
                "Se eliminaran todos los campos actuales antes de cargar los datos, esta seguro?"):

        # primero limpiamos cualquier dato que pueda a llegar a haber cargado el usuario
        for entradas in entradas_totales:
            entradas.delete(0, END)

        obra.delete(0, END)

        tot_hormigon.config(state=NORMAL)
        tot_hormigon.delete(0, END)
        tot_hormigon.config(state="readonly")

        tot_fi6.config(state=NORMAL)
        tot_fi6.delete(0, END)
        tot_fi6.config(state="readonly")

        tot_fi8.config(state=NORMAL)
        tot_fi8.delete(0, END)
        tot_fi8.config(state="readonly")

        tot_fi10.config(state=NORMAL)
        tot_fi10.delete(0, END)
        tot_fi10.config(state="readonly")

        tot_fi12.config(state=NORMAL)
        tot_fi12.delete(0, END)
        tot_fi12.config(state="readonly")

        tot_fi16.config(state=NORMAL)
        tot_fi16.delete(0, END)
        tot_fi16.config(state="readonly")

        tot_fi20.config(state=NORMAL)
        tot_fi20.delete(0, END)
        tot_fi20.config(state="readonly")

        tot_fi25.config(state=NORMAL)
        tot_fi25.delete(0, END)
        tot_fi25.config(state="readonly")

        for entradas in entradas_totales:
            entradas.destroy()

        # Movemos junto con la eliminacion de los entrys los botones y labels
        entradas_plantas = []
        entradas_hormigon = []
        entradas_fi6 = []
        entradas_fi8 = []
        entradas_fi10 = []
        entradas_fi12 = []
        entradas_fi16 = []
        entradas_fi20 = []
        entradas_fi25 = []
        entradas_totales = []
        entradas_plantasid = []
        entradas_totalid = []
        contador_columnas = 0

        add_planta.grid(column=2)
        del_planta.grid(column=2)
        imp_datos.grid(column=2)
        suma_datos.grid(column=2)

        total.grid(column=1)
        tot_hormigon.grid(column=1)
        tot_fi6.grid(column=1)
        tot_fi8.grid(column=1)
        tot_fi10.grid(column=1)
        tot_fi12.grid(column=1)
        tot_fi16.grid(column=1)
        tot_fi20.grid(column=1)
        tot_fi25.grid(column=1)

        materiales.grid(columnspan=1)

        try:
            # Nos conectamos a nuestra base de datos
            jbda_bd = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="de_angelis_bd"
            )

            # Creamos el cursor
            micursor = jbda_bd.cursor()

            # Seleccionamos todos los campos con sus registros para su importacion
            micursor.execute("SELECT * FROM computos")
            # Le decimos al cursor que nos importe todo, y lo asociamos a una variable
            resultado = micursor.fetchall()

            # Cometemos los cambios
            jbda_bd.commit()

            # Cerramos la conexion a la base de datos
            jbda_bd.close()

            for i in resultado:  # Recorremos las tuplas dentro de la lista "resultado"

                # Filtramos los nombres de las obras y solamente obtenemos el nombre buscado
                if obra_acargar == i[1]:

                    # Cargamos todos los valores de las plantas a excepcion de la planta de "TOTALES"
                    if i[2] != "total":
                        # Creamos entrys en la columna siguente
                        ent_planta = Entry(
                            master,
                            justify=CENTER,
                        )
                        ent_planta.grid(
                            column=(contador_columnas + 1),
                            row=1,
                            sticky="nsew"
                        )

                        ent_hormigon = Entry(
                            master,
                            justify=CENTER
                        )
                        ent_hormigon.grid(
                            column=(contador_columnas + 1),
                            row=3,
                            sticky="nsew"
                        )

                        ent_fi6 = Entry(
                            master,
                            justify=CENTER
                        )
                        ent_fi6.grid(
                            column=(contador_columnas + 1),
                            row=5,
                            sticky="nsew"
                        )

                        ent_fi8 = Entry(
                            master,
                            justify=CENTER
                        )
                        ent_fi8.grid(
                            column=(contador_columnas + 1),
                            row=6,
                            sticky="nsew"
                        )

                        ent_fi10 = Entry(
                            master,
                            justify=CENTER
                        )
                        ent_fi10.grid(
                            column=(contador_columnas + 1),
                            row=7,
                            sticky="nsew"
                        )

                        ent_fi12 = Entry(
                            master,
                            justify=CENTER
                        )
                        ent_fi12.grid(
                            column=(contador_columnas + 1),
                            row=8,
                            sticky="nsew"
                        )

                        ent_fi16 = Entry(
                            master,
                            justify=CENTER
                        )
                        ent_fi16.grid(
                            column=(contador_columnas + 1),
                            row=9,
                            sticky="nsew"
                        )

                        ent_fi20 = Entry(
                            master,
                            justify=CENTER
                        )
                        ent_fi20.grid(
                            column=(contador_columnas + 1),
                            row=10,
                            sticky="nsew"
                        )

                        ent_fi25 = Entry(
                            master,
                            justify=CENTER
                        )
                        ent_fi25.grid(
                            column=(contador_columnas + 1),
                            row=11,
                            sticky="nsew"
                        )

                        ent_planta.insert(END, str(i[2]))
                        ent_hormigon.insert(END, str(i[3]))
                        ent_fi6.insert(END, str(i[4]))
                        ent_fi8.insert(END, str(i[5]))
                        ent_fi10.insert(END, str(i[6]))
                        ent_fi12.insert(END, str(i[7]))
                        ent_fi16.insert(END, str(i[8]))
                        ent_fi20.insert(END, str(i[9]))
                        ent_fi25.insert(END, str(i[10]))

                        # Movemos junto con la creacion de los entrys los botones y labels
                        add_planta.grid(column=contador_columnas+3)
                        del_planta.grid(column=contador_columnas+3)
                        imp_datos.grid(column=contador_columnas+3)
                        suma_datos.grid(column=contador_columnas+3)

                        total.grid(column=contador_columnas+2)
                        tot_hormigon.grid(column=contador_columnas+2)
                        tot_fi6.grid(column=contador_columnas+2)
                        tot_fi8.grid(column=contador_columnas+2)
                        tot_fi10.grid(column=contador_columnas+2)
                        tot_fi12.grid(column=contador_columnas+2)
                        tot_fi16.grid(column=contador_columnas+2)
                        tot_fi20.grid(column=contador_columnas+2)
                        tot_fi25.grid(column=contador_columnas+2)

                        materiales.grid(columnspan=contador_columnas+2)

                        # aniadimos los datos de las entradas a las listas, asi de esa manera luego podremos recuperar la informacion
                        entradas_plantas.append(ent_planta)
                        entradas_hormigon.append(ent_hormigon)
                        entradas_fi6.append(ent_fi6)
                        entradas_fi8.append(ent_fi8)
                        entradas_fi10.append(ent_fi10)
                        entradas_fi12.append(ent_fi12)
                        entradas_fi16.append(ent_fi16)
                        entradas_fi20.append(ent_fi20)
                        entradas_fi25.append(ent_fi25)
                        entradas_plantasid.append(i[0])

                        entradas_totales.extend([
                            ent_planta,
                            ent_hormigon,
                            ent_fi6,
                            ent_fi8,
                            ent_fi10,
                            ent_fi12,
                            ent_fi16,
                            ent_fi20,
                            ent_fi25
                        ])

                        contador_columnas += 1

                    # Para el caso de la planta de "TOTALES" obtenemos sus datos de manera separada
                    elif i[2] == "total":
                        tot_hormigon.config(state=NORMAL)
                        tot_hormigon.insert(END, i[3])
                        tot_hormigon.config(state="readonly")

                        tot_fi6.config(state=NORMAL)
                        tot_fi6.insert(END, str(i[4]))
                        tot_fi6.config(state="readonly")

                        tot_fi8.config(state=NORMAL)
                        tot_fi8.insert(END, str(i[5]))
                        tot_fi8.config(state="readonly")

                        tot_fi10.config(state=NORMAL)
                        tot_fi10.insert(END, str(i[6]))
                        tot_fi10.config(state="readonly")

                        tot_fi12.config(state=NORMAL)
                        tot_fi12.insert(END, str(i[7]))
                        tot_fi12.config(state="readonly")

                        tot_fi16.config(state=NORMAL)
                        tot_fi16.insert(END, str(i[8]))
                        tot_fi16.config(state="readonly")

                        tot_fi20.config(state=NORMAL)
                        tot_fi20.insert(END, str(i[9]))
                        tot_fi20.config(state="readonly")

                        tot_fi25.config(state=NORMAL)
                        tot_fi25.insert(END, str(i[10]))
                        tot_fi25.config(state="readonly")

                        entradas_totalid.append(i[0])

                    # Si llegara a cargar algun dato el contador aumenta y de esa manera se si se cargo algun dato
                    contador_plantas += 1

            if contador_plantas >= 1:  # Si el contador aumento significa que cargo datos

                # El nombre de la obra cargada se mueve de lugar
                obra.insert(END, obra_acargar)

                # bloqueo el boton para cargar obras, asi de esa manera no se cargan obras de mas
                cargar_obra.config(state=DISABLED)

                # Borro el contenido del cuadro de busqueda
                entrada_editar.delete(0, END)

                # Bloqueo el cuadro de busqueda
                entrada_editar.config(state="readonly")

                # Habilito el boton para modificar los registros de la base de datos
                actualizar_registros.config(state=NORMAL)
                entrada_borrar.config(state=NORMAL)
                borrar_planta.config(state=NORMAL)
                borrar_obra.config(state=NORMAL)

                # desabilito el boton para eliminar la ultima planta agregada
                del_planta.config(state=DISABLED)

            else:  # Si el contador no aumento, significa que no se cargaron datos, puede ser que el nombre este mal escrito
                showinfo("Error al cargar obra",
                         "No se pudo cargar la obra ingresada, verifique si esta bien escrita o si esta ingresada")
                entrada_editar.delete(0, END)

        except:
            showinfo("Fallo en la conexion con la base de datos",
                     "No se pudo cargar la obra, Verifique si la base de datos esta creada")


def update_registros():  # Funcion para actualizar los registros de la base de datos

    # Definimos las variables globales que se utilizaran en la funcion
    global entradas_plantas
    global entradas_hormigon
    global entradas_fi6
    global entradas_fi8
    global entradas_fi10
    global entradas_fi12
    global entradas_fi16
    global entradas_fi20
    global entradas_fi25
    global entradas_totales
    global contador_columnas
    global entradas_totalid
    global entradas_plantasid

    try:
        # Nos conectamos a la base de datos y la tabla
        jbda_bd = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="de_angelis_bd"
        )
        # Creamos el cursor
        micursor = jbda_bd.cursor()

        pos = 0  # Contador para indicar la posicion del elemento que esta siendo recorrido

        if entradas_plantasid:  # si la lista de id contiene elementos, entonces significa que se cargo alguna obra

            # recorremos la lista de obras una por una para modificar cada uno de sus campos
            for i in range(0, len(entradas_plantasid)):
                sql = """UPDATE computos SET
                        nombre_obra = %s,
                        plantas = %s,
                        hormigon = %s,
                        fi_6 = %s,
                        fi_8 = %s,
                        fi_10 = %s,
                        fi_12 = %s,
                        fi_16 = %s,
                        fi_20 = %s,
                        fi_25 = %s
                        WHERE id = %s"""

                record = (
                    obra.get(),
                    entradas_plantas[pos].get(),
                    entradas_hormigon[pos].get(),
                    entradas_fi6[pos].get(),
                    entradas_fi8[pos].get(),
                    entradas_fi10[pos].get(),
                    entradas_fi12[pos].get(),
                    entradas_fi16[pos].get(),
                    entradas_fi20[pos].get(),
                    entradas_fi25[pos].get(),
                    entradas_plantasid[pos]
                )

                micursor.execute(sql, record)
                jbda_bd.commit()

                pos += 1  # paso al siguiente elemento

            # Una vez modificadas las plantas se procede a actualizar el "TOTAL"
            sql = """UPDATE computos SET
                        nombre_obra = %s,
                        plantas = %s,
                        hormigon = %s,
                        fi_6 = %s,
                        fi_8 = %s,
                        fi_10 = %s,
                        fi_12 = %s,
                        fi_16 = %s,
                        fi_20 = %s,
                        fi_25 = %s
                        WHERE id = %s"""
            record = (
                obra.get(),
                "total",
                tot_hormigon.get(),
                tot_fi6.get(),
                tot_fi8.get(),
                tot_fi10.get(),
                tot_fi12.get(),
                tot_fi16.get(),
                tot_fi20.get(),
                tot_fi25.get(),
                entradas_totalid[0]
            )

            micursor.execute(sql, record)
            jbda_bd.commit()

            if len(entradas_plantas) > len(entradas_plantasid):
                # Si llegara a tener mas elementos en la lista de plantas que en la lista de ID esto significa que se aniadieron elementos
                # Por lo tanto procedo a agregar a la tabla los elementos que se agregaron
                # Recorro los elementos restantes que no fueron actualizados y necesitan ser agregados
                # Continuo de donde dejo el bucle anterior
                for i in range(len(entradas_plantasid), len(entradas_plantas)):
                    sql = """INSERT INTO computos (nombre_obra, plantas, hormigon, fi_6, fi_8, fi_10, fi_12, fi_16, fi_20, fi_25)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                    record = (
                        obra.get(),
                        entradas_plantas[pos].get(),
                        entradas_hormigon[pos].get(),
                        entradas_fi6[pos].get(),
                        entradas_fi8[pos].get(),
                        entradas_fi10[pos].get(),
                        entradas_fi12[pos].get(),
                        entradas_fi16[pos].get(),
                        entradas_fi20[pos].get(),
                        entradas_fi25[pos].get(),
                    )

                    micursor.execute(sql, record)
                    jbda_bd.commit()

                    pos += 1  # agrego el siguiente de donde dejo el bucle anterior

            # Si todo se actualiza correctamente deberia mostrar este mensaje
            showinfo("Datos Actualizados",
                     "Los Datos fueron actualizados y cargados con exito!!")

            # Vuelvo a activar el boton para cargar una nueva obra
            cargar_obra.config(state=NORMAL)
            # Desbloqueo el cuadro de busqueda
            entrada_editar.config(state="normal")
            # Cerramos la conexion a la base de datos
            jbda_bd.close()
            # Vuelvo a desactivar los botones y entrys de borrar para que no puedan ser usados
            entrada_borrar.config(state="readonly")
            borrar_planta.config(state=DISABLED)
            borrar_obra.config(state=DISABLED)
            actualizar_registros.config(state=DISABLED)

            # Deshabilito el control de elimnar ultima ya que no habria columnas para eliminar
            del_planta.config(state=DISABLED)

            # Limpiamos y borramos los registros luego de su importacion
            for entradas in entradas_totales:
                entradas.delete(0, END)

            obra.delete(0, END)

            tot_hormigon.config(state=NORMAL)
            tot_hormigon.delete(0, END)
            tot_hormigon.config(state="readonly")

            tot_fi6.config(state=NORMAL)
            tot_fi6.delete(0, END)
            tot_fi6.config(state="readonly")

            tot_fi8.config(state=NORMAL)
            tot_fi8.delete(0, END)
            tot_fi8.config(state="readonly")

            tot_fi10.config(state=NORMAL)
            tot_fi10.delete(0, END)
            tot_fi10.config(state="readonly")

            tot_fi12.config(state=NORMAL)
            tot_fi12.delete(0, END)
            tot_fi12.config(state="readonly")

            tot_fi16.config(state=NORMAL)
            tot_fi16.delete(0, END)
            tot_fi16.config(state="readonly")

            tot_fi20.config(state=NORMAL)
            tot_fi20.delete(0, END)
            tot_fi20.config(state="readonly")

            tot_fi25.config(state=NORMAL)
            tot_fi25.delete(0, END)
            tot_fi25.config(state="readonly")

            # Destruimos todas las entrys que se utilizaron
            for entradas in entradas_totales:
                entradas.destroy()

            # Vaciamos las listas
            entradas_plantas = []
            entradas_hormigon = []
            entradas_fi6 = []
            entradas_fi8 = []
            entradas_fi10 = []
            entradas_fi12 = []
            entradas_fi16 = []
            entradas_fi20 = []
            entradas_fi25 = []
            entradas_totales = []
            entradas_plantasid = []
            entradas_totalid = []
            contador_columnas = 0

            # Movemos junto con la eliminacion de los entrys los botones y labels
            add_planta.grid(column=2)
            del_planta.grid(column=2)
            imp_datos.grid(column=2)
            suma_datos.grid(column=2)

            total.grid(column=1)
            tot_hormigon.grid(column=1)
            tot_fi6.grid(column=1)
            tot_fi8.grid(column=1)
            tot_fi10.grid(column=1)
            tot_fi12.grid(column=1)
            tot_fi16.grid(column=1)
            tot_fi20.grid(column=1)
            tot_fi25.grid(column=1)

            materiales.grid(columnspan=1)

        else:
            showinfo("Fallo al guardar cambios",
                     "Usted no a cargado una obra")

    except:
        showinfo("Fallo en la conexion con la base de datos",
                 "No se pudieron actualizar los registros, Verifique si la base de datos esta creada")


def eliminar_planta():  # Funcion para eliminar la planta especificada en el cuadro de entrada de "Borrar Datos"

    # Definimos las variables globales que se utilizaran en la funcion
    global entradas_plantas
    global entradas_hormigon
    global entradas_fi6
    global entradas_fi8
    global entradas_fi10
    global entradas_fi12
    global entradas_fi16
    global entradas_fi20
    global entradas_fi25
    global entradas_totales
    global contador_columnas
    global entradas_plantasid

    if entrada_borrar.get() != "":  # Si El cuadro de entrada esta vacio no se ejecutaria la funcion

        try:
            # Nos conectamos a la base de datos y la tabla
            jbda_bd = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="de_angelis_bd"
            )
            # Creamos el cursor
            micursor = jbda_bd.cursor()

            pos = 0  # Iniciamos un contador de posicion

            contador_planta = 0  # Iniciamos un contador para saber si se cargo algun elemento

            # Recorremos la lista de ids los cuales coinciden con mis elementos cargados
            for i in range(0, len(entradas_plantasid)):

                # cuando el elemento coincida con mi cuadro de busqueda ahi ingresa en la funcion para eliminalo
                if str(entrada_borrar.get()) == str(entradas_plantas[pos].get()):

                    sql = "DELETE FROM computos WHERE id = %s"
                    eliminar = (str(entradas_plantasid[pos]),)

                    micursor.execute(sql, eliminar)
                    jbda_bd.commit()

                    break
                    # una vez elminado el elemento salgo del bucle asi de esa manera me queda guardada la posicion
                    # De esa manera podre recuperar dicha posicion mas adelante
                pos += 1

            # Cerramos la conexion a la base de datos
            jbda_bd.close()

            # Una Vez eliminado el elemento
            # Destruimos las entrys y sacamos de la lista de "entradas_totales" los items eliminiados
            for i in entradas_plantas:
                if str(entrada_borrar.get()) == str(i.get()):
                    for i in entradas_totales:
                        if i == entradas_plantas[pos]:
                            indice = entradas_totales.index(
                                entradas_plantas[pos])
                            entradas_totales.pop(indice)
                            i.destroy()

                    for i in entradas_totales:
                        if i == entradas_hormigon[pos]:
                            indice = entradas_totales.index(
                                entradas_hormigon[pos])
                            entradas_totales.pop(indice)
                            i.destroy()

                    for i in entradas_totales:
                        if i == entradas_fi6[pos]:
                            indice = entradas_totales.index(entradas_fi6[pos])
                            entradas_totales.pop(indice)
                            i.destroy()

                    for i in entradas_totales:
                        if i == entradas_fi8[pos]:
                            indice = entradas_totales.index(entradas_fi8[pos])
                            entradas_totales.pop(indice)
                            i.destroy()

                    for i in entradas_totales:
                        if i == entradas_fi10[pos]:
                            indice = entradas_totales.index(entradas_fi10[pos])
                            entradas_totales.pop(indice)
                            i.destroy()

                    for i in entradas_totales:
                        if i == entradas_fi12[pos]:
                            indice = entradas_totales.index(entradas_fi12[pos])
                            entradas_totales.pop(indice)
                            i.destroy()

                    for i in entradas_totales:
                        if i == entradas_fi16[pos]:
                            indice = entradas_totales.index(entradas_fi16[pos])
                            entradas_totales.pop(indice)
                            i.destroy()

                    for i in entradas_totales:
                        if i == entradas_fi20[pos]:
                            indice = entradas_totales.index(entradas_fi20[pos])
                            entradas_totales.pop(indice)
                            i.destroy()

                    for i in entradas_totales:
                        if i == entradas_fi25[pos]:
                            indice = entradas_totales.index(entradas_fi25[pos])
                            entradas_totales.pop(indice)
                            i.destroy()

                    # Una vez eliminados los entrys sacamos de las listas restantes los items eliminados
                    indice = entradas_plantas.index(entradas_plantas[pos])
                    entradas_plantas.pop(indice)

                    indice = entradas_hormigon.index(entradas_hormigon[pos])
                    entradas_hormigon.pop(indice)

                    indice = entradas_fi6.index(entradas_fi6[pos])
                    entradas_fi6.pop(indice)

                    indice = entradas_fi8.index(entradas_fi8[pos])
                    entradas_fi8.pop(indice)

                    indice = entradas_fi10.index(entradas_fi10[pos])
                    entradas_fi10.pop(indice)

                    indice = entradas_fi12.index(entradas_fi12[pos])
                    entradas_fi12.pop(indice)

                    indice = entradas_fi16.index(entradas_fi16[pos])
                    entradas_fi16.pop(indice)

                    indice = entradas_fi20.index(entradas_fi20[pos])
                    entradas_fi20.pop(indice)

                    indice = entradas_fi25.index(entradas_fi25[pos])
                    entradas_fi25.pop(indice)

                    indice = entradas_plantasid.index(entradas_plantasid[pos])
                    entradas_plantasid.pop(indice)

                    contador_planta += 1
                    entrada_borrar.delete(0, END)

            if contador_planta == 0:
                # si el contador es 0 significa que no se proceso ningun dato, por lo tanto no se excribio correctamente el nombre de la planta
                showinfo("No se pudo encontrar la planta solicitada",
                         "El nombre de la planta que usted ingreso no coincide con la plantas cargadas")
                entrada_borrar.delete(0, END)

        except IndexError:
            showinfo("Error al borrar planta",
                     "La planta que usted precisa borrar no se encuentra cargada en la base de datos")
            entrada_borrar.delete(0, END)
            try:
                consu.destroy()
                consu.update()
            except:
                pass

        except:
            showinfo("Fallo al borrar datos",
                     "Hubo algun problema con la conexion entre la base de datos, verifique si la base de datos esta creada")

    else:
        showinfo("Fallo al eliminar datos",
                 "Esciba el nombre de la planta que usted quiere elimniar")


def eliminar_obra():  # Funcion para eliminar la obra entera de la base de datos

    # Definimos las variables globales que se utilizaran en la funcion
    global entradas_plantas
    global entradas_hormigon
    global entradas_fi6
    global entradas_fi8
    global entradas_fi10
    global entradas_fi12
    global entradas_fi16
    global entradas_fi20
    global entradas_fi25
    global entradas_totales
    global contador_columnas
    global entradas_plantasid

    if askyesno("Eliminar obra", "Esta seguro que desea remover la obra de la base de datos?"):

        try:
            # Nos conectamos a la base de datos y la tabla
            jbda_bd = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="de_angelis_bd"
            )
            # Creamos el cursor
            micursor = jbda_bd.cursor()

            sql = "DELETE FROM computos WHERE nombre_obra = %s"
            eliminar = (str(obra.get()),)

            micursor.execute(sql, eliminar)
            jbda_bd.commit()
            # Cerramos la conexion a la base de datos
            jbda_bd.close()

            showinfo("OBRA ELIMINADA",
                     "La obra se elimino correctamente de la base de datos!")

            # Vuelvo a desactivar los botones y entrys de borrar para que no puedan ser usados
            entrada_borrar.config(state="readonly")
            borrar_planta.config(state=DISABLED)
            borrar_obra.config(state=DISABLED)
            actualizar_registros.config(state=DISABLED)
            del_planta.config(state=DISABLED)

            # Vuelvo a activar los botones para Actualizar los registros de la tabla
            cargar_obra.config(state=NORMAL)
            entrada_editar.config(state=NORMAL)

            # Limpiamos y borramos los registros luego de su importacion
            for entradas in entradas_totales:
                entradas.delete(0, END)

            obra.delete(0, END)

            tot_hormigon.config(state=NORMAL)
            tot_hormigon.delete(0, END)
            tot_hormigon.config(state="readonly")

            tot_fi6.config(state=NORMAL)
            tot_fi6.delete(0, END)
            tot_fi6.config(state="readonly")

            tot_fi8.config(state=NORMAL)
            tot_fi8.delete(0, END)
            tot_fi8.config(state="readonly")

            tot_fi10.config(state=NORMAL)
            tot_fi10.delete(0, END)
            tot_fi10.config(state="readonly")

            tot_fi12.config(state=NORMAL)
            tot_fi12.delete(0, END)
            tot_fi12.config(state="readonly")

            tot_fi16.config(state=NORMAL)
            tot_fi16.delete(0, END)
            tot_fi16.config(state="readonly")

            tot_fi20.config(state=NORMAL)
            tot_fi20.delete(0, END)
            tot_fi20.config(state="readonly")

            tot_fi25.config(state=NORMAL)
            tot_fi25.delete(0, END)
            tot_fi25.config(state="readonly")

            # Destruimos todas las entrys que se utilizaron
            for entradas in entradas_totales:
                entradas.destroy()

            # Vaciamos las listas
            entradas_plantas = []
            entradas_hormigon = []
            entradas_fi6 = []
            entradas_fi8 = []
            entradas_fi10 = []
            entradas_fi12 = []
            entradas_fi16 = []
            entradas_fi20 = []
            entradas_fi25 = []
            entradas_totales = []
            entradas_plantasid = []
            entradas_totalid = []
            contador_columnas = 0

            # Movemos junto con la eliminacion de los entrys los botones y labels
            add_planta.grid(column=2)
            del_planta.grid(column=2)
            imp_datos.grid(column=2)
            suma_datos.grid(column=2)

            total.grid(column=1)
            tot_hormigon.grid(column=1)
            tot_fi6.grid(column=1)
            tot_fi8.grid(column=1)
            tot_fi10.grid(column=1)
            tot_fi12.grid(column=1)
            tot_fi16.grid(column=1)
            tot_fi20.grid(column=1)
            tot_fi25.grid(column=1)

            materiales.grid(columnspan=1)

        except:
            showinfo("Fallo al borrar datos",
                     "Hubo algun problema con la conexion entre la base de datos, verifique si la base de datos esta creada")


# Creamos las etiquetas que nos pediran los datos
Label(
    text="Nombre del edificio",
    anchor=W,
    justify=LEFT
).grid(
    column=0,
    row=0,
    sticky="nsew",
    padx=10,
    pady=5
)

Label(
    text="Plantas",
    anchor=W,
    justify=LEFT
).grid(
    column=0,
    row=1,
    sticky="nsew",
    padx=10,
    pady=5
)

materiales = Label(
    text="Materiales",
    justify=CENTER,
    borderwidth=2,
    relief="solid"
)
materiales.grid(
    column=0,
    row=2,
    sticky="nsew",
    padx=10,
    pady=5
)

Label(
    text="Hormigon",
    justify=CENTER
).grid(
    column=0,
    row=3,
    sticky="nsew",
    padx=10,
    pady=5
)

Label(
    text="Barras",
    anchor=W,
    justify=LEFT
).grid(
    column=0,
    row=4,
    columnspan=3,
    sticky="nsew",
    padx=10,
    pady=5
)

Label(
    text="Ø6",
    justify=CENTER
).grid(
    column=0,
    row=5,
    sticky="snew",
    padx=10,
    pady=5
)

Label(
    text="Ø8",
    justify=CENTER
).grid(
    column=0,
    row=6,
    sticky="snew",
    padx=10,
    pady=5
)

Label(
    text="Ø10",
    justify=CENTER
).grid(
    column=0,
    row=7,
    sticky="snew",
    padx=10,
    pady=5
)

Label(
    text="Ø12",
    justify=CENTER
).grid(
    column=0,
    row=8,
    sticky="snew",
    padx=10,
    pady=5
)

Label(
    text="Ø16",
    justify=CENTER
).grid(
    column=0,
    row=9,
    sticky="snew",
    padx=10,
    pady=5
)

Label(
    text="Ø20",
    justify=CENTER
).grid(
    column=0,
    row=10,
    sticky="snew",
    padx=10,
    pady=5
)

Label(
    text="Ø25",
    justify=CENTER
).grid(
    column=0,
    row=11,
    sticky="snew",
    padx=10,
    pady=5
)

total = Label(
    text="TOTAL",
    justify=CENTER
)
total.grid(
    column=1,
    row=2,
    sticky="nsew",
    padx=10,
    pady=5
)


# Creamos los cuadros de entrada del nombre de la obra
obra = Entry(
    master,
    justify=CENTER
)
obra.grid(
    column=1,
    row=0,
    sticky="nsew",
    pady=2.5
)


# Creamos los cuadros de lectura del "TOTAL" de elementos computados
tot_hormigon = Entry(
    master,
    justify=CENTER,
    state="readonly"
)
tot_hormigon.grid(
    column=1,
    row=3,
    sticky="nsew"
)

tot_fi6 = Entry(
    master,
    justify=CENTER,
    state="readonly"
)
tot_fi6.grid(
    column=1,
    row=5,
    sticky="nsew"
)

tot_fi8 = Entry(
    master,
    justify=CENTER,
    state="readonly"
)
tot_fi8.grid(
    column=1,
    row=6,
    sticky="nsew"
)

tot_fi10 = Entry(
    master,
    justify=CENTER,
    state="readonly"
)
tot_fi10.grid(
    column=1,
    row=7,
    sticky="nsew"
)

tot_fi12 = Entry(
    master,
    justify=CENTER,
    state="readonly"
)
tot_fi12.grid(
    column=1,
    row=8,
    sticky="nsew"
)

tot_fi16 = Entry(
    master,
    justify=CENTER,
    state="readonly"
)
tot_fi16.grid(
    column=1,
    row=9,
    sticky="nsew"
)

tot_fi20 = Entry(
    master,
    justify=CENTER,
    state="readonly"
)
tot_fi20.grid(
    column=1,
    row=10,
    sticky="nsew"
)

tot_fi25 = Entry(
    master,
    justify=CENTER,
    state="readonly"
)
tot_fi25.grid(
    column=1,
    row=11,
    sticky="nsew"
)

# Creamos los marcos en los cuales estaran alojados los elementos para la edicion y la eliminacion de datos
frame_editar = LabelFrame(master, text="Editar Datos", pady=5, padx=5)
frame_editar.grid(column=0, row=12, padx=10, pady=10)

Label(
    frame_editar,
    text="Obra",
    justify=CENTER).grid(
    column=0,
    row=0,
    sticky="nsew",
    padx=5,
    pady=5
)

entrada_editar = Entry(
    frame_editar,
    justify=CENTER
)
entrada_editar.grid(
    column=1,
    row=0,
    sticky="nsew",
    padx=5,
    pady=5
)

cargar_obra = Button(
    frame_editar,
    text="Cargar",
    command=lambda: exportar_obra(),
    justify=CENTER
)
cargar_obra.grid(
    column=0,
    row=1,
    columnspan=2,
    sticky="nsew",
    padx=5,
    pady=5
)

actualizar_registros = Button(
    frame_editar,
    text="Guardar Cambios",
    command=lambda: update_registros(),
    justify=CENTER,
    state=DISABLED
)
actualizar_registros.grid(
    column=0,
    row=2,
    columnspan=2,
    sticky="nsew",
    padx=5,
    pady=5
)

frame_borrar = LabelFrame(master, text="Borrar Datos", pady=5, padx=5)
frame_borrar.grid(column=0, row=13, padx=10, pady=10)

Label(
    frame_borrar,
    text="Planta",
    justify=CENTER).grid(
    column=0,
    row=0,
    sticky="nsew",
    padx=5,
    pady=5
)

entrada_borrar = Entry(
    frame_borrar,
    justify=CENTER,
    state="readonly",
)
entrada_borrar.grid(
    column=1,
    row=0,
    sticky="nsew",
    padx=5,
    pady=5
)

borrar_planta = Button(
    frame_borrar,
    text="Borrar",
    justify=CENTER,
    state=DISABLED,
    command=lambda: eliminar_planta()
)
borrar_planta.grid(
    column=0,
    row=1,
    columnspan=2,
    sticky="nsew",
    padx=5,
    pady=5
)

borrar_obra = Button(
    frame_borrar,
    text="Borrar Obra",
    justify=CENTER,
    command=lambda: eliminar_obra(),
    state=DISABLED
)
borrar_obra.grid(
    column=0,
    row=2,
    columnspan=2,
    sticky="nsew",
    padx=5,
    pady=5
)

# Creamos botones dentro del cuadro principal
imp_datos = Button(
    master,
    text="Imprimir datos",
    command=lambda: imprimir_datos(),
    pady=5,
    padx=5
)
imp_datos.grid(
    column=2,
    row=0,
    rowspan=2,
    sticky="nsew",
    padx=10,
    pady=5
)

suma_datos = Button(
    master,
    text="Sumar",
    command=lambda: suma(),
    pady=5,
    padx=5
)
suma_datos.grid(
    column=2,
    row=2,
    rowspan=3,
    sticky="nsew",
    padx=10,
    pady=5
)

add_planta = Button(
    master,
    text="Agregar Planta",
    command=lambda: add_columna(),
    pady=5,
    padx=5
)
add_planta.grid(
    column=2,
    row=5,
    rowspan=4,
    sticky="nsew",
    padx=10,
    pady=5
)

del_planta = Button(
    master,
    text="Eliminar Ultima",
    command=lambda: borrar_ultima(),
    pady=5,
    padx=5,
    state=DISABLED
)
del_planta.grid(
    column=2,
    row=9,
    rowspan=3,
    sticky="nsew",
    padx=10,
    pady=5
)


# Creamos una barra de menu para la manipulacion de la base de datos
menubar = Menu(master)
master.config(menu=menubar)

archivo_menu = Menu(
    menubar,
    tearoff=0
)

archivo_menu.add_command(
    label="Crear Base de Datos",
    command=lambda: crear_bd()
)

archivo_menu.add_command(
    label="Insertar Registros",
    command=lambda: importar_registros()
)

archivo_menu.add_command(
    label="Consultar Registros",
    command=lambda: consultar_registros()
)

archivo_menu.add_separator()

archivo_menu.add_command(
    label="Salir",
    command=lambda: salir()
)

menubar.add_cascade(
    label="Archivo",
    menu=archivo_menu
)

master.protocol("WM_DELETE_WINDOW", salir)
master.mainloop()
