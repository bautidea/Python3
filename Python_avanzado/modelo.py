from tkinter import END
from peewee import *
from tkinter.messagebox import *
from decorator import Decorator
import observers

# Implementamos el ORM peewee, para el CRUD de la base de datos

# Indicamos el nombre de la base de datos y el tipo.
db = SqliteDatabase('de_angelis.db')

class BaseModel(Model):
    # Clase con la cual especificamos la base de datos con la cual
    # vamos a trabajar
    
    class Meta:
        database = db


class Noticia(BaseModel):
    # Clase que va a ser mapeada por el ORM, cada atributo
    # corresponde a una columna de la base de datos
    titulo = CharField(unique=True)
    descripcion = TextField()
    mensaje = CharField()


class Abmc(observers.Tema):
    # Clase encargada del CRUD de la base de datos, esta clase
    # hereda de la clase 'tema', del modulo 'observers.py', la cual
    # le avisa a los observadores que a habido un cambio de estado
    # cuando se ejecuta determinado metodo ('alta', 'bajo', 'modificar')
    # para que los observadores creen un log que informe los cambios.
    
    def __init__(self):
        # Metodo de instancia, nos conecta a la base de datos
        # crea la tabla 'noticias' si esta no esta creda
        
        db.connect()
        db.create_tables([Noticia])

    def actualizar_treeview(self, mitreeview):
        # Metodo de clase, limpia el treeview, y hace un query de los datos
        # para mostrarlos en el mismo.
        
        # Lista vacia para poder agregar datos de la base. 
        lista_datos = []
        
        contador = 0
        
        # limpieza de tabla.
        records = mitreeview.get_children()
        for element in records:
            mitreeview.delete(element)
            
        # Consiguiendo datos y añadiendolos a lista_datos.
        for i in Noticia.select().order_by(Noticia.id.desc()):
            lista_datos.append((i.id, i.titulo, i.descripcion, i.mensaje))

        # Inserto los datos recuperados de la base.
        for i in lista_datos:
            mitreeview.insert(
                "",
                0,
                values=i
            )
            contador += 1
    
    @Decorator
    def alta(self, titulo, descripcion, mitreeview, accion):
        # Metodo de clase, sube los parametros que se le pasa desde 'vista.py'
        # a la base de datos.
        try:
            dato = [titulo.get(), descripcion.get(), accion]
            noticia = Noticia(
                titulo=dato[0], descripcion=dato[1], mensaje=dato[2])

            noticia.save()

            self.actualizar_treeview(mitreeview)
            
            # Ejecuto el metodo de la clase padre 'Temas', para que notifica a los observers de que
            # se realizo un alta de datos, le paso el parametro agregado a la base de datos.
            self.Notify_alta(titulo.get())

        except:
            # En caso de que ya haya un titulo con el mismo nombre, me lo advierte.
            showinfo("Error en alta de datos",
                     "Ya se encuentra un titulo cargado con ese nombre, intente otro")

    @Decorator
    def baja(self,titulo, mitreeview):
        # Metodo de clase, borra el elemento seleccionado en el treeview de la base de datos.

        item_seleccionado = mitreeview.focus()
        valor_id = mitreeview.item(item_seleccionado, "values")
        id_eliminar = valor_id[0]

        noticia = Noticia.get(Noticia.id == id_eliminar)
        noticia.delete_instance()

        self.actualizar_treeview(mitreeview)
        
        # Ejecuto el metodo de la clase padre 'Temas', para que notifique a los observers de que
        # se realizo una baja de datos, le paso el parametro del titulo borrado de la base de datos.
        self.Notify_borrar(titulo.get())


    @Decorator
    def modificar(self, titulo, descripcion, mitreeview, accion, titulo_anterior):
        # Metodo de clase, modifica los valores del elemento seleccionado en el treeview.
        
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
            
            # Ejecuto el metodo de la clase padre 'Temas', para que noifique a los observers de que
            # se realizo una modificacion de datos, le paso el parametro del titulo modificado y 
            # del titulo anterior.
            self.Notify_modificar(titulo.get(), titulo_anterior)
        except:
            # En caso de que ya haya un titulo con el mismo nombre, me lo advierte.
            showinfo("Error en alta de datos",
                     "Ya se encuentra un titulo cargado con ese nombre, intente otro")
            titulo.delete(0, END)
