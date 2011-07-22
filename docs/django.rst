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

Definamos la base de datos
===========================
settings.py
--------------
.. code-block:: python
DATABASES = { 
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'plus.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }   
}
.. note:: 
    Diccionarion es Python

Modelo
========
    * Descripción de los tipo de datos en una aplicación
    * ORM - Object Relational Mapper
    * Mapeo de un objeto a una tabla de una base de datos
    * Nos olvidamos del SQL

Definamos un Modelo
===================
.. code-block:: python
from django.db import models

class Status(models.Model):
    text    = models.TextField()
    author  = models.ForeignKey("auth.User")
    created = models.DateTimeField(auto_now_add=True)

Modelos contienen relaciones
=============================
imagen de una tabla

SQL de una tabla
=================
.. code-block:: bash
$ python manage.py sql polls

.. code-block:: sql
BEGIN;
CREATE TABLE "plus_status" (
    "id" integer NOT NULL PRIMARY KEY,
    "text" text NOT NULL,
    "author_id" integer NOT NULL REFERENCES "auth_user" ("id"),
    "created" datetime NOT NULL
);
COMMIT;

Sincronizando la BD
====================
.. code-block:: bash
$ ./manage.py syncdb

API de Base de Datos
====================
    * Django provee de una API de alto nivel para trabajar con objetos
    * Provee funciones para crear, obtener, actualizar, eliminar datos 

Jugando con la API de la BD
============================
.. code-block:: bash
$ python manage.py shell

Creando Objetos
================
Creando un usario
------------------
.. code-block:: python
>>> from django.contrib.auth.models import User
>>> user = User.objects.create_user('erik','erik@rivera.pro', 'erik')
>>> user.save()
>>> user
<User: erik>

Creando Objetos
================
Creando un status
------------------
.. code-block:: python
>>> from plus.models import Status
>>> Status
<class 'plus.models.Status'>
>>> status = Status(text="Primer estado del taller", author=user)
>>> status.save()
>>> status
>>> status.text
'Primer estado del taller'
>>> status.author
<User: erik>
>>>

Obteniendo objetos
===================
.. code-block:: python
los modelos tienen un miembro llamado 'objects', usado para recuperar datos
>>> from django.contrib.auth.models import User 
>>> User.objects.all()
[<User: admin>, <User: juan>]
>>> user = User.objects.get(id=2)
>>> user
<User: erik>
>>> user.email
u'erik@rivera.pro'


Django Admin
=====================================

 * Panel de control para los modelos
 * El panel de control es opcional

Instalando el panel
====================

    * agregar django.contrib.admin a INSTALLED_APPS
    * editar djplus/urls.py 
    * .. code-block:: bash
        $./manage.py syncdb



Agrgando modelos al panel
=========================
 * crear el archivo admin.py
.. code-block:: python
from plus.models import Status
from django.contrib import admin

admin.site.register(Status)

Extendiendo 'Metadata' del modelo
========================= 
.. code-block:: python
class Status(models.Model):
    text    = models.TextField()
    author  = models.ForeignKey("auth.User")
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.text

    class Meta:
        verbose_name_plural = 'Statuses'
        ordering = ['created',]

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
from django.http import HttpResponse
 
def my_status(request):
    return HttpResponse("Hello World!")

URLConf
========
    * Sistema de ruteo de django
    * Mapea las vistas o plantillas a una URL
    * Usa expresiones regulares
    * Evita url sucias

Ejemplo de URLConf
===================
.. code-block:: python
from django.conf.urls.defaults import *
 
urlpatterns = patterns('',
    (r'^hello/', "plus.views.my_status"),
)

Practiquemos!
===============

from django.http import HttpResponse
from plus.models import Status

def my_status(request):
    status = Status.objects.all()
    count = len(status)
    text = "There are %s statuses" %(count)
    return HttpResponse(text)


Vistas Genéricas
=============
    * Conjunto de vistas que integran funcionalidades genéricas y reutilizables
    * Apoyan en el ahorro de tiempo no reescribiendo funciones comúnes

.. note:: Django 1.3 ahora implementa las vistas como Clases, a diferencia pasada que eran funciones las cuales quedarán obsoletas.

Plantillas
===========
    * Define el tipo de dato de una pagina
    * Comunmente usado para generar xHTML
    * Pero se usa para cualquier formato de texto (e-mail, RSS, CSV, XML, etc.)
    * Fueron diseñados pensando en diseñadores gráficos.

Ejemplo de Plantilla
====================
.. code-block:: html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>My Status</title>
    </head>
    <body>
        <h1>Total: {{ statuses|length }}</h1>
        <ul>
        {% for status in stuses %}
            <li>
                <img src="http://rivera.pro/default.gif" width="32px" height="32px">
                <b>{{ status.author.username }} </b>: {{ status.text }}
            </li>
        {% endfor %}
        </ul>
    </body>
</html>

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
.. code-block:: html


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




