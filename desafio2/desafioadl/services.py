# Se importan los modelos creados
from .models import Tarea, SubTarea

# Generación del CRUD de objetos de los modelos

# Leer tareas y subtareas
def recupera_tareas_y_sub_tareas():
    
    tareas = list(Tarea.objects.all())
    subtareas = list(SubTarea.objects.all())

    return tareas, subtareas # Retorna una arreglo con la información

# Imprimir datos en pantalla
def imprimir_en_pantalla():

    # Llama a los registros de la db
    tareas, subtareas = recupera_tareas_y_sub_tareas()

    # Itera las tareas
    for tarea in tareas:
        print(f"[{str(tarea.id)}] {tarea.descripcion}") # Imprime id y descripción

        # Selecciona las subtareas que correspondan a la tarea iterada
        subtareas_filtradas = [subtarea for subtarea in subtareas if subtarea.tarea.id == tarea.id]

        # Itera las subtareas seleccionadas
        for subtarea in subtareas_filtradas:
            print(f".... [{str(subtarea.id)}] {subtarea.descripcion}") # Imprime id y descripción

# Crear una nueva tarea
def crear_nueva_tarea(descripcion):

    # Crea el objeto con el parámetro ingresado
    nueva_tarea = Tarea(descripcion=descripcion)
    nueva_tarea.save() # Almacena la nueva tarea en la db

    imprimir_en_pantalla() # Llama a la función que se encarga de imprimir los datos de la db en pantalla

# Crear una nueva subtarea
def crear_nueva_sub_tarea(tarea_id, descripcion):

    # Obtener la instancia de la tarea
    tarea = Tarea.objects.get(id=tarea_id)

    # Crea el objeto con los parámetros necesarios
    nueva_sub_tarea = SubTarea(tarea=tarea, descripcion=descripcion)
    nueva_sub_tarea.save() # Almacena la nueva subtarea en la db

    imprimir_en_pantalla() # Llama a la función que se encarga de imprimir los datos de la db en pantalla

# Eliminar una tarea
def eliminar_tarea(tarea_id):
    
    # Obtiene la instancia del objeto en base al id
    tarea = Tarea.objects.get(id=tarea_id)
    tarea.delete() # Elimina la tarea de la db

    imprimir_en_pantalla() # Llama a la función que se encarga de imprimir los datos de la db en pantalla

# Eliminar una subtarea
def eliminar_sub_tarea(sub_tarea_id):
    
    # Obtiene la instancia del objeto en base al id
    sub_tarea = SubTarea.objects.get(id=sub_tarea_id)
    sub_tarea.delete() # Elimina la subtarea de la db

    imprimir_en_pantalla() # Llama a la función que se encarga de imprimir los datos de la db en pantalla
