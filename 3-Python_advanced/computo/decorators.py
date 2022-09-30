import datetime
from tkinter.messagebox import askyesno, showinfo
import re

def Decorator(method):
    '''
    Decorador que aneja la logica para ejecutar algun metodo, si todo va bien
    ejecuta el meteodo y avisa que accion se realizo en el treeview 'Acciones'
    '''
    def wrap(*args, **kwargs):
        # Definimos la variable del treeview para poder operar con ella
        tree = args[1]
        
        # Definimos los mensajes que se utilizaran en las alertas
        mensaje1 = "Eliminacion de datos"
        mensaje2 = "Se eliminaran todos los campos actuales para realizar la accion, esta seguro?"
        mensaje3 = "Eliminar seleccion"
        mensaje4 = "Los elementos seleccionados tambien seran eliminados de la base de datos, proceder de igual manera?"
        mensaje5 = "Esta seguro que desea remover la obra de la base de datos?"
        
        # Obtenemos el tiempo en el que se ejecut el decorador
        time = datetime.datetime.now().strftime("%H:%M")
        
        if method.__name__ == 'Inicio':
            action = 'App Iniciada -' + time
            tree.insert('', 0, values = (action,))
            
            method(*args,**kwargs)
        
        if method.__name__ == 'Add_columna':
            action = 'Columna agregada -' + time
            tree.insert('', 0, values = (action,))
            
            method(*args,**kwargs)
        
        if method.__name__ == 'Imprimir_datos':
            obra = args[2].get()
            action = 'Computos_' + obra +'.txt creado -' + time
            tree.insert('', 0, values = (action,))
            
            method(*args,**kwargs)
        
        if method.__name__ == 'Alta':
            
            # Verificamos que el nombre de la obra este todo en minusculas y sin espacios, antes de importar losd datos a la tabla
            # Usamos regex para verificar que la obra sea escrita en minusucla, para recuperar datos de manera mas facil
            obra = str(args[2].get())
            patron = "[a-z_0-9]"
            obra_presente = args[3]
            
            if (re.match(patron, obra)):
                if obra not in obra_presente:    
                    if askyesno(mensaje1, mensaje2):
                        
                        action = 'Obra ' + obra + ' guardada -' + time
                        tree.insert('', 0, values = (action,))
                        
                        method(*args,**kwargs)
                        
                else:
                    showinfo("Error al importar obra",
                         "No se pudo importar la obra, ya hay una obra con el mismo nombre")
    
            else:  # Si el nombre de la obra no esta escrito con los caracteres especificados me avisa de ello y no me deja importar los registros
                showinfo("Fallo en importacion",
                         "Fallo al subir los registros a la tabla, el nombre del edificio debe ser escrito todo en minuscula y sin espacios")
            
        
        if method.__name__ == 'Cargar_obra':
            # Mensaje para avisar si esta seguro de la accion a ejecutar
            if askyesno(mensaje1, mensaje2):
                
                obra = args[2]
                action = 'Obra ' + obra + ' cargada -' + time
                tree.insert('', 0, values = (action,))

                method(*args,**kwargs)
        
        if method.__name__ == 'Modificacion':
            # Mensaje para avisar si esta seguro de la accion a ejecutar
            if askyesno(mensaje1, mensaje2):
                
                obra = args[2]
                action = 'Obra ' + obra + ' modificada -' + time
                tree.insert('', 0, values = (action,))

                method(*args,**kwargs)
        
        if method.__name__ == 'Eliminar_seleccion':
            if askyesno(mensaje3, mensaje4):        
            
                chechboxes = args[2]
                contador = 0
                
                for i in chechboxes:
                    if i.get() == 1:
                        contador += 1
                
                contador = str(contador)
                
                action = 'Se eliminaron ' + contador + ' plantas -' + time
                tree.insert('', 0, values = (action,))

                method(*args,**kwargs)
        
        if method.__name__ == 'Eliminar_obra':
            # Mensaje para avisar si esta seguro de la accion a ejecutar
            if askyesno(mensaje1, mensaje5):
                
                obra = args[2]
                action = 'Obra ' + obra + ' eliminada -' + time
                tree.insert('', 0, values = (action,))

                method(*args,**kwargs)        
    return wrap