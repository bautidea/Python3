from unittest import result
from modelo import bdd
from peewee import *

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

db.connect()
db.create_tables ([Computos])


resultado = []
# Seleccionamos todos los campos con sus registros para su importacion
# importamos todo y se lo agregamos a la lista vacia
for obra in Computos.select():
    resultado.append(obra)
    
print(resultado)

