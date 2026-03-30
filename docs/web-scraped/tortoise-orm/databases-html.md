# Source: https://tortoise.github.io/databases.html

Title: Databases - Tortoise ORM v1.1.6 Documentation

URL Source: https://tortoise.github.io/databases.html

Published Time: Thu, 05 Mar 2026 07:20:56 GMT

Markdown Content:
Databases - Tortoise ORM v1.1.6 Documentation
===============
- [x] - [x] [![Image 1: logo](https://tortoise.github.io/_static/tortoise.png)](https://tortoise.github.io/toc.html "Tortoise ORM v1.1.6 Documentation")

 Tortoise ORM 1.1.6 Documentation 

 Databases 

[](javascript:void(0) "Share")

 Initializing search 

[tortoise-orm](https://github.com/tortoise/tortoise-orm "Go to repository")

*   [Tortoise ORM](https://tortoise.github.io/index.html)
*   [Getting started](https://tortoise.github.io/getting_started.html)
*   [Reference](https://tortoise.github.io/reference.html)
*   [Examples](https://tortoise.github.io/examples.html)
*   [Contrib](https://tortoise.github.io/contrib.html)
*   [Migration Guide: Tortoise 1.0](https://tortoise.github.io/migration_guide.html)
*   [Changelog](https://tortoise.github.io/CHANGELOG.html)
*   [Roadmap](https://tortoise.github.io/roadmap.html)
*   [Contribution Guide](https://tortoise.github.io/CONTRIBUTING.html)
*   [Thanks](https://tortoise.github.io/CONTRIBUTORS.html)

[![Image 2: logo](https://tortoise.github.io/_static/tortoise.png)](https://tortoise.github.io/toc.html "Tortoise ORM v1.1.6 Documentation") Tortoise ORM v1.1.6 Documentation  

[tortoise-orm](https://github.com/tortoise/tortoise-orm "Go to repository")

*   [Tortoise ORM](https://tortoise.github.io/index.html)
*   [Getting started](https://tortoise.github.io/getting_started.html)
*   - [x] [Reference](https://tortoise.github.io/reference.html) Reference 
    *   [Set up](https://tortoise.github.io/setup.html)
    *   - [x] Databases [Databases](https://tortoise.github.io/databases.html#) Table of contents  
        *   [DB_ URL](https://tortoise.github.io/databases.html#db-url)
        *   [Capabilities](https://tortoise.github.io/databases.html#capabilities)
            *   [C tortoise.backends.base.client.Capabilities](https://tortoise.github.io/databases.html#tortoise.backends.base.client.Capabilities)
                *   [Parameters](https://tortoise.github.io/databases.html#tortoise.backends.base.client.Capabilities-parameters)
                    *   [p dialect](https://tortoise.github.io/databases.html#tortoise.backends.base.client.Capabilities.__init__.dialect)
                    *   [p daemon](https://tortoise.github.io/databases.html#tortoise.backends.base.client.Capabilities.__init__.daemon)
                    *   [p requires_ limit](https://tortoise.github.io/databases.html#tortoise.backends.base.client.Capabilities.__init__.requires_limit)
                    *   [p inline_ comment](https://tortoise.github.io/databases.html#tortoise.backends.base.client.Capabilities.__init__.inline_comment)
                    *   [p supports_ transactions](https://tortoise.github.io/databases.html#tortoise.backends.base.client.Capabilities.__init__.supports_transactions)
                    *   [p support_ for_ update](https://tortoise.github.io/databases.html#tortoise.backends.base.client.Capabilities.__init__.support_for_update)
                    *   [p support_ index_ hint](https://tortoise.github.io/databases.html#tortoise.backends.base.client.Capabilities.__init__.support_index_hint)
                    *   [p support_ update_ limit_ order_ by](https://tortoise.github.io/databases.html#tortoise.backends.base.client.Capabilities.__init__.support_update_limit_order_by)
                    *   [p support_ for_ posix_ regex_ queries](https://tortoise.github.io/databases.html#tortoise.backends.base.client.Capabilities.__init__.support_for_posix_regex_queries)
                    *   [p support_ json_ attributes](https://tortoise.github.io/databases.html#tortoise.backends.base.client.Capabilities.__init__.support_json_attributes)
                    *   [p can_ rollback_ ddl](https://tortoise.github.io/databases.html#tortoise.backends.base.client.Capabilities.__init__.can_rollback_ddl)

        *   [SQLite](https://tortoise.github.io/databases.html#sqlite)
            *   [Required Parameters](https://tortoise.github.io/databases.html#required-parameters)
            *   [Optional parameters:](https://tortoise.github.io/databases.html#optional-parameters)

        *   [Postgre SQL](https://tortoise.github.io/databases.html#postgresql)
            *   [Required Parameters](https://tortoise.github.io/databases.html#id3)
            *   [Optional parameters:](https://tortoise.github.io/databases.html#id4)

        *   [My SQL/Maria DB](https://tortoise.github.io/databases.html#mysql-mariadb)
            *   [Required Parameters](https://tortoise.github.io/databases.html#id5)
            *   [Optional parameters:](https://tortoise.github.io/databases.html#id6)

        *   [MSSQL/Oracle](https://tortoise.github.io/databases.html#mssql-oracle)
            *   [Required Parameters](https://tortoise.github.io/databases.html#id7)
            *   [Optional parameters:](https://tortoise.github.io/databases.html#id8)

        *   [Encoding in Oracle:](https://tortoise.github.io/databases.html#encoding-in-oracle)
        *   [Passing in custom SSL Certificates](https://tortoise.github.io/databases.html#passing-in-custom-ssl-certificates)
        *   [Base DB client](https://tortoise.github.io/databases.html#base-db-client)
            *   [C tortoise.backends.base.client.Base DBAsync Client](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient)
                *   [A query_ class](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.query_class)
                *   [A executor_ class](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.executor_class)
                *   [A schema_ generator](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.schema_generator)
                *   [A capabilities](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.capabilities)
                *   [M acquire_ connection](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.acquire_connection)
                    *   [Return type](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.acquire_connection-return-type)

                *   [M close](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.close)
                    *   [Return type](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.close-return-type)

                *   [M create_ connection](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.create_connection)
                    *   [Parameters](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.create_connection-parameters)
                        *   [p with_ db](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.create_connection.with_db)

                    *   [Return type](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.create_connection-return-type)

                *   [M db_ create](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.db_create)
                    *   [Return type](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.db_create-return-type)

                *   [M db_ delete](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.db_delete)
                    *   [Return type](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.db_delete-return-type)

                *   [M execute_ insert](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_insert)
                    *   [Parameters](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_insert-parameters)
                        *   [p query](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_insert.query)
                        *   [p values](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_insert.values)

                    *   [Return type](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_insert-return-type)
                    *   [Returns](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_insert-returns)

                *   [M execute_ many](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_many)
                    *   [Parameters](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_many-parameters)
                        *   [p query](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_many.query)
                        *   [p values](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_many.values)

                    *   [Return type](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_many-return-type)

                *   [M execute_ query](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_query)
                    *   [Parameters](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_query-parameters)
                        *   [p query](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_query.query)
                        *   [p values](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_query.values)

                    *   [Return type](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_query-return-type)
                    *   [Returns](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_query-returns)

                *   [M execute_ query_ dict](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_query_dict)
                    *   [Parameters](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_query_dict-parameters)
                        *   [p query](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_query_dict.query)
                        *   [p values](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_query_dict.values)

                    *   [Return type](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_query_dict-return-type)

                *   [M execute_ query_ dict_ with_ affected](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_query_dict_with_affected)
                    *   [Parameters](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_query_dict_with_affected-parameters)
                        *   [p query](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_query_dict_with_affected.query)
                        *   [p values](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_query_dict_with_affected.values)

                    *   [Return type](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_query_dict_with_affected-return-type)

                *   [M execute_ script](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_script)
                    *   [Parameters](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_script-parameters)
                        *   [p query](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_script.query)

                    *   [Return type](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_script-return-type)

    *   [Models](https://tortoise.github.io/models.html)
    *   [Fields](https://tortoise.github.io/fields.html)
    *   [Indexes](https://tortoise.github.io/indexes.html)
    *   [Timezone](https://tortoise.github.io/timezone.html)
    *   [Schema Creation](https://tortoise.github.io/schema.html)
    *   [Query API](https://tortoise.github.io/query.html)
    *   [Direct Py Pika Queries](https://tortoise.github.io/direct_queries.html)
    *   [Manager](https://tortoise.github.io/manager.html)
    *   [Functions & Aggregates](https://tortoise.github.io/functions.html)
    *   [Expressions](https://tortoise.github.io/expressions.html)
    *   [Transactions](https://tortoise.github.io/transactions.html)
    *   [Connections](https://tortoise.github.io/connections.html)
    *   [Exceptions](https://tortoise.github.io/exceptions.html)
    *   [Signals](https://tortoise.github.io/signals.html)
    *   [Migrations](https://tortoise.github.io/migration.html)
    *   [Validators](https://tortoise.github.io/validators.html)
    *   [Logging](https://tortoise.github.io/logging.html)
    *   [Router](https://tortoise.github.io/router.html)
    *   [Tortoise CLI](https://tortoise.github.io/cli.html)

*   [Examples](https://tortoise.github.io/examples.html)
*   [Contrib](https://tortoise.github.io/contrib.html)
*   [Migration Guide: Tortoise 1.0](https://tortoise.github.io/migration_guide.html)
*   [Changelog](https://tortoise.github.io/CHANGELOG.html)
*   [Roadmap](https://tortoise.github.io/roadmap.html)
*   [Contribution Guide](https://tortoise.github.io/CONTRIBUTING.html)
*   [Thanks](https://tortoise.github.io/CONTRIBUTORS.html)

Databases[¶](https://tortoise.github.io/databases.html#databases "Link to this heading")
========================================================================================

Tortoise currently supports the following databases:

*   SQLite (using `aiosqlite`）

*   PostgreSQL >= 9.4 (using `asyncpg` or `psycopg`)

*   MySQL/MariaDB (using `asyncmy` or `aiomysql`)

*   Microsoft SQL Server (using `asyncodbc`)

To use, please ensure that corresponding asyncio driver is installed.

DB_URL[¶](https://tortoise.github.io/databases.html#db-url "Link to this heading")
----------------------------------------------------------------------------------

Tortoise supports specifying Database configuration in a URL form. The form is:

`DB_TYPE://USERNAME:PASSWORD@HOST:PORT/DB_NAME?PARAM1=value&PARAM2=value`

If password contains special characters it need to be URL encoded:

```
>>> import urllib.parse
>>> urllib.parse.quote_plus("kx%jj5/g")
'kx%25jj5%2Fg'
```

Note

Passwords containing `%` followed by valid hex digits (e.g., `foo%bar`) may not be parsed correctly from a URL string, because the URL parser interprets such sequences as percent-encoded characters. If your password contains `%`, either percent-encode it (as shown above) or use the dict-based configuration format instead, which bypasses URL parsing entirely:

```
await Tortoise.init(config={
    "connections": {
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "host": "127.0.0.1",
                "port": 5432,
                "user": "myuser",
                "password": "ADM[r$VIS]",
                "database": "mydb",
            }
        }
    },
    "apps": {
        "models": {
            "models": ["myapp.models"],
            "default_connection": "default",
        }
    },
})
```

The supported `DB_TYPE`:

`sqlite`:
Typically in the form of `sqlite://DB_FILE` So if the `DB_FILE` is “/data/db.sqlite3” then the string will be `sqlite:///data/db.sqlite` (note the three /’s)

`postgres`
Using `asyncpg`: Typically in the form of `postgres://postgres:pass@db.host:5432/somedb`

Or specifically `asyncpg`/`psycopg` using:

*   `psycopg`: `psycopg://postgres:pass@db.host:5432/somedb`

*   `asyncpg`: `asyncpg://postgres:pass@db.host:5432/somedb`

`mysql`:
Typically in the form of `mysql://myuser:mypass@db.host:3306/somedb`

`mssql`:
Typically in the form of `mssql://myuser:mypass@db.host:1433/somedb?driver=the odbc driver` You can also pass driver options such as `encrypt` and `trust_server_certificate` (or their ODBC-cased equivalents `Encrypt` and `TrustServerCertificate`) which will be appended to the DSN. For example:

```
mssql://myuser:mypass@db.host:1433/somedb?driver=ODBC%20Driver%2018%20for%20SQL%20Server&encrypt=no&trust_server_certificate=yes
```

Capabilities[¶](https://tortoise.github.io/databases.html#capabilities "Link to this heading")
----------------------------------------------------------------------------------------------

Since each database has a different set of features we have a `Capabilities` that is registered on each client. Primarily this is to work around larger-than SQL differences, or common issues.

_class_ tortoise.backends.base.client.Capabilities(_[dialect](https://tortoise.github.io/databases.html#tortoise.backends.base.client.Capabilities.\_\_init\_\_.dialect "tortoise.backends.base.client.Capabilities.\_\_init\_\_.dialect (Python parameter) — Dialect name of the DB Client driver.")_, _*_, _[daemon](https://tortoise.github.io/databases.html#tortoise.backends.base.client.Capabilities.\_\_init\_\_.daemon "tortoise.backends.base.client.Capabilities.\_\_init\_\_.daemon (Python parameter) — Is the DB an external Daemon we connect to?")=`True`_, _[requires\_limit](https://tortoise.github.io/databases.html#tortoise.backends.base.client.Capabilities.\_\_init\_\_.requires\_limit "tortoise.backends.base.client.Capabilities.\_\_init\_\_.requires\_limit (Python parameter) — Indicates that this DB requires a LIMIT statement for an OFFSET statement to work.")=`False`_, _[inline\_comment](https://tortoise.github.io/databases.html#tortoise.backends.base.client.Capabilities.\_\_init\_\_.inline\_comment "tortoise.backends.base.client.Capabilities.\_\_init\_\_.inline\_comment (Python parameter) — Indicates that comments should be rendered in line with the DDL statement, and not as a separate statement.")=`False`_, _[supports\_transactions](https://tortoise.github.io/databases.html#tortoise.backends.base.client.Capabilities.\_\_init\_\_.supports\_transactions "tortoise.backends.base.client.Capabilities.\_\_init\_\_.supports\_transactions (Python parameter) — Indicates that this DB supports transactions.")=`True`_, _[support\_for\_update](https://tortoise.github.io/databases.html#tortoise.backends.base.client.Capabilities.\_\_init\_\_.support\_for\_update "tortoise.backends.base.client.Capabilities.\_\_init\_\_.support\_for\_update (Python parameter) — Indicates that this DB supports SELECT ...")=`True`_, _[support\_for\_no\_key\_update](https://tortoise.github.io/databases.html#tortoise.backends.base.client.Capabilities "tortoise.backends.base.client.Capabilities.\_\_init\_\_.support\_for\_no\_key\_update (Python parameter)")=`False`_, _[support\_index\_hint](https://tortoise.github.io/databases.html#tortoise.backends.base.client.Capabilities.\_\_init\_\_.support\_index\_hint "tortoise.backends.base.client.Capabilities.\_\_init\_\_.support\_index\_hint (Python parameter) — Support force index or use index.")=`False`_, _[support\_update\_limit\_order\_by](https://tortoise.github.io/databases.html#tortoise.backends.base.client.Capabilities.\_\_init\_\_.support\_update\_limit\_order\_by "tortoise.backends.base.client.Capabilities.\_\_init\_\_.support\_update\_limit\_order\_by (Python parameter) — support update/delete with limit and order by.")=`True`_, _[support\_for\_posix\_regex\_queries](https://tortoise.github.io/databases.html#tortoise.backends.base.client.Capabilities.\_\_init\_\_.support\_for\_posix\_regex\_queries "tortoise.backends.base.client.Capabilities.\_\_init\_\_.support\_for\_posix\_regex\_queries (Python parameter) — indicated if the db supports posix regex queries")=`False`_, _[support\_json\_attributes](https://tortoise.github.io/databases.html#tortoise.backends.base.client.Capabilities.\_\_init\_\_.support\_json\_attributes "tortoise.backends.base.client.Capabilities.\_\_init\_\_.support\_json\_attributes (Python parameter) — indicated if the db supports accessing json attributes")=`False`_, _[can\_rollback\_ddl](https://tortoise.github.io/databases.html#tortoise.backends.base.client.Capabilities.\_\_init\_\_.can\_rollback\_ddl "tortoise.backends.base.client.Capabilities.\_\_init\_\_.can\_rollback\_ddl (Python parameter) — Whether the database supports transactional DDL. Used to determine if migrations can be run atomically.")=`False`_)[[source]](https://tortoise.github.io/_modules/tortoise/backends/base/client.html#Capabilities)[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.Capabilities "Link to this definition")
DB Client Capabilities indicates the supported feature-set, and is also used to note common workarounds to deficiencies.

Defaults are set with the following standard:

*   Deficiencies: assume it is working right.

*   Features: assume it doesn’t have it.

Parameters:[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.Capabilities-parameters "Permalink to this headline")dialect[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.Capabilities.__init__.dialect "Permalink to this definition")
Dialect name of the DB Client driver.

daemon=`True`[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.Capabilities.__init__.daemon "Permalink to this definition")
Is the DB an external Daemon we connect to?

requires_limit=`False`[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.Capabilities.__init__.requires_limit "Permalink to this definition")
Indicates that this DB requires a `LIMIT` statement for an `OFFSET` statement to work.

inline_comment=`False`[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.Capabilities.__init__.inline_comment "Permalink to this definition")
Indicates that comments should be rendered in line with the DDL statement, and not as a separate statement.

supports_transactions=`True`[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.Capabilities.__init__.supports_transactions "Permalink to this definition")
Indicates that this DB supports transactions.

support_for_update=`True`[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.Capabilities.__init__.support_for_update "Permalink to this definition")
Indicates that this DB supports SELECT … FOR UPDATE SQL statement.

support_for_update_no_key
Indicates that this DB supports SELECT … FOR NO KEY UPDATE SQL statement.

support_index_hint=`False`[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.Capabilities.__init__.support_index_hint "Permalink to this definition")
Support force index or use index.

support_update_limit_order_by=`True`[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.Capabilities.__init__.support_update_limit_order_by "Permalink to this definition")
support update/delete with limit and order by.

support_for_posix_regex_queries=`False`[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.Capabilities.__init__.support_for_posix_regex_queries "Permalink to this definition")
indicated if the db supports posix regex queries

support_json_attributes=`False`[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.Capabilities.__init__.support_json_attributes "Permalink to this definition")
indicated if the db supports accessing json attributes

can_rollback_ddl=`False`[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.Capabilities.__init__.can_rollback_ddl "Permalink to this definition")
Whether the database supports transactional DDL. Used to determine if migrations can be run atomically.

SQLite[¶](https://tortoise.github.io/databases.html#sqlite "Link to this heading")
----------------------------------------------------------------------------------

SQLite is an embedded database, and can run on a file or in-memory. Good database for local development or testing of code logic, but not recommended for production use.

Caution

SQLite doesn’t support many of the common datatypes natively, although we do emulation where we can, not everything is perfect.

For example `DecimalField` has precision preserved by storing values as strings, except when doing aggregates/ordering on it. In those cases we have to cast to/from floating-point numbers.

Similarly case-insensitivity is only partially implemented.

DB URL is typically in the form of `sqlite://DB_FILE` So if the `DB_FILE` is “/data/db.sqlite3” then the string will be `sqlite:///data/db.sqlite` (note the three /’s)

### Required Parameters[¶](https://tortoise.github.io/databases.html#required-parameters "Link to this heading")

`file_path`:
Path to SQLite3 file. `:memory:` is a special path that indicates in-memory database.

### Optional parameters:[¶](https://tortoise.github.io/databases.html#optional-parameters "Link to this heading")

SQLite optional parameters is basically any of the `PRAGMA` statements documented [here.](https://sqlite.org/pragma.html#toc)

`journal_mode` (defaults to `WAL`):
Specify SQLite journal mode.

`journal_size_limit` (defaults to `16384`):
The journal size.

`foreign_keys` (defaults to `ON`)
Set to `OFF` to not enforce referential integrity.

PostgreSQL[¶](https://tortoise.github.io/databases.html#postgresql "Link to this heading")
------------------------------------------------------------------------------------------

DB URL is typically in the form of `postgres://postgres:pass@db.host:5432/somedb`, or, if connecting via Unix domain socket `postgres:///somedb`.

### Required Parameters[¶](https://tortoise.github.io/databases.html#id3 "Link to this heading")

`user`:
Username to connect with.

`password`:
Password for username.

`host`:
Network host that database is available at.

`port`:
Network port that database is available at. (defaults to `5432`)

`database`:
Database to use.

### Optional parameters:[¶](https://tortoise.github.io/databases.html#id4 "Link to this heading")

PostgreSQL optional parameters are pass-though parameters to the driver, see [here](https://magicstack.github.io/asyncpg/current/api/index.html#connection-pools) for more details.

`minsize` (defaults to `1`):
Minimum connection pool size

`maxsize` (defaults to `5`):
Maximum connection pool size

`max_queries` (defaults to `50000`):
Maximum no of queries before a connection is closed and replaced.

`max_inactive_connection_lifetime` (defaults to `300.0`):
Duration of inactive connection before assuming that it has gone stale, and force a re-connect.

`schema` (uses user’s default schema by default):
A specific schema to use by default.

`ssl` (defaults to ‘’False``):
Either `True` or a custom SSL context for self-signed certificates. See [MSSQL/Oracle](https://tortoise.github.io/databases.html#db-ssl) for more info.

In case any of `user`, `password`, `host`, `port` parameters is missing, we are letting `asyncpg`/`psycopg` retrieve it from default sources (standard PostgreSQL environment variables or default values).

MySQL/MariaDB[¶](https://tortoise.github.io/databases.html#mysql-mariadb "Link to this heading")
------------------------------------------------------------------------------------------------

DB URL is typically in the form of `mysql://myuser:mypass@db.host:3306/somedb`

### Required Parameters[¶](https://tortoise.github.io/databases.html#id5 "Link to this heading")

`user`:
Username to connect with.

`password`:
Password for username.

`host`:
Network host that database is available at.

`port`:
Network port that database is available at. (defaults to `3306`)

`database`:
Database to use.

### Optional parameters:[¶](https://tortoise.github.io/databases.html#id6 "Link to this heading")

MySQL optional parameters are pass-though parameters to the driver, see [here](https://aiomysql.readthedocs.io/en/latest/connection.html#connection) for more details.

`minsize` (defaults to `1`):
Minimum connection pool size

`maxsize` (defaults to `5`):
Maximum connection pool size

`connect_timeout` (defaults to `None`):
Duration to wait for connection before throwing error.

`echo` (defaults to `False`):
Set to True` to echo SQL queries (debug only)

`charset` (defaults to `utf8mb4`):
Sets the character set in use

`ssl` (defaults to `False`):
Either `True` or a custom SSL context for self-signed certificates. See [MSSQL/Oracle](https://tortoise.github.io/databases.html#db-ssl) for more info.

MSSQL/Oracle[¶](https://tortoise.github.io/databases.html#mssql-oracle "Link to this heading")
----------------------------------------------------------------------------------------------

DB URL is typically in the form of `mssql or oracle://myuser:mypass@db.host:1433/somedb?driver=the odbc driver`

### Required Parameters[¶](https://tortoise.github.io/databases.html#id7 "Link to this heading")

`user`:
Username to connect with.

`password`:
Password for username.

`host`:
Network host that database is available at.

`port`:
Network port that database is available at. (defaults to `1433`)

`database`:
Database to use.

`driver`:
The ODBC driver to use. Actual name of the ODBC driver in your odbcinst.ini file (you can find it’s location using odbcinst -j command). It requires unixodbc to be installed in your system.

### Optional parameters:[¶](https://tortoise.github.io/databases.html#id8 "Link to this heading")

MSSQL/Oracle optional parameters are pass-though parameters to the driver, see [here](https://github.com/tortoise/asyncodbc) for more details.

`minsize` (defaults to `1`):
Minimum connection pool size

`maxsize` (defaults to `10`):
Maximum connection pool size

`pool_recycle` (defaults to `-1`):
Pool recycle timeout in seconds.

`echo` (defaults to `False`):
Set to `True` to echo SQL queries (debug only)

Encoding in Oracle:[¶](https://tortoise.github.io/databases.html#encoding-in-oracle "Link to this heading")
-----------------------------------------------------------------------------------------------------------

If you get `???` values in Varchar fields instead of your actual text (russian/chinese/etc), then set `NLS_LANG` variable in your client environment to support UTF8. For example, “American_America.UTF8”.

Passing in custom SSL Certificates[¶](https://tortoise.github.io/databases.html#passing-in-custom-ssl-certificates "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------

To pass in a custom SSL Cert, one has to use the verbose init structure as the URL parser can’t handle complex objects.

```
# Here we create a custom SSL context
import ssl
ctx = ssl.create_default_context()
# And in this example we disable validation...
# Please don't do this. Look at the official Python ``ssl`` module documentation
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Here we do a verbose init
await Tortoise.init(
    config={
        "connections": {
            "default": {
                "engine": "tortoise.backends.asyncpg",
                "credentials": {
                    "database": None,
                    "host": "127.0.0.1",
                    "password": "moo",
                    "port": 54321,
                    "user": "postgres",
                    "ssl": ctx  # Here we pass in the SSL context
                }
            }
        },
        "apps": {
            "models": {
                "models": ["some.models"],
                "default_connection": "default",
            }
        },
    }
)
```

Base DB client[¶](https://tortoise.github.io/databases.html#base-db-client "Link to this heading")
--------------------------------------------------------------------------------------------------

The Base DB client interface is provided here, but should only be directly used as an advanced case.

_class_ tortoise.backends.base.client.BaseDBAsyncClient(_[connection\_name](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient "tortoise.backends.base.client.BaseDBAsyncClient.\_\_init\_\_.connection\_name (Python parameter)")_, _[fetch\_inserted](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient "tortoise.backends.base.client.BaseDBAsyncClient.\_\_init\_\_.fetch\_inserted (Python parameter)")=`True`_, _**[kwargs](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient "tortoise.backends.base.client.BaseDBAsyncClient.\_\_init\_\_.kwargs (Python parameter)")_)[[source]](https://tortoise.github.io/_modules/tortoise/backends/base/client.html#BaseDBAsyncClient)[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient "Link to this definition")
Base class for containing a DB connection.

Parameters get passed as kwargs, and is mostly driver specific.

query_class _type[pypika\_tortoise.Query]_[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.query_class "Link to this definition")
The PyPika Query dialect (low level dialect)

executor_class _type[BaseExecutor]_[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.executor_class "Link to this definition")
The executor dialect class (high level dialect)

schema_generator _type[BaseSchemaGenerator]_[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.schema_generator "Link to this definition")
The DDL schema generator

capabilities _Capabilities_[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.capabilities "Link to this definition")
Contains the connection capabilities

acquire_connection()[[source]](https://tortoise.github.io/_modules/tortoise/backends/base/client.html#BaseDBAsyncClient.acquire_connection)[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.acquire_connection "Link to this definition")
Acquires a connection from the pool. Will return the current context connection if already in a transaction.

Return type:[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.acquire_connection-return-type "Permalink to this headline")
tortoise.backends.base.client.ConnectionWrapper | tortoise.backends.base.client.PoolConnectionWrapper

_async_ close()[[source]](https://tortoise.github.io/_modules/tortoise/backends/base/client.html#BaseDBAsyncClient.close)[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.close "Link to this definition")
Closes the DB connection.

Return type:[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.close-return-type "Permalink to this headline")
`None`

_async_ create_connection(_[with\_db](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.create\_connection.with\_db "tortoise.backends.base.client.BaseDBAsyncClient.create\_connection.with\_db (Python parameter) — If True, then select the DB to use, else use default. Use case for this is to create/drop a database.")_)[[source]](https://tortoise.github.io/_modules/tortoise/backends/base/client.html#BaseDBAsyncClient.create_connection)[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.create_connection "Link to this definition")
Establish a DB connection.

Parameters:[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.create_connection-parameters "Permalink to this headline")with_db[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.create_connection.with_db "Permalink to this definition")
If True, then select the DB to use, else use default. Use case for this is to create/drop a database.

Return type:[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.create_connection-return-type "Permalink to this headline")
`None`

_async_ db_create()[[source]](https://tortoise.github.io/_modules/tortoise/backends/base/client.html#BaseDBAsyncClient.db_create)[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.db_create "Link to this definition")
Created the database in the server. Typically only called by the test runner.

Need to have called `create_connection()`` with parameter `with_db=False` set to use the default connection instead of the configured one, else you would get errors indicating the database doesn’t exist.

Return type:[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.db_create-return-type "Permalink to this headline")
`None`

_async_ db_delete()[[source]](https://tortoise.github.io/_modules/tortoise/backends/base/client.html#BaseDBAsyncClient.db_delete)[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.db_delete "Link to this definition")
Delete the database from the Server. Typically only called by the test runner.

Need to have called `create_connection()`` with parameter `with_db=False` set to use the default connection instead of the configured one, else you would get errors indicating the database is in use.

Return type:[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.db_delete-return-type "Permalink to this headline")
`None`

_async_ execute_insert(_[query](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute\_insert.query "tortoise.backends.base.client.BaseDBAsyncClient.execute\_insert.query (Python parameter) — The SQL string, pre-parametrized for the target DB dialect.")_, _[values](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute\_insert.values "tortoise.backends.base.client.BaseDBAsyncClient.execute\_insert.values (Python parameter) — A sequence of positional DB parameters.")_)[[source]](https://tortoise.github.io/_modules/tortoise/backends/base/client.html#BaseDBAsyncClient.execute_insert)[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_insert "Link to this definition")
Executes a RAW SQL insert statement, with provided parameters.

Parameters:[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_insert-parameters "Permalink to this headline")query[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_insert.query "Permalink to this definition")
The SQL string, pre-parametrized for the target DB dialect.

values[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_insert.values "Permalink to this definition")
A sequence of positional DB parameters.

Return type:[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_insert-return-type "Permalink to this headline")
`Any`

Returns:[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_insert-returns "Permalink to this headline")
The primary key if it is generated by the DB. (Currently only integer autonumber PK’s)

_async_ execute_many(_[query](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute\_many.query "tortoise.backends.base.client.BaseDBAsyncClient.execute\_many.query (Python parameter) — The SQL string, pre-parametrized for the target DB dialect.")_, _[values](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute\_many.values "tortoise.backends.base.client.BaseDBAsyncClient.execute\_many.values (Python parameter) — A sequence of positional DB parameters.")_)[[source]](https://tortoise.github.io/_modules/tortoise/backends/base/client.html#BaseDBAsyncClient.execute_many)[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_many "Link to this definition")
Executes a RAW bulk insert statement, like execute_insert, but returns no data.

Parameters:[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_many-parameters "Permalink to this headline")query[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_many.query "Permalink to this definition")
The SQL string, pre-parametrized for the target DB dialect.

values[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_many.values "Permalink to this definition")
A sequence of positional DB parameters.

Return type:[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_many-return-type "Permalink to this headline")
`None`

_async_ execute_query(_[query](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute\_query.query "tortoise.backends.base.client.BaseDBAsyncClient.execute\_query.query (Python parameter) — The SQL string, pre-parametrized for the target DB dialect.")_, _[values](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute\_query.values "tortoise.backends.base.client.BaseDBAsyncClient.execute\_query.values (Python parameter) — A sequence of positional DB parameters.")=`None`_)[[source]](https://tortoise.github.io/_modules/tortoise/backends/base/client.html#BaseDBAsyncClient.execute_query)[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_query "Link to this definition")
Executes a RAW SQL query statement, and returns the resultset.

Parameters:[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_query-parameters "Permalink to this headline")query[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_query.query "Permalink to this definition")
The SQL string, pre-parametrized for the target DB dialect.

values=`None`[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_query.values "Permalink to this definition")
A sequence of positional DB parameters.

Return type:[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_query-return-type "Permalink to this headline")
`tuple`

Returns:[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_query-returns "Permalink to this headline")
A tuple of: (The number of rows affected, The resultset)

_async_ execute_query_dict(_[query](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute\_query\_dict.query "tortoise.backends.base.client.BaseDBAsyncClient.execute\_query\_dict.query (Python parameter) — The SQL string, pre-parametrized for the target DB dialect.")_, _[values](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute\_query\_dict.values "tortoise.backends.base.client.BaseDBAsyncClient.execute\_query\_dict.values (Python parameter) — A sequence of positional DB parameters.")=`None`_)[[source]](https://tortoise.github.io/_modules/tortoise/backends/base/client.html#BaseDBAsyncClient.execute_query_dict)[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_query_dict "Link to this definition")
Executes a RAW SQL query statement, and returns the resultset as a list of dicts.

Parameters:[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_query_dict-parameters "Permalink to this headline")query[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_query_dict.query "Permalink to this definition")
The SQL string, pre-parametrized for the target DB dialect.

values=`None`[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_query_dict.values "Permalink to this definition")
A sequence of positional DB parameters.

Return type:[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_query_dict-return-type "Permalink to this headline")
`list`

_async_ execute_query_dict_with_affected(_[query](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute\_query\_dict\_with\_affected.query "tortoise.backends.base.client.BaseDBAsyncClient.execute\_query\_dict\_with\_affected.query (Python parameter) — The SQL string, pre-parametrized for the target DB dialect.")_, _[values](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute\_query\_dict\_with\_affected.values "tortoise.backends.base.client.BaseDBAsyncClient.execute\_query\_dict\_with\_affected.values (Python parameter) — A sequence of positional DB parameters.")=`None`_)[[source]](https://tortoise.github.io/_modules/tortoise/backends/base/client.html#BaseDBAsyncClient.execute_query_dict_with_affected)[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_query_dict_with_affected "Link to this definition")
Executes a RAW SQL query statement, and returns the resultset as a list of dicts along with the rows affected if available.

Parameters:[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_query_dict_with_affected-parameters "Permalink to this headline")query[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_query_dict_with_affected.query "Permalink to this definition")
The SQL string, pre-parametrized for the target DB dialect.

values=`None`[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_query_dict_with_affected.values "Permalink to this definition")
A sequence of positional DB parameters.

Return type:[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_query_dict_with_affected-return-type "Permalink to this headline")
`tuple`

_async_ execute_script(_[query](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute\_script.query "tortoise.backends.base.client.BaseDBAsyncClient.execute\_script.query (Python parameter) — The SQL string, which will be passed on verbatim. Semicolons is supported here.")_)[[source]](https://tortoise.github.io/_modules/tortoise/backends/base/client.html#BaseDBAsyncClient.execute_script)[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_script "Link to this definition")
Executes a RAW SQL script with multiple statements, and returns nothing.

Parameters:[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_script-parameters "Permalink to this headline")query[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_script.query "Permalink to this definition")
The SQL string, which will be passed on verbatim. Semicolons is supported here.

Return type:[¶](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient.execute_script-return-type "Permalink to this headline")
`None`

 Back to top 

 © Copyright 2018 - 2026, Andrey Bondar & Nickolas Grigoriadis & long2ice. 

 Created using [Sphinx](https://www.sphinx-doc.org/) 8.1.3. and [Sphinx-Immaterial](https://github.com/jbms/sphinx-immaterial/)
