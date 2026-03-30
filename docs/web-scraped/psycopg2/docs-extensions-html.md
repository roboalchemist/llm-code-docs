# Source: https://www.psycopg.org/docs/extensions.html

Title: psycopg2.extensions – Extensions to the DB API — Psycopg 2.9.11 documentation

URL Source: https://www.psycopg.org/docs/extensions.html

Markdown Content:
The module contains a few objects and function extending the minimum set of functionalities defined by the [DB API 2.0](https://www.python.org/dev/peps/pep-0249/).

Classes definitions[¶](https://www.psycopg.org/docs/extensions.html#classes-definitions "Link to this heading")
---------------------------------------------------------------------------------------------------------------

Instances of these classes are usually returned by factory functions or attributes. Their definitions are exposed here to allow subclassing, introspection etc.

_class_ psycopg2.extensions.connection(_dsn_, _async=False_)[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.connection "Link to this definition")
Is the class usually returned by the [`connect()`](https://www.psycopg.org/docs/module.html#psycopg2.connect "psycopg2.connect") function. It is exposed by the `extensions` module in order to allow subclassing to extend its behaviour: the subclass should be passed to the `connect()` function using the `connection_factory` parameter. See also [Connection and cursor factories](https://www.psycopg.org/docs/advanced.html#subclassing-connection).

For a complete description of the class, see [`connection`](https://www.psycopg.org/docs/connection.html#connection "connection").

Changed in version 2.7: _async\__ can be used as alias for _async_.

_class_ psycopg2.extensions.cursor(_conn_, _name=None_)[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.cursor "Link to this definition")
It is the class usually returned by the [`connection.cursor()`](https://www.psycopg.org/docs/connection.html#connection.cursor "connection.cursor") method. It is exposed by the `extensions` module in order to allow subclassing to extend its behaviour: the subclass should be passed to the `cursor()` method using the `cursor_factory` parameter. See also [Connection and cursor factories](https://www.psycopg.org/docs/advanced.html#subclassing-cursor).

For a complete description of the class, see [`cursor`](https://www.psycopg.org/docs/cursor.html#cursor "cursor").

_class_ psycopg2.extensions.lobject(_conn_[, _oid_[, _mode_[, _new\_oid_[, _new\_file_]]]])[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.lobject "Link to this definition")
Wrapper for a PostgreSQL large object. See [Access to PostgreSQL large objects](https://www.psycopg.org/docs/usage.html#large-objects) for an overview.

The class can be subclassed: see the [`connection.lobject()`](https://www.psycopg.org/docs/connection.html#connection.lobject "connection.lobject") to know how to specify a `lobject` subclass.

Added in version 2.0.8.

oid[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.lobject.oid "Link to this definition")
Database OID of the object.

mode[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.lobject.mode "Link to this definition")
The mode the database was open. See [`connection.lobject()`](https://www.psycopg.org/docs/connection.html#connection.lobject "connection.lobject") for a description of the available modes.

read(_bytes=-1_)[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.lobject.read "Link to this definition")
Read a chunk of data from the current file position. If -1 (default) read all the remaining data.

The result is an Unicode string (decoded according to [`connection.encoding`](https://www.psycopg.org/docs/connection.html#connection.encoding "connection.encoding")) if the file was open in `t` mode, a bytes string for `b` mode.

Changed in version 2.4: added Unicode support.

write(_str_)[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.lobject.write "Link to this definition")
Write a string to the large object. Return the number of bytes written. Unicode strings are encoded in the [`connection.encoding`](https://www.psycopg.org/docs/connection.html#connection.encoding "connection.encoding") before writing.

Changed in version 2.4: added Unicode support.

export(_file\_name_)[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.lobject.export "Link to this definition")
Export the large object content to the file system.

The method uses the efficient [`lo_export()`](https://www.postgresql.org/docs/current/static/lo-interfaces.html#LO-EXPORT) libpq function.

seek(_offset_, _whence=0_)[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.lobject.seek "Link to this definition")
Set the lobject current position.

Changed in version 2.6: added support for _offset_> 2GB.

tell()[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.lobject.tell "Link to this definition")
Return the lobject current position.

Added in version 2.2.

Changed in version 2.6: added support for return value > 2GB.

truncate(_len=0_)[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.lobject.truncate "Link to this definition")
Truncate the lobject to the given size.

The method will only be available if Psycopg has been built against libpq from PostgreSQL 8.3 or later and can only be used with PostgreSQL servers running these versions. It uses the [`lo_truncate()`](https://www.postgresql.org/docs/current/static/lo-interfaces.html#LO-TRUNCATE) libpq function.

Added in version 2.2.

Changed in version 2.6: added support for _len_> 2GB.

Warning

If Psycopg is built with `lo_truncate()` support or with the 64 bits API support (resp. from PostgreSQL versions 8.3 and 9.3) but at runtime an older version of the dynamic library is found, the `psycopg2` module will fail to import. See [the lo_truncate FAQ](https://www.psycopg.org/docs/faq.html#faq-lo-truncate) about the problem.

close()[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.lobject.close "Link to this definition")
Close the object.

closed[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.lobject.closed "Link to this definition")
Boolean attribute specifying if the object is closed.

unlink()[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.lobject.unlink "Link to this definition")
Close the object and remove it from the database.

_class_ psycopg2.extensions.ConnectionInfo(_connection_)[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ConnectionInfo "Link to this definition")
Details about the native PostgreSQL database connection.

This class exposes several [informative functions](https://www.postgresql.org/docs/current/static/libpq-status.html) about the status of the libpq connection.

Objects of this class are exposed as the [`connection.info`](https://www.psycopg.org/docs/connection.html#connection.info "connection.info") attribute.

Added in version 2.8.

dbname[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ConnectionInfo.dbname "Link to this definition")
The database name of the connection.

See also

libpq docs for [PQdb()](https://www.postgresql.org/docs/current/static/libpq-status.html#LIBPQ-PQDB) for details.

user[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ConnectionInfo.user "Link to this definition")
The user name of the connection.

See also

libpq docs for [PQuser()](https://www.postgresql.org/docs/current/static/libpq-status.html#LIBPQ-PQUSER) for details.

password[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ConnectionInfo.password "Link to this definition")
The password of the connection.

See also

libpq docs for [PQpass()](https://www.postgresql.org/docs/current/static/libpq-status.html#LIBPQ-PQPASS) for details.

host[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ConnectionInfo.host "Link to this definition")
The server host name of the connection.

This can be a host name, an IP address, or a directory path if the connection is via Unix socket. (The path case can be distinguished because it will always be an absolute path, beginning with `/`.)

See also

libpq docs for [PQhost()](https://www.postgresql.org/docs/current/static/libpq-status.html#LIBPQ-PQHOST) for details.

port[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ConnectionInfo.port "Link to this definition")
The port of the connection.

Type:
`int`

See also

libpq docs for [PQport()](https://www.postgresql.org/docs/current/static/libpq-status.html#LIBPQ-PQPORT) for details.

options[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ConnectionInfo.options "Link to this definition")
The command-line options passed in the connection request.

dsn_parameters[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ConnectionInfo.dsn_parameters "Link to this definition")
The effective connection parameters.

Type:
`dict`

The results include values which weren’t explicitly set by the connection string, such as defaults, environment variables, etc. The _password_ parameter is removed from the results.

Example:

>>> conn.info.dsn_parameters
{'dbname': 'test', 'user': 'postgres', 'port': '5432', 'sslmode': 'prefer'}

Requires libpq >= 9.3.

status[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ConnectionInfo.status "Link to this definition")
The status of the connection.

Type:
`int`

transaction_status[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ConnectionInfo.transaction_status "Link to this definition")
The current in-transaction status of the connection.

Symbolic constants for the values are defined in the module [`psycopg2.extensions`](https://www.psycopg.org/docs/extensions.html#module-psycopg2.extensions "psycopg2.extensions"): see [Transaction status constants](https://www.psycopg.org/docs/extensions.html#transaction-status-constants) for the available values.

Type:
`int`

parameter_status(_name_)[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ConnectionInfo.parameter_status "Link to this definition")
Looks up a current parameter setting of the server.

Parameters:
**name** (`str`) – The name of the parameter to return.

Returns:
The parameter value, `None` if the parameter is unknown.

Return type:
`str`

protocol_version[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ConnectionInfo.protocol_version "Link to this definition")
The frontend/backend protocol being used.

Type:
`int`

Currently Psycopg supports only protocol 3, which allows connection to PostgreSQL server from version 7.4. Psycopg versions previous than 2.3 support both protocols 2 and 3.

server_version[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ConnectionInfo.server_version "Link to this definition")
Returns an integer representing the server version.

Type:
`int`

The number is formed by converting the major, minor, and revision numbers into two-decimal-digit numbers and appending them together. After PostgreSQL 10 the minor version was dropped, so the second group of digits is always `00`. For example, version 9.3.5 will be returned as `90305`, version 10.2 as `100002`.

error_message[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ConnectionInfo.error_message "Link to this definition")
The error message most recently generated by an operation on the connection.

`None` if there is no current message.

socket[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ConnectionInfo.socket "Link to this definition")
The file descriptor number of the connection socket to the server.

Type:
`int`

backend_pid[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ConnectionInfo.backend_pid "Link to this definition")
The process ID (PID) of the backend process you connected to.

Type:
`int`

needs_password[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ConnectionInfo.needs_password "Link to this definition")
The connection authentication method required a password, but none was available.

Type:
`bool`

used_password[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ConnectionInfo.used_password "Link to this definition")
The connection authentication method used a password.

Type:
`bool`

ssl_in_use[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ConnectionInfo.ssl_in_use "Link to this definition")
`True` if the connection uses SSL, `False` if not.

Only available if psycopg was built with libpq >= 9.5; raise [`NotSupportedError`](https://www.psycopg.org/docs/module.html#psycopg2.NotSupportedError "psycopg2.NotSupportedError") otherwise.

Type:
`bool`

ssl_attribute(_name_)[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ConnectionInfo.ssl_attribute "Link to this definition")
Returns SSL-related information about the connection.

Parameters:
**name** (`str`) – The name of the attribute to return.

Returns:
The attribute value, `None` if unknown.

Return type:
`str`

Only available if psycopg was built with libpq >= 9.5; raise [`NotSupportedError`](https://www.psycopg.org/docs/module.html#psycopg2.NotSupportedError "psycopg2.NotSupportedError") otherwise.

Valid names are available in [`ssl_attribute_names`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ConnectionInfo.ssl_attribute_names "psycopg2.extensions.ConnectionInfo.ssl_attribute_names").

ssl_attribute_names[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ConnectionInfo.ssl_attribute_names "Link to this definition")
The list of the SSL attribute names available.

Type:
`list` of `str`

Only available if psycopg was built with libpq >= 9.5; raise [`NotSupportedError`](https://www.psycopg.org/docs/module.html#psycopg2.NotSupportedError "psycopg2.NotSupportedError") otherwise.

_class_ psycopg2.extensions.Column(_\*args_, _\*\*kwargs_)[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Column "Link to this definition")
Description of one result column, exposed as items of the [`cursor.description`](https://www.psycopg.org/docs/cursor.html#cursor.description "cursor.description") sequence.

Added in version 2.8: in previous version the `description` attribute was a sequence of simple tuples or namedtuples.

name[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Column.name "Link to this definition")
The name of the column returned.

type_code[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Column.type_code "Link to this definition")
The PostgreSQL OID of the column. You can use the [`pg_type`](https://www.postgresql.org/docs/current/static/catalog-pg-type.html) system table to get more informations about the type. This is the value used by Psycopg to decide what Python type use to represent the value. See also [Type casting of SQL types into Python objects](https://www.psycopg.org/docs/advanced.html#type-casting-from-sql-to-python).

display_size[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Column.display_size "Link to this definition")
Supposed to be the actual length of the column in bytes. Obtaining this value is computationally intensive, so it is always `None`.

Changed in version 2.8: It was previously possible to obtain this value using a compiler flag at builtin.

internal_size[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Column.internal_size "Link to this definition")
The size in bytes of the column associated to this column on the server. Set to a negative value for variable-size types See also [PQfsize](https://www.postgresql.org/docs/current/static/libpq-exec.html#LIBPQ-PQFSIZE).

precision[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Column.precision "Link to this definition")
Total number of significant digits in columns of type [`NUMERIC`](https://www.postgresql.org/docs/current/static/datatype-numeric.html#DATATYPE-NUMERIC-DECIMAL). `None` for other types.

scale[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Column.scale "Link to this definition")
Count of decimal digits in the fractional part in columns of type `NUMERIC`. `None` for other types.

null_ok[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Column.null_ok "Link to this definition")
Always `None` as not easy to retrieve from the libpq.

table_oid[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Column.table_oid "Link to this definition")
The oid of the table from which the column was fetched (matching `pg_class.oid`). `None` if the column is not a simple reference to a table column. See also [PQftable](https://www.postgresql.org/docs/current/static/libpq-exec.html#LIBPQ-PQFTABLE).

Added in version 2.8.

table_column[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Column.table_column "Link to this definition")
The number of the column (within its table) making up the result (matching `pg_attribute.attnum`, so it will start from 1). `None` if the column is not a simple reference to a table column. See also [PQftablecol](https://www.postgresql.org/docs/current/static/libpq-exec.html#LIBPQ-PQFTABLECOL).

Added in version 2.8.

_class_ psycopg2.extensions.Notify(_pid_, _channel_, _payload=''_)[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Notify "Link to this definition")
A notification received from the backend.

`Notify` instances are made available upon reception on the [`notifies`](https://www.psycopg.org/docs/connection.html#connection.notifies "connection.notifies") member of the listening connection. The object can be also accessed as a 2 items tuple returning the members `(pid,channel)` for backward compatibility.

See [Asynchronous notifications](https://www.psycopg.org/docs/advanced.html#async-notify) for details.

Added in version 2.3.

channel[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Notify.channel "Link to this definition")
The name of the channel to which the notification was sent.

payload[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Notify.payload "Link to this definition")
The payload message of the notification.

Attaching a payload to a notification is only available since PostgreSQL 9.0: for notifications received from previous versions of the server this member is always the empty string.

pid[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Notify.pid "Link to this definition")
The ID of the backend process that sent the notification.

Note: if the sending session was handled by Psycopg, you can use `backend_pid` to know its PID.

_class_ psycopg2.extensions.Xid(_format\_id_, _gtrid_, _bqual_)[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Xid "Link to this definition")
A transaction identifier used for two-phase commit.

Usually returned by the connection methods [`xid()`](https://www.psycopg.org/docs/connection.html#connection.xid "connection.xid") and [`tpc_recover()`](https://www.psycopg.org/docs/connection.html#connection.tpc_recover "connection.tpc_recover"). `Xid` instances can be unpacked as a 3-item tuples containing the items `(format_id,gtrid,bqual)`. The `str()` of the object returns the _transaction ID_ used in the commands sent to the server.

See [Two-Phase Commit protocol support](https://www.psycopg.org/docs/usage.html#tpc) for an introduction.

Added in version 2.3.

_static_ from_string(_s_)[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Xid.from_string "Link to this definition")
Create a `Xid` object from a string representation. Static method.

If _s_ is a PostgreSQL transaction ID produced by a XA transaction, the returned object will have [`format_id`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Xid.format_id "psycopg2.extensions.Xid.format_id"), [`gtrid`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Xid.gtrid "psycopg2.extensions.Xid.gtrid"), [`bqual`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Xid.bqual "psycopg2.extensions.Xid.bqual") set to the values of the preparing XA id. Otherwise only the `gtrid` is populated with the unparsed string. The operation is the inverse of the one performed by `str(xid)`.

bqual[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Xid.bqual "Link to this definition")
Branch qualifier of the transaction.

In a XA transaction every resource participating to a transaction receives a distinct branch qualifier. `None` if the transaction doesn’t follow the XA standard.

database[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Xid.database "Link to this definition")
Database the recovered transaction belongs to.

format_id[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Xid.format_id "Link to this definition")
Format ID in a XA transaction.

A non-negative 32 bit integer. `None` if the transaction doesn’t follow the XA standard.

gtrid[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Xid.gtrid "Link to this definition")
Global transaction ID in a XA transaction.

If the transaction doesn’t follow the XA standard, it is the plain _transaction ID_ used in the server commands.

owner[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Xid.owner "Link to this definition")
Name of the user who prepared a recovered transaction.

prepared[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Xid.prepared "Link to this definition")
Timestamp (with timezone) in which a recovered transaction was prepared.

_class_ psycopg2.extensions.Diagnostics(_exception_)[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Diagnostics "Link to this definition")
Details from a database error report.

The object is returned by the [`diag`](https://www.psycopg.org/docs/module.html#psycopg2.Error.diag "psycopg2.Error.diag") attribute of the `Error` object. All the information available from the [`PQresultErrorField()`](https://www.postgresql.org/docs/current/static/libpq-exec.html#LIBPQ-PQRESULTERRORFIELD) function are exposed as attributes by the object, e.g. the `severity` attribute returns the `PG_DIAG_SEVERITY` code. Please refer to the [PostgreSQL documentation](https://www.postgresql.org/docs/current/static/libpq-exec.html#LIBPQ-PQRESULTERRORFIELD) for the meaning of all the attributes.

Added in version 2.5.

The attributes currently available are:

column_name[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Diagnostics.column_name "Link to this definition")constraint_name[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Diagnostics.constraint_name "Link to this definition")context[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Diagnostics.context "Link to this definition")datatype_name[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Diagnostics.datatype_name "Link to this definition")internal_position[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Diagnostics.internal_position "Link to this definition")internal_query[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Diagnostics.internal_query "Link to this definition")message_detail[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Diagnostics.message_detail "Link to this definition")message_hint[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Diagnostics.message_hint "Link to this definition")message_primary[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Diagnostics.message_primary "Link to this definition")schema_name[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Diagnostics.schema_name "Link to this definition")severity[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Diagnostics.severity "Link to this definition")severity_nonlocalized[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Diagnostics.severity_nonlocalized "Link to this definition")source_file[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Diagnostics.source_file "Link to this definition")source_function[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Diagnostics.source_function "Link to this definition")source_line[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Diagnostics.source_line "Link to this definition")sqlstate[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Diagnostics.sqlstate "Link to this definition")statement_position[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Diagnostics.statement_position "Link to this definition")table_name[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Diagnostics.table_name "Link to this definition")
A string with the error field if available; `None` if not available. The attribute value is available only if the error sent by the server: not all the fields are available for all the errors and for all the server versions.

Added in version 2.8: The `severity_nonlocalized` attribute.

SQL adaptation protocol objects[¶](https://www.psycopg.org/docs/extensions.html#sql-adaptation-protocol-objects "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------

Psycopg provides a flexible system to adapt Python objects to the SQL syntax (inspired to the [**PEP 246**](https://peps.python.org/pep-0246/)), allowing serialization in PostgreSQL. See [Adapting new Python types to SQL syntax](https://www.psycopg.org/docs/advanced.html#adapting-new-types) for a detailed description. The following objects deal with Python objects adaptation:

psycopg2.extensions.adapt(_obj_)[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.adapt "Link to this definition")
Return the SQL representation of _obj_ as an [`ISQLQuote`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ISQLQuote "psycopg2.extensions.ISQLQuote"). Raise a [`ProgrammingError`](https://www.psycopg.org/docs/module.html#psycopg2.ProgrammingError "psycopg2.ProgrammingError") if how to adapt the object is unknown. In order to allow new objects to be adapted, register a new adapter for it using the [`register_adapter()`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.register_adapter "psycopg2.extensions.register_adapter") function.

The function is the entry point of the adaptation mechanism: it can be used to write adapters for complex objects by recursively calling `adapt()` on its components.

psycopg2.extensions.register_adapter(_class_, _adapter_)[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.register_adapter "Link to this definition")
Register a new adapter for the objects of class _class_.

_adapter_ should be a function taking a single argument (the object to adapt) and returning an object conforming to the [`ISQLQuote`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ISQLQuote "psycopg2.extensions.ISQLQuote") protocol (e.g. exposing a `getquoted()` method). The [`AsIs`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.AsIs "psycopg2.extensions.AsIs") is often useful for this task.

Once an object is registered, it can be safely used in SQL queries and by the [`adapt()`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.adapt "psycopg2.extensions.adapt") function.

_class_ psycopg2.extensions.ISQLQuote(_wrapped\_object_)[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ISQLQuote "Link to this definition")
Represents the SQL adaptation protocol. Objects conforming this protocol should implement a [`getquoted()`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ISQLQuote.getquoted "psycopg2.extensions.ISQLQuote.getquoted") and optionally a [`prepare()`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ISQLQuote.prepare "psycopg2.extensions.ISQLQuote.prepare") method.

Adapters may subclass `ISQLQuote`, but is not necessary: it is enough to expose a `getquoted()` method to be conforming.

_wrapped[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ISQLQuote._wrapped "Link to this definition")
The wrapped object passes to the constructor

getquoted()[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ISQLQuote.getquoted "Link to this definition")
Subclasses or other conforming objects should return a valid SQL string representing the wrapped object. In Python 3 the SQL must be returned in a `bytes` object. The `ISQLQuote` implementation does nothing.

prepare(_conn_)[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ISQLQuote.prepare "Link to this definition")
Prepare the adapter for a connection. The method is optional: if implemented, it will be invoked before `getquoted()` with the connection to adapt for as argument.

A conform object can implement this method if the SQL representation depends on any server parameter, such as the server version or the `standard_conforming_string` setting. Container objects may store the connection and use it to recursively prepare contained objects: see the implementation for [`psycopg2.extensions.SQL_IN`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.SQL_IN "psycopg2.extensions.SQL_IN") for a simple example.

_class_ psycopg2.extensions.AsIs(_object_)[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.AsIs "Link to this definition")
Adapter conform to the [`ISQLQuote`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ISQLQuote "psycopg2.extensions.ISQLQuote") protocol useful for objects whose string representation is already valid as SQL representation.

getquoted()[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.AsIs.getquoted "Link to this definition")
Return the `str()` conversion of the wrapped object.

>>> AsIs(42).getquoted()
'42'

_class_ psycopg2.extensions.QuotedString(_str_)[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.QuotedString "Link to this definition")
Adapter conform to the [`ISQLQuote`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ISQLQuote "psycopg2.extensions.ISQLQuote") protocol for string-like objects.

getquoted()[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.QuotedString.getquoted "Link to this definition")
Return the string enclosed in single quotes. Any single quote appearing in the string is escaped by doubling it according to SQL string constants syntax. Backslashes are escaped too.

>>> QuotedString(r"O'Reilly").getquoted()
"'O''Reilly'"

_class_ psycopg2.extensions.Binary(_str_)[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Binary "Link to this definition")
Adapter conform to the [`ISQLQuote`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ISQLQuote "psycopg2.extensions.ISQLQuote") protocol for binary objects.

getquoted()[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Binary.getquoted "Link to this definition")
Return the string enclosed in single quotes. It performs the same escaping of the [`QuotedString`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.QuotedString "psycopg2.extensions.QuotedString") adapter, plus it knows how to escape non-printable chars.

>>> Binary("\x00\x08\x0F").getquoted()
"'\\\\000\\\\010\\\\017'"

Changed in version 2.0.14: previously the adapter was not exposed by the `extensions` module. In older versions it can be imported from the implementation module `psycopg2._psycopg`.

_class_ psycopg2.extensions.Boolean[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Boolean "Link to this definition")_class_ psycopg2.extensions.Float[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Float "Link to this definition")_class_ psycopg2.extensions.SQL_IN[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.SQL_IN "Link to this definition")
Specialized adapters for builtin objects.

_class_ psycopg2.extensions.DateFromPy[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.DateFromPy "Link to this definition")_class_ psycopg2.extensions.TimeFromPy[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.TimeFromPy "Link to this definition")_class_ psycopg2.extensions.TimestampFromPy[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.TimestampFromPy "Link to this definition")_class_ psycopg2.extensions.IntervalFromPy[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.IntervalFromPy "Link to this definition")
Specialized adapters for Python datetime objects.

psycopg2.extensions.adapters[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.adapters "Link to this definition")
Dictionary of the currently registered object adapters. Use [`register_adapter()`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.register_adapter "psycopg2.extensions.register_adapter") to add an adapter for a new type.

Database types casting functions[¶](https://www.psycopg.org/docs/extensions.html#database-types-casting-functions "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------

These functions are used to manipulate type casters to convert from PostgreSQL types to Python objects. See [Type casting of SQL types into Python objects](https://www.psycopg.org/docs/advanced.html#type-casting-from-sql-to-python) for details.

psycopg2.extensions.new_type(_oids_, _name_, _adapter_)[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.new_type "Link to this definition")
Create a new type caster to convert from a PostgreSQL type to a Python object. The object created must be registered using [`register_type()`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.register_type "psycopg2.extensions.register_type") to be used.

Parameters:

* **oids** – tuple of OIDs of the PostgreSQL type to convert.

* **name** – the name of the new type adapter.

* **adapter** – the adaptation function.

The object OID can be read from the [`cursor.description`](https://www.psycopg.org/docs/cursor.html#cursor.description "cursor.description") attribute or by querying from the PostgreSQL catalog.

_adapter_ should have signature `fun(value, cur)` where _value_ is the string representation returned by PostgreSQL and _cur_ is the cursor from which data are read. In case of `NULL`, _value_ will be `None`. The adapter should return the converted object.

See [Type casting of SQL types into Python objects](https://www.psycopg.org/docs/advanced.html#type-casting-from-sql-to-python) for an usage example.

psycopg2.extensions.new_array_type(_oids_, _name_, _base\_caster_)[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.new_array_type "Link to this definition")
Create a new type caster to convert from a PostgreSQL array type to a list of Python object. The object created must be registered using [`register_type()`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.register_type "psycopg2.extensions.register_type") to be used.

Parameters:

* **oids** – tuple of OIDs of the PostgreSQL type to convert. It should probably contain the oid of the array type (e.g. the `typarray` field in the `pg_type` table).

* **name** – the name of the new type adapter.

* **base_caster** – a Psycopg typecaster, e.g. created using the [`new_type()`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.new_type "psycopg2.extensions.new_type") function. The caster should be able to parse a single item of the desired type.

Added in version 2.4.3.

Note

The function can be used to create a generic array typecaster, returning a list of strings: just use [`psycopg2.STRING`](https://www.psycopg.org/docs/module.html#psycopg2.STRING "psycopg2.STRING") as base typecaster. For instance, if you want to receive an array of `macaddr` from the database, each address represented by string, you can use:

# select typarray from pg_type where typname = 'macaddr' -> 1040

psycopg2.extensions.register_type(
    psycopg2.extensions.new_array_type(
        (1040,), 'MACADDR[]', psycopg2.STRING))

psycopg2.extensions.register_type(_obj_[, _scope_])[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.register_type "Link to this definition")
Register a type caster created using [`new_type()`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.new_type "psycopg2.extensions.new_type").

If _scope_ is specified, it should be a [`connection`](https://www.psycopg.org/docs/connection.html#connection "connection") or a [`cursor`](https://www.psycopg.org/docs/cursor.html#cursor "cursor"): the type caster will be effective only limited to the specified object. Otherwise it will be globally registered.

psycopg2.extensions.string_types[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.string_types "Link to this definition")
The global register of type casters.

psycopg2.extensions.encodings[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.encodings "Link to this definition")
Mapping from [PostgreSQL encoding](https://www.postgresql.org/docs/current/static/multibyte.html) to [Python encoding](https://docs.python.org/library/codecs.html#standard-encodings) names. Used by Psycopg when adapting or casting unicode strings. See [Unicode handling](https://www.psycopg.org/docs/usage.html#unicode-handling).

Additional exceptions[¶](https://www.psycopg.org/docs/extensions.html#additional-exceptions "Link to this heading")
-------------------------------------------------------------------------------------------------------------------

The module exports a few exceptions in addition to the [standard ones](https://www.psycopg.org/docs/module.html#dbapi-exceptions) defined by the [DB API 2.0](https://www.python.org/dev/peps/pep-0249/).

Note

From psycopg 2.8 these error classes are also exposed by the [`psycopg2.errors`](https://www.psycopg.org/docs/errors.html#module-psycopg2.errors "psycopg2.errors") module.

_exception_ psycopg2.extensions.QueryCanceledError[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.QueryCanceledError "Link to this definition")
(subclasses [`OperationalError`](https://www.psycopg.org/docs/module.html#psycopg2.OperationalError "psycopg2.OperationalError"))

Error related to SQL query cancellation. It can be trapped specifically to detect a timeout.

Added in version 2.0.7.

_exception_ psycopg2.extensions.TransactionRollbackError[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.TransactionRollbackError "Link to this definition")
(subclasses [`OperationalError`](https://www.psycopg.org/docs/module.html#psycopg2.OperationalError "psycopg2.OperationalError"))

Error causing transaction rollback (deadlocks, serialization failures, etc). It can be trapped specifically to detect a deadlock.

Added in version 2.0.7.

Coroutines support functions[¶](https://www.psycopg.org/docs/extensions.html#coroutines-support-functions "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------

These functions are used to set and retrieve the callback function for [cooperation with coroutine libraries](https://www.psycopg.org/docs/advanced.html#green-support).

Added in version 2.2.

psycopg2.extensions.set_wait_callback(_f_)[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.set_wait_callback "Link to this definition")
Register a callback function to block waiting for data.

The callback should have signature `fun(conn)` and is called to wait for data available whenever a blocking function from the libpq is called. Use `set_wait_callback(None)` to revert to the original behaviour (i.e. using blocking libpq functions).

The function is an hook to allow coroutine-based libraries (such as [Eventlet](https://eventlet.net/) or [gevent](http://www.gevent.org/)) to switch when Psycopg is blocked, allowing other coroutines to run concurrently.

See [`wait_select()`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.wait_select "psycopg2.extras.wait_select") for an example of a wait callback implementation.

psycopg2.extensions.get_wait_callback()[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.get_wait_callback "Link to this definition")
Return the currently registered wait callback.

Return `None` if no callback is currently registered.

Other functions[¶](https://www.psycopg.org/docs/extensions.html#other-functions "Link to this heading")
-------------------------------------------------------------------------------------------------------

psycopg2.extensions.libpq_version()[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.libpq_version "Link to this definition")
Return the version number of the `libpq` dynamic library loaded as an integer, in the same format of [`server_version`](https://www.psycopg.org/docs/connection.html#connection.server_version "connection.server_version").

Raise [`NotSupportedError`](https://www.psycopg.org/docs/module.html#psycopg2.NotSupportedError "psycopg2.NotSupportedError") if the `psycopg2` module was compiled with a `libpq` version lesser than 9.1 (which can be detected by the [`__libpq_version__`](https://www.psycopg.org/docs/module.html#psycopg2.__libpq_version__ "psycopg2.__libpq_version__") constant).

Added in version 2.7.

psycopg2.extensions.make_dsn(_dsn=None_, _\*\*kwargs_)[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.make_dsn "Link to this definition")
Create a valid connection string from arguments.

Put together the arguments in _kwargs_ into a connection string. If _dsn_ is specified too, merge the arguments coming from both the sources. If the same argument name is specified in both the sources, the _kwargs_ value overrides the _dsn_ value.

The input arguments are validated: the output should always be a valid connection string (as far as [`parse_dsn()`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.parse_dsn "psycopg2.extensions.parse_dsn") is concerned). If not raise [`ProgrammingError`](https://www.psycopg.org/docs/module.html#psycopg2.ProgrammingError "psycopg2.ProgrammingError").

Example:

>>> from psycopg2.extensions import make_dsn
>>> make_dsn('dbname=foo host=example.com', password="s3cr3t")
'host=example.com password=s3cr3t dbname=foo'

Added in version 2.7.

psycopg2.extensions.parse_dsn(_dsn_)[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.parse_dsn "Link to this definition")
Parse connection string into a dictionary of keywords and values.

Parsing is delegated to the libpq: different versions of the client library may support different formats or parameters (for example, [connection URIs](https://www.postgresql.org/docs/current/static/libpq-connect.html#LIBPQ-CONNSTRING) are only supported from libpq 9.2). Raise [`ProgrammingError`](https://www.psycopg.org/docs/module.html#psycopg2.ProgrammingError "psycopg2.ProgrammingError") if the _dsn_ is not valid.

Example:

>>> from psycopg2.extensions import parse_dsn
>>> parse_dsn('dbname=test user=postgres password=secret')
{'password': 'secret', 'user': 'postgres', 'dbname': 'test'}
>>> parse_dsn("postgresql://someone@example.com/somedb?connect_timeout=10")
{'host': 'example.com', 'user': 'someone', 'dbname': 'somedb', 'connect_timeout': '10'}

Added in version 2.7.

psycopg2.extensions.quote_ident(_str_, _scope_)[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.quote_ident "Link to this definition")
Return quoted identifier according to PostgreSQL quoting rules.

The _scope_ must be a [`connection`](https://www.psycopg.org/docs/connection.html#connection "connection") or a [`cursor`](https://www.psycopg.org/docs/cursor.html#cursor "cursor"), the underlying connection encoding is used for any necessary character conversion.

Added in version 2.7.

psycopg2.extensions.encrypt_password(_password_, _user_, _scope=None_, _algorithm=None_)[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.encrypt_password "Link to this definition")
Return the encrypted form of a PostgreSQL password.

Parameters:

* **password** – the cleartext password to encrypt

* **user** – the name of the user to use the password for

* **scope** ([`connection`](https://www.psycopg.org/docs/connection.html#connection "connection") or [`cursor`](https://www.psycopg.org/docs/cursor.html#cursor "cursor")) – the scope to encrypt the password into; if _algorithm_ is `md5` it can be `None`

* **algorithm** – the password encryption algorithm to use

The _algorithm_`md5` is always supported. Other algorithms are only supported if the client libpq version is at least 10 and may require a compatible server version: check the [PostgreSQL encryption documentation](https://www.postgresql.org/docs/current/static/encryption-options.html) to know the algorithms supported by your server.

Using `None` as _algorithm_ will result in querying the server to know the current server password encryption setting, which is a blocking operation: query the server separately and specify a value for _algorithm_ if you want to maintain a non-blocking behaviour.

Added in version 2.8.

Isolation level constants[¶](https://www.psycopg.org/docs/extensions.html#isolation-level-constants "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------

Psycopg2 [`connection`](https://www.psycopg.org/docs/connection.html#connection "connection") objects hold informations about the PostgreSQL [transaction isolation level](https://www.postgresql.org/docs/current/static/transaction-iso.html). By default Psycopg doesn’t change the default configuration of the server ([`ISOLATION_LEVEL_DEFAULT`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ISOLATION_LEVEL_DEFAULT "psycopg2.extensions.ISOLATION_LEVEL_DEFAULT")); the default for PostgreSQL servers is typically `READ COMMITTED`, but this may be changed in the server configuration files. A different isolation level can be set through the [`set_isolation_level()`](https://www.psycopg.org/docs/connection.html#connection.set_isolation_level "connection.set_isolation_level") or [`set_session()`](https://www.psycopg.org/docs/connection.html#connection.set_session "connection.set_session") methods. The level can be set to one of the following constants:

psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT "Link to this definition")
No transaction is started when commands are executed and no [`commit()`](https://www.psycopg.org/docs/connection.html#connection.commit "connection.commit") or [`rollback()`](https://www.psycopg.org/docs/connection.html#connection.rollback "connection.rollback") is required. Some PostgreSQL command such as `CREATE DATABASE` or `VACUUM` can’t run into a transaction: to run such command use:

>>> conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

See also [Transactions control](https://www.psycopg.org/docs/usage.html#transactions-control).

psycopg2.extensions.ISOLATION_LEVEL_READ_UNCOMMITTED[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ISOLATION_LEVEL_READ_UNCOMMITTED "Link to this definition")
The `READ UNCOMMITTED` isolation level is defined in the SQL standard but not available in the MVCC model of PostgreSQL: it is replaced by the stricter `READ COMMITTED`.

psycopg2.extensions.ISOLATION_LEVEL_READ_COMMITTED[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ISOLATION_LEVEL_READ_COMMITTED "Link to this definition")
This is usually the default PostgreSQL value, but a different default may be set in the database configuration.

A new transaction is started at the first [`execute()`](https://www.psycopg.org/docs/cursor.html#cursor.execute "cursor.execute") command on a cursor and at each new `execute()` after a [`commit()`](https://www.psycopg.org/docs/connection.html#connection.commit "connection.commit") or a [`rollback()`](https://www.psycopg.org/docs/connection.html#connection.rollback "connection.rollback"). The transaction runs in the PostgreSQL `READ COMMITTED` isolation level: a `SELECT` query sees only data committed before the query began; it never sees either uncommitted data or changes committed during query execution by concurrent transactions.

psycopg2.extensions.ISOLATION_LEVEL_REPEATABLE_READ[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ISOLATION_LEVEL_REPEATABLE_READ "Link to this definition")
As in `ISOLATION_LEVEL_READ_COMMITTED`, a new transaction is started at the first [`execute()`](https://www.psycopg.org/docs/cursor.html#cursor.execute "cursor.execute") command. Transactions run at a `REPEATABLE READ` isolation level: all the queries in a transaction see a snapshot as of the start of the transaction, not as of the start of the current query within the transaction. However applications using this level must be prepared to retry transactions due to serialization failures.

While this level provides a guarantee that each transaction sees a completely stable view of the database, this view will not necessarily always be consistent with some serial (one at a time) execution of concurrent transactions of the same level.

Changed in version 2.4.2: The value was an alias for `ISOLATION_LEVEL_SERIALIZABLE` before. The two levels are distinct since PostgreSQL 9.1

psycopg2.extensions.ISOLATION_LEVEL_SERIALIZABLE[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ISOLATION_LEVEL_SERIALIZABLE "Link to this definition")
As in `ISOLATION_LEVEL_READ_COMMITTED`, a new transaction is started at the first [`execute()`](https://www.psycopg.org/docs/cursor.html#cursor.execute "cursor.execute") command. Transactions run at a `SERIALIZABLE` isolation level. This is the strictest transactions isolation level, equivalent to having the transactions executed serially rather than concurrently. However applications using this level must be prepared to retry transactions due to serialization failures.

Starting from PostgreSQL 9.1, this mode monitors for conditions which could make execution of a concurrent set of serializable transactions behave in a manner inconsistent with all possible serial (one at a time) executions of those transaction. In previous version the behaviour was the same of the `REPEATABLE READ` isolation level.

psycopg2.extensions.ISOLATION_LEVEL_DEFAULT[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ISOLATION_LEVEL_DEFAULT "Link to this definition")
A new transaction is started at the first [`execute()`](https://www.psycopg.org/docs/cursor.html#cursor.execute "cursor.execute") command, but the isolation level is not explicitly selected by Psycopg: the server will use whatever level is defined in its configuration or by statements executed within the session outside Pyscopg control. If you want to know what the value is you can use a query such as

```
show
transaction_isolation
```

.

Added in version 2.7.

Transaction status constants[¶](https://www.psycopg.org/docs/extensions.html#transaction-status-constants "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------

These values represent the possible status of a transaction: the current value can be read using the `connection.info.transaction_status` property.

psycopg2.extensions.TRANSACTION_STATUS_IDLE[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.TRANSACTION_STATUS_IDLE "Link to this definition")
The session is idle and there is no current transaction.

psycopg2.extensions.TRANSACTION_STATUS_ACTIVE[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.TRANSACTION_STATUS_ACTIVE "Link to this definition")
A command is currently in progress.

psycopg2.extensions.TRANSACTION_STATUS_INTRANS[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.TRANSACTION_STATUS_INTRANS "Link to this definition")
The session is idle in a valid transaction block.

psycopg2.extensions.TRANSACTION_STATUS_INERROR[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.TRANSACTION_STATUS_INERROR "Link to this definition")
The session is idle in a failed transaction block.

psycopg2.extensions.TRANSACTION_STATUS_UNKNOWN[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.TRANSACTION_STATUS_UNKNOWN "Link to this definition")
Reported if the connection with the server is bad.

Connection status constants[¶](https://www.psycopg.org/docs/extensions.html#connection-status-constants "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------

These values represent the possible status of a connection: the current value can be read from the [`status`](https://www.psycopg.org/docs/connection.html#connection.status "connection.status") attribute.

It is possible to find the connection in other status than the one shown below. Those are the only states in which a working connection is expected to be found during the execution of regular Python client code: other states are for internal usage and Python code should not rely on them.

psycopg2.extensions.STATUS_READY[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.STATUS_READY "Link to this definition")
Connection established. No transaction in progress.

psycopg2.extensions.STATUS_BEGIN[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.STATUS_BEGIN "Link to this definition")
Connection established. A transaction is currently in progress.

psycopg2.extensions.STATUS_IN_TRANSACTION[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.STATUS_IN_TRANSACTION "Link to this definition")
An alias for [`STATUS_BEGIN`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.STATUS_BEGIN "psycopg2.extensions.STATUS_BEGIN")

psycopg2.extensions.STATUS_PREPARED[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.STATUS_PREPARED "Link to this definition")
The connection has been prepared for the second phase in a [two-phase commit](https://www.psycopg.org/docs/usage.html#tpc) transaction. The connection can’t be used to send commands to the database until the transaction is finished with [`tpc_commit()`](https://www.psycopg.org/docs/connection.html#connection.tpc_commit "connection.tpc_commit") or [`tpc_rollback()`](https://www.psycopg.org/docs/connection.html#connection.tpc_rollback "connection.tpc_rollback").

Added in version 2.3.

Poll constants[¶](https://www.psycopg.org/docs/extensions.html#poll-constants "Link to this heading")
-----------------------------------------------------------------------------------------------------

Added in version 2.2.

These values can be returned by [`connection.poll()`](https://www.psycopg.org/docs/connection.html#connection.poll "connection.poll") during asynchronous connection and communication. They match the values in the libpq enum `PostgresPollingStatusType`. See [Asynchronous support](https://www.psycopg.org/docs/advanced.html#async-support) and [Support for coroutine libraries](https://www.psycopg.org/docs/advanced.html#green-support).

psycopg2.extensions.POLL_OK[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.POLL_OK "Link to this definition")
The data being read is available, or the file descriptor is ready for writing: reading or writing will not block.

psycopg2.extensions.POLL_READ[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.POLL_READ "Link to this definition")
Some data is being read from the backend, but it is not available yet on the client and reading would block. Upon receiving this value, the client should wait for the connection file descriptor to be ready _for reading_. For example:

select.select([conn.fileno()], [], [])

psycopg2.extensions.POLL_WRITE[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.POLL_WRITE "Link to this definition")
Some data is being sent to the backend but the connection file descriptor can’t currently accept new data. Upon receiving this value, the client should wait for the connection file descriptor to be ready _for writing_. For example:

select.select([], [conn.fileno()], [])

psycopg2.extensions.POLL_ERROR[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.POLL_ERROR "Link to this definition")
There was a problem during connection polling. This value should actually never be returned: in case of poll error usually an exception containing the relevant details is raised.

Additional database types[¶](https://www.psycopg.org/docs/extensions.html#additional-database-types "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------

The `extensions` module includes typecasters for many standard PostgreSQL types. These objects allow the conversion of returned data into Python objects. All the typecasters are automatically registered, except [`UNICODE`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.UNICODE "psycopg2.extensions.UNICODE") and [`UNICODEARRAY`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.UNICODEARRAY "psycopg2.extensions.UNICODEARRAY"): you can register them using [`register_type()`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.register_type "psycopg2.extensions.register_type") in order to receive Unicode objects instead of strings from the database. See [Unicode handling](https://www.psycopg.org/docs/usage.html#unicode-handling) for details.

psycopg2.extensions.BOOLEAN[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.BOOLEAN "Link to this definition")psycopg2.extensions.BYTES[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.BYTES "Link to this definition")psycopg2.extensions.DATE[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.DATE "Link to this definition")psycopg2.extensions.DECIMAL[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.DECIMAL "Link to this definition")psycopg2.extensions.FLOAT[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.FLOAT "Link to this definition")psycopg2.extensions.INTEGER[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.INTEGER "Link to this definition")psycopg2.extensions.INTERVAL[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.INTERVAL "Link to this definition")psycopg2.extensions.LONGINTEGER[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.LONGINTEGER "Link to this definition")psycopg2.extensions.TIME[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.TIME "Link to this definition")psycopg2.extensions.UNICODE[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.UNICODE "Link to this definition")
Typecasters for basic types. Note that a few other ones ([`BINARY`](https://www.psycopg.org/docs/module.html#psycopg2.BINARY "psycopg2.BINARY"), [`DATETIME`](https://www.psycopg.org/docs/module.html#psycopg2.DATETIME "psycopg2.DATETIME"), [`NUMBER`](https://www.psycopg.org/docs/module.html#psycopg2.NUMBER "psycopg2.NUMBER"), [`ROWID`](https://www.psycopg.org/docs/module.html#psycopg2.ROWID "psycopg2.ROWID"), [`STRING`](https://www.psycopg.org/docs/module.html#psycopg2.STRING "psycopg2.STRING")) are exposed by the [`psycopg2`](https://www.psycopg.org/docs/module.html#module-psycopg2 "psycopg2") module for [DB API 2.0](https://www.python.org/dev/peps/pep-0249/) compliance.

psycopg2.extensions.BINARYARRAY[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.BINARYARRAY "Link to this definition")psycopg2.extensions.BOOLEANARRAY[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.BOOLEANARRAY "Link to this definition")psycopg2.extensions.BYTESARRAY[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.BYTESARRAY "Link to this definition")psycopg2.extensions.DATEARRAY[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.DATEARRAY "Link to this definition")psycopg2.extensions.DATETIMEARRAY[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.DATETIMEARRAY "Link to this definition")psycopg2.extensions.DECIMALARRAY[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.DECIMALARRAY "Link to this definition")psycopg2.extensions.FLOATARRAY[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.FLOATARRAY "Link to this definition")psycopg2.extensions.INTEGERARRAY[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.INTEGERARRAY "Link to this definition")psycopg2.extensions.INTERVALARRAY[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.INTERVALARRAY "Link to this definition")psycopg2.extensions.LONGINTEGERARRAY[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.LONGINTEGERARRAY "Link to this definition")psycopg2.extensions.ROWIDARRAY[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ROWIDARRAY "Link to this definition")psycopg2.extensions.STRINGARRAY[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.STRINGARRAY "Link to this definition")psycopg2.extensions.TIMEARRAY[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.TIMEARRAY "Link to this definition")psycopg2.extensions.UNICODEARRAY[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.UNICODEARRAY "Link to this definition")
Typecasters to convert arrays of sql types into Python lists.

psycopg2.extensions.PYDATE[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.PYDATE "Link to this definition")psycopg2.extensions.PYDATETIME[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.PYDATETIME "Link to this definition")psycopg2.extensions.PYDATETIMETZ[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.PYDATETIMETZ "Link to this definition")psycopg2.extensions.PYINTERVAL[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.PYINTERVAL "Link to this definition")psycopg2.extensions.PYTIME[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.PYTIME "Link to this definition")psycopg2.extensions.PYDATEARRAY[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.PYDATEARRAY "Link to this definition")psycopg2.extensions.PYDATETIMEARRAY[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.PYDATETIMEARRAY "Link to this definition")psycopg2.extensions.PYDATETIMETZARRAY[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.PYDATETIMETZARRAY "Link to this definition")psycopg2.extensions.PYINTERVALARRAY[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.PYINTERVALARRAY "Link to this definition")psycopg2.extensions.PYTIMEARRAY[¶](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.PYTIMEARRAY "Link to this definition")
Typecasters to convert time-related data types to Python `datetime` objects.

Changed in version 2.2: previously the [`DECIMAL`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.DECIMAL "psycopg2.extensions.DECIMAL") typecaster and the specific time-related typecasters (`PY*` and `MX*`) were not exposed by the `extensions` module. In older versions they can be imported from the implementation module `psycopg2._psycopg`.

Added in version 2.7.2: the `*DATETIMETZ*` objects.

Added in version 2.8: the `BYTES` and [`BYTESARRAY`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.BYTESARRAY "psycopg2.extensions.BYTESARRAY") objects.
