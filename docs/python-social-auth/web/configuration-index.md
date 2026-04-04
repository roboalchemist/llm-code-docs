# Configuration/Index

Source: https://python-social-auth.readthedocs.io/en/latest/configuration/index.html

Configuration
¶

All the apps share the settings names, some settings for Django framework are
special (like 

AUTHENTICATION_BACKENDS

).

Below there’s a main settings document detailing each configuration and its
purpose, plus sections detailed for each framework and their particularities.

Support for more frameworks will be added in the future, pull-requests are very
welcome.

Contents:

Configuration

Application setup

Settings name

Keys and secrets

Authentication backends

URLs options

User model

Tweaking some fields length

Username generation

Extra arguments on auth processes

OAuth2 provider URLs override

Configurable User ID Key

Processing requests and redirects

Whitelists

Miscellaneous settings

Account disconnection

Django Framework

Installing

Quickstart

Register the application

Database

Authentication backends

URLs entries

Requiring POST only login

Templates

Template Context Processors

Personalized Configuration

ORMs

Active users filtering

JSON field support

Exceptions Middleware

Django Admin

Flask Framework

Dependencies

Installing

Enabling the application

Models Setup

User model reference

Global user

Flask-Login

Remembering sessions

Exceptions handling

Pyramid Framework

Dependencies

Installing

Enabling the application

Models Setup

User model reference

Global user

User login

Social auth in templates context

CherryPy Framework

Dependencies

Installing

Enabling the application

Models Setup

Login mechanism

Webpy Framework

Dependencies

Installing

Configuration

URLs

Session

User model

Porting from django-social-auth

Installed apps

URLs

Porting settings

Authentication backends

Session