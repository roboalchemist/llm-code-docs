# Source: https://banana.readthedocs.io/en/r3.0/multidb.html

Title: Banana and multiple databases — Banana 2.0 documentation

URL Source: https://banana.readthedocs.io/en/r3.0/multidb.html

Markdown Content:
The way we deploy TRAP and Banana at the University of Amsterdam is that various scientists create multiple PostgreSQL and MonetDB databases and populate these with data. We want to be able to visualise the content of all these databases.

We’ve created various helper functions (`project.settings.database`) that assist in automatically populating the Django configuration with our site specific configuration. It is adviced **not** to use these in production, but rather build a manual configuration.

The database which is used is based on the URL, specifically the URL variable. We’ve crafted a combination of Django middleware and Django database routing that makes Django use the desired database. Below is the module documentation for that logic.

Module documentation[¶](https://banana.readthedocs.io/en/r3.0/multidb.html#module-project.multidb "Permalink to this headline")
-------------------------------------------------------------------------------------------------------------------------------

Select database based on URL variable

Inspired by [this Django snipped](https://djangosnippets.org/snippets/2037/).

It’s assumed that any view in the system with a cfg keyword argument passed to it from the urlconf may be routed to a separate database. for example:

url( r'^(?P<db>\w+)/account/$', 'views.account' )

The middleware and router will select a database whose alias is <db>, **default** if no db argument is given and raise a 404 exception if not listed in **settings.DATABASES**, all completely transparent to the view itself.

_class_`project.multidb.``MultiDbRouter`[[source]](https://banana.readthedocs.io/en/r3.0/_modules/project/multidb.html#MultiDbRouter)[¶](https://banana.readthedocs.io/en/r3.0/multidb.html#project.multidb.MultiDbRouter "Permalink to this definition")
The multiple database router.

Add this to your Django database router configuration, for example:

DATABASE_ROUTERS += ['project.multidb.MultiDbRouter']

_class_`project.multidb.``MultiDbRouterMiddleware`[[source]](https://banana.readthedocs.io/en/r3.0/_modules/project/multidb.html#MultiDbRouterMiddleware)[¶](https://banana.readthedocs.io/en/r3.0/multidb.html#project.multidb.MultiDbRouterMiddleware "Permalink to this definition")
The Multidb router middelware.

he middleware process_view (or process_request) function sets some context from the URL into thread local storage, and process_response deletes it. In between, any database operation will call the router, which checks for this context and returns an appropriate database alias.

Add this to your middleware, for example:

MIDDLEWARE_CLASSES += ['project.multidb.MultiDbRouterMiddleware']

`project.multidb.``multidb_context_processor`(_request_)[[source]](https://banana.readthedocs.io/en/r3.0/_modules/project/multidb.html#multidb_context_processor)[¶](https://banana.readthedocs.io/en/r3.0/multidb.html#project.multidb.multidb_context_processor "Permalink to this definition")
This context processor will add a db_name to the request.

Add this to your Django context processors, for example:

TEMPLATE_CONTEXT_PROCESSORS +=[
    'project.multidb.multidb_context_processor']
