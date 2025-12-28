# Source: https://docs.searxng.org/src/searx.sqlitedb.html

[]

# SQLite DB[¶](#sqlite-db "Link to this heading")

Implementations to make access to SQLite databases a little more convenient.

[[`SQLiteAppl`]](#searx.sqlitedb.SQLiteAppl "searx.sqlitedb.SQLiteAppl")

:   Abstract class with which DB applications can be implemented.

[[`SQLiteProperties`]](#searx.sqlitedb.SQLiteProperties "searx.sqlitedb.SQLiteProperties"):

:   Class to manage properties stored in a database.

Examplarical implementations based on [[`SQLiteAppl`]](#searx.sqlitedb.SQLiteAppl "searx.sqlitedb.SQLiteAppl"):

[[`searx.cache.ExpireCacheSQLite`]](searx.cache.html#searx.cache.ExpireCacheSQLite "searx.cache.ExpireCacheSQLite") :

:   Cache that manages key/value pairs in a SQLite DB, in which the key/value pairs are deleted after an "expire" time. This type of cache is used, for example, for the engines, see [[`searx.enginelib.EngineCache`]](../dev/engines/enginelib.html#searx.enginelib.EngineCache "searx.enginelib.EngineCache").

[[`searx.favicons.cache.FaviconCacheSQLite`]](searx.favicons.html#searx.favicons.cache.FaviconCacheSQLite "searx.favicons.cache.FaviconCacheSQLite") :

:   Favicon cache that manages the favicon BLOBs in a SQLite DB.

------------------------------------------------------------------------

*[[class]][ ]*[[searx.sqlitedb.]][[DBSession]][(]*[[app]][[:]][ ][[[SQLiteAppl]](#searx.sqlitedb.SQLiteAppl "searx.sqlitedb.SQLiteAppl")]*[)][[[\[source\]]]](../_modules/searx/sqlitedb.html#DBSession)[¶](#searx.sqlitedb.DBSession "Link to this definition")

:   A *thead-local* DB session

    *[[classmethod]][ ]*[[get_connect]][(]*[[app]][[:]][ ][[[SQLiteAppl]](#searx.sqlitedb.SQLiteAppl "searx.sqlitedb.SQLiteAppl")]*[)] [[→] [[[Connection]](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection "(in Python v3.14)")]][[[\[source\]]]](../_modules/searx/sqlitedb.html#DBSession.get_connect)[¶](#searx.sqlitedb.DBSession.get_connect "Link to this definition")

    :   Returns a thread local DB connection. The connection is only established once per thread.

```
<!-- -->
```

*[[class]][ ]*[[searx.sqlitedb.]][[SQLiteAppl]][(]*[[db_url]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*[)][[[\[source\]]]](../_modules/searx/sqlitedb.html#SQLiteAppl)[¶](#searx.sqlitedb.SQLiteAppl "Link to this definition")

:   Abstract base class for implementing convenient DB access in SQLite applications. In the constructor, a [[`SQLiteProperties`]](#searx.sqlitedb.SQLiteProperties "searx.sqlitedb.SQLiteProperties") instance is already aggregated under [`self.properties`].

    [[DB_SCHEMA]]*[[:]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[=]][ ][1]*[¶](#searx.sqlitedb.SQLiteAppl.DB_SCHEMA "Link to this definition")

    :   As soon as changes are made to the DB schema, the version number must be increased. Changes to the version number require the DB to be recreated (or migrated / if an migration path exists and is implemented).

    [[SQLITE_THREADING_MODE]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[=]][ ][\'serialized\']*[¶](#searx.sqlitedb.SQLiteAppl.SQLITE_THREADING_MODE "Link to this definition")

    :   Threading mode of the SQLite library. Depends on the options used at compile time and is different for different distributions and architectures.

        Possible values are 0:[`single-thread`], 1:[`multi-thread`], 3:[`serialized`] (see [[`sqlite3.threadsafety`]](https://docs.python.org/3/library/sqlite3.html#sqlite3.threadsafety "(in Python v3.14)")). Pre- Python 3.11 this value was hard coded to 1.

        Depending on this value, optimizations are made, e.g. in "serialized" mode it is not necessary to create a separate DB connector for each thread.

    [[SQLITE_JOURNAL_MODE]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[=]][ ][\'WAL\']*[¶](#searx.sqlitedb.SQLiteAppl.SQLITE_JOURNAL_MODE "Link to this definition")

    :   [`SQLiteAppl`] applications are optimized for [WAL](https://sqlite.org/wal.html) mode, its not recommend to change the journal mode (see [`SQLiteAppl.tear_down`]).

    [[SQLITE_CONNECT_ARGS]]*[[:]][ ][[dict]](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[\|]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[\]]][ ][[=]][ ][ [0,] [\'check_same_thread\':] [False}]*[¶](#searx.sqlitedb.SQLiteAppl.SQLITE_CONNECT_ARGS "Link to this definition")

    :   Connection arguments ([[`sqlite3.connect`]](https://docs.python.org/3/library/sqlite3.html#sqlite3.connect "(in Python v3.14)"))

        [`check_same_thread`]: *bool*

        :   Is disabled by default when [[`SQLITE_THREADING_MODE`]](#searx.sqlitedb.SQLiteAppl.SQLITE_THREADING_MODE "searx.sqlitedb.SQLiteAppl.SQLITE_THREADING_MODE") is serialized. The check is more of a hindrance when [threadsafety](https://docs.python.org/3/library/sqlite3.html#sqlite3.threadsafety) is serialized because it would prevent a DB connector from being used in multiple threads.

            Is enabled when [threadsafety](https://docs.python.org/3/library/sqlite3.html#sqlite3.threadsafety) is [`single-thread`] or [`multi-thread`] (when threads cannot share a connection [PEP-0249](https://peps.python.org/pep-0249/#threadsafety)).

        [`cached_statements`]:

        :   Is set to [`0`] by default. Note: Python 3.12+ fetch result are not consistent in multi-threading application and causing an API misuse error.

            The multithreading use in SQLiteAppl is intended and supported if threadsafety is set to 3 (aka "serialized"). CPython supports "serialized" from version 3.12 on, but unfortunately only with errors:

            -   [https://github.com/python/cpython/issues/118172](https://github.com/python/cpython/issues/118172)

            -   [https://github.com/python/cpython/issues/123873](https://github.com/python/cpython/issues/123873)

            The workaround for SQLite3 multithreading cache inconsistency is to set option [`cached_statements`] to [`0`] by default.

        [`isolation_level`]: *unset*

        :   If the connection attribute [isolation_level](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.isolation_level) is **not** [`None`], new transactions are implicitly opened before [`execute()`] and [`executemany()`] executes SQL- INSERT, UPDATE, DELETE, or REPLACE statements [\[1\]](https://docs.python.org/3/library/sqlite3.html#sqlite3-transaction-control-isolation-level).

            By default, the value is not set, which means the default from Python is used: Python's default is [`""`], which is an alias for [`"DEFERRED"`].

        [`autocommit`]: *unset*

        :   Starting with Python 3.12 the DB connection has a [`autocommit`] attribute and the recommended way of controlling transaction behaviour is through this attribute [\[2\]](https://docs.python.org/3/library/sqlite3.html#transaction-control-via-the-autocommit-attribute).

            By default, the value is not set, which means the default from Python is used: Python's default is the constant [LEGACY_TRANSACTION_CONTROL](https://docs.python.org/3/library/sqlite3.html#sqlite3.LEGACY_TRANSACTION_CONTROL): Pre-Python 3.12 (non-PEP 249-compliant) transaction control, see [`isolation_level`] above for more details.

    [[connect]][(][)] [[→] [[[Connection]](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection "(in Python v3.14)")]][[[\[source\]]]](../_modules/searx/sqlitedb.html#SQLiteAppl.connect)[¶](#searx.sqlitedb.SQLiteAppl.connect "Link to this definition")

    :   Creates a new DB connection ([[`SQLITE_CONNECT_ARGS`]](#searx.sqlitedb.SQLiteAppl.SQLITE_CONNECT_ARGS "searx.sqlitedb.SQLiteAppl.SQLITE_CONNECT_ARGS")). If not already done, the DB schema is set up. The caller must take care of closing the resource. Alternatively, [[`SQLiteAppl.DB`]](#searx.sqlitedb.SQLiteAppl.DB "searx.sqlitedb.SQLiteAppl.DB") can also be used (the resource behind self.DB is automatically closed when the process or thread is terminated).

    [[register_functions]][(]*[[conn]][[:]][ ][[[Connection]](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection "(in Python v3.14)")]*[)][[[\[source\]]]](../_modules/searx/sqlitedb.html#SQLiteAppl.register_functions)[¶](#searx.sqlitedb.SQLiteAppl.register_functions "Link to this definition")

    :   Create [user-defined](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.create_function) SQL functions.

        [`REGEXP(<pattern>,`]` `[`<field>)`][0 \| 1]

        :   [re.search](https://docs.python.org/3/library/re.html#re.search) returns (int) 1 for a match and 0 for none match of [`<pattern>`] in [`<field>`].

            ::: 
            ::: highlight
                SELECT '12' AS field WHERE REGEXP('^[0-9][0-9]$', field)
                -- 12

                SELECT REGEXP('[0-9][0-9]', 'X12Y')
                -- 1
                SELECT REGEXP('[0-9][0-9]', 'X1Y')
                -- 0
            :::
            :::

    *[[property]][ ]*[[DB]]*[[:]][ ][[Connection]](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection "(in Python v3.14)")*[¶](#searx.sqlitedb.SQLiteAppl.DB "Link to this definition")

    :   Provides a DB connection. The connection is a *singleton* and therefore well suited for read access. If [[`SQLITE_THREADING_MODE`]](#searx.sqlitedb.SQLiteAppl.SQLITE_THREADING_MODE "searx.sqlitedb.SQLiteAppl.SQLITE_THREADING_MODE") is [`serialized`] only one DB connection is created for all threads.

        ::: 
        Note

        For dedicated [transaction control](https://docs.python.org/3/library/sqlite3.html#sqlite3-controlling-transactions), it is recommended to create a new connection ([[`SQLiteAppl.connect`]](#searx.sqlitedb.SQLiteAppl.connect "searx.sqlitedb.SQLiteAppl.connect")).
        :::

    [[init]][(]*[[conn]][[:]][ ][[[Connection]](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection "(in Python v3.14)")]*[)] [[→] [[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")]][[[\[source\]]]](../_modules/searx/sqlitedb.html#SQLiteAppl.init)[¶](#searx.sqlitedb.SQLiteAppl.init "Link to this definition")

    :   Initializes the DB schema and properties, is only executed once even if called several times.

        If the initialization has not yet taken place, it is carried out and a True is returned to the caller at the end. If the initialization has already been carried out in the past, False is returned.

```
<!-- -->
```

*[[class]][ ]*[[searx.sqlitedb.]][[SQLiteProperties]][(]*[[db_url]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*[)][[[\[source\]]]](../_modules/searx/sqlitedb.html#SQLiteProperties)[¶](#searx.sqlitedb.SQLiteProperties "Link to this definition")

:   Simple class to manage properties of a DB application in the DB. The object has its own DB connection and transaction area.

    ::: 
    ::: highlight
        CREATE TABLE IF NOT EXISTS properties (
          name       TEXT,
          value      TEXT,
          m_time     INTEGER DEFAULT (strftime('%s', 'now')),
          PRIMARY KEY (name))
    :::
    :::

    [[SQLITE_JOURNAL_MODE]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[=]][ ][\'WAL\']*[¶](#searx.sqlitedb.SQLiteProperties.SQLITE_JOURNAL_MODE "Link to this definition")

    :   [`SQLiteAppl`] applications are optimized for [WAL](https://sqlite.org/wal.html) mode, its not recommend to change the journal mode (see [`SQLiteAppl.tear_down`]).

    [[DDL_PROPERTIES]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[=]][ ][\"CREATE] [TABLE] [IF] [NOT] [EXISTS] [properties] [(\\n]  [name]       [TEXT,\\n]  [value]      [TEXT,\\n]  [m_time]     [INTEGER] [DEFAULT] [(strftime(\'%s\',] [\'now\')),]  [\--] [last] [modified] [(unix] [epoch)] [time] [in] [sec.\\n]  [PRIMARY] [KEY] [(name))\"]*[¶](#searx.sqlitedb.SQLiteProperties.DDL_PROPERTIES "Link to this definition")

    :   Table to store properties of the DB application

    [[SQLITE_CONNECT_ARGS]]*[[:]][ ][[dict]](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[\|]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[\]]][ ][[=]][ ][ [0,] [\'check_same_thread\':] [False}]*[¶](#searx.sqlitedb.SQLiteProperties.SQLITE_CONNECT_ARGS "Link to this definition")

    :   Connection arguments ([[`sqlite3.connect`]](https://docs.python.org/3/library/sqlite3.html#sqlite3.connect "(in Python v3.14)"))

        [`check_same_thread`]: *bool*

        :   Is disabled by default when [`SQLITE_THREADING_MODE`] is serialized. The check is more of a hindrance when [threadsafety](https://docs.python.org/3/library/sqlite3.html#sqlite3.threadsafety) is serialized because it would prevent a DB connector from being used in multiple threads.

            Is enabled when [threadsafety](https://docs.python.org/3/library/sqlite3.html#sqlite3.threadsafety) is [`single-thread`] or [`multi-thread`] (when threads cannot share a connection [PEP-0249](https://peps.python.org/pep-0249/#threadsafety)).

        [`cached_statements`]:

        :   Is set to [`0`] by default. Note: Python 3.12+ fetch result are not consistent in multi-threading application and causing an API misuse error.

            The multithreading use in SQLiteAppl is intended and supported if threadsafety is set to 3 (aka "serialized"). CPython supports "serialized" from version 3.12 on, but unfortunately only with errors:

            -   [https://github.com/python/cpython/issues/118172](https://github.com/python/cpython/issues/118172)

            -   [https://github.com/python/cpython/issues/123873](https://github.com/python/cpython/issues/123873)

            The workaround for SQLite3 multithreading cache inconsistency is to set option [`cached_statements`] to [`0`] by default.

        [`isolation_level`]: *unset*

        :   If the connection attribute [isolation_level](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.isolation_level) is **not** [`None`], new transactions are implicitly opened before [`execute()`] and [`executemany()`] executes SQL- INSERT, UPDATE, DELETE, or REPLACE statements [\[1\]](https://docs.python.org/3/library/sqlite3.html#sqlite3-transaction-control-isolation-level).

            By default, the value is not set, which means the default from Python is used: Python's default is [`""`], which is an alias for [`"DEFERRED"`].

        [`autocommit`]: *unset*

        :   Starting with Python 3.12 the DB connection has a [`autocommit`] attribute and the recommended way of controlling transaction behaviour is through this attribute [\[2\]](https://docs.python.org/3/library/sqlite3.html#transaction-control-via-the-autocommit-attribute).

            By default, the value is not set, which means the default from Python is used: Python's default is the constant [LEGACY_TRANSACTION_CONTROL](https://docs.python.org/3/library/sqlite3.html#sqlite3.LEGACY_TRANSACTION_CONTROL): Pre-Python 3.12 (non-PEP 249-compliant) transaction control, see [`isolation_level`] above for more details.

    [[init]][(]*[[conn]][[:]][ ][[[Connection]](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection "(in Python v3.14)")]*[)] [[→] [[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")]][[[\[source\]]]](../_modules/searx/sqlitedb.html#SQLiteProperties.init)[¶](#searx.sqlitedb.SQLiteProperties.init "Link to this definition")

    :   Initializes DB schema of the properties in the DB.

    [[set]][(]*[[name]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *[[value]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[\|]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*[)][[[\[source\]]]](../_modules/searx/sqlitedb.html#SQLiteProperties.set)[¶](#searx.sqlitedb.SQLiteProperties.set "Link to this definition")

    :   Set [`value`] of property [`name`] in DB. If property already exists, update the [`m_time`] (and the value).

    [[delete]][(]*[[name]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*[)] [[→] [[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]][[[\[source\]]]](../_modules/searx/sqlitedb.html#SQLiteProperties.delete)[¶](#searx.sqlitedb.SQLiteProperties.delete "Link to this definition")

    :   Delete of property [`name`] from DB.

    [[row]][(]*[[name]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *[[default]][[:]][ ][[[Any]](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")][ ][[=]][ ][[None]]*[)][[[\[source\]]]](../_modules/searx/sqlitedb.html#SQLiteProperties.row)[¶](#searx.sqlitedb.SQLiteProperties.row "Link to this definition")

    :   Returns the DB row of property [`name`] or [`default`] if property not exists in DB.

    [[m_time]][(]*[[name]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *[[default]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[0]]*[)] [[→] [[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]][[[\[source\]]]](../_modules/searx/sqlitedb.html#SQLiteProperties.m_time)[¶](#searx.sqlitedb.SQLiteProperties.m_time "Link to this definition")

    :   Last modification time of this property.