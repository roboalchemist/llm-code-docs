# Source: https://www.psycopg.org/docs/sql.html

Title: psycopg2.sql – SQL string composition — Psycopg 2.9.11 documentation

URL Source: https://www.psycopg.org/docs/sql.html

Markdown Content:
Added in version 2.7.

The module contains objects and functions useful to generate SQL dynamically, in a convenient and safe way. SQL identifiers (e.g. names of tables and fields) cannot be passed to the [`execute()`](https://www.psycopg.org/docs/cursor.html#cursor.execute "cursor.execute") method like query arguments:

# This will not work

table_name = 'my_table'
cur.execute("insert into %s values (%s, %s)", [table_name, 10, 20])

The SQL query should be composed before the arguments are merged, for instance:

# This works, but it is not optimal

table_name = 'my_table'
cur.execute(
    "insert into %s values (%%s, %%s)" % table_name,
    [10, 20])

This sort of works, but it is an accident waiting to happen: the table name may be an invalid SQL literal and need quoting; even more serious is the security problem in case the table name comes from an untrusted source. The name should be escaped using [`quote_ident()`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.quote_ident "psycopg2.extensions.quote_ident"):

# This works, but it is not optimal

table_name = 'my_table'
cur.execute(
    "insert into %s values (%%s, %%s)" % ext.quote_ident(table_name, cur),
    [10, 20])

This is now safe, but it somewhat ad-hoc. In case, for some reason, it is necessary to include a value in the query string (as opposite as in a value) the merging rule is still different ([`adapt()`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.adapt "psycopg2.extensions.adapt") should be used…). It is also still relatively dangerous: if `quote_ident()` is forgotten somewhere, the program will usually work, but will eventually crash in the presence of a table or field name with containing characters to escape, or will present a potentially exploitable weakness.

The objects exposed by the `psycopg2.sql` module allow generating SQL statements on the fly, separating clearly the variable parts of the statement from the query parameters:

from psycopg2 import sql

cur.execute(
    sql.SQL("insert into {} values (%s, %s)")
        .format(sql.Identifier('my_table')),
    [10, 20])

Module usage[¶](https://www.psycopg.org/docs/sql.html#module-usage "Link to this heading")
------------------------------------------------------------------------------------------

Usually you should express the template of your query as an [`SQL`](https://www.psycopg.org/docs/sql.html#psycopg2.sql.SQL "psycopg2.sql.SQL") instance with `{}`-style placeholders and use [`format()`](https://www.psycopg.org/docs/sql.html#psycopg2.sql.SQL.format "psycopg2.sql.SQL.format") to merge the variable parts into them, all of which must be [`Composable`](https://www.psycopg.org/docs/sql.html#psycopg2.sql.Composable "psycopg2.sql.Composable") subclasses. You can still have `%s`-style placeholders in your query and pass values to [`execute()`](https://www.psycopg.org/docs/cursor.html#cursor.execute "cursor.execute"): such value placeholders will be untouched by `format()`:

query = sql.SQL("select {field} from {table} where {pkey} = %s").format(
    field=sql.Identifier('my_name'),
    table=sql.Identifier('some_table'),
    pkey=sql.Identifier('id'))

The resulting object is meant to be passed directly to cursor methods such as [`execute()`](https://www.psycopg.org/docs/cursor.html#cursor.execute "cursor.execute"), [`executemany()`](https://www.psycopg.org/docs/cursor.html#cursor.executemany "cursor.executemany"), [`copy_expert()`](https://www.psycopg.org/docs/cursor.html#cursor.copy_expert "cursor.copy_expert"), but can also be used to compose a query as a Python string, using the [`as_string()`](https://www.psycopg.org/docs/sql.html#psycopg2.sql.Composable.as_string "psycopg2.sql.Composable.as_string") method:

cur.execute(query, (42,))

If part of your query is a variable sequence of arguments, such as a comma-separated list of field names, you can use the [`SQL.join()`](https://www.psycopg.org/docs/sql.html#psycopg2.sql.SQL.join "psycopg2.sql.SQL.join") method to pass them to the query:

query = sql.SQL("select {fields} from {table}").format(
    fields=sql.SQL(',').join([
        sql.Identifier('field1'),
        sql.Identifier('field2'),
        sql.Identifier('field3'),
    ]),
    table=sql.Identifier('some_table'))

`sql` objects[¶](https://www.psycopg.org/docs/sql.html#sql-objects "Link to this heading")
------------------------------------------------------------------------------------------

The `sql` objects are in the following inheritance hierarchy:

[`Composable`](https://www.psycopg.org/docs/sql.html#psycopg2.sql.Composable "psycopg2.sql.Composable"): the base class exposing the common interface

`|__`[`SQL`](https://www.psycopg.org/docs/sql.html#psycopg2.sql.SQL "psycopg2.sql.SQL"): a literal snippet of an SQL query

`|__`[`Identifier`](https://www.psycopg.org/docs/sql.html#psycopg2.sql.Identifier "psycopg2.sql.Identifier"): a PostgreSQL identifier or dot-separated sequence of identifiers

`|__`[`Literal`](https://www.psycopg.org/docs/sql.html#psycopg2.sql.Literal "psycopg2.sql.Literal"): a value hardcoded into a query

`|__`[`Placeholder`](https://www.psycopg.org/docs/sql.html#psycopg2.sql.Placeholder "psycopg2.sql.Placeholder"): a `%s`-style placeholder whose value will be added later e.g. by [`execute()`](https://www.psycopg.org/docs/cursor.html#cursor.execute "cursor.execute")

`|__`[`Composed`](https://www.psycopg.org/docs/sql.html#psycopg2.sql.Composed "psycopg2.sql.Composed"): a sequence of `Composable` instances.

_class_ psycopg2.sql.Composable(_wrapped_)[¶](https://www.psycopg.org/docs/sql.html#psycopg2.sql.Composable "Link to this definition")
Abstract base class for objects that can be used to compose an SQL string.

`Composable` objects can be passed directly to [`execute()`](https://www.psycopg.org/docs/cursor.html#cursor.execute "cursor.execute"), [`executemany()`](https://www.psycopg.org/docs/cursor.html#cursor.executemany "cursor.executemany"), [`copy_expert()`](https://www.psycopg.org/docs/cursor.html#cursor.copy_expert "cursor.copy_expert") in place of the query string.

`Composable` objects can be joined using the `+` operator: the result will be a [`Composed`](https://www.psycopg.org/docs/sql.html#psycopg2.sql.Composed "psycopg2.sql.Composed") instance containing the objects joined. The operator `*` is also supported with an integer argument: the result is a `Composed` instance containing the left argument repeated as many times as requested.

as_string(_context_)[¶](https://www.psycopg.org/docs/sql.html#psycopg2.sql.Composable.as_string "Link to this definition")
Return the string value of the object.

Parameters:
**context** ([`connection`](https://www.psycopg.org/docs/connection.html#connection "connection") or [`cursor`](https://www.psycopg.org/docs/cursor.html#cursor "cursor")) – the context to evaluate the string into.

The method is automatically invoked by [`execute()`](https://www.psycopg.org/docs/cursor.html#cursor.execute "cursor.execute"), [`executemany()`](https://www.psycopg.org/docs/cursor.html#cursor.executemany "cursor.executemany"), [`copy_expert()`](https://www.psycopg.org/docs/cursor.html#cursor.copy_expert "cursor.copy_expert") if a `Composable` is passed instead of the query string.

_class_ psycopg2.sql.SQL(_string_)[¶](https://www.psycopg.org/docs/sql.html#psycopg2.sql.SQL "Link to this definition")
A [`Composable`](https://www.psycopg.org/docs/sql.html#psycopg2.sql.Composable "psycopg2.sql.Composable") representing a snippet of SQL statement.

`SQL` exposes [`join()`](https://www.psycopg.org/docs/sql.html#psycopg2.sql.SQL.join "psycopg2.sql.SQL.join") and [`format()`](https://www.psycopg.org/docs/sql.html#psycopg2.sql.SQL.format "psycopg2.sql.SQL.format") methods useful to create a template where to merge variable parts of a query (for instance field or table names).

The _string_ doesn’t undergo any form of escaping, so it is not suitable to represent variable identifiers or values: you should only use it to pass constant strings representing templates or snippets of SQL statements; use other objects such as [`Identifier`](https://www.psycopg.org/docs/sql.html#psycopg2.sql.Identifier "psycopg2.sql.Identifier") or [`Literal`](https://www.psycopg.org/docs/sql.html#psycopg2.sql.Literal "psycopg2.sql.Literal") to represent variable parts.

Example:

>>> query = sql.SQL("select {0} from {1}").format(
...    sql.SQL(', ').join([sql.Identifier('foo'), sql.Identifier('bar')]),
...    sql.Identifier('table'))
>>> print(query.as_string(conn))
select "foo", "bar" from "table"

string[¶](https://www.psycopg.org/docs/sql.html#psycopg2.sql.SQL.string "Link to this definition")
The string wrapped by the `SQL` object.

format(_*args_, _**kwargs_)[¶](https://www.psycopg.org/docs/sql.html#psycopg2.sql.SQL.format "Link to this definition")
Merge [`Composable`](https://www.psycopg.org/docs/sql.html#psycopg2.sql.Composable "psycopg2.sql.Composable") objects into a template.

Parameters:

* **args** ([_Composable_](https://www.psycopg.org/docs/sql.html#psycopg2.sql.Composable "psycopg2.sql.Composable")) – parameters to replace to numbered (`{0}`, `{1}`) or auto-numbered (`{}`) placeholders

* **kwargs** ([_Composable_](https://www.psycopg.org/docs/sql.html#psycopg2.sql.Composable "psycopg2.sql.Composable")) – parameters to replace to named (`{name}`) placeholders

Returns:
the union of the `SQL` string with placeholders replaced

Return type:
[`Composed`](https://www.psycopg.org/docs/sql.html#psycopg2.sql.Composed "psycopg2.sql.Composed")

The method is similar to the Python `str.format()` method: the string template supports auto-numbered (`{}`), numbered (`{0}`, `{1}`…), and named placeholders (`{name}`), with positional arguments replacing the numbered placeholders and keywords replacing the named ones. However placeholder modifiers (`{0!r}`, `{0:<10}`) are not supported. Only `Composable` objects can be passed to the template.

Example:

>>> print(sql.SQL("select *from {} where {} = %s")
...     .format(sql.Identifier('people'), sql.Identifier('id'))
...     .as_string(conn))
select* from "people" where "id" = %s

>>> print(sql.SQL("select *from {tbl} where {pkey} = %s")
...     .format(tbl=sql.Identifier('people'), pkey=sql.Identifier('id'))
...     .as_string(conn))
select* from "people" where "id" = %s

join(_seq_)[¶](https://www.psycopg.org/docs/sql.html#psycopg2.sql.SQL.join "Link to this definition")
Join a sequence of [`Composable`](https://www.psycopg.org/docs/sql.html#psycopg2.sql.Composable "psycopg2.sql.Composable").

Parameters:
**seq** (iterable of `Composable`) – the elements to join.

Use the `SQL` object’s _string_ to separate the elements in _seq_. Note that [`Composed`](https://www.psycopg.org/docs/sql.html#psycopg2.sql.Composed "psycopg2.sql.Composed") objects are iterable too, so they can be used as argument for this method.

Example:

>>> snip = sql.SQL(', ').join(
...     sql.Identifier(n) for n in ['foo', 'bar', 'baz'])
>>> print(snip.as_string(conn))
"foo", "bar", "baz"

_class_ psycopg2.sql.Identifier(_*strings_)[¶](https://www.psycopg.org/docs/sql.html#psycopg2.sql.Identifier "Link to this definition")
A [`Composable`](https://www.psycopg.org/docs/sql.html#psycopg2.sql.Composable "psycopg2.sql.Composable") representing an SQL identifier or a dot-separated sequence.

Identifiers usually represent names of database objects, such as tables or fields. PostgreSQL identifiers follow [different rules](https://www.postgresql.org/docs/current/static/sql-syntax-lexical.html#SQL-SYNTAX-IDENTIFIERS) than SQL string literals for escaping (e.g. they use double quotes instead of single).

Example:

>>> t1 = sql.Identifier("foo")
>>> t2 = sql.Identifier("ba'r")
>>> t3 = sql.Identifier('ba"z')
>>> print(sql.SQL(', ').join([t1, t2, t3]).as_string(conn))
"foo", "ba'r", "ba""z"

Multiple strings can be passed to the object to represent a qualified name, i.e. a dot-separated sequence of identifiers.

Example:

>>> query = sql.SQL("select {} from {}").format(
...     sql.Identifier("table", "field"),
...     sql.Identifier("schema", "table"))
>>> print(query.as_string(conn))
select "table"."field" from "schema"."table"

Changed in version 2.8: added support for multiple strings.

strings[¶](https://www.psycopg.org/docs/sql.html#psycopg2.sql.Identifier.strings "Link to this definition")
A tuple with the strings wrapped by the [`Identifier`](https://www.psycopg.org/docs/sql.html#psycopg2.sql.Identifier "psycopg2.sql.Identifier").

Added in version 2.8: previous verions only had a `string` attribute. The attribute still exists but is deprecate and will only work if the `Identifier` wraps a single string.

_class_ psycopg2.sql.Literal(_wrapped_)[¶](https://www.psycopg.org/docs/sql.html#psycopg2.sql.Literal "Link to this definition")
A [`Composable`](https://www.psycopg.org/docs/sql.html#psycopg2.sql.Composable "psycopg2.sql.Composable") representing an SQL value to include in a query.

Usually you will want to include placeholders in the query and pass values as [`execute()`](https://www.psycopg.org/docs/cursor.html#cursor.execute "cursor.execute") arguments. If however you really really need to include a literal value in the query you can use this object.

The string returned by `as_string()` follows the normal [adaptation rules](https://www.psycopg.org/docs/usage.html#python-types-adaptation) for Python objects.

Example:

>>> s1 = sql.Literal("foo")
>>> s2 = sql.Literal("ba'r")
>>> s3 = sql.Literal(42)
>>> print(sql.SQL(', ').join([s1, s2, s3]).as_string(conn))
'foo', 'ba''r', 42

wrapped[¶](https://www.psycopg.org/docs/sql.html#psycopg2.sql.Literal.wrapped "Link to this definition")
The object wrapped by the `Literal`.

_class_ psycopg2.sql.Placeholder(_name=None_)[¶](https://www.psycopg.org/docs/sql.html#psycopg2.sql.Placeholder "Link to this definition")
A [`Composable`](https://www.psycopg.org/docs/sql.html#psycopg2.sql.Composable "psycopg2.sql.Composable") representing a placeholder for query parameters.

If the name is specified, generate a named placeholder (e.g. `%(name)s`), otherwise generate a positional placeholder (e.g. `%s`).

The object is useful to generate SQL queries with a variable number of arguments.

Examples:

>>> names = ['foo', 'bar', 'baz']

>>> q1 = sql.SQL("insert into table ({}) values ({})").format(
...     sql.SQL(', ').join(map(sql.Identifier, names)),
...     sql.SQL(', ').join(sql.Placeholder() * len(names)))
>>> print(q1.as_string(conn))
insert into table ("foo", "bar", "baz") values (%s, %s, %s)

>>> q2 = sql.SQL("insert into table ({}) values ({})").format(
...     sql.SQL(', ').join(map(sql.Identifier, names)),
...     sql.SQL(', ').join(map(sql.Placeholder, names)))
>>> print(q2.as_string(conn))
insert into table ("foo", "bar", "baz") values (%(foo)s, %(bar)s, %(baz)s)

name[¶](https://www.psycopg.org/docs/sql.html#psycopg2.sql.Placeholder.name "Link to this definition")
The name of the `Placeholder`.

_class_ psycopg2.sql.Composed(_seq_)[¶](https://www.psycopg.org/docs/sql.html#psycopg2.sql.Composed "Link to this definition")
A [`Composable`](https://www.psycopg.org/docs/sql.html#psycopg2.sql.Composable "psycopg2.sql.Composable") object made of a sequence of `Composable`.

The object is usually created using `Composable` operators and methods. However it is possible to create a `Composed` directly specifying a sequence of `Composable` as arguments.

Example:

>>> comp = sql.Composed(
...     [sql.SQL("insert into "), sql.Identifier("table")])
>>> print(comp.as_string(conn))
insert into "table"

`Composed` objects are iterable (so they can be used in [`SQL.join`](https://www.psycopg.org/docs/sql.html#psycopg2.sql.SQL.join "psycopg2.sql.SQL.join") for instance).

seq[¶](https://www.psycopg.org/docs/sql.html#psycopg2.sql.Composed.seq "Link to this definition")
The list of the content of the `Composed`.

join(_joiner_)[¶](https://www.psycopg.org/docs/sql.html#psycopg2.sql.Composed.join "Link to this definition")
Return a new `Composed` interposing the _joiner_ with the `Composed` items.

The _joiner_ must be a [`SQL`](https://www.psycopg.org/docs/sql.html#psycopg2.sql.SQL "psycopg2.sql.SQL") or a string which will be interpreted as an [`SQL`](https://www.psycopg.org/docs/sql.html#psycopg2.sql.SQL "psycopg2.sql.SQL").

Example:

>>> fields = sql.Identifier('foo') + sql.Identifier('bar')  # a Composed
>>> print(fields.join(', ').as_string(conn))
"foo", "bar"
