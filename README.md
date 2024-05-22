# Desafio - Django Acceso a Datos

Este proyecto consiste en un sistema de administración de tareas desarrollado en Django, que permite gestionar tanto las tareas principales como sus sub tareas asociadas.

## Requerimientos del Proyecto

1. **Proyecto y Aplicación**: El proyecto se denomina "desafio2" y contiene una aplicación llamada "desafioadl".

2. **Base de Datos**: La conexión a la base de datos se realiza utilizando PostgreSQL.

3. **Modelos**: En la aplicación "desafioadl" existen dos modelos: Tarea y SubTarea. Ambos modelos tienen campos de id y descripción, y la SubTarea tiene una relación con Tarea.

4. **Servicios**: Se crea el archivo `services.py` en la carpeta `desafioadl`, donde se implementan seis funciones para operar sobre los modelos:
    - `recupera_tareas_y_sub_tareas`
    - `crear_nueva_tarea`
    - `crear_sub_tarea`
    - `eliminar_tarea`
    - `eliminar_sub_tarea`
    - `imprimir_en_pantalla`

5. **Funcionalidad**: Cada función que opera sobre los modelos debe devolver un arreglo con las tareas y subtareas actualizadas. La función `imprimir_en_pantalla` debe recibir este arreglo y mostrar las tareas y subtareas de manera ordenada.

## Capturas de Pantalla

Se adjunta una carpeta en el directorio raíz llamada "screenshots" que contiene capturas de pantalla que muestran el proceso de trabajo realizado, incluyendo la ejecución de las funciones desde la shell de Python, la creación de tareas y subtareas, y la impresión ordenada de tareas y subtareas, entre otros.

## Configuración del Proyecto

Para ejecutar el proyecto:

1. Clona el repositorio en tu máquina local.
2. Configura el entorno virtual y activa el entorno.
3. Instala las dependencias del proyecto utilizando el archivo `requirements.txt`.
4. Asegúrate de tener PostgreSQL instalado y configurado.
5. Configura las credenciales de tu base de datos en el archivo `settings.py`.
6. Ejecuta las migraciones para crear las tablas en la base de datos.
7. Accede a la shell de Django `python manage.py shell`.
8. Ejecuta las funciones definidas en el archivo `services.py`.

## Autor

Este proyecto fue desarrollado por Jose Contreras Stoltze
