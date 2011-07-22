Django
===========
objetivos
-----------
entender la estructura de los proyectos
aplicaciones
arquitectura



Django
===========
definición
--------------

Proyectos y Aplicaciones
======================

Proyecto
==========
    * Es la configuración de una instancia de Django
    * Contiene cosas como:
      - configuración de la BD
      - aplicaciones
      - archivos estáticos
      - etc.
    * Usualmente asociado a un solo sitio aunque puede contener varios.

Creando proyecto
===================

$ django-admin.py startproject djplus

Estructura del proyecto
=======================

djplus
    __init__.py
    manage.py
    settings.py
    urls.py

Corriendo el proyecto
=====================

$ ./manage.py runserver

Comprobemos
=============

Screenshot

Aplicación
=============
    * Colección de código de Django para definir una funcionalidad específica del sitio web
    * Un proyecto puede estar constituido por múltiples aplicaciones
    * Con capacidades para ser reutilizada en otros proyectos

Creando aplicación
===================
$ django-admin.py startapp plus

Estructura de la App
=================
djplus
    plus/
        __init__.py
        models.py
        views.py
    __init__.py
    manage.py
    settings.py
    urls.py

Instalando la aplicación
========================
    * En settings.py
    

Entrando en Detalles
====================

imagen de tripas

Arquitectura
=============
foto arquitectura

Model - View - Template
========================

imagen mtv

Django MVT
============
    * Inspirado en la filosofía MVC
    * Les gustó "romper paradigmas"
    * El modelo se mantiene
    * Controlador -> Vista
    * Vista -> Template 

Vamos por partes
================
foto sushi

Modelo
========
imagen de una modelo


Modelo
========
    * Descripción de los tipo de datos en una aplicación
    * ORM - Object Relational Mapper
    * Mapeo de un objeto a una tabla de una base de datos
    * Nos olvidamos del SQL

Definamos un Modelo
===================
class Status


Modelos contienen relaciones
=============================
imagen de una tabla

SQL de una tabla
=================

Sincronizando la BD
====================

$ ./manage.py syncdb

API de Base de Datos
====================
    * Django provee de una API de alto nivel para trabajar con objetos
    * Provee funciones para crear, obtener, actualizar, eliminar datos 

Creando Objetos
================

* crear un usuario
* crear un status

Obteniendo objetos
===================
los modelos tienen un miembro llamado 'objects', usado para recuperar datos

Users.objects.all()
Users.objects.get(id=10)


Django Admin
=====================================

 * Panel de control para los modelos
 * Opcional
 * agregar django.contrib.admin a INSTALLED_APPS

.. code-block:: bash
    $./manage.py syncdb

 * editar djplus/urls.py

Extendiendo el Panel
========================= 

    * __unicode__
    * class Meta

Vistas
=======
* foto de vista

Vistas
======
objetivos
-----------


Que son las Vistas 
===================

* Tipo de pagina web parte de una aplicación
* Una vista puede realizar funciones específicas y presentar una plantilla
* Una vista es una clase de Python que recibe una petición HTTP y retorna una respuesta HTTP

Ejemplo de Vista
=================

.. code-block:: python


Generic Views
=============

URLConf
========
    * Mapear vistas


Plantillas
===========
    * Define el tipo de dato de una pagina
    * Comunmente usado para generar xHTML
    * Pero se usado para cualquier archivo basado en texto (e-mail, RSS, CSV, XML, etc.)
    * Fueron diseñados pensando en diseñadores gráficos.

Ejemplo de Plantilla
====================
.. code-block:: html


Componentes de Plantillas
=========================
    * Variables
    * Tags
    * Filter

Variables
==========
.. code-block:: html

Filters
========
.. code-block:: html

Tags
======

Herencia de Plantillas
======================

Bloques
=======

Plantilla Base
==============

Plantilla hija
==============

Forms
=======
objetivos



Mas cosas de Django
====================
    * Caching
    * Internacionalización
    * Sesiones
    * Testing
    * Middleware




