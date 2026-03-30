# Source: https://www.psycopg.org/docs/faq.html

Title: Frequently Asked Questions — Psycopg 2.9.11 documentation

URL Source: https://www.psycopg.org/docs/faq.html

Published Time: Sun, 08 Mar 2026 18:42:13 GMT

Markdown Content:
Frequently Asked Questions — Psycopg 2.9.11 documentation
===============

[Psycopg 2.9.11 documentation](https://www.psycopg.org/docs/index.html)
=======================================================================

* ← [`psycopg2.errorcodes` – Error codes defined by PostgreSQL](https://www.psycopg.org/docs/errorcodes.html "Previous document")
* [Release notes](https://www.psycopg.org/docs/news.html "Next document") →

* [Home](https://www.psycopg.org/docs/index.html)

Frequently Asked Questions[¶](https://www.psycopg.org/docs/faq.html#frequently-asked-questions "Link to this heading")
======================================================================================================================

Here are a few gotchas you may encounter using [`psycopg2`](https://www.psycopg.org/docs/module.html#module-psycopg2 "psycopg2"). Feel free to suggest new entries!

Meta[¶](https://www.psycopg.org/docs/faq.html#meta "Link to this heading")
--------------------------------------------------------------------------

How do I ask a question?

* Have you first checked if your question is answered already in the documentation?

* If your question is about installing psycopg, have you checked the [install FAQ](https://www.psycopg.org/docs/faq.html#faq-compile) and the [install docs](https://www.psycopg.org/docs/install.html#installation)?

* Have you googled for your error message?

* If you haven’t found an answer yet, please write to the [Mailing List](https://www.postgresql.org/list/psycopg/).

* If you haven’t found a bug, DO NOT write to the bug tracker to ask questions. You will only get piro grumpy.

Problems with transactions handling[¶](https://www.psycopg.org/docs/faq.html#problems-with-transactions-handling "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------

Why does `psycopg2` leave database sessions “idle in transaction”?
Psycopg normally starts a new transaction the first time a query is executed, e.g. calling [`cursor.execute()`](https://www.psycopg.org/docs/cursor.html#cursor.execute "cursor.execute"), even if the command is a `SELECT`. The transaction is not closed until an explicit [`commit()`](https://www.psycopg.org/docs/connection.html#connection.commit "connection.commit") or [`rollback()`](https://www.psycopg.org/docs/connection.html#connection.rollback "connection.rollback").

If you are writing a long-living program, you should probably make sure to call one of the transaction closing methods before leaving the connection unused for a long time (which may also be a few seconds, depending on the concurrency level in your database). Alternatively you can use a connection in [`autocommit`](https://www.psycopg.org/docs/connection.html#connection.autocommit "connection.autocommit") mode to avoid a new transaction to be started at the first command.

I receive the error _current transaction is aborted, commands ignored until end of transaction block_ and can’t do anything else!
There was a problem _in the previous_ command to the database, which resulted in an error. The database will not recover automatically from this condition: you must run a [`rollback()`](https://www.psycopg.org/docs/connection.html#connection.rollback "connection.rollback") before sending new commands to the session (if this seems too harsh, remember that PostgreSQL supports nested transactions using the [`SAVEPOINT`](https://www.postgresql.org/docs/current/static/sql-savepoint.html) command).

Why do I get the error _current transaction is aborted, commands ignored until end of transaction block_ when I use `multiprocessing` (or any other forking system) and not when use `threading`?
Psycopg’s connections can’t be shared across processes (but are thread safe). If you are forking the Python process make sure to create a new connection in each forked child. See [Thread and process safety](https://www.psycopg.org/docs/usage.html#thread-safety) for further informations.

Problems with type conversions[¶](https://www.psycopg.org/docs/faq.html#problems-with-type-conversions "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------

Why does `cursor.execute()` raise the exception _can’t adapt_?
Psycopg converts Python objects in a SQL string representation by looking at the object class. The exception is raised when you are trying to pass as query parameter an object for which there is no adapter registered for its class. See [Adapting new Python types to SQL syntax](https://www.psycopg.org/docs/advanced.html#adapting-new-types) for informations.

I can’t pass an integer or a float parameter to my query: it says _a number is required_, but _it is_ a number!
In your query string, you always have to use `%s` placeholders, even when passing a number. All Python objects are converted by Psycopg in their SQL representation, so they get passed to the query as strings. See [Passing parameters to SQL queries](https://www.psycopg.org/docs/usage.html#query-parameters).

>>> cur.execute("INSERT INTO numbers VALUES (%d)", (42,)) # WRONG
>>> cur.execute("INSERT INTO numbers VALUES (%s)", (42,)) # correct

I try to execute a query but it fails with the error _not all arguments converted during string formatting_ (or _object does not support indexing_). Why?
Psycopg always require positional arguments to be passed as a sequence, even when the query takes a single parameter. And remember that to make a single item tuple in Python you need a comma! See [Passing parameters to SQL queries](https://www.psycopg.org/docs/usage.html#query-parameters).

>>> cur.execute("INSERT INTO foo VALUES (%s)", "bar")    # WRONG
>>> cur.execute("INSERT INTO foo VALUES (%s)", ("bar"))  # WRONG
>>> cur.execute("INSERT INTO foo VALUES (%s)", ("bar",)) # correct
>>> cur.execute("INSERT INTO foo VALUES (%s)", ["bar"])  # correct

My database is Unicode, but I receive all the strings as UTF-8 `str`. Can I receive `unicode` objects instead?
The following magic formula will do the trick:

psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)

See [Unicode handling](https://www.psycopg.org/docs/usage.html#unicode-handling) for the gory details.

My database is in mixed encoding. My program was working on Python 2 but Python 3 fails decoding the strings. How do I avoid decoding?
From psycopg 2.8 you can use the following adapters to always return bytes from strings:

psycopg2.extensions.register_type(psycopg2.extensions.BYTES)
psycopg2.extensions.register_type(psycopg2.extensions.BYTESARRAY)

See [Unicode handling](https://www.psycopg.org/docs/usage.html#unicode-handling) for an example.

Psycopg converts `decimal`/`numeric` database types into Python `Decimal` objects. Can I have `float` instead?
You can register a customized adapter for PostgreSQL decimal type:

DEC2FLOAT = psycopg2.extensions.new_type(
    psycopg2.extensions.DECIMAL.values,
    'DEC2FLOAT',
    lambda value, curs: float(value) if value is not None else None)
psycopg2.extensions.register_type(DEC2FLOAT)

See [Type casting of SQL types into Python objects](https://www.psycopg.org/docs/advanced.html#type-casting-from-sql-to-python) to read the relevant documentation. If you find `psycopg2.extensions.DECIMAL` not available, use `psycopg2._psycopg.DECIMAL` instead.

Psycopg automatically converts PostgreSQL `json` data into Python objects. How can I receive strings instead?
The easiest way to avoid JSON parsing is to register a no-op function with [`register_default_json()`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.register_default_json "psycopg2.extras.register_default_json"):

psycopg2.extras.register_default_json(loads=lambda x: x)

See [JSON adaptation](https://www.psycopg.org/docs/extras.html#adapt-json) for further details.

Psycopg converts `json` values into Python objects but `jsonb` values are returned as strings. Can `jsonb` be converted automatically?
Automatic conversion of `jsonb` values is supported from Psycopg release 2.5.4. For previous versions you can register the `json` typecaster on the `jsonb` oids (which are known and not supposed to change in future PostgreSQL versions):

psycopg2.extras.register_json(oid=3802, array_oid=3807, globally=True)

See [JSON adaptation](https://www.psycopg.org/docs/extras.html#adapt-json) for further details.

How can I pass field/table names to a query?
The arguments in the [`execute()`](https://www.psycopg.org/docs/cursor.html#cursor.execute "cursor.execute") methods can only represent data to pass to the query: they cannot represent a table or field name:

# This doesn't work

cur.execute("insert into %s values (%s)", ["my_table", 42])

If you want to build a query dynamically you can use the objects exposed by the [`psycopg2.sql`](https://www.psycopg.org/docs/sql.html#module-psycopg2.sql "psycopg2.sql") module:

cur.execute(
    sql.SQL("insert into %s values (%%s)") % [sql.Identifier("my_table")],
    [42])

Transferring binary data from PostgreSQL 9.0 doesn’t work.
PostgreSQL 9.0 uses by default [the “hex” format](https://www.postgresql.org/docs/current/static/datatype-binary.html) to transfer `bytea` data: the format can’t be parsed by the libpq 8.4 and earlier. The problem is solved in Psycopg 2.4.1, that uses its own parser for the `bytea` format. For previous Psycopg releases, three options to solve the problem are:

* set the [bytea_output](https://www.postgresql.org/docs/current/static/runtime-config-client.html#GUC-BYTEA-OUTPUT) parameter to `escape` in the server;

* execute the database command `SET bytea_output TO escape;` in the session before reading binary data;

* upgrade the libpq library on the client to at least 9.0.

Arrays of _TYPE_ are not casted to list.
Arrays are only casted to list when their oid is known, and an array typecaster is registered for them. If there is no typecaster, the array is returned unparsed from PostgreSQL (e.g. `{a,b,c}`). It is easy to create a generic arrays typecaster, returning a list of array: an example is provided in the [`new_array_type()`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.new_array_type "psycopg2.extensions.new_array_type") documentation.

Best practices[¶](https://www.psycopg.org/docs/faq.html#best-practices "Link to this heading")
----------------------------------------------------------------------------------------------

When should I save and re-use a cursor as opposed to creating a new one as needed?
Cursors are lightweight objects and creating lots of them should not pose any kind of problem. But note that cursors used to fetch result sets will cache the data and use memory in proportion to the result set size. Our suggestion is to almost always create a new cursor and dispose old ones as soon as the data is not required anymore (call [`close()`](https://www.psycopg.org/docs/cursor.html#cursor.close "cursor.close") on them.) The only exception are tight loops where one usually use the same cursor for a whole bunch of `INSERT`s or `UPDATE`s.

When should I save and re-use a connection as opposed to creating a new one as needed?
Creating a connection can be slow (think of SSL over TCP) so the best practice is to create a single connection and keep it open as long as required. It is also good practice to rollback or commit frequently (even after a single `SELECT` statement) to make sure the backend is never left “idle in transaction”. See also [`psycopg2.pool`](https://www.psycopg.org/docs/pool.html#module-psycopg2.pool "psycopg2.pool") for lightweight connection pooling.

What are the advantages or disadvantages of using named cursors?
The only disadvantages is that they use up resources on the server and that there is a little overhead because at least two queries (one to create the cursor and one to fetch the initial result set) are issued to the backend. The advantage is that data is fetched one chunk at a time: using small [`fetchmany()`](https://www.psycopg.org/docs/cursor.html#cursor.fetchmany "cursor.fetchmany") values it is possible to use very little memory on the client and to skip or discard parts of the result set.

How do I interrupt a long-running query in an interactive shell?
Normally the interactive shell becomes unresponsive to Ctrl-C when running a query. Using a connection in green mode allows Python to receive and handle the interrupt, although it may leave the connection broken, if the async callback doesn’t handle the `KeyboardInterrupt` correctly.

Starting from psycopg 2.6.2, the [`wait_select`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.wait_select "psycopg2.extras.wait_select") callback can handle a Ctrl-C correctly. For previous versions, you can use [this implementation](https://www.psycopg.org/articles/2014/07/20/cancelling-postgresql-statements-python/).

>>> psycopg2.extensions.set_wait_callback(psycopg2.extras.wait_select)
>>> cnn = psycopg2.connect('')
>>> cur = cnn.cursor()
>>> cur.execute("select pg_sleep(10)")
^C
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
 QueryCanceledError: canceling statement due to user request

>>> cnn.rollback()
>>>
>>> # You can use the connection and cursor again from here

Problems compiling and installing psycopg2[¶](https://www.psycopg.org/docs/faq.html#problems-compiling-and-installing-psycopg2 "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------

Psycopg 2.8 fails to install, Psycopg 2.7 was working fine.
With Psycopg 2.7 you were installing binary packages, but they have proven unreliable so now you have to install them explicitly using the `psycopg2-binary` package. See [Quick Install](https://www.psycopg.org/docs/install.html#binary-packages) for all the details.

I can’t compile `psycopg2`: the compiler says _error: Python.h: No such file or directory_. What am I missing?
You need to install a Python development package: it is usually called `python-dev` or `python3-dev` according to your Python version.

I can’t compile `psycopg2`: the compiler says _error: libpq-fe.h: No such file or directory_. What am I missing?
You need to install the development version of the libpq: the package is usually called `libpq-dev`.

`psycopg2` raises `ImportError` with message _\_psycopg.so: undefined symbol: lo\_truncate_ when imported.
This means that Psycopg was compiled with [`lo_truncate()`](https://www.postgresql.org/docs/current/static/lo-interfaces.html#LO-TRUNCATE) support (_i.e._ the libpq used at compile time was version >= 8.3) but at runtime an older libpq dynamic library is found.

Fast-forward several years, if the message reports _undefined symbol: lo\_truncate64_ it means that Psycopg was built with large objects 64 bits API support (_i.e._ the libpq used at compile time was at least 9.3) but at runtime an older libpq dynamic library is found.

You can use:

$ ldd /path/to/packages/psycopg2/_psycopg.so | grep libpq

to find what is the libpq dynamic library used at runtime.

You can avoid the problem by using the same version of the **pg_config** at install time and the libpq at runtime.

Psycopg raises _ImportError: cannot import name tz_ on import in mod_wsgi / ASP, but it works fine otherwise.
If `psycopg2` is installed in an [egg](http://peak.telecommunity.com/DevCenter/PythonEggs) (e.g. because installed by **easy_install**), the user running the program may be unable to write in the [eggs cache](https://stackoverflow.com/questions/2192323/what-is-the-python-egg-cache-python-egg-cache). Set the env variable `PYTHON_EGG_CACHE` to a writable directory. With modwsgi you can use the [WSGIPythonEggs](https://modwsgi.readthedocs.io/en/develop/configuration-directives/WSGIPythonEggs.html) directive.

### [Table of Contents](https://www.psycopg.org/docs/index.html)

* [Frequently Asked Questions](https://www.psycopg.org/docs/faq.html#)
  * [Meta](https://www.psycopg.org/docs/faq.html#meta)
  * [Problems with transactions handling](https://www.psycopg.org/docs/faq.html#problems-with-transactions-handling)
  * [Problems with type conversions](https://www.psycopg.org/docs/faq.html#problems-with-type-conversions)
  * [Best practices](https://www.psycopg.org/docs/faq.html#best-practices)
  * [Problems compiling and installing psycopg2](https://www.psycopg.org/docs/faq.html#problems-compiling-and-installing-psycopg2)

### Quick search

* ← [`psycopg2.errorcodes` – Error codes defined by PostgreSQL](https://www.psycopg.org/docs/errorcodes.html "Previous document")
* [Release notes](https://www.psycopg.org/docs/news.html "Next document") →

* [Home](https://www.psycopg.org/docs/index.html)

© 2001-2021, Federico Di Gregorio, Daniele Varrazzo, The Psycopg Team.
