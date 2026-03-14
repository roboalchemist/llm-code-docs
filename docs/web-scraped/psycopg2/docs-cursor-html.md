# Source: https://www.psycopg.org/docs/cursor.html

Title: The cursor class — Psycopg 2.9.11 documentation

URL Source: https://www.psycopg.org/docs/cursor.html

Markdown Content:
_class_ cursor[¶](https://www.psycopg.org/docs/cursor.html#cursor "Link to this definition")
Allows Python code to execute PostgreSQL command in a database session. Cursors are created by the [`connection.cursor()`](https://www.psycopg.org/docs/connection.html#connection.cursor "connection.cursor") method: they are bound to the connection for the entire lifetime and all the commands are executed in the context of the database session wrapped by the connection.

Cursors created from the same connection are not isolated, i.e., any changes done to the database by a cursor are immediately visible by the other cursors. Cursors created from different connections can or can not be isolated, depending on the connections’ [isolation level](https://www.psycopg.org/docs/usage.html#transactions-control). See also [`rollback()`](https://www.psycopg.org/docs/connection.html#connection.rollback "connection.rollback") and [`commit()`](https://www.psycopg.org/docs/connection.html#connection.commit "connection.commit") methods.

Cursors are _not_ thread safe: a multithread application can create many cursors from the same connection and should use each cursor from a single thread. See [Thread and process safety](https://www.psycopg.org/docs/usage.html#thread-safety) for details.

Cursors can be used as context managers: leaving the context will close the cursor.

with conn.cursor() as curs:
    curs.execute(SQL)

# the cursor is now closed

description[¶](https://www.psycopg.org/docs/cursor.html#cursor.description "Link to this definition")
Read-only attribute describing the result of a query. It is a sequence of [`Column`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Column "psycopg2.extensions.Column") instances, each one describing one result column in order. The attribute is `None` for operations that do not return rows or if the cursor has not had an operation invoked via the [`execute*()`](https://www.psycopg.org/docs/cursor.html#execute) methods yet.

For compatibility with the DB-API, every object can be unpacked as a 7-items sequence: the attributes retuned this way are the following. For further details and other attributes available check the [`Column`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Column "psycopg2.extensions.Column") documentation.

1. [`name`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Column.name "psycopg2.extensions.Column.name"): the name of the column returned.

2. [`type_code`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Column.type_code "psycopg2.extensions.Column.type_code"): the PostgreSQL OID of the column.

3. [`display_size`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Column.display_size "psycopg2.extensions.Column.display_size"): the actual length of the column in bytes.

4. [`internal_size`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Column.internal_size "psycopg2.extensions.Column.internal_size"): the size in bytes of the column associated to this column on the server.

5. [`precision`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Column.precision "psycopg2.extensions.Column.precision"): total number of significant digits in columns of type `NUMERIC`. `None` for other types.

6. [`scale`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Column.scale "psycopg2.extensions.Column.scale"): count of decimal digits in the fractional part in columns of type `NUMERIC`. `None` for other types.

7. [`null_ok`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Column.null_ok "psycopg2.extensions.Column.null_ok"): always `None` as not easy to retrieve from the libpq.

Changed in version 2.4: if possible, columns descriptions are named tuple instead of regular tuples.

Changed in version 2.8: columns descriptions are instances of `Column`, exposing extra attributes.

close()[¶](https://www.psycopg.org/docs/cursor.html#cursor.close "Link to this definition")
Close the cursor now (rather than whenever `del` is executed). The cursor will be unusable from this point forward; an [`InterfaceError`](https://www.psycopg.org/docs/module.html#psycopg2.InterfaceError "psycopg2.InterfaceError") will be raised if any operation is attempted with the cursor.

Changed in version 2.5: if the cursor is used in a `with` statement, the method is automatically called at the end of the `with` block.

closed[¶](https://www.psycopg.org/docs/cursor.html#cursor.closed "Link to this definition")
Read-only boolean attribute: specifies if the cursor is closed (`True`) or not (`False`).

DB API extension

The [`closed`](https://www.psycopg.org/docs/cursor.html#cursor.closed "cursor.closed") attribute is a Psycopg extension to the DB API 2.0.

Added in version 2.0.7.

connection[¶](https://www.psycopg.org/docs/cursor.html#cursor.connection "Link to this definition")
Read-only attribute returning a reference to the [`connection`](https://www.psycopg.org/docs/connection.html#connection "connection") object on which the cursor was created.

name[¶](https://www.psycopg.org/docs/cursor.html#cursor.name "Link to this definition")
Read-only attribute containing the name of the cursor if it was created as named cursor by [`connection.cursor()`](https://www.psycopg.org/docs/connection.html#connection.cursor "connection.cursor"), or `None` if it is a client side cursor. See [Server side cursors](https://www.psycopg.org/docs/usage.html#server-side-cursors).

DB API extension

The [`name`](https://www.psycopg.org/docs/cursor.html#cursor.name "cursor.name") attribute is a Psycopg extension to the DB API 2.0.

scrollable[¶](https://www.psycopg.org/docs/cursor.html#cursor.scrollable "Link to this definition")
Read/write attribute: specifies if a named cursor is declared `SCROLL`, hence is capable to scroll backwards (using [`scroll()`](https://www.psycopg.org/docs/cursor.html#cursor.scroll "cursor.scroll")). If `True`, the cursor can be scrolled backwards, if `False` it is never scrollable. If `None` (default) the cursor scroll option is not specified, usually but not always meaning no backward scroll (see the [`DECLARE` notes](https://www.postgresql.org/docs/current/static/sql-declare.html#SQL-DECLARE-NOTES)).

Note

set the value before calling [`execute()`](https://www.psycopg.org/docs/cursor.html#cursor.execute "cursor.execute") or use the [`connection.cursor()`](https://www.psycopg.org/docs/connection.html#connection.cursor "connection.cursor")_scrollable_ parameter, otherwise the value will have no effect.

Added in version 2.5.

DB API extension

The [`scrollable`](https://www.psycopg.org/docs/cursor.html#cursor.scrollable "cursor.scrollable") attribute is a Psycopg extension to the DB API 2.0.

withhold[¶](https://www.psycopg.org/docs/cursor.html#cursor.withhold "Link to this definition")
Read/write attribute: specifies if a named cursor lifetime should extend outside of the current transaction, i.e., it is possible to fetch from the cursor even after a [`connection.commit()`](https://www.psycopg.org/docs/connection.html#connection.commit "connection.commit") (but not after a [`connection.rollback()`](https://www.psycopg.org/docs/connection.html#connection.rollback "connection.rollback")). See [Server side cursors](https://www.psycopg.org/docs/usage.html#server-side-cursors)

Note

set the value before calling [`execute()`](https://www.psycopg.org/docs/cursor.html#cursor.execute "cursor.execute") or use the [`connection.cursor()`](https://www.psycopg.org/docs/connection.html#connection.cursor "connection.cursor")_withhold_ parameter, otherwise the value will have no effect.

Added in version 2.4.3.

DB API extension

The [`withhold`](https://www.psycopg.org/docs/cursor.html#cursor.withhold "cursor.withhold") attribute is a Psycopg extension to the DB API 2.0.

Commands execution methods

execute(_query_, _vars=None_)[¶](https://www.psycopg.org/docs/cursor.html#cursor.execute "Link to this definition")
Execute a database operation (query or command).

Parameters may be provided as sequence or mapping and will be bound to variables in the operation. Variables are specified either with positional (`%s`) or named (`%(name)s`) placeholders. See [Passing parameters to SQL queries](https://www.psycopg.org/docs/usage.html#query-parameters).

The method returns `None`. If a query was executed, the returned values can be retrieved using [`fetch*()`](https://www.psycopg.org/docs/cursor.html#fetch) methods.

executemany(_query_, _vars\_list_)[¶](https://www.psycopg.org/docs/cursor.html#cursor.executemany "Link to this definition")
Execute a database operation (query or command) against all parameter tuples or mappings found in the sequence _vars\_list_.

The function is mostly useful for commands that update the database: any result set returned by the query is discarded.

Parameters are bounded to the query using the same rules described in the [`execute()`](https://www.psycopg.org/docs/cursor.html#cursor.execute "cursor.execute") method.

>>> nums = ((1,), (5,), (10,))
>>> cur.executemany("INSERT INTO test (num) VALUES (%s)", nums)

>>> tuples = ((123, "foo"), (42, "bar"), (23, "baz"))
>>> cur.executemany("INSERT INTO test (num, data) VALUES (%s, %s)", tuples)

Warning

In its current implementation this method is not faster than executing [`execute()`](https://www.psycopg.org/docs/cursor.html#cursor.execute "cursor.execute") in a loop. For better performance you can use the functions described in [Fast execution helpers](https://www.psycopg.org/docs/extras.html#fast-exec).

callproc(_procname_[, _parameters_])[¶](https://www.psycopg.org/docs/cursor.html#cursor.callproc "Link to this definition")
Call a stored database procedure with the given name. The sequence of parameters must contain one entry for each argument that the procedure expects. Overloaded procedures are supported. Named parameters can be used by supplying the parameters as a dictionary.

This function is, at present, not DBAPI-compliant. The return value is supposed to consist of the sequence of parameters with modified output and input/output parameters. In future versions, the DBAPI-compliant return value may be implemented, but for now the function returns None.

The procedure may provide a result set as output. This is then made available through the standard [`fetch*()`](https://www.psycopg.org/docs/cursor.html#fetch) methods.

Changed in version 2.7: added support for named arguments.

Note

`callproc()` can only be used with PostgreSQL [functions](https://www.postgresql.org/docs/current/sql-createfunction.html), not with the [procedures](https://www.postgresql.org/docs/current/sql-createprocedure.html) introduced in PostgreSQL 11, which require the `CALL` statement to run. Please use a normal [`execute()`](https://www.psycopg.org/docs/cursor.html#cursor.execute "cursor.execute") to run them.

mogrify(_operation_[, _parameters_])[¶](https://www.psycopg.org/docs/cursor.html#cursor.mogrify "Link to this definition")
Return a query string after arguments binding. The string returned is exactly the one that would be sent to the database running the [`execute()`](https://www.psycopg.org/docs/cursor.html#cursor.execute "cursor.execute") method or similar.

The returned string is always a bytes string.

>>> cur.mogrify("INSERT INTO test (num, data) VALUES (%s, %s)", (42, 'bar'))
"INSERT INTO test (num, data) VALUES (42, E'bar')"

DB API extension

The [`mogrify()`](https://www.psycopg.org/docs/cursor.html#cursor.mogrify "cursor.mogrify") method is a Psycopg extension to the DB API 2.0.

setinputsizes(_sizes_)[¶](https://www.psycopg.org/docs/cursor.html#cursor.setinputsizes "Link to this definition")
This method is exposed in compliance with the DB API 2.0. It currently does nothing but it is safe to call it.

Results retrieval methods

The following methods are used to read data from the database after an [`execute()`](https://www.psycopg.org/docs/cursor.html#cursor.execute "cursor.execute") call.

Note

[`cursor`](https://www.psycopg.org/docs/cursor.html#cursor "cursor") objects are iterable, so, instead of calling explicitly [`fetchone()`](https://www.psycopg.org/docs/cursor.html#cursor.fetchone "cursor.fetchone") in a loop, the object itself can be used:

>>> cur.execute("SELECT * FROM test;")
>>> for record in cur:
...     print(record)
...
(1, 100, "abc'def")
(2, None, 'dada')
(3, 42, 'bar')

Changed in version 2.4: iterating over a [named cursor](https://www.psycopg.org/docs/usage.html#server-side-cursors) fetches [`itersize`](https://www.psycopg.org/docs/cursor.html#cursor.itersize "cursor.itersize") records at time from the backend. Previously only one record was fetched per roundtrip, resulting in a large overhead.

fetchone()[¶](https://www.psycopg.org/docs/cursor.html#cursor.fetchone "Link to this definition")
Fetch the next row of a query result set, returning a single tuple, or `None` when no more data is available:

>>> cur.execute("SELECT * FROM test WHERE id = %s", (3,))
>>> cur.fetchone()
(3, 42, 'bar')

A [`ProgrammingError`](https://www.psycopg.org/docs/module.html#psycopg2.ProgrammingError "psycopg2.ProgrammingError") is raised if the previous call to [`execute*()`](https://www.psycopg.org/docs/cursor.html#execute) did not produce any result set or no call was issued yet.

fetchmany([_size=cursor.arraysize_])[¶](https://www.psycopg.org/docs/cursor.html#cursor.fetchmany "Link to this definition")
Fetch the next set of rows of a query result, returning a list of tuples. An empty list is returned when no more rows are available.

The number of rows to fetch per call is specified by the parameter. If it is not given, the cursor’s [`arraysize`](https://www.psycopg.org/docs/cursor.html#cursor.arraysize "cursor.arraysize") determines the number of rows to be fetched. The method should try to fetch as many rows as indicated by the size parameter. If this is not possible due to the specified number of rows not being available, fewer rows may be returned:

>>> cur.execute("SELECT * FROM test;")
>>> cur.fetchmany(2)
[(1, 100, "abc'def"), (2, None, 'dada')]
>>> cur.fetchmany(2)
[(3, 42, 'bar')]
>>> cur.fetchmany(2)
[]

A [`ProgrammingError`](https://www.psycopg.org/docs/module.html#psycopg2.ProgrammingError "psycopg2.ProgrammingError") is raised if the previous call to [`execute*()`](https://www.psycopg.org/docs/cursor.html#execute) did not produce any result set or no call was issued yet.

Note there are performance considerations involved with the size parameter. For optimal performance, it is usually best to use the [`arraysize`](https://www.psycopg.org/docs/cursor.html#cursor.arraysize "cursor.arraysize") attribute. If the size parameter is used, then it is best for it to retain the same value from one [`fetchmany()`](https://www.psycopg.org/docs/cursor.html#cursor.fetchmany "cursor.fetchmany") call to the next.

fetchall()[¶](https://www.psycopg.org/docs/cursor.html#cursor.fetchall "Link to this definition")
Fetch all (remaining) rows of a query result, returning them as a list of tuples. An empty list is returned if there is no more record to fetch.

>>> cur.execute("SELECT * FROM test;")
>>> cur.fetchall()
[(1, 100, "abc'def"), (2, None, 'dada'), (3, 42, 'bar')]

A [`ProgrammingError`](https://www.psycopg.org/docs/module.html#psycopg2.ProgrammingError "psycopg2.ProgrammingError") is raised if the previous call to [`execute*()`](https://www.psycopg.org/docs/cursor.html#execute) did not produce any result set or no call was issued yet.

scroll(_value_[, _mode='relative'_])[¶](https://www.psycopg.org/docs/cursor.html#cursor.scroll "Link to this definition")
Scroll the cursor in the result set to a new position according to mode.

If `mode` is `relative` (default), value is taken as offset to the current position in the result set, if set to `absolute`, value states an absolute target position.

If the scroll operation would leave the result set, a [`ProgrammingError`](https://www.psycopg.org/docs/module.html#psycopg2.ProgrammingError "psycopg2.ProgrammingError") is raised and the cursor position is not changed.

Note

According to the [DB API 2.0](https://www.python.org/dev/peps/pep-0249/), the exception raised for a cursor out of bound should have been `IndexError`. The best option is probably to catch both exceptions in your code:

try:
    cur.scroll(1000 * 1000)
except (ProgrammingError, IndexError), exc:
    deal_with_it(exc)

The method can be used both for client-side cursors and [server-side cursors](https://www.psycopg.org/docs/usage.html#server-side-cursors). Server-side cursors can usually scroll backwards only if declared [`scrollable`](https://www.psycopg.org/docs/cursor.html#cursor.scrollable "cursor.scrollable"). Moving out-of-bound in a server-side cursor doesn’t result in an exception, if the backend doesn’t raise any (Postgres doesn’t tell us in a reliable way if we went out of bound).

arraysize[¶](https://www.psycopg.org/docs/cursor.html#cursor.arraysize "Link to this definition")
This read/write attribute specifies the number of rows to fetch at a time with [`fetchmany()`](https://www.psycopg.org/docs/cursor.html#cursor.fetchmany "cursor.fetchmany"). It defaults to 1 meaning to fetch a single row at a time.

itersize[¶](https://www.psycopg.org/docs/cursor.html#cursor.itersize "Link to this definition")
Read/write attribute specifying the number of rows to fetch from the backend at each network roundtrip during [iteration](https://www.psycopg.org/docs/cursor.html#cursor-iterable) on a [named cursor](https://www.psycopg.org/docs/usage.html#server-side-cursors). The default is 2000.

Added in version 2.4.

DB API extension

The [`itersize`](https://www.psycopg.org/docs/cursor.html#cursor.itersize "cursor.itersize") attribute is a Psycopg extension to the DB API 2.0.

rowcount[¶](https://www.psycopg.org/docs/cursor.html#cursor.rowcount "Link to this definition")
This read-only attribute specifies the number of rows that the last [`execute*()`](https://www.psycopg.org/docs/cursor.html#execute) produced (for DQL statements like `SELECT`) or affected (for DML statements like `UPDATE` or `INSERT`).

The attribute is -1 in case no `execute*()` has been performed on the cursor or the row count of the last operation if it can’t be determined by the interface.

Note

The [DB API 2.0](https://www.python.org/dev/peps/pep-0249/) interface reserves to redefine the latter case to have the object return `None` instead of -1 in future versions of the specification.

rownumber[¶](https://www.psycopg.org/docs/cursor.html#cursor.rownumber "Link to this definition")
This read-only attribute provides the current 0-based index of the cursor in the result set or `None` if the index cannot be determined.

The index can be seen as index of the cursor in a sequence (the result set). The next fetch operation will fetch the row indexed by [`rownumber`](https://www.psycopg.org/docs/cursor.html#cursor.rownumber "cursor.rownumber") in that sequence.

lastrowid[¶](https://www.psycopg.org/docs/cursor.html#cursor.lastrowid "Link to this definition")
This read-only attribute provides the OID of the last row inserted by the cursor. If the table wasn’t created with OID support or the last operation is not a single record insert, the attribute is set to `None`.

Note

PostgreSQL currently advices to not create OIDs on the tables and the default for [`CREATE TABLE`](https://www.postgresql.org/docs/current/static/sql-createtable.html) is to not support them. The [`INSERT ... RETURNING`](https://www.postgresql.org/docs/current/static/sql-insert.html) syntax available from PostgreSQL 8.3 allows more flexibility.

query[¶](https://www.psycopg.org/docs/cursor.html#cursor.query "Link to this definition")
Read-only attribute containing the body of the last query sent to the backend (including bound arguments) as bytes string. `None` if no query has been executed yet:

>>> cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (42, 'bar'))
>>> cur.query
"INSERT INTO test (num, data) VALUES (42, E'bar')"

DB API extension

The [`query`](https://www.psycopg.org/docs/cursor.html#cursor.query "cursor.query") attribute is a Psycopg extension to the DB API 2.0.

statusmessage[¶](https://www.psycopg.org/docs/cursor.html#cursor.statusmessage "Link to this definition")
Read-only attribute containing the message returned by the last command:

>>> cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (42, 'bar'))
>>> cur.statusmessage
'INSERT 0 1'

DB API extension

The [`statusmessage`](https://www.psycopg.org/docs/cursor.html#cursor.statusmessage "cursor.statusmessage") attribute is a Psycopg extension to the DB API 2.0.

cast(_oid_, _s_)[¶](https://www.psycopg.org/docs/cursor.html#cursor.cast "Link to this definition")
Convert a value from the PostgreSQL string representation to a Python object.

Use the most specific of the typecasters registered by [`register_type()`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.register_type "psycopg2.extensions.register_type").

Added in version 2.4.

DB API extension

The [`cast()`](https://www.psycopg.org/docs/cursor.html#cursor.cast "cursor.cast") method is a Psycopg extension to the DB API 2.0.

tzinfo_factory[¶](https://www.psycopg.org/docs/cursor.html#cursor.tzinfo_factory "Link to this definition")
The time zone factory used to handle data types such as `TIMESTAMP WITH TIME ZONE`. It should be a [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "(in Python v3.14)") object. Default is [`datetime.timezone`](https://docs.python.org/3/library/datetime.html#datetime.timezone "(in Python v3.14)").

nextset()[¶](https://www.psycopg.org/docs/cursor.html#cursor.nextset "Link to this definition")
This method is not supported (PostgreSQL does not have multiple data sets) and will raise a [`NotSupportedError`](https://www.psycopg.org/docs/module.html#psycopg2.NotSupportedError "psycopg2.NotSupportedError") exception.

setoutputsize(_size_[, _column_])[¶](https://www.psycopg.org/docs/cursor.html#cursor.setoutputsize "Link to this definition")
This method is exposed in compliance with the DB API 2.0. It currently does nothing but it is safe to call it.

COPY-related methods

Efficiently copy data from file-like objects to the database and back. See [Using COPY TO and COPY FROM](https://www.psycopg.org/docs/usage.html#copy) for an overview.

DB API extension

The `COPY` command is a PostgreSQL extension to the SQL standard. As such, its support is a Psycopg extension to the DB API 2.0.

copy_from(_file_, _table_, _sep='\\t'_, _null='\\\\N'_, _size=8192_, _columns=None_)[¶](https://www.psycopg.org/docs/cursor.html#cursor.copy_from "Link to this definition")
Read data _from_ the file-like object _file_ appending them to the table named _table_.

Parameters:

* **file** – file-like object to read data from. It must have both `read()` and `readline()` methods.

* **table** – name of the table to copy data into.

* **sep** – columns separator expected in the file. Defaults to a tab.

* **null** – textual representation of `NULL` in the file. The default is the two characters string `\N`.

* **size** – size of the buffer used to read from the file.

* **columns** – iterable with name of the columns to import. The length and types should match the content of the file to read. If not specified, it is assumed that the entire table matches the file structure.

Example:

>>> f = StringIO("42\tfoo\n74\tbar\n")
>>> cur.copy_from(f, 'test', columns=('num', 'data'))
>>> cur.execute("select * from test where id > 5;")
>>> cur.fetchall()
[(6, 42, 'foo'), (7, 74, 'bar')]

Changed in version 2.0.6: added the _columns_ parameter.

Changed in version 2.4: data read from files implementing the [`io.TextIOBase`](https://docs.python.org/3/library/io.html#io.TextIOBase "(in Python v3.14)") interface are encoded in the connection [`encoding`](https://www.psycopg.org/docs/connection.html#connection.encoding "connection.encoding") when sent to the backend.

Changed in version 2.9: the table and fields names are now quoted. If you need to specify a schema-qualified table please use [`copy_expert()`](https://www.psycopg.org/docs/cursor.html#cursor.copy_expert "cursor.copy_expert").

copy_to(_file_, _table_, _sep='\\t'_, _null='\\\\N'_, _columns=None_)[¶](https://www.psycopg.org/docs/cursor.html#cursor.copy_to "Link to this definition")
Write the content of the table named _table_ _to_ the file-like object _file_. See [Using COPY TO and COPY FROM](https://www.psycopg.org/docs/usage.html#copy) for an overview.

Parameters:

* **file** – file-like object to write data into. It must have a `write()` method.

* **table** – name of the table to copy data from.

* **sep** – columns separator expected in the file. Defaults to a tab.

* **null** – textual representation of `NULL` in the file. The default is the two characters string `\N`.

* **columns** – iterable with name of the columns to export. If not specified, export all the columns.

Example:

>>> cur.copy_to(sys.stdout, 'test', sep="|")
1|100|abc'def
2|\N|dada
...

Changed in version 2.0.6: added the _columns_ parameter.

Changed in version 2.4: data sent to files implementing the [`io.TextIOBase`](https://docs.python.org/3/library/io.html#io.TextIOBase "(in Python v3.14)") interface are decoded in the connection [`encoding`](https://www.psycopg.org/docs/connection.html#connection.encoding "connection.encoding") when read from the backend.

Changed in version 2.9: the table and fields names are now quoted. If you need to specify a schema-qualified table please use [`copy_expert()`](https://www.psycopg.org/docs/cursor.html#cursor.copy_expert "cursor.copy_expert").

copy_expert(_sql_, _file_, _size=8192_)[¶](https://www.psycopg.org/docs/cursor.html#cursor.copy_expert "Link to this definition")
Submit a user-composed `COPY` statement. The method is useful to handle all the parameters that PostgreSQL makes available (see [`COPY`](https://www.postgresql.org/docs/current/static/sql-copy.html) command documentation).

Parameters:

* **sql** – the `COPY` statement to execute.

* **file** – a file-like object to read or write (according to _sql_).

* **size** – size of the read buffer to be used in `COPY FROM`.

The _sql_ statement should be in the form

```
COPY table TO
STDOUT
```

 to export `table` to the _file_ object passed as argument or `COPY table FROM STDIN` to import the content of the _file_ object into `table`. If you need to compose a `COPY` statement dynamically (because table, fields, or query parameters are in Python variables) you may use the objects provided by the [`psycopg2.sql`](https://www.psycopg.org/docs/sql.html#module-psycopg2.sql "psycopg2.sql") module.

_file_ must be a readable file-like object (as required by [`copy_from()`](https://www.psycopg.org/docs/cursor.html#cursor.copy_from "cursor.copy_from")) for _sql_ statement `COPY ... FROM STDIN` or a writable one (as required by [`copy_to()`](https://www.psycopg.org/docs/cursor.html#cursor.copy_to "cursor.copy_to")) for

```
COPY
... TO STDOUT
```

.

Example:

>>> cur.copy_expert("COPY test TO STDOUT WITH CSV HEADER", sys.stdout)
id,num,data
1,100,abc'def
2,,dada
...

Added in version 2.0.6.

Changed in version 2.4: files implementing the [`io.TextIOBase`](https://docs.python.org/3/library/io.html#io.TextIOBase "(in Python v3.14)") interface are dealt with using Unicode data instead of bytes.

Interoperation with other C API modules

pgresult_ptr[¶](https://www.psycopg.org/docs/cursor.html#cursor.pgresult_ptr "Link to this definition")
Return the cursor’s internal `PGresult*` as integer. Useful to pass the libpq raw result structure to C functions, e.g. via [`ctypes`](https://docs.python.org/3/library/ctypes.html#module-ctypes "(in Python v3.14)"):

>>> import ctypes
>>> libpq = ctypes.pydll.LoadLibrary(ctypes.util.find_library('pq'))
>>> libpq.PQcmdStatus.argtypes = [ctypes.c_void_p]
>>> libpq.PQcmdStatus.restype = ctypes.c_char_p

>>> curs.execute("select 'x'")
>>> libpq.PQcmdStatus(curs.pgresult_ptr)
b'SELECT 1'

Added in version 2.8.
