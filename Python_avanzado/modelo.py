from tkinter import END
from peewee import *
from tkinter.messagebox import *
from decorator import Decorator
import observers

db = SqliteDatabase('de_angelis.db')


class BaseModel(Model):
    class Meta:
        database = db


class Noticia(BaseModel):
    titulo = CharField(unique=True)
    descripcion = TextField()
    mensaje = CharField()


class Abmc(observers.Tema):
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
    
    @Decorator
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

    @Decorator
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

    @Decorator
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
