from json.tool import main
import mysql.connector
from tkinter.messagebox import *
from tkinter import *
from tkinter.messagebox import *
import os
import datetime


class bdd():
    """
    Clase que contiene los metodos encargados del manejo de la base de datos
    """
    ruta = os.path.dirname(os.path.abspath(__file__))+"\\log.txt"
    obra_presente = False

    def __init__(self, ventana):  # Al iniciar creo la base de datos
        """
        Al instanciarse en el modulo "main" crea la base de datos "de_angelis_bd"
        Crea un archivo de texto el cual muestra todas las acciones que se realizan en la base de datos
        """

        try:
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

            jbda_bd.close()

            if not os.path.isfile(self.ruta):
                self.log_info(
                    "REGISTRO CREADO",
                    "Se creo el registo de datos",
                    datetime.datetime.now()
                )

            # Si todo va bien se nos notifica de la creacion de la base de datos
            self.log_info(
                "EXITO",
                "Se creo la base de datos",
                datetime.datetime.now()
            )

        # En caso de que la base de datos este creada, para que no haya error
        except mysql.connector.errors.DatabaseError as nro_error:

            err = nro_error.errno

            if err == 2003:
                if not os.path.isfile(self.ruta):
                    self.log_info(
                        "REGISTRO CREADO",
                        "Se creo el registo de datos",
                        datetime.datetime.now()
                    )

                try:
                    raise error_bdd()

                except error_bdd as ce:
                    ce.mi_error("ERROR",
                                "No es posible conectarse al servidor MySQL",
                                datetime.datetime.now(),
                                ventana
                                )

            elif err == 1007:
                if not os.path.isfile(self.ruta):
                    self.log_info(
                        "REGISTRO CREADO",
                        "Se creo el registo de datos",
                        datetime.datetime.now()
                    )

                self.log_info(
                    "MENSAJE",
                    "La base de datos ya existe",
                    datetime.datetime.now()
                )

        except:
            self.log_info(
                "ERROR",
                "Se producio un error no identificado",
                datetime.datetime.now()
            )

    def crear_tabla(self):
        """
        Crea la tabla "computos" en la base de datos creada en la instanciacion
        Este metodo se ejecuta de manera automatica al iniciarse la aplicacion
        """

        try:
            # Nos conectamos a la base de datos creada
            jbda_bd = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="de_angelis_bd"
            )

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

            jbda_bd.commit()

            # Cerramos la conexion a la base de datos
            jbda_bd.close()

            # Si todo va bien se nos notifica de la creacion de la tabla
            self.log_info("EXITO", "Tabla computos creada",
                          datetime.datetime.now())
        except mysql.connector.errors.DatabaseError as nro_error:

            err = nro_error.errno

            if err == 1050:
                if not os.path.isfile(self.ruta):
                    self.log_info(
                        "REGISTRO CREADO",
                        "Se creo el registo de datos",
                        datetime.datetime.now()
                    )

                self.log_info(
                    "MENSAJE",
                    "La tabla computos ya existe",
                    datetime.datetime.now()
                )

    def log_info(self, evento, mensaje, fecha):
        """
        Graba en el archivo de texto las acciones que se realizan en la base de datos
        Crea Ventanas emergentes con dichas acciones
        """

        showinfo(evento, mensaje)
        log = open(self.ruta, "a")
        print(evento, mensaje, fecha, file=log)

    def conectar(self):
        """
        Metodo el cual se va a utilizara para contectarse a la base de datos
        """

        # Nos conectamos a la base de datos creada
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="de_angelis_bd"
        )

        return con

    def importar_registros(self, obra, th, t6, t8, t10, t12, t16, t20, t25, ep, eh, e6, e8, e10, e12, e16, e20, e25):
        """
        Se importan los registros a la tabla "computos" de la base de datos
        """

        con = self.conectar()

        micursor = con.cursor()

        # Insertamos los registros
        pos = 0
        for i in range(0, len(ep)):
            sql = """INSERT INTO computos (nombre_obra, plantas, hormigon, fi_6, fi_8, fi_10, fi_12, fi_16, fi_20, fi_25)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            record = (
                obra.get(),
                ep[pos].get(),
                eh[pos].get(),
                e6[pos].get(),
                e8[pos].get(),
                e10[pos].get(),
                e12[pos].get(),
                e16[pos].get(),
                e20[pos].get(),
                e25[pos].get(),
            )

            micursor.execute(sql, record)

            pos += 1

        sql_total = """INSERT INTO computos (nombre_obra, plantas, hormigon, fi_6, fi_8, fi_10, fi_12, fi_16, fi_20, fi_25)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        record_total = (
            obra.get(),
            "total",
            th.get(),
            t6.get(),
            t8.get(),
            t10.get(),
            t12.get(),
            t16.get(),
            t20.get(),
            t25.get(),
        )

        micursor.execute(sql_total, record_total)

        con.commit()
        con.close()

        mensaje = "La obra " + str(obra.get()) + " se importo con exito"

        self.log_info("IMPORTACION EXITOSA", mensaje, datetime.datetime.now())

    def consultar_bdd(self):
        """
        De la base de datos se obtienen todos los datos para luego utilizarlos
        """

        con = self.conectar()
        micursor = con.cursor()

        # Seleccionamos todos los campos con sus registros para su importacion
        micursor.execute("SELECT * FROM computos")
        # Le decimos al cursor que nos importe todo, y lo asociamos a una variable
        resultado = micursor.fetchall()

        con.commit()
        con.close()

        log = open(self.ruta, "a")

        print("CONSULTA", "La tabla computos fue consultada",
              datetime.datetime.now(), file=log)

        return resultado

    def consultar_obra(self, obra):
        """
        Consulta si el nombre de la obra que se esta a punto de cargar no sea igual 
        A las obras que se encuentran en la base de datos
        Si la obra esta en la base de datos devuelve un valor booleano que impide cargar la obra
        """

        con = self.conectar()
        micursor = con.cursor()

        # Seleccionamos todos los campos con sus registros para su importacion
        micursor.execute("SELECT nombre_obra FROM computos")
        # Le decimos al cursor que nos importe todo, y lo asociamos a una variable
        obra_bdd = micursor.fetchall()

        con.commit()
        con.close()

        for i in obra_bdd:
            if i[0] == obra.get():
                self.obra_presente = True
                break

    def modificar_registros(self, obra, ep, eh, e6, e8, e10, e12, e16, e20, e25, epid, th, t6, t8, t10, t12, t16, t20, t25, etid):
        """
        Modifica los registros de la base de datos, agregando los cambios realizados o las columnas agregadas
        """

        con = self.conectar()
        micursor = con.cursor()

        pos = 0
        # recorremos la lista de obras una por una para modificar cada uno de sus campos
        for i in range(0, len(epid)):
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
                ep[pos].get(),
                eh[pos].get(),
                e6[pos].get(),
                e8[pos].get(),
                e10[pos].get(),
                e12[pos].get(),
                e16[pos].get(),
                e20[pos].get(),
                e25[pos].get(),
                epid[pos]
            )
            micursor.execute(sql, record)
            con.commit()

            pos += 1  # Paso al siguiente elemento de la lista

        if len(ep) > len(epid):
            # Si llegara a tener mas elementos en la lista de plantas que en la lista de ID esto significa que se aniadieron elementos
            # Por lo tanto procedo a agregar a la tabla los elementos que se agregaron
            # Recorro los elementos restantes que no fueron actualizados y necesitan ser agregados
            # Continuo de donde dejo el bucle anterior
            for i in range(len(epid), len(ep)):
                sql = """INSERT INTO computos (nombre_obra, plantas, hormigon, fi_6, fi_8, fi_10, fi_12, fi_16, fi_20, fi_25)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                record = (
                    obra.get(),
                    ep[pos].get(),
                    eh[pos].get(),
                    e6[pos].get(),
                    e8[pos].get(),
                    e10[pos].get(),
                    e12[pos].get(),
                    e16[pos].get(),
                    e20[pos].get(),
                    e25[pos].get(),
                )

                micursor.execute(sql, record)
                con.commit()

                pos += 1  # agrego el siguiente de donde dejo el bucle anterior

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
            th.get(),
            t6.get(),
            t8.get(),
            t10.get(),
            t12.get(),
            t16.get(),
            t20.get(),
            t25.get(),
            etid[0]
        )
        micursor.execute(sql, record)
        con.commit()

        con.close()
        msje = "La obra " + str(obra.get()) + " fue modificada"
        self.log_info("REGISTRO MODIFICADO", msje, datetime.datetime.now())

    def eliminar_planta(self, elemento, eb, obra):
        """
        Elimina de la base de datos la planta especificada en el cuadro de entrada del marco "Borrar Datos"
        """

        try:
            con = self.conectar()
            micursor = con.cursor()

            sql = "DELETE FROM computos WHERE id = %s"
            eliminar = (str(elemento),)

            micursor.execute(sql, eliminar)
            con.commit()
            con.close()

            msje = "La planta " + str(eb.get()) + \
                " fue eliminada de la obra " + obra.get()

            self.log_info("PLANTA ELIMINADA", msje, datetime.datetime.now())

        except IndexError:
            showinfo("Error al borrar planta",
                     "La planta que usted precisa borrar no se encuentra cargada en la base de datos")
            eb.delete(0, END)

    def eliminar_obra(self, obra):
        """
        Elimina la obra cargada de la base de datos
        """

        con = self.conectar()
        micursor = con.cursor()

        sql = "DELETE FROM computos WHERE nombre_obra = %s"
        eliminar = (str(obra.get()),)

        micursor.execute(sql, eliminar)
        con.commit()
        # Cerramos la conexion a la base de datos
        con.close()

        msje = "La obra " + str(obra.get()) + \
            " fue eliminada de la base de datos"
        self.log_info("OBRA ELIMINAD", msje, datetime.datetime.now())


class error_bdd (Exception):
    """
    Esta clase se utiliza para el manejos de excepciones
    En caso de que no sea posible conectarse al servidor MySQL
    No permite utilizar la aplicacion ya que la cierra
    """

    ruta = os.path.dirname(os.path.abspath(__file__))+"\\log.txt"

    def mi_error(self, evento, mensaje, fecha, ventana):
        showinfo(evento, mensaje)
        log = open(self.ruta, "a")
        print(evento, mensaje, fecha, file=log)
        ventana.destroy()
