# Source: https://www.psycopg.org/docs/connection.html

Title: The connection class — Psycopg 2.9.11 documentation

URL Source: https://www.psycopg.org/docs/connection.html

Markdown Content:
_class_ connection[¶](https://www.psycopg.org/docs/connection.html#connection "Link to this definition")
Handles the connection to a PostgreSQL database instance. It encapsulates a database session.

Connections are created using the factory function [`connect()`](https://www.psycopg.org/docs/module.html#psycopg2.connect "psycopg2.connect").

Connections are thread safe and can be shared among many threads. See [Thread and process safety](https://www.psycopg.org/docs/usage.html#thread-safety) for details.

Connections can be used as context managers. Note that a context wraps a transaction: if the context exits with success the transaction is committed, if it exits with an exception the transaction is rolled back. Note that the connection is not closed by the context and it can be used for several contexts.

conn = psycopg2.connect(DSN)

with conn:
    with conn.cursor() as curs:
        curs.execute(SQL1)

with conn:
    with conn.cursor() as curs:
        curs.execute(SQL2)

# leaving contexts doesn't close the connection

conn.close()

cursor(_name=None_, _cursor\_factory=None_, _scrollable=None_, _withhold=False_)[¶](https://www.psycopg.org/docs/connection.html#connection.cursor "Link to this definition")
Return a new [`cursor`](https://www.psycopg.org/docs/cursor.html#cursor "cursor") object using the connection.

If _name_ is specified, the returned cursor will be a [server side cursor](https://www.psycopg.org/docs/usage.html#server-side-cursors) (also known as _named cursor_). Otherwise it will be a regular _client side_ cursor. By default a named cursor is declared without `SCROLL` option and `WITHOUT HOLD`: set the argument or property [`scrollable`](https://www.psycopg.org/docs/cursor.html#cursor.scrollable "cursor.scrollable") to `True`/`False` and or [`withhold`](https://www.psycopg.org/docs/cursor.html#cursor.withhold "cursor.withhold") to `True` to change the declaration.

The name can be a string not valid as a PostgreSQL identifier: for example it may start with a digit and contain non-alphanumeric characters and quotes.

Changed in version 2.4: previously only valid PostgreSQL identifiers were accepted as cursor name.

The _cursor\_factory_ argument can be used to create non-standard cursors. The class returned must be a subclass of [`psycopg2.extensions.cursor`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.cursor "psycopg2.extensions.cursor"). See [Connection and cursor factories](https://www.psycopg.org/docs/advanced.html#subclassing-cursor) for details. A default factory for the connection can also be specified using the [`cursor_factory`](https://www.psycopg.org/docs/connection.html#connection.cursor_factory "connection.cursor_factory") attribute.

Changed in version 2.4.3: added the _withhold_ argument.

Changed in version 2.5: added the _scrollable_ argument.

DB API extension

All the function arguments are Psycopg extensions to the DB API 2.0.

commit()[¶](https://www.psycopg.org/docs/connection.html#connection.commit "Link to this definition")
Commit any pending transaction to the database.

By default, Psycopg opens a transaction before executing the first command: if `commit()` is not called, the effect of any data manipulation will be lost.

The connection can be also set in “autocommit” mode: no transaction is automatically open, commands have immediate effect. See [Transactions control](https://www.psycopg.org/docs/usage.html#transactions-control) for details.

Changed in version 2.5: if the connection is used in a `with` statement, the method is automatically called if no exception is raised in the `with` block.

rollback()[¶](https://www.psycopg.org/docs/connection.html#connection.rollback "Link to this definition")
Roll back to the start of any pending transaction. Closing a connection without committing the changes first will cause an implicit rollback to be performed.

Changed in version 2.5: if the connection is used in a `with` statement, the method is automatically called if an exception is raised in the `with` block.

close()[¶](https://www.psycopg.org/docs/connection.html#connection.close "Link to this definition")
Close the connection now (rather than whenever `del` is executed). The connection will be unusable from this point forward; an [`InterfaceError`](https://www.psycopg.org/docs/module.html#psycopg2.InterfaceError "psycopg2.InterfaceError") will be raised if any operation is attempted with the connection. The same applies to all cursor objects trying to use the connection. Note that closing a connection without committing the changes first will cause any pending change to be discarded as if a `ROLLBACK` was performed (unless a different isolation level has been selected: see [`set_isolation_level()`](https://www.psycopg.org/docs/connection.html#connection.set_isolation_level "connection.set_isolation_level")).

Changed in version 2.2: previously an explicit `ROLLBACK` was issued by Psycopg on `close()`. The command could have been sent to the backend at an inappropriate time, so Psycopg currently relies on the backend to implicitly discard uncommitted changes. Some middleware are known to behave incorrectly though when the connection is closed during a transaction (when [`status`](https://www.psycopg.org/docs/connection.html#connection.status "connection.status") is [`STATUS_IN_TRANSACTION`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.STATUS_IN_TRANSACTION "psycopg2.extensions.STATUS_IN_TRANSACTION")), e.g. [PgBouncer](http://www.pgbouncer.org/) reports an `unclean server` and discards the connection. To avoid this problem you can ensure to terminate the transaction with a [`commit()`](https://www.psycopg.org/docs/connection.html#connection.commit "connection.commit")/[`rollback()`](https://www.psycopg.org/docs/connection.html#connection.rollback "connection.rollback") before closing.

Exceptions as connection class attributes

The `connection` also exposes as attributes the same exceptions available in the [`psycopg2`](https://www.psycopg.org/docs/module.html#module-psycopg2 "psycopg2") module. See [Exceptions](https://www.psycopg.org/docs/module.html#dbapi-exceptions).

Two-phase commit support methods

Added in version 2.3.

Note that PostgreSQL supports two-phase commit since release 8.1: these methods raise [`NotSupportedError`](https://www.psycopg.org/docs/module.html#psycopg2.NotSupportedError "psycopg2.NotSupportedError") if used with an older version server.

xid(_format\_id_, _gtrid_, _bqual_)[¶](https://www.psycopg.org/docs/connection.html#connection.xid "Link to this definition")
Returns a [`Xid`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Xid "psycopg2.extensions.Xid") instance to be passed to the `tpc_*()` methods of this connection. The argument types and constraints are explained in [Two-Phase Commit protocol support](https://www.psycopg.org/docs/usage.html#tpc).

The values passed to the method will be available on the returned object as the members [`format_id`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Xid.format_id "psycopg2.extensions.Xid.format_id"), [`gtrid`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Xid.gtrid "psycopg2.extensions.Xid.gtrid"), [`bqual`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Xid.bqual "psycopg2.extensions.Xid.bqual"). The object also allows accessing to these members and unpacking as a 3-items tuple.

tpc_begin(_xid_)[¶](https://www.psycopg.org/docs/connection.html#connection.tpc_begin "Link to this definition")
Begins a TPC transaction with the given transaction ID _xid_.

This method should be called outside of a transaction (i.e. nothing may have executed since the last [`commit()`](https://www.psycopg.org/docs/connection.html#connection.commit "connection.commit") or [`rollback()`](https://www.psycopg.org/docs/connection.html#connection.rollback "connection.rollback") and [`connection.status`](https://www.psycopg.org/docs/connection.html#connection.status "connection.status") is [`STATUS_READY`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.STATUS_READY "psycopg2.extensions.STATUS_READY")).

Furthermore, it is an error to call `commit()` or `rollback()` within the TPC transaction: in this case a [`ProgrammingError`](https://www.psycopg.org/docs/module.html#psycopg2.ProgrammingError "psycopg2.ProgrammingError") is raised.

The _xid_ may be either an object returned by the [`xid()`](https://www.psycopg.org/docs/connection.html#connection.xid "connection.xid") method or a plain string: the latter allows to create a transaction using the provided string as PostgreSQL transaction id. See also [`tpc_recover()`](https://www.psycopg.org/docs/connection.html#connection.tpc_recover "connection.tpc_recover").

tpc_prepare()[¶](https://www.psycopg.org/docs/connection.html#connection.tpc_prepare "Link to this definition")
Performs the first phase of a transaction started with [`tpc_begin()`](https://www.psycopg.org/docs/connection.html#connection.tpc_begin "connection.tpc_begin"). A [`ProgrammingError`](https://www.psycopg.org/docs/module.html#psycopg2.ProgrammingError "psycopg2.ProgrammingError") is raised if this method is used outside of a TPC transaction.

After calling `tpc_prepare()`, no statements can be executed until [`tpc_commit()`](https://www.psycopg.org/docs/connection.html#connection.tpc_commit "connection.tpc_commit") or [`tpc_rollback()`](https://www.psycopg.org/docs/connection.html#connection.tpc_rollback "connection.tpc_rollback") will be called. The [`reset()`](https://www.psycopg.org/docs/connection.html#connection.reset "connection.reset") method can be used to restore the status of the connection to [`STATUS_READY`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.STATUS_READY "psycopg2.extensions.STATUS_READY"): the transaction will remain prepared in the database and will be possible to finish it with `tpc_commit(xid)` and `tpc_rollback(xid)`.

tpc_commit([_xid_])[¶](https://www.psycopg.org/docs/connection.html#connection.tpc_commit "Link to this definition")
When called with no arguments, `tpc_commit()` commits a TPC transaction previously prepared with [`tpc_prepare()`](https://www.psycopg.org/docs/connection.html#connection.tpc_prepare "connection.tpc_prepare").

If `tpc_commit()` is called prior to `tpc_prepare()`, a single phase commit is performed. A transaction manager may choose to do this if only a single resource is participating in the global transaction.

When called with a transaction ID _xid_, the database commits the given transaction. If an invalid transaction ID is provided, a [`ProgrammingError`](https://www.psycopg.org/docs/module.html#psycopg2.ProgrammingError "psycopg2.ProgrammingError") will be raised. This form should be called outside of a transaction, and is intended for use in recovery.

On return, the TPC transaction is ended.

tpc_rollback([_xid_])[¶](https://www.psycopg.org/docs/connection.html#connection.tpc_rollback "Link to this definition")
When called with no arguments, `tpc_rollback()` rolls back a TPC transaction. It may be called before or after [`tpc_prepare()`](https://www.psycopg.org/docs/connection.html#connection.tpc_prepare "connection.tpc_prepare").

When called with a transaction ID _xid_, it rolls back the given transaction. If an invalid transaction ID is provided, a [`ProgrammingError`](https://www.psycopg.org/docs/module.html#psycopg2.ProgrammingError "psycopg2.ProgrammingError") is raised. This form should be called outside of a transaction, and is intended for use in recovery.

On return, the TPC transaction is ended.

tpc_recover()[¶](https://www.psycopg.org/docs/connection.html#connection.tpc_recover "Link to this definition")
Returns a list of [`Xid`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Xid "psycopg2.extensions.Xid") representing pending transactions, suitable for use with [`tpc_commit()`](https://www.psycopg.org/docs/connection.html#connection.tpc_commit "connection.tpc_commit") or [`tpc_rollback()`](https://www.psycopg.org/docs/connection.html#connection.tpc_rollback "connection.tpc_rollback").

If a transaction was not initiated by Psycopg, the returned Xids will have attributes [`format_id`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Xid.format_id "psycopg2.extensions.Xid.format_id") and [`bqual`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Xid.bqual "psycopg2.extensions.Xid.bqual") set to `None` and the [`gtrid`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Xid.gtrid "psycopg2.extensions.Xid.gtrid") set to the PostgreSQL transaction ID: such Xids are still usable for recovery. Psycopg uses the same algorithm of the [PostgreSQL JDBC driver](https://jdbc.postgresql.org/) to encode a XA triple in a string, so transactions initiated by a program using such driver should be unpacked correctly.

Xids returned by `tpc_recover()` also have extra attributes [`prepared`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Xid.prepared "psycopg2.extensions.Xid.prepared"), [`owner`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Xid.owner "psycopg2.extensions.Xid.owner"), [`database`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Xid.database "psycopg2.extensions.Xid.database") populated with the values read from the server.

DB API extension

The above methods are the only ones defined by the DB API 2.0 protocol. The Psycopg connection objects exports the following additional methods and attributes.

closed[¶](https://www.psycopg.org/docs/connection.html#connection.closed "Link to this definition")
Read-only integer attribute: 0 if the connection is open, nonzero if it is closed or broken.

cancel()[¶](https://www.psycopg.org/docs/connection.html#connection.cancel "Link to this definition")
Cancel the current database operation.

The method interrupts the processing of the current operation. If no query is being executed, it does nothing. You can call this function from a different thread than the one currently executing a database operation, for instance if you want to cancel a long running query if a button is pushed in the UI. Interrupting query execution will cause the cancelled method to raise a [`QueryCanceledError`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.QueryCanceledError "psycopg2.extensions.QueryCanceledError"). Note that the termination of the query is not guaranteed to succeed: see the documentation for [`PQcancel()`](https://www.postgresql.org/docs/current/static/libpq-cancel.html#LIBPQ-PQCANCEL).

Added in version 2.3.

reset()[¶](https://www.psycopg.org/docs/connection.html#connection.reset "Link to this definition")
Reset the connection to the default.

The method rolls back an eventual pending transaction and executes the PostgreSQL [`RESET`](https://www.postgresql.org/docs/current/static/sql-reset.html) and [`SET SESSION AUTHORIZATION`](https://www.postgresql.org/docs/current/static/sql-set-session-authorization.html) to revert the session to the default values. A two-phase commit transaction prepared using [`tpc_prepare()`](https://www.psycopg.org/docs/connection.html#connection.tpc_prepare "connection.tpc_prepare") will remain in the database available for recover.

Added in version 2.0.12.

dsn[¶](https://www.psycopg.org/docs/connection.html#connection.dsn "Link to this definition")
Read-only string containing the connection string used by the connection.

If a password was specified in the connection string it will be obscured.

Transaction control methods and attributes.

set_session(_isolation\_level=None_, _readonly=None_, _deferrable=None_, _autocommit=None_)[¶](https://www.psycopg.org/docs/connection.html#connection.set_session "Link to this definition")
Set one or more parameters for the next transactions or statements in the current session.

Parameters:

* **isolation_level** – set the [isolation level](https://www.postgresql.org/docs/current/static/transaction-iso.html) for the next transactions/statements. The value can be one of the literal values `READ UNCOMMITTED`, `READ COMMITTED`,

```
REPEATABLE
READ
```

, `SERIALIZABLE` or the equivalent [constant](https://www.psycopg.org/docs/extensions.html#isolation-level-constants) defined in the [`extensions`](https://www.psycopg.org/docs/extensions.html#module-psycopg2.extensions "psycopg2.extensions") module.

* **readonly** – if `True`, set the connection to read only; read/write if `False`.

* **deferrable** – if `True`, set the connection to deferrable; non deferrable if `False`. Only available from PostgreSQL 9.1.

* **autocommit** – switch the connection to autocommit mode: not a PostgreSQL session setting but an alias for setting the [`autocommit`](https://www.psycopg.org/docs/connection.html#connection.autocommit "connection.autocommit") attribute.

Arguments set to `None` (the default for all) will not be changed. The parameters _isolation\_level_, _readonly_ and _deferrable_ also accept the string `DEFAULT` as a value: the effect is to reset the parameter to the server default. Defaults are defined by the server configuration: see values for [`default_transaction_isolation`](https://www.postgresql.org/docs/current/static/runtime-config-client.html#GUC-DEFAULT-TRANSACTION-ISOLATION), [`default_transaction_read_only`](https://www.postgresql.org/docs/current/static/runtime-config-client.html#GUC-DEFAULT-TRANSACTION-READ-ONLY), [`default_transaction_deferrable`](https://www.postgresql.org/docs/current/static/runtime-config-client.html#GUC-DEFAULT-TRANSACTION-DEFERRABLE).

The function must be invoked with no transaction in progress.

See also

[`SET TRANSACTION`](https://www.postgresql.org/docs/current/static/sql-set-transaction.html) for further details about the behaviour of the transaction parameters in the server.

Added in version 2.4.2.

Changed in version 2.7: Before this version, the function would have set `default_transaction_*` attribute in the current session; this implementation has the problem of not playing well with external connection pooling working at transaction level and not resetting the state of the session: changing the default transaction would pollute the connections in the pool and create problems to other applications using the same pool.

Starting from 2.7, if the connection is not autocommit, the transaction characteristics are issued together with `BEGIN` and will leave the `default_transaction_*` settings untouched. For example:

conn.set_session(readonly=True)

will not change `default_transaction_read_only`, but following transaction will start with a `BEGIN READ ONLY`. Conversely, using:

conn.set_session(readonly=True, autocommit=True)

will set `default_transaction_read_only` to `on` and rely on the server to apply the read only state to whatever transaction, implicit or explicit, is executed in the connection.

autocommit[¶](https://www.psycopg.org/docs/connection.html#connection.autocommit "Link to this definition")
Read/write attribute: if `True`, no transaction is handled by the driver and every statement sent to the backend has immediate effect; if `False` a new transaction is started at the first command execution: the methods [`commit()`](https://www.psycopg.org/docs/connection.html#connection.commit "connection.commit") or [`rollback()`](https://www.psycopg.org/docs/connection.html#connection.rollback "connection.rollback") must be manually invoked to terminate the transaction.

The autocommit mode is useful to execute commands requiring to be run outside a transaction, such as `CREATE DATABASE` or `VACUUM`.

The default is `False` (manual commit) as per DBAPI specification.

Warning

By default, any query execution, including a simple `SELECT` will start a transaction: for long-running programs, if no further action is taken, the session will remain “idle in transaction”, an undesirable condition for several reasons (locks are held by the session, tables bloat…). For long lived scripts, either ensure to terminate a transaction as soon as possible or use an autocommit connection.

Added in version 2.4.2.

isolation_level[¶](https://www.psycopg.org/docs/connection.html#connection.isolation_level "Link to this definition")
Return or set the [transaction isolation level](https://www.postgresql.org/docs/current/static/transaction-iso.html) for the current session. The value is one of the [Isolation level constants](https://www.psycopg.org/docs/extensions.html#isolation-level-constants) defined in the [`psycopg2.extensions`](https://www.psycopg.org/docs/extensions.html#module-psycopg2.extensions "psycopg2.extensions") module. On set it is also possible to use one of the literal values `READ UNCOMMITTED`,

```
READ
COMMITTED
```

, `REPEATABLE READ`, `SERIALIZABLE`, `DEFAULT`.

Changed in version 2.7: the property is writable.

Changed in version 2.7: the default value for `isolation_level` is [`ISOLATION_LEVEL_DEFAULT`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ISOLATION_LEVEL_DEFAULT "psycopg2.extensions.ISOLATION_LEVEL_DEFAULT"); previously the property would have queried the server and returned the real value applied. To know this value you can run a query such as

```
show
transaction_isolation
```

. Usually the default value is

```
READ
COMMITTED
```

, but this may be changed in the server configuration.

This value is now entirely separate from the [`autocommit`](https://www.psycopg.org/docs/connection.html#connection.autocommit "connection.autocommit") property: in previous version, if `autocommit` was set to `True` this property would have returned [`ISOLATION_LEVEL_AUTOCOMMIT`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT "psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT"); it will now return the server isolation level.

readonly[¶](https://www.psycopg.org/docs/connection.html#connection.readonly "Link to this definition")
Return or set the read-only status for the current session. Available values are `True` (new transactions will be in read-only mode), `False` (new transactions will be writable), `None` (use the default configured for the server by `default_transaction_read_only`).

Added in version 2.7.

deferrable[¶](https://www.psycopg.org/docs/connection.html#connection.deferrable "Link to this definition")
Return or set the [deferrable status](https://www.postgresql.org/docs/current/static/sql-set-transaction.html) for the current session. Available values are `True` (new transactions will be in deferrable mode), `False` (new transactions will be in non deferrable mode), `None` (use the default configured for the server by `default_transaction_deferrable`).

Added in version 2.7.

set_isolation_level(_level_)[¶](https://www.psycopg.org/docs/connection.html#connection.set_isolation_level "Link to this definition")

Note

This is a legacy method mixing `isolation_level` and `autocommit`. Using the respective properties is a better option.

Set the [transaction isolation level](https://www.postgresql.org/docs/current/static/transaction-iso.html) for the current session. The level defines the different phenomena that can happen in the database between concurrent transactions.

The value set is an integer: symbolic constants are defined in the module [`psycopg2.extensions`](https://www.psycopg.org/docs/extensions.html#module-psycopg2.extensions "psycopg2.extensions"): see [Isolation level constants](https://www.psycopg.org/docs/extensions.html#isolation-level-constants) for the available values.

The default level is [`ISOLATION_LEVEL_DEFAULT`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ISOLATION_LEVEL_DEFAULT "psycopg2.extensions.ISOLATION_LEVEL_DEFAULT"): at this level a transaction is automatically started the first time a database command is executed. If you want an _autocommit_ mode, switch to [`ISOLATION_LEVEL_AUTOCOMMIT`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT "psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT") before executing any command:

>>> conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

See also [Transactions control](https://www.psycopg.org/docs/usage.html#transactions-control).

encoding[¶](https://www.psycopg.org/docs/connection.html#connection.encoding "Link to this definition")set_client_encoding(_enc_)[¶](https://www.psycopg.org/docs/connection.html#connection.set_client_encoding "Link to this definition")
Read or set the client encoding for the current session. The default is the encoding defined by the database. It should be one of the [characters set supported by PostgreSQL](https://www.postgresql.org/docs/current/static/multibyte.html)

notices[¶](https://www.psycopg.org/docs/connection.html#connection.notices "Link to this definition")
A list containing all the database messages sent to the client during the session.

>>> cur.execute("CREATE TABLE foo (id serial PRIMARY KEY);")
>>> pprint(conn.notices)
['NOTICE: CREATE TABLE / PRIMARY KEY will create implicit index "foo_pkey" for table "foo"\n',
 'NOTICE: CREATE TABLE will create implicit sequence "foo_id_seq" for serial column "foo.id"\n']

Changed in version 2.7: The `notices` attribute is writable: the user may replace it with any Python object exposing an `append()` method. If appending raises an exception the notice is silently dropped.

To avoid a leak in case excessive notices are generated, only the last 50 messages are kept. This check is only in place if the `notices` attribute is a list: if any other object is used it will be up to the user to guard from leakage.

You can configure what messages to receive using [PostgreSQL logging configuration parameters](https://www.postgresql.org/docs/current/static/runtime-config-logging.html) such as `log_statement`, `client_min_messages`, `log_min_duration_statement` etc.

notifies[¶](https://www.psycopg.org/docs/connection.html#connection.notifies "Link to this definition")
List of [`Notify`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Notify "psycopg2.extensions.Notify") objects containing asynchronous notifications received by the session.

For other details see [Asynchronous notifications](https://www.psycopg.org/docs/advanced.html#async-notify).

Changed in version 2.3: Notifications are instances of the `Notify` object. Previously the list was composed by 2 items tuples `(pid,channel)` and the payload was not accessible. To keep backward compatibility, `Notify` objects can still be accessed as 2 items tuples.

Changed in version 2.7: The `notifies` attribute is writable: the user may replace it with any Python object exposing an `append()` method. If appending raises an exception the notification is silently dropped.

cursor_factory[¶](https://www.psycopg.org/docs/connection.html#connection.cursor_factory "Link to this definition")
The default cursor factory used by [`cursor()`](https://www.psycopg.org/docs/connection.html#connection.cursor "connection.cursor") if the parameter is not specified.

Added in version 2.5.

info[¶](https://www.psycopg.org/docs/connection.html#connection.info "Link to this definition")
A [`ConnectionInfo`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ConnectionInfo "psycopg2.extensions.ConnectionInfo") object exposing information about the native libpq connection.

Added in version 2.8.

status[¶](https://www.psycopg.org/docs/connection.html#connection.status "Link to this definition")
A read-only integer representing the status of the connection. Symbolic constants for the values are defined in the module [`psycopg2.extensions`](https://www.psycopg.org/docs/extensions.html#module-psycopg2.extensions "psycopg2.extensions"): see [Connection status constants](https://www.psycopg.org/docs/extensions.html#connection-status-constants) for the available values.

The status is undefined for [`closed`](https://www.psycopg.org/docs/connection.html#connection.closed "connection.closed") connections.

lobject([_oid_[, _mode_[, _new\_oid_[, _new\_file_[, _lobject\_factory_]]]]])[¶](https://www.psycopg.org/docs/connection.html#connection.lobject "Link to this definition")
Return a new database large object as a [`lobject`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.lobject "psycopg2.extensions.lobject") instance.

See [Access to PostgreSQL large objects](https://www.psycopg.org/docs/usage.html#large-objects) for an overview.

Parameters:

* **oid** – The OID of the object to read or write. 0 to create a new large object and and have its OID assigned automatically.

* **mode** – Access mode to the object, see below.

* **new_oid** – Create a new object using the specified OID. The function raises [`OperationalError`](https://www.psycopg.org/docs/module.html#psycopg2.OperationalError "psycopg2.OperationalError") if the OID is already in use. Default is 0, meaning assign a new one automatically.

* **new_file** – The name of a file to be imported in the database (using the [`lo_import()`](https://www.postgresql.org/docs/current/static/lo-interfaces.html#LO-IMPORT) function)

* **lobject_factory** – Subclass of [`lobject`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.lobject "psycopg2.extensions.lobject") to be instantiated.

Available values for _mode_ are:

| _mode_ | meaning |
| --- | --- |
| `r` | Open for read only |
| `w` | Open for write only |
| `rw` | Open for read/write |
| `n` | Don’t open the file |
| `b` | Don’t decode read data (return data as `str` in Python 2 or `bytes` in Python 3) |
| `t` | Decode read data according to [`connection.encoding`](https://www.psycopg.org/docs/connection.html#connection.encoding "connection.encoding") (return data as `unicode` in Python 2 or `str` in Python 3) |

`b` and `t` can be specified together with a read/write mode. If neither `b` nor `t` is specified, the default is `b` in Python 2 and `t` in Python 3.

Added in version 2.0.8.

Changed in version 2.4: added `b` and `t` mode and unicode support.

Methods related to asynchronous support

Added in version 2.2.

async[¶](https://www.psycopg.org/docs/connection.html#connection.async "Link to this definition")async_[¶](https://www.psycopg.org/docs/connection.html#connection.async_ "Link to this definition")
Read only attribute: 1 if the connection is asynchronous, 0 otherwise.

Changed in version 2.7: added the `async_` alias for Python versions where `async` is a keyword.

poll()[¶](https://www.psycopg.org/docs/connection.html#connection.poll "Link to this definition")
Used during an asynchronous connection attempt, or when a cursor is executing a query on an asynchronous connection, make communication proceed if it wouldn’t block.

Return one of the constants defined in [Poll constants](https://www.psycopg.org/docs/extensions.html#poll-constants). If it returns [`POLL_OK`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.POLL_OK "psycopg2.extensions.POLL_OK") then the connection has been established or the query results are available on the client. Otherwise wait until the file descriptor returned by [`fileno()`](https://www.psycopg.org/docs/connection.html#connection.fileno "connection.fileno") is ready to read or to write, as explained in [Asynchronous support](https://www.psycopg.org/docs/advanced.html#async-support). [`poll()`](https://www.psycopg.org/docs/connection.html#connection.poll "connection.poll") should be also used by the function installed by [`set_wait_callback()`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.set_wait_callback "psycopg2.extensions.set_wait_callback") as explained in [Support for coroutine libraries](https://www.psycopg.org/docs/advanced.html#green-support).

[`poll()`](https://www.psycopg.org/docs/connection.html#connection.poll "connection.poll") is also used to receive asynchronous notifications from the database: see [Asynchronous notifications](https://www.psycopg.org/docs/advanced.html#async-notify) from further details.

fileno()[¶](https://www.psycopg.org/docs/connection.html#connection.fileno "Link to this definition")
Return the file descriptor underlying the connection: useful to read its status during asynchronous communication.

isexecuting()[¶](https://www.psycopg.org/docs/connection.html#connection.isexecuting "Link to this definition")
Return `True` if the connection is executing an asynchronous operation.

Interoperation with other C API modules

pgconn_ptr[¶](https://www.psycopg.org/docs/connection.html#connection.pgconn_ptr "Link to this definition")
Return the internal `PGconn*` as integer. Useful to pass the libpq raw connection structure to C functions, e.g. via [`ctypes`](https://docs.python.org/3/library/ctypes.html#module-ctypes "(in Python v3.14)"):

>>> import ctypes
>>> import ctypes.util
>>> libpq = ctypes.pydll.LoadLibrary(ctypes.util.find_library('pq'))
>>> libpq.PQserverVersion.argtypes = [ctypes.c_void_p]
>>> libpq.PQserverVersion.restype = ctypes.c_int
>>> libpq.PQserverVersion(conn.pgconn_ptr)
90611

Added in version 2.8.

get_native_connection()[¶](https://www.psycopg.org/docs/connection.html#connection.get_native_connection "Link to this definition")
Return the internal `PGconn*` wrapped in a PyCapsule object. This is only useful for passing the `libpq` raw connection associated to this connection object to other C-level modules that may have a use for it.

Added in version 2.8.

informative methods of the native connection

Note

These methods are better accessed using the [`info`](https://www.psycopg.org/docs/connection.html#connection.info "connection.info") attributes and may be dropped in future versions.

get_transaction_status()[¶](https://www.psycopg.org/docs/connection.html#connection.get_transaction_status "Link to this definition")
Also available as [`info`](https://www.psycopg.org/docs/connection.html#connection.info "connection.info")`.`[`transaction_status`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ConnectionInfo.transaction_status "psycopg2.extensions.ConnectionInfo.transaction_status").

Return the current session transaction status as an integer. Symbolic constants for the values are defined in the module [`psycopg2.extensions`](https://www.psycopg.org/docs/extensions.html#module-psycopg2.extensions "psycopg2.extensions"): see [Transaction status constants](https://www.psycopg.org/docs/extensions.html#transaction-status-constants) for the available values.

protocol_version[¶](https://www.psycopg.org/docs/connection.html#connection.protocol_version "Link to this definition")
Also available as [`info`](https://www.psycopg.org/docs/connection.html#connection.info "connection.info")`.`[`protocol_version`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ConnectionInfo.protocol_version "psycopg2.extensions.ConnectionInfo.protocol_version").

A read-only integer representing frontend/backend protocol being used. Currently Psycopg supports only protocol 3, which allows connection to PostgreSQL server from version 7.4. Psycopg versions previous than 2.3 support both protocols 2 and 3.

Added in version 2.0.12.

server_version[¶](https://www.psycopg.org/docs/connection.html#connection.server_version "Link to this definition")
Also available as [`info`](https://www.psycopg.org/docs/connection.html#connection.info "connection.info")`.`[`server_version`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ConnectionInfo.server_version "psycopg2.extensions.ConnectionInfo.server_version").

A read-only integer representing the backend version.

The number is formed by converting the major, minor, and revision numbers into two-decimal-digit numbers and appending them together. For example, version 8.1.5 will be returned as `80105`.

Added in version 2.0.12.

get_backend_pid()[¶](https://www.psycopg.org/docs/connection.html#connection.get_backend_pid "Link to this definition")
Also available as [`info`](https://www.psycopg.org/docs/connection.html#connection.info "connection.info")`.`[`backend_pid`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ConnectionInfo.backend_pid "psycopg2.extensions.ConnectionInfo.backend_pid").

Returns the process ID (PID) of the backend server process _you connected to_. Note that if you use a connection pool service such as [PgBouncer](http://www.pgbouncer.org/) this value will not be updated if your connection is switched to a different backend.

Note that the PID belongs to a process executing on the database server host, not the local host!

Added in version 2.0.8.

get_parameter_status(_parameter_)[¶](https://www.psycopg.org/docs/connection.html#connection.get_parameter_status "Link to this definition")
Also available as [`info`](https://www.psycopg.org/docs/connection.html#connection.info "connection.info")`.`[`parameter_status()`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ConnectionInfo.parameter_status "psycopg2.extensions.ConnectionInfo.parameter_status").

Look up a current parameter setting of the server.

Potential values for `parameter` are: `server_version`, `server_encoding`, `client_encoding`, `is_superuser`, `session_authorization`, `DateStyle`, `TimeZone`, `integer_datetimes`, and `standard_conforming_strings`.

If server did not report requested parameter, return `None`.

Added in version 2.0.12.

get_dsn_parameters()[¶](https://www.psycopg.org/docs/connection.html#connection.get_dsn_parameters "Link to this definition")
Also available as [`info`](https://www.psycopg.org/docs/connection.html#connection.info "connection.info")`.`[`dsn_parameters`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ConnectionInfo.dsn_parameters "psycopg2.extensions.ConnectionInfo.dsn_parameters").

Get the effective dsn parameters for the connection as a dictionary.

The _password_ parameter is removed from the result.

Example:

>>> conn.get_dsn_parameters()
{'dbname': 'test', 'user': 'postgres', 'port': '5432', 'sslmode': 'prefer'}

Requires libpq >= 9.3.

Added in version 2.7.
