from peewee import *
from tkinter.messagebox import *
from tkinter import *
from tkinter.messagebox import *

db = SqliteDatabase('bd_deangelis_intermedio.db')   

class Computos(Model):
    nombre_obra = CharField()
    plantas = CharField()
    hormigon = FloatField()
    fi_6 = FloatField()
    fi_8 = FloatField()
    fi_10 = FloatField()
    fi_12 = FloatField()
    fi_16 = FloatField()
    fi_20 = FloatField()
    fi_25 = FloatField()
    
    class Meta:
        database = db

class bdd():
    """
    Clase que contiene los metodos encargados del manejo de la base de datos
    """

    def __init__(self):  # Al instanciar creo la base de datos
        """
        Al instanciarse en el modulo "main" crea la base de datos "bd_deangelis_intermedio.db"
        Crea la tabla "Computos" y nos conecta a ella
        """

        db.connect()
        db.create_tables ([Computos])

    def Alta(self, obra, th, t6, t8, t10, t12, t16, t20, t25, ep, eh, e6, e8, e10, e12, e16, e20, e25):
        """
        Se hace un alta de registros a la tabla "computos" de la base de datos
        """
        
        # Insertamos los registros
        pos = 0
        for i in range(0, len(ep)):
            computo = Computos(
                nombre_obra = obra.get(),
                plantas = ep[pos].get(),
                hormigon = eh[pos].get(),
                fi_6 = e6[pos].get(),
                fi_8 = e8[pos].get(),
                fi_10 = e10[pos].get(),
                fi_12 = e12[pos].get(),
                fi_16 = e16[pos].get(),
                fi_20 = e20[pos].get(),
                fi_25 = e25[pos].get()
            )
            computo.save()
            pos += 1

        computo_total = Computos(
                nombre_obra = obra.get(),
                plantas = 'Total',
                hormigon = th.get(),
                fi_6 = t6.get(),
                fi_8 = t8.get(),
                fi_10 = t10.get(),
                fi_12 = t12.get(),
                fi_16 = t16.get(),
                fi_20 = t20.get(),
                fi_25 = t25.get()
            )
        computo_total.save()
        

    def Consultar_bdd(self):
        """
        De la base de datos se obtienen todos los datos para luego utilizarlos
        """
        
        resultado = []
        
        # Seleccionamos todos los campos con sus registros para su importacion
        # importamos todo como tupla de datos y se lo agregamos a la lista vacia
        for obra in Computos.select().tuples():
            resultado.append(obra)
            
        return resultado


    def Consultar_obra(self):
        """
        Consulta si el nombre de la obra que se esta a punto de cargar no sea igual 
        A las obras que se encuentran en la base de datos
        Si la obra esta en la base de datos devuelve un valor booleano que impide cargar la obra
        """
        
        lista_obras = []
        for obras in Computos.select():
            lista_obras.append(obras.nombre_obra)     

        return lista_obras


    def Modificacion(self, obra, ep, eh, e6, e8, e10, e12, e16, e20, e25, epid, th, t6, t8, t10, t12, t16, t20, t25, etid):
        """
        Modifica los registros de la base de datos, agregando los cambios realizados o las columnas agregadas
        """

        pos = 0
        # recorremos la lista de obras una por una para modificar cada uno de sus campos
        for i in range(0, len(epid)):
            Computos.update(
                nombre_obra = obra.get(),
                plantas = ep[pos].get(),
                hormigon = eh[pos].get(),
                fi_6 = e6[pos].get(),
                fi_8 = e8[pos].get(),
                fi_10 = e10[pos].get(),
                fi_12 = e12[pos].get(),
                fi_16 = e16[pos].get(),
                fi_20 = e20[pos].get(),
                fi_25 = e25[pos].get(),
            ).where(
                Computos.id == epid[pos]
            ).execute()
            pos += 1  # Paso al siguiente elemento de la lista

        if len(ep) > len(epid):
            # Si llegara a tener mas elementos en la lista de plantas que en la lista de ID esto significa que se aniadieron elementos
            # Por lo tanto procedo a agregar a la tabla los elementos que se agregaron
            # Recorro los elementos restantes que no fueron actualizados y necesitan ser agregados
            
            # Continuo de donde dejo el bucle anterior
            for i in range(len(epid), len(ep)):
                computo = Computos(
                nombre_obra = obra.get(),
                plantas = ep[pos].get(),
                hormigon = eh[pos].get(),
                fi_6 = e6[pos].get(),
                fi_8 = e8[pos].get(),
                fi_10 = e10[pos].get(),
                fi_12 = e12[pos].get(),
                fi_16 = e16[pos].get(),
                fi_20 = e20[pos].get(),
                fi_25 = e25[pos].get()
                )
                computo.save()

                pos += 1  # agrego el siguiente de donde dejo el bucle anterior

        # Una vez modificadas las plantas se procede a actualizar el "TOTAL"
        Computos.update(
                nombre_obra = obra.get(),
                plantas = 'Total',
                hormigon = th.get(),
                fi_6 = t6.get(),
                fi_8 = t8.get(),
                fi_10 = t10.get(),
                fi_12 = t12.get(),
                fi_16 = t16.get(),
                fi_20 = t20.get(),
                fi_25 = t25.get(),
            ).where(
                Computos.id == etid[0]
            ).execute()


    def Eliminar_seleccion(self, id_a_eliminar):
        """
        Elimina de la base de datos la planta seleccionada en los checkboxes
        """

        for i in id_a_eliminar:
            borrar = Computos.get(Computos.id == i)
            borrar.delete_instance()


    def Eliminar_obra(self, obra):
        """
        Elimina la obra cargada de la base de datos
        """

        borrar = Computos.delete().where(Computos.nombre_obra == obra.get())
        borrar.execute()


