# DJANGO DOCS

[Django 4.2 Docs](https://docs.djangoproject.com/en/4.2/)

### Topic Guides

A set of complete guides to various Django topics. e.g. model system, template engine, forms framework, etc.

Most developers spend most of their time here. Knowing these guides means a very high level of knowledge of Django.

### How-To Guides

These handle some specific commmon practices used with Django apps. e.g. generatieng PDFs with Django, writing custom template tags, etc.

The FAQ section also has answers to more common questions.

### Reference Guides

The Topic Guides are relatively complete but all the nuts and bolts are in the Reference guides.

## URLs

The `urls.py` file maps URL paths to callback functions (`views.py`).

Each view is passed a request object meta data which is captured in regEx patterns.

## Views

Each view is responsible for returing the HTTP response or raising an exception.

## Templates

The template search path reduces redundancy among templates.
