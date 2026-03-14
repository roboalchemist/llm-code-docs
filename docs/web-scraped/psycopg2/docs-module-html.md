# Source: https://www.psycopg.org/docs/module.html

Title: The psycopg2 module content — Psycopg 2.9.11 documentation

URL Source: https://www.psycopg.org/docs/module.html

Markdown Content:
The module interface respects the standard defined in the [DB API 2.0](https://www.python.org/dev/peps/pep-0249/).

psycopg2.connect(_dsn=None_, _connection\_factory=None_, _cursor\_factory=None_, _async=False_, _\*\*kwargs_)[¶](https://www.psycopg.org/docs/module.html#psycopg2.connect "Link to this definition")
Create a new database session and return a new [`connection`](https://www.psycopg.org/docs/connection.html#connection "connection") object.

The connection parameters can be specified as a [libpq connection string](https://www.postgresql.org/docs/current/static/libpq-connect.html#LIBPQ-CONNSTRING) using the _dsn_ parameter:

conn = psycopg2.connect("dbname=test user=postgres password=secret")

or using a set of keyword arguments:

conn = psycopg2.connect(dbname="test", user="postgres", password="secret")

or using a mix of both: if the same parameter name is specified in both sources, the _kwargs_ value will have precedence over the _dsn_ value. Note that either the _dsn_ or at least one connection-related keyword argument is required.

The basic connection parameters are:

* `dbname` – the database name (`database` is a deprecated alias)

* `user` – user name used to authenticate

* `password` – password used to authenticate

* `host` – database host address (defaults to UNIX socket if not provided)

* `port` – connection port number (defaults to 5432 if not provided)

Any other connection parameter supported by the client library/server can be passed either in the connection string or as a keyword. The PostgreSQL documentation contains the complete list of the [supported parameters](https://www.postgresql.org/docs/current/static/libpq-connect.html#LIBPQ-PARAMKEYWORDS). Also note that the same parameters can be passed to the client library using [environment variables](https://www.postgresql.org/docs/current/static/libpq-envars.html).

Using the _connection\_factory_ parameter a different class or connections factory can be specified. It should be a callable object taking a _dsn_ string argument. See [Connection and cursor factories](https://www.psycopg.org/docs/advanced.html#subclassing-connection) for details. If a _cursor\_factory_ is specified, the connection’s [`cursor_factory`](https://www.psycopg.org/docs/connection.html#connection.cursor_factory "connection.cursor_factory") is set to it. If you only need customized cursors you can use this parameter instead of subclassing a connection.

Using _async_=`True` an asynchronous connection will be created: see [Asynchronous support](https://www.psycopg.org/docs/advanced.html#async-support) to know about advantages and limitations. _async\__ is a valid alias for the Python version where `async` is a keyword.

Changed in version 2.4.3: any keyword argument is passed to the connection. Previously only the basic parameters (plus `sslmode`) were supported as keywords.

Changed in version 2.5: added the _cursor\_factory_ parameter.

Changed in version 2.7: both _dsn_ and keyword arguments can be specified.

Changed in version 2.7: added _async\__ alias.

See also

* [`parse_dsn`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.parse_dsn "psycopg2.extensions.parse_dsn")

* libpq [connection string syntax](https://www.postgresql.org/docs/current/static/libpq-connect.html#LIBPQ-CONNSTRING)

* libpq supported [connection parameters](https://www.postgresql.org/docs/current/static/libpq-connect.html#LIBPQ-PARAMKEYWORDS)

* libpq supported [environment variables](https://www.postgresql.org/docs/current/static/libpq-envars.html)

DB API extension

The non-connection-related keyword parameters are Psycopg extensions to the [DB API 2.0](https://www.python.org/dev/peps/pep-0249/).

psycopg2.apilevel[¶](https://www.psycopg.org/docs/module.html#psycopg2.apilevel "Link to this definition")
String constant stating the supported DB API level. For [`psycopg2`](https://www.psycopg.org/docs/module.html#module-psycopg2 "psycopg2") is `2.0`.

psycopg2.threadsafety[¶](https://www.psycopg.org/docs/module.html#psycopg2.threadsafety "Link to this definition")
Integer constant stating the level of thread safety the interface supports. For [`psycopg2`](https://www.psycopg.org/docs/module.html#module-psycopg2 "psycopg2") is `2`, i.e. threads can share the module and the connection. See [Thread and process safety](https://www.psycopg.org/docs/usage.html#thread-safety) for details.

psycopg2.paramstyle[¶](https://www.psycopg.org/docs/module.html#psycopg2.paramstyle "Link to this definition")
String constant stating the type of parameter marker formatting expected by the interface. For [`psycopg2`](https://www.psycopg.org/docs/module.html#module-psycopg2 "psycopg2") is `pyformat`. See also [Passing parameters to SQL queries](https://www.psycopg.org/docs/usage.html#query-parameters).

psycopg2. __libpq_version__ [¶](https://www.psycopg.org/docs/module.html#psycopg2.__libpq_version__ "Link to this definition")
Integer constant reporting the version of the `libpq` library this `psycopg2` module was compiled with (in the same format of [`server_version`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ConnectionInfo.server_version "psycopg2.extensions.ConnectionInfo.server_version")). If this value is greater or equal than `90100` then you may query the version of the actually loaded library using the [`libpq_version()`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.libpq_version "psycopg2.extensions.libpq_version") function.

Exceptions[¶](https://www.psycopg.org/docs/module.html#exceptions "Link to this heading")
-----------------------------------------------------------------------------------------

In compliance with the [DB API 2.0](https://www.python.org/dev/peps/pep-0249/), the module makes informations about errors available through the following exceptions:

_exception_ psycopg2.Warning[¶](https://www.psycopg.org/docs/module.html#psycopg2.Warning "Link to this definition")
Exception raised for important warnings like data truncations while inserting, etc. It is a subclass of the Python `StandardError` ([`Exception`](https://docs.python.org/3/library/exceptions.html#Exception "(in Python v3.14)") on Python 3).

_exception_ psycopg2.Error[¶](https://www.psycopg.org/docs/module.html#psycopg2.Error "Link to this definition")
Exception that is the base class of all other error exceptions. You can use this to catch all errors with one single `except` statement. Warnings are not considered errors and thus not use this class as base. It is a subclass of the Python `StandardError` ([`Exception`](https://docs.python.org/3/library/exceptions.html#Exception "(in Python v3.14)") on Python 3).

pgerror[¶](https://www.psycopg.org/docs/module.html#psycopg2.Error.pgerror "Link to this definition")
String representing the error message returned by the backend, `None` if not available.

pgcode[¶](https://www.psycopg.org/docs/module.html#psycopg2.Error.pgcode "Link to this definition")
String representing the error code returned by the backend, `None` if not available. The [`errorcodes`](https://www.psycopg.org/docs/errorcodes.html#module-psycopg2.errorcodes "psycopg2.errorcodes") module contains symbolic constants representing PostgreSQL error codes.

>>> try:
...     cur.execute("SELECT * FROM barf")
... except psycopg2.Error as e:
...     pass

>>> e.pgcode
'42P01'
>>> print(e.pgerror)
ERROR: relation "barf" does not exist
LINE 1: SELECT * FROM barf
 ^

cursor[¶](https://www.psycopg.org/docs/module.html#psycopg2.Error.cursor "Link to this definition")
The cursor the exception was raised from; [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") if not applicable.

diag[¶](https://www.psycopg.org/docs/module.html#psycopg2.Error.diag "Link to this definition")
A [`Diagnostics`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Diagnostics "psycopg2.extensions.Diagnostics") object containing further information about the error.

>>> try:
...     cur.execute("SELECT * FROM barf")
... except psycopg2.Error as e:
...     pass

>>> e.diag.severity
'ERROR'
>>> e.diag.message_primary
'relation "barf" does not exist'

Added in version 2.5.

DB API extension

The [`pgerror`](https://www.psycopg.org/docs/module.html#psycopg2.Error.pgerror "psycopg2.Error.pgerror"), [`pgcode`](https://www.psycopg.org/docs/module.html#psycopg2.Error.pgcode "psycopg2.Error.pgcode"), [`cursor`](https://www.psycopg.org/docs/module.html#psycopg2.Error.cursor "psycopg2.Error.cursor"), and [`diag`](https://www.psycopg.org/docs/module.html#psycopg2.Error.diag "psycopg2.Error.diag") attributes are Psycopg extensions.

_exception_ psycopg2.InterfaceError[¶](https://www.psycopg.org/docs/module.html#psycopg2.InterfaceError "Link to this definition")
Exception raised for errors that are related to the database interface rather than the database itself. It is a subclass of [`Error`](https://www.psycopg.org/docs/module.html#psycopg2.Error "psycopg2.Error").

_exception_ psycopg2.DatabaseError[¶](https://www.psycopg.org/docs/module.html#psycopg2.DatabaseError "Link to this definition")
Exception raised for errors that are related to the database. It is a subclass of [`Error`](https://www.psycopg.org/docs/module.html#psycopg2.Error "psycopg2.Error").

_exception_ psycopg2.DataError[¶](https://www.psycopg.org/docs/module.html#psycopg2.DataError "Link to this definition")
Exception raised for errors that are due to problems with the processed data like division by zero, numeric value out of range, etc. It is a subclass of [`DatabaseError`](https://www.psycopg.org/docs/module.html#psycopg2.DatabaseError "psycopg2.DatabaseError").

_exception_ psycopg2.OperationalError[¶](https://www.psycopg.org/docs/module.html#psycopg2.OperationalError "Link to this definition")
Exception raised for errors that are related to the database’s operation and not necessarily under the control of the programmer, e.g. an unexpected disconnect occurs, the data source name is not found, a transaction could not be processed, a memory allocation error occurred during processing, etc. It is a subclass of [`DatabaseError`](https://www.psycopg.org/docs/module.html#psycopg2.DatabaseError "psycopg2.DatabaseError").

_exception_ psycopg2.IntegrityError[¶](https://www.psycopg.org/docs/module.html#psycopg2.IntegrityError "Link to this definition")
Exception raised when the relational integrity of the database is affected, e.g. a foreign key check fails. It is a subclass of [`DatabaseError`](https://www.psycopg.org/docs/module.html#psycopg2.DatabaseError "psycopg2.DatabaseError").

_exception_ psycopg2.InternalError[¶](https://www.psycopg.org/docs/module.html#psycopg2.InternalError "Link to this definition")
Exception raised when the database encounters an internal error, e.g. the cursor is not valid anymore, the transaction is out of sync, etc. It is a subclass of [`DatabaseError`](https://www.psycopg.org/docs/module.html#psycopg2.DatabaseError "psycopg2.DatabaseError").

_exception_ psycopg2.ProgrammingError[¶](https://www.psycopg.org/docs/module.html#psycopg2.ProgrammingError "Link to this definition")
Exception raised for programming errors, e.g. table not found or already exists, syntax error in the SQL statement, wrong number of parameters specified, etc. It is a subclass of [`DatabaseError`](https://www.psycopg.org/docs/module.html#psycopg2.DatabaseError "psycopg2.DatabaseError").

_exception_ psycopg2.NotSupportedError[¶](https://www.psycopg.org/docs/module.html#psycopg2.NotSupportedError "Link to this definition")
Exception raised in case a method or database API was used which is not supported by the database, e.g. requesting a `rollback()` on a connection that does not support transaction or has transactions turned off. It is a subclass of [`DatabaseError`](https://www.psycopg.org/docs/module.html#psycopg2.DatabaseError "psycopg2.DatabaseError").

DB API extension

Psycopg actually raises a different exception for each `SQLSTATE` error returned by the database: the classes are available in the [`psycopg2.errors`](https://www.psycopg.org/docs/errors.html#module-psycopg2.errors "psycopg2.errors") module. Every exception class is a subclass of one of the exception classes defined here though, so they don’t need to be trapped specifically: trapping `Error` or `DatabaseError` is usually what needed to write a generic error handler; trapping a specific error such as `NotNullViolation` can be useful to write specific exception handlers.

This is the exception inheritance layout:

`StandardError`
|__[`Warning`](https://www.psycopg.org/docs/module.html#psycopg2.Warning "psycopg2.Warning")
|__ [`Error`](https://www.psycopg.org/docs/module.html#psycopg2.Error "psycopg2.Error")
    |__[`InterfaceError`](https://www.psycopg.org/docs/module.html#psycopg2.InterfaceError "psycopg2.InterfaceError")
    |__ [`DatabaseError`](https://www.psycopg.org/docs/module.html#psycopg2.DatabaseError "psycopg2.DatabaseError")
        |__[`DataError`](https://www.psycopg.org/docs/module.html#psycopg2.DataError "psycopg2.DataError")
        |__ [`OperationalError`](https://www.psycopg.org/docs/module.html#psycopg2.OperationalError "psycopg2.OperationalError")
        |__[`IntegrityError`](https://www.psycopg.org/docs/module.html#psycopg2.IntegrityError "psycopg2.IntegrityError")
        |__ [`InternalError`](https://www.psycopg.org/docs/module.html#psycopg2.InternalError "psycopg2.InternalError")
        |__[`ProgrammingError`](https://www.psycopg.org/docs/module.html#psycopg2.ProgrammingError "psycopg2.ProgrammingError")
        |__ [`NotSupportedError`](https://www.psycopg.org/docs/module.html#psycopg2.NotSupportedError "psycopg2.NotSupportedError")
Type Objects and Constructors[¶](https://www.psycopg.org/docs/module.html#type-objects-and-constructors "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------

Many databases need to have the input in a particular format for binding to an operation’s input parameters. For example, if an input is destined for a DATE column, then it must be bound to the database in a particular string format. Similar problems exist for “Row ID” columns or large binary items (e.g. blobs or RAW columns). This presents problems for Python since the parameters to the .execute*() method are untyped. When the database module sees a Python string object, it doesn’t know if it should be bound as a simple CHAR column, as a raw BINARY item, or as a DATE.

To overcome this problem, a module must provide the constructors defined below to create objects that can hold special values. When passed to the cursor methods, the module can then detect the proper type of the input parameter and bind it accordingly.

A Cursor Object’s description attribute returns information about each of the result columns of a query. The type_code must compare equal to one of Type Objects defined below. Type Objects may be equal to more than one type code (e.g. DATETIME could be equal to the type codes for date, time and timestamp columns; see the Implementation Hints below for details).

The module exports the following constructors and singletons:

psycopg2.Date(_year_, _month_, _day_)[¶](https://www.psycopg.org/docs/module.html#psycopg2.Date "Link to this definition")
This function constructs an object holding a date value.

psycopg2.Time(_hour_, _minute_, _second_)[¶](https://www.psycopg.org/docs/module.html#psycopg2.Time "Link to this definition")
This function constructs an object holding a time value.

psycopg2.Timestamp(_year_, _month_, _day_, _hour_, _minute_, _second_)[¶](https://www.psycopg.org/docs/module.html#psycopg2.Timestamp "Link to this definition")
This function constructs an object holding a time stamp value.

psycopg2.DateFromTicks(_ticks_)[¶](https://www.psycopg.org/docs/module.html#psycopg2.DateFromTicks "Link to this definition")
This function constructs an object holding a date value from the given ticks value (number of seconds since the epoch; see the documentation of the standard Python time module for details).

psycopg2.TimeFromTicks(_ticks_)[¶](https://www.psycopg.org/docs/module.html#psycopg2.TimeFromTicks "Link to this definition")
This function constructs an object holding a time value from the given ticks value (number of seconds since the epoch; see the documentation of the standard Python time module for details).

psycopg2.TimestampFromTicks(_ticks_)[¶](https://www.psycopg.org/docs/module.html#psycopg2.TimestampFromTicks "Link to this definition")
This function constructs an object holding a time stamp value from the given ticks value (number of seconds since the epoch; see the documentation of the standard Python time module for details).

psycopg2.Binary(_string_)[¶](https://www.psycopg.org/docs/module.html#psycopg2.Binary "Link to this definition")
This function constructs an object capable of holding a binary (long) string value.

Note

All the adapters returned by the module level factories (`Binary`, `Date`, `Time`, `Timestamp` and the `*FromTicks` variants) expose the wrapped object (a regular Python object such as `datetime`) in an `adapted` attribute.

psycopg2.STRING[¶](https://www.psycopg.org/docs/module.html#psycopg2.STRING "Link to this definition")
This type object is used to describe columns in a database that are string-based (e.g. CHAR).

psycopg2.BINARY[¶](https://www.psycopg.org/docs/module.html#psycopg2.BINARY "Link to this definition")
This type object is used to describe (long) binary columns in a database (e.g. LONG, RAW, BLOBs).

psycopg2.NUMBER[¶](https://www.psycopg.org/docs/module.html#psycopg2.NUMBER "Link to this definition")
This type object is used to describe numeric columns in a database.

psycopg2.DATETIME[¶](https://www.psycopg.org/docs/module.html#psycopg2.DATETIME "Link to this definition")
This type object is used to describe date/time columns in a database.

psycopg2.ROWID[¶](https://www.psycopg.org/docs/module.html#psycopg2.ROWID "Link to this definition")
This type object is used to describe the “Row ID” column in a database.
