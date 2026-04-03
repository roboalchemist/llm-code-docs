# Installing

Source: https://python-social-auth.readthedocs.io/en/latest/installing.html

Installation
¶

python-social-auth
 is a very modular library looking to provide the
basic tools to implement social authentication / authorization in
Python projects. For that reason, the project is split in smaller
components that focus on providing a simpler functionality. Some
components are:

social-auth-core

Core library that the rest depends on, this contains the basic
functionality to establish an authentication/authorization flow with
the different supported providers.

social-auth-storage-sqlalchemy
, 
social-auth-storage-peewee
, 
social-auth-storage-mongoengine

Different storage solutions that can be reused across the supported
frameworks or newer implementations.

social-auth-app-django
, 
social-auth-app-django-mongoengine

Django framework integration

social-auth-app-flask
, 
social-auth-app-flask-sqlalchemy
, 
social-auth-app-flask-mongoengine
, 
social-auth-app-flask-peewee

Flask framework integration

social-auth-app-pyramid

Pyramid framework integration

social-auth-app-cherrypy

Cherrypy framework integration

social-auth-app-tornado

Tornado framework integration

social-auth-app-webpy

Webpy framework integration

Dependencies
¶

Dependencies are properly defined in the requirements files.
There are some 

extras

 defined to install the corresponding
dependencies since they are required to build extensions that, unless
used, are undesired.

SAML

 support requires the use of the 

saml

 extra.

Shopify

 support requires the use of the 

shopify

 extra.

Google

 One Tap support requires the use of the 

google-onetap

 extra.

Microsoft Azure Active Directory

 support requires the use of the 

azuread

 extra.

There’s also the 

all

 extra that will install all the extra options.

Several backends demand application registration on their
corresponding sites and other dependencies like 
SQLAlchemy
 on Flask
and Webpy.

Get a copy
¶

From 
PyPI
:

$ pip install social-auth-&lt;component&gt;

Or, grab the relevant repository from 
GitHub
, then:

$ cd social-auth-&lt;component&gt;
$ sudo python setup.py install

Using the 

extras

 options
¶

To enable any of the 

extras

 options to bring the dependencies for

SAML
, or all:

$ pip install &quot;social-auth-core[saml]&quot;
$ pip install &quot;social-auth-core[all]&quot;