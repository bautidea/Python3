from tkinter import END
from peewee import *
from tkinter.messagebox import *
import os
import datetime

class Log():
    def Decorator(method):
        def txt(self, *args):
            ruta = os.path.dirname(os.path.abspath(__file__))+"\\Log.txt"
            log = open(ruta, 'a+')
            
            time = datetime.datetime.now().strftime("%d/%m/%y %H:%M")
            titulo = args[0].get()
            
            if method.__name__ == 'alta':
                estado = 'Creado'
            
            if method.__name__ == 'baja':
                estado = 'Eliminado'
            
            if method.__name__ == 'modificar':
                if titulo != args[4]: 
                    estado = 'Nombre modificado' + ' - (Nombre anterior: ' + str(args[4]) + ')'
                else:
                    estado = 'Modificado'

            print(time, '-', 'Titulo', titulo, estado, file= log)  
            log.close()    
            method(self,*args)
        return txt

db = SqliteDatabase('de_angelis.db')


class BaseModel(Model):
    class Meta:
        database = db


class Noticia(BaseModel):
    titulo = CharField(unique=True)
    descripcion = TextField()
    mensaje = CharField()


class Abmc(Log):
    def __init__(self):
        db.connect()
        db.create_tables([Noticia])

    def actualizar_treeview(self, mitreeview):
        lista_datos = []
        contador = 0
        # limpieza de tabla
        records = mitreeview.get_children()
        for element in records:
            mitreeview.delete(element)
        # Consiguiendo datos
        for i in Noticia.select().order_by(Noticia.id.desc()):
            lista_datos.append((i.id, i.titulo, i.descripcion, i.mensaje))

        for i in lista_datos:
            mitreeview.insert(
                "",
                0,
                values=i
            )
            contador += 1
    
    @Log.Decorator
    def alta(self, titulo, descripcion, mitreeview, accion):
        try:
            dato = [titulo.get(), descripcion.get(), accion]
            noticia = Noticia(
                titulo=dato[0], descripcion=dato[1], mensaje=dato[2])

            noticia.save()

            self.actualizar_treeview(mitreeview)

        except:
            showinfo("Error en alta de datos",
                     "Ya se encuentra un titulo cargado con ese nombre, intente otro")

    @Log.Decorator
    def baja(self,titulo, mitreeview):
        try:
            item_seleccionado = mitreeview.focus()
            valor_id = mitreeview.item(item_seleccionado, "values")
            datos = valor_id[0]

            noticia = Noticia.get(Noticia.id == datos)
            noticia.delete_instance()

            self.actualizar_treeview(mitreeview)
        except:
            showinfo("Error al borrar datos",
                     "Usted no a seleccionado ninguna fila para eliminar")

    @Log.Decorator
    def modificar(self, titulo, descripcion, mitreeview, accion, titulo_anterior):
        try:
            item_seleccionado = mitreeview.focus()
            valor_id = mitreeview.item(item_seleccionado, "values")
            datos = [titulo.get(), descripcion.get(), valor_id[0], accion]

            Noticia.update(
                titulo=datos[0],
                descripcion=datos[1],
                mensaje=accion
            ).where(
                Noticia.id == datos[2]
            ).execute()

            self.actualizar_treeview(mitreeview)
        except:
            showinfo("Error en alta de datos",
                     "Ya se encuentra un titulo cargado con ese nombre, intente otro")
            titulo.delete(0, END)
