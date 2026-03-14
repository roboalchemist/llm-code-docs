# Source: https://docs.djangoproject.com/en/6.0/ref/databases/

Title: Databases | Django documentation

URL Source: https://docs.djangoproject.com/en/6.0/ref/databases/

Markdown Content:
Databases | Django documentation | Django
===============
[Skip to main content](https://docs.djangoproject.com/en/6.0/ref/databases/#main-content)

[Django](https://www.djangoproject.com/)
The web framework for perfectionists with deadlines.

Menu Main navigation
*   [Overview](https://www.djangoproject.com/start/overview/)
*   [Download](https://www.djangoproject.com/download/)
*   [Documentation](https://docs.djangoproject.com/)
*   [News](https://www.djangoproject.com/weblog/)
*   [Code](https://github.com/django/django)
*   [Issues](https://code.djangoproject.com/)
*   [Community](https://www.djangoproject.com/community/)
*   [Foundation](https://www.djangoproject.com/foundation/)
*   [♥ Donate](https://www.djangoproject.com/fundraising/)

Search Submit

Toggle theme (current theme: auto)

Toggle theme (current theme: light)

Toggle theme (current theme: dark)

Toggle Light / Dark / Auto color theme

[Documentation](https://docs.djangoproject.com/en/6.0/)

*   [Getting Help](https://docs.djangoproject.com/en/6.0/faq/help/)

*   Language: **en**
*   [zh-hans](https://docs.djangoproject.com/zh-hans/6.0/ref/databases/)
*   [sv](https://docs.djangoproject.com/sv/6.0/ref/databases/)
*   [pt-br](https://docs.djangoproject.com/pt-br/6.0/ref/databases/)
*   [pl](https://docs.djangoproject.com/pl/6.0/ref/databases/)
*   [ko](https://docs.djangoproject.com/ko/6.0/ref/databases/)
*   [ja](https://docs.djangoproject.com/ja/6.0/ref/databases/)
*   [it](https://docs.djangoproject.com/it/6.0/ref/databases/)
*   [id](https://docs.djangoproject.com/id/6.0/ref/databases/)
*   [fr](https://docs.djangoproject.com/fr/6.0/ref/databases/)
*   [es](https://docs.djangoproject.com/es/6.0/ref/databases/)
*   [el](https://docs.djangoproject.com/el/6.0/ref/databases/)

*   Documentation version: **6.0**
*   [dev](https://docs.djangoproject.com/en/dev/ref/databases/)
*   [5.2](https://docs.djangoproject.com/en/5.2/ref/databases/)
*   [5.1](https://docs.djangoproject.com/en/5.1/ref/databases/)
*   [5.0](https://docs.djangoproject.com/en/5.0/ref/databases/)
*   [4.2](https://docs.djangoproject.com/en/4.2/ref/databases/)
*   [4.1](https://docs.djangoproject.com/en/4.1/ref/databases/)
*   [4.0](https://docs.djangoproject.com/en/4.0/ref/databases/)
*   [3.2](https://docs.djangoproject.com/en/3.2/ref/databases/)
*   [3.1](https://docs.djangoproject.com/en/3.1/ref/databases/)
*   [3.0](https://docs.djangoproject.com/en/3.0/ref/databases/)
*   [2.2](https://docs.djangoproject.com/en/2.2/ref/databases/)
*   [2.1](https://docs.djangoproject.com/en/2.1/ref/databases/)
*   [2.0](https://docs.djangoproject.com/en/2.0/ref/databases/)
*   [1.11](https://docs.djangoproject.com/en/1.11/ref/databases/)
*   [1.10](https://docs.djangoproject.com/en/1.10/ref/databases/)
*   [1.8](https://docs.djangoproject.com/en/1.8/ref/databases/)

*   [](https://docs.djangoproject.com/en/6.0/ref/databases/#top)

Databases[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#databases "Link to this heading")
===================================================================================================

Django officially supports the following databases:

*   [PostgreSQL](https://docs.djangoproject.com/en/6.0/ref/databases/#postgresql-notes)

*   [MariaDB](https://docs.djangoproject.com/en/6.0/ref/databases/#mariadb-notes)

*   [MySQL](https://docs.djangoproject.com/en/6.0/ref/databases/#mysql-notes)

*   [Oracle](https://docs.djangoproject.com/en/6.0/ref/databases/#oracle-notes)

*   [SQLite](https://docs.djangoproject.com/en/6.0/ref/databases/#sqlite-notes)

There are also a number of [database backends provided by third parties](https://docs.djangoproject.com/en/6.0/ref/databases/#third-party-notes).

Django attempts to support as many features as possible on all database backends. However, not all database backends are alike, and we’ve had to make design decisions on which features to support and which assumptions we can make safely.

This file describes some of the features that might be relevant to Django usage. It is not intended as a replacement for server-specific documentation or reference manuals.

General notes[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#general-notes "Link to this heading")
-----------------------------------------------------------------------------------------------------------

### Persistent connections[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#persistent-connections "Link to this heading")

Persistent connections avoid the overhead of reestablishing a connection to the database in each HTTP request. They’re controlled by the [`CONN_MAX_AGE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-CONN_MAX_AGE) parameter which defines the maximum lifetime of a connection. It can be set independently for each database.

The default value is `0`, preserving the historical behavior of closing the database connection at the end of each request. To enable persistent connections, set [`CONN_MAX_AGE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-CONN_MAX_AGE) to a positive integer of seconds. For unlimited persistent connections, set it to `None`.

When using ASGI, persistent connections should be disabled. Instead, use your database backend’s built-in connection pooling if available, or investigate a third-party connection pooling option if required.

#### Connection management[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#connection-management "Link to this heading")

Django opens a connection to the database when it first makes a database query. It keeps this connection open and reuses it in subsequent requests. Django closes the connection once it exceeds the maximum age defined by [`CONN_MAX_AGE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-CONN_MAX_AGE) or when it isn’t usable any longer.

In detail, Django automatically opens a connection to the database whenever it needs one and doesn’t have one already — either because this is the first connection, or because the previous connection was closed.

At the beginning of each request, Django closes the connection if it has reached its maximum age. If your database terminates idle connections after some time, you should set [`CONN_MAX_AGE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-CONN_MAX_AGE) to a lower value, so that Django doesn’t attempt to use a connection that has been terminated by the database server. (This problem may only affect very low traffic sites.)

At the end of each request, Django closes the connection if it has reached its maximum age or if it is in an unrecoverable error state. If any database errors have occurred while processing the requests, Django checks whether the connection still works, and closes it if it doesn’t. Thus, database errors affect at most one request per each application’s worker thread; if the connection becomes unusable, the next request gets a fresh connection.

Setting [`CONN_HEALTH_CHECKS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-CONN_HEALTH_CHECKS) to `True` can be used to improve the robustness of connection reuse and prevent errors when a connection has been closed by the database server which is now ready to accept and serve new connections, e.g. after database server restart. The health check is performed only once per request and only if the database is being accessed during the handling of the request.

#### Caveats[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#caveats "Link to this heading")

Since each thread maintains its own connection, your database must support at least as many simultaneous connections as you have worker threads.

Sometimes a database won’t be accessed by the majority of your views, for example because it’s the database of an external system, or thanks to caching. In such cases, you should set [`CONN_MAX_AGE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-CONN_MAX_AGE) to a low value or even `0`, because it doesn’t make sense to maintain a connection that’s unlikely to be reused. This will help keep the number of simultaneous connections to this database small.

The development server creates a new thread for each request it handles, negating the effect of persistent connections. Don’t enable them during development.

When Django establishes a connection to the database, it sets up appropriate parameters, depending on the backend being used. If you enable persistent connections, this setup is no longer repeated every request. If you modify parameters such as the connection’s isolation level or time zone, you should either restore Django’s defaults at the end of each request, force an appropriate value at the beginning of each request, or disable persistent connections.

If a connection is created in a long-running process, outside of Django’s request-response cycle, the connection will remain open until explicitly closed, or timeout occurs. You can use `django.db.close_old_connections()` to close all old or unusable connections.

### Encoding[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#encoding "Link to this heading")

Django assumes that all databases use UTF-8 encoding. Using other encodings may result in unexpected behavior such as “value too long” errors from your database for data that is valid in Django. See the database specific notes below for information on how to set up your database correctly.

PostgreSQL notes[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#postgresql-notes "Link to this heading")
-----------------------------------------------------------------------------------------------------------------

Django supports PostgreSQL 14 and higher. [psycopg](https://www.psycopg.org/psycopg3/) 3.1.12+ or [psycopg2](https://www.psycopg.org/) 2.9.9+ is required, though the latest [psycopg](https://www.psycopg.org/psycopg3/) 3.1.12+ is recommended.

Note

Support for `psycopg2` is likely to be deprecated and removed at some point in the future.

### PostgreSQL connection settings[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#postgresql-connection-settings "Link to this heading")

See [`HOST`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-HOST) for details.

To connect using a service name from the [connection service file](https://www.postgresql.org/docs/current/libpq-pgservice.html) and a password from the [password file](https://www.postgresql.org/docs/current/libpq-pgpass.html), you must specify them in the [`OPTIONS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-OPTIONS) part of your database configuration in [`DATABASES`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATABASES):

`settings.py`[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#id16 "Link to this code")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "OPTIONS": {
            "service": "my_service",
            "passfile": ".my_pgpass",
        },
    }
}

`.pg_service.conf`[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#id17 "Link to this code")

[my_service]
host=localhost
user=USER
dbname=NAME
port=5432

`.my_pgpass`[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#id18 "Link to this code")

localhost:5432:NAME:USER:PASSWORD

The PostgreSQL backend passes the content of [`OPTIONS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-OPTIONS) as keyword arguments to the connection constructor, allowing for more advanced control of driver behavior. All available [parameters](https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-PARAMKEYWORDS) are described in detail in the PostgreSQL documentation.

Warning

Using a service name for testing purposes is not supported. This [may be implemented later](https://code.djangoproject.com/ticket/33685).

### Optimizing PostgreSQL’s configuration[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#optimizing-postgresql-s-configuration "Link to this heading")

Django needs the following parameters for its database connections:

*   `client_encoding`: `'UTF8'`,

*   `default_transaction_isolation`: `'read committed'` by default, or the value set in the connection options (see below),

*   `timezone`:
    *   when [`USE_TZ`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-USE_TZ) is `True`, `'UTC'` by default, or the [`TIME_ZONE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATABASE-TIME_ZONE) value set for the connection,

    *   when [`USE_TZ`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-USE_TZ) is `False`, the value of the global [`TIME_ZONE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-TIME_ZONE) setting.

If these parameters already have the correct values, Django won’t set them for every new connection, which improves performance slightly. You can configure them directly in `postgresql.conf` or more conveniently per database user with [ALTER ROLE](https://www.postgresql.org/docs/current/sql-alterrole.html).

Django will work just fine without this optimization, but each new connection will do some additional queries to set these parameters.

### Isolation level[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#isolation-level "Link to this heading")

Like PostgreSQL itself, Django defaults to the `READ COMMITTED`[isolation level](https://www.postgresql.org/docs/current/transaction-iso.html). If you need a higher isolation level such as `REPEATABLE READ` or `SERIALIZABLE`, set it in the [`OPTIONS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-OPTIONS) part of your database configuration in [`DATABASES`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATABASES):

from django.db.backends.postgresql.psycopg_any import IsolationLevel

DATABASES = {
    # ...
    "OPTIONS": {
        "isolation_level": IsolationLevel.SERIALIZABLE,
    },
}

Note

Under higher isolation levels, your application should be prepared to handle exceptions raised on serialization failures. This option is designed for advanced uses.

### Role[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#role "Link to this heading")

If you need to use a different role for database connections than the role used to establish the connection, set it in the [`OPTIONS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-OPTIONS) part of your database configuration in [`DATABASES`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATABASES):

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        # ...
        "OPTIONS": {
            "assume_role": "my_application_role",
        },
    },
}

### Connection pool[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#connection-pool "Link to this heading")

To use a connection pool with [psycopg](https://www.psycopg.org/psycopg3/), you can either set `"pool"` in the [`OPTIONS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-OPTIONS) part of your database configuration in [`DATABASES`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATABASES) to be a dict to be passed to [`ConnectionPool`](https://www.psycopg.org/psycopg3/docs/api/pool.html#psycopg_pool.ConnectionPool "(in psycopg)"), or to `True` to use the `ConnectionPool` defaults:

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        # ...
        "OPTIONS": {
            "pool": True,
        },
    },
}

This option requires `psycopg[pool]` or [psycopg-pool](https://pypi.org/project/psycopg-pool/) to be installed and is ignored with `psycopg2`.

### Server-side parameters binding[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#server-side-parameters-binding "Link to this heading")

With [psycopg](https://www.psycopg.org/psycopg3/) 3.1.8+, Django defaults to the [client-side binding cursors](https://www.psycopg.org/psycopg3/docs/advanced/cursors.html#client-side-binding-cursors "(in psycopg)"). If you want to use the [server-side binding](https://www.psycopg.org/psycopg3/docs/basic/from_pg2.html#server-side-binding "(in psycopg)") set it in the [`OPTIONS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-OPTIONS) part of your database configuration in [`DATABASES`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATABASES):

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        # ...
        "OPTIONS": {
            "server_side_binding": True,
        },
    },
}

This option is ignored with `psycopg2`.

### Indexes for `varchar` and `text` columns[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#indexes-for-varchar-and-text-columns "Link to this heading")

When specifying `db_index=True` on your model fields, Django typically outputs a single `CREATE INDEX` statement. However, if the database type for the field is either `varchar` or `text` (e.g., used by `CharField`, `FileField`, and `TextField`), then Django will create an additional index that uses an appropriate [PostgreSQL operator class](https://www.postgresql.org/docs/current/indexes-opclass.html) for the column. The extra index is necessary to correctly perform lookups that use the `LIKE` operator in their SQL, as is done with the `contains` and `startswith` lookup types.

### Migration operation for adding extensions[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#migration-operation-for-adding-extensions "Link to this heading")

If you need to add a PostgreSQL extension (like `hstore`, `postgis`, etc.) using a migration, use the [`CreateExtension`](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/operations/#django.contrib.postgres.operations.CreateExtension "django.contrib.postgres.operations.CreateExtension") operation.

### Server-side cursors[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#server-side-cursors "Link to this heading")

When using [`QuerySet.iterator()`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet.iterator "django.db.models.query.QuerySet.iterator"), Django opens a [server-side cursor](https://www.psycopg.org/psycopg3/docs/advanced/cursors.html#server-side-cursors "(in psycopg)"). By default, PostgreSQL assumes that only the first 10% of the results of cursor queries will be fetched. The query planner spends less time planning the query and starts returning results faster, but this could diminish performance if more than 10% of the results are retrieved. PostgreSQL’s assumptions on the number of rows retrieved for a cursor query is controlled with the [cursor_tuple_fraction](https://www.postgresql.org/docs/current/runtime-config-query.html#GUC-CURSOR-TUPLE-FRACTION) option.

#### Transaction pooling and server-side cursors[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#transaction-pooling-and-server-side-cursors "Link to this heading")

Using a connection pooler in transaction pooling mode (e.g. [PgBouncer](https://www.pgbouncer.org/)) requires disabling server-side cursors for that connection.

Server-side cursors are local to a connection and remain open at the end of a transaction when [`AUTOCOMMIT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATABASE-AUTOCOMMIT) is `True`. A subsequent transaction may attempt to fetch more results from a server-side cursor. In transaction pooling mode, there’s no guarantee that subsequent transactions will use the same connection. If a different connection is used, an error is raised when the transaction references the server-side cursor, because server-side cursors are only accessible in the connection in which they were created.

One solution is to disable server-side cursors for a connection in [`DATABASES`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATABASES) by setting [`DISABLE_SERVER_SIDE_CURSORS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATABASE-DISABLE_SERVER_SIDE_CURSORS) to `True`.

To benefit from server-side cursors in transaction pooling mode, you could set up [another connection to the database](https://docs.djangoproject.com/en/6.0/topics/db/multi-db/) in order to perform queries that use server-side cursors. This connection needs to either be directly to the database or to a connection pooler in session pooling mode.

Another option is to wrap each `QuerySet` using server-side cursors in an [`atomic()`](https://docs.djangoproject.com/en/6.0/topics/db/transactions/#django.db.transaction.atomic "django.db.transaction.atomic") block, because it disables `autocommit` for the duration of the transaction. This way, the server-side cursor will only live for the duration of the transaction.

### Manually-specifying values of auto-incrementing primary keys[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#manually-specifying-values-of-auto-incrementing-primary-keys "Link to this heading")

Django uses PostgreSQL’s identity columns to store auto-incrementing primary keys. An identity column is populated with values from a [sequence](https://www.postgresql.org/docs/current/sql-createsequence.html) that keeps track of the next available value. Manually assigning a value to an auto-incrementing field doesn’t update the field’s sequence, which might later cause a conflict. For example:

>>> from django.contrib.auth.models import User
>>> User.objects.create(username="alice", pk=1)
<User: alice>
>>> # The sequence hasn't been updated; its next value is 1.
>>> User.objects.create(username="bob")
IntegrityError: duplicate key value violates unique constraint
"auth_user_pkey" DETAIL: Key (id)=(1) already exists.

If you need to specify such values, reset the sequence afterward to avoid reusing a value that’s already in the table. The [`sqlsequencereset`](https://docs.djangoproject.com/en/6.0/ref/django-admin/#django-admin-sqlsequencereset) management command generates the SQL statements to do that.

### Test database templates[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#test-database-templates "Link to this heading")

You can use the [`TEST['TEMPLATE']`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-TEST_TEMPLATE) setting to specify a [template](https://www.postgresql.org/docs/current/sql-createdatabase.html) (e.g. `'template0'`) from which to create a test database.

### Speeding up test execution with non-durable settings[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#speeding-up-test-execution-with-non-durable-settings "Link to this heading")

You can speed up test execution times by [configuring PostgreSQL to be non-durable](https://www.postgresql.org/docs/current/non-durability.html).

Warning

This is dangerous: it will make your database more susceptible to data loss or corruption in the case of a server crash or power loss. Only use this on a development machine where you can easily restore the entire contents of all databases in the cluster.

MariaDB notes[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#mariadb-notes "Link to this heading")
-----------------------------------------------------------------------------------------------------------

Django supports MariaDB 10.6 and higher.

To use MariaDB, use the MySQL backend, which is shared between the two. See the [MySQL notes](https://docs.djangoproject.com/en/6.0/ref/databases/#mysql-notes) for more details.

MySQL notes[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#mysql-notes "Link to this heading")
-------------------------------------------------------------------------------------------------------

### Version support[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#version-support "Link to this heading")

Django supports MySQL 8.0.11 and higher.

Django’s `inspectdb` feature uses the `information_schema` database, which contains detailed data on all database schemas.

Django expects the database to support Unicode (UTF-8 encoding) and delegates to it the task of enforcing transactions and referential integrity. It is important to be aware of the fact that the two latter ones aren’t actually enforced by MySQL when using the MyISAM storage engine, see the next section.

### Storage engines[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#storage-engines "Link to this heading")

MySQL has several [storage engines](https://dev.mysql.com/doc/refman/en/storage-engines.html). You can change the default storage engine in the server configuration.

MySQL’s default storage engine is [InnoDB](https://dev.mysql.com/doc/refman/en/innodb-storage-engine.html). This engine is fully transactional and supports foreign key references. It’s the recommended choice. However, the InnoDB autoincrement counter is lost on a MySQL restart because it does not remember the `AUTO_INCREMENT` value, instead recreating it as “max(id)+1”. This may result in an inadvertent reuse of [`AutoField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.AutoField "django.db.models.AutoField") values.

The main drawbacks of [MyISAM](https://dev.mysql.com/doc/refman/en/myisam-storage-engine.html) are that it doesn’t support transactions or enforce foreign-key constraints.

### MySQL DB API Drivers[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#mysql-db-api-drivers "Link to this heading")

MySQL has a couple drivers that implement the Python Database API described in [**PEP 249**](https://peps.python.org/pep-0249/):

*   [mysqlclient](https://pypi.org/project/mysqlclient/) is a native driver. It’s **the recommended choice**.

*   [MySQL Connector/Python](https://dev.mysql.com/downloads/connector/python/) is a pure Python driver from Oracle that does not require the MySQL client library or any Python modules outside the standard library.

In addition to a DB API driver, Django needs an adapter to access the database drivers from its ORM. Django provides an adapter for mysqlclient while MySQL Connector/Python includes [its own](https://dev.mysql.com/doc/connector-python/en/connector-python-django-backend.html).

#### mysqlclient[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#mysqlclient "Link to this heading")

Django requires [mysqlclient](https://docs.djangoproject.com/en/6.0/ref/databases/#mysqlclient) 2.2.1 or later.

#### MySQL Connector/Python[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#id8 "Link to this heading")

MySQL Connector/Python is available from the [download page](https://dev.mysql.com/downloads/connector/python/). The Django adapter is available in versions 1.1.X and later. It may not support the most recent releases of Django.

### Time zone definitions[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#time-zone-definitions "Link to this heading")

If you plan on using Django’s [timezone support](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/), use [mysql_tzinfo_to_sql](https://dev.mysql.com/doc/refman/en/mysql-tzinfo-to-sql.html) to load time zone tables into the MySQL database. This needs to be done just once for your MySQL server, not per database.

### Creating your database[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#creating-your-database "Link to this heading")

You can [create your database](https://dev.mysql.com/doc/refman/en/create-database.html) using the command-line tools and this SQL:

CREATE DATABASE <dbname> CHARACTER SET utf8mb4;

This ensures all tables and columns will use UTF-8 by default.

#### Collation settings[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#collation-settings "Link to this heading")

The collation setting for a column controls the order in which data is sorted as well as what strings compare as equal. You can specify the `db_collation` parameter to set the collation name of the column for [`CharField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.CharField.db_collation "django.db.models.CharField.db_collation") and [`TextField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.TextField.db_collation "django.db.models.TextField.db_collation").

The collation can also be set on a database-wide level and per-table. This is [documented thoroughly](https://dev.mysql.com/doc/refman/en/charset.html) in the MySQL documentation. In such cases, you must set the collation by directly manipulating the database settings or tables. Django doesn’t provide an API to change them.

By default, with a UTF-8 database, MySQL will use the `utf8mb4_0900_ai_ci` collation. This results in all string equality comparisons being done in a _case-insensitive_ manner. That is, `"Fred"` and `"freD"` are considered equal at the database level. If you have a unique constraint on a field, it would be illegal to try to insert both `"aa"` and `"AA"` into the same column, since they compare as equal (and, hence, non-unique) with the default collation. If you want case-sensitive comparisons on a particular column or table, change the column or table to use the `utf8mb4_0900_as_cs` collation.

Please note that according to [MySQL Unicode Character Sets](https://dev.mysql.com/doc/refman/en/charset-unicode-sets.html), comparisons for the `utf8mb4_general_ci` collation are faster, but slightly less correct, than comparisons for `utf8mb4_unicode_ci`. If this is acceptable for your application, you should use `utf8mb4_general_ci` because it is faster. If this is not acceptable (for example, if you require German dictionary order), use `utf8mb4_unicode_ci` because it is more accurate.

Warning

Model formsets validate unique fields in a case-sensitive manner. Thus when using a case-insensitive collation, a formset with unique field values that differ only by case will pass validation, but upon calling `save()`, an `IntegrityError` will be raised.

### Connecting to the database[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#connecting-to-the-database "Link to this heading")

Refer to the [settings documentation](https://docs.djangoproject.com/en/6.0/ref/settings/).

Connection settings are used in this order:

1.   [`OPTIONS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-OPTIONS).

2.   [`NAME`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-NAME), [`USER`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-USER), [`PASSWORD`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-PASSWORD), [`HOST`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-HOST), [`PORT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-PORT)

3.   MySQL option files.

In other words, if you set the name of the database in [`OPTIONS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-OPTIONS), this will take precedence over [`NAME`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-NAME), which would override anything in a [MySQL option file](https://dev.mysql.com/doc/refman/en/option-files.html).

Here’s a sample configuration which uses a MySQL option file:

# settings.py
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "OPTIONS": {
            "read_default_file": "/path/to/my.cnf",
        },
    }
}

# my.cnf
[client]
database = NAME
user = USER
password = PASSWORD
default-character-set = utf8mb4

Several other [MySQLdb connection options](https://mysqlclient.readthedocs.io/user_guide.html#functions-and-attributes) may be useful, such as `ssl`, `init_command`, and `sql_mode`.

#### Setting `sql_mode`[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#setting-sql-mode "Link to this heading")

The default value of the `sql_mode` option contains `STRICT_TRANS_TABLES`. That option escalates warnings into errors when data are truncated upon insertion, so Django highly recommends activating a [strict mode](https://dev.mysql.com/doc/refman/en/sql-mode.html#sql-mode-strict) for MySQL to prevent data loss (either `STRICT_TRANS_TABLES` or `STRICT_ALL_TABLES`).

If you need to customize the SQL mode, you can set the `sql_mode` variable like other MySQL options: either in a config file or with the entry `'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"` in the [`OPTIONS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-OPTIONS) part of your database configuration in [`DATABASES`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATABASES).

#### Isolation level[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#mysql-isolation-level "Link to this heading")

When running concurrent loads, database transactions from different sessions (say, separate threads handling different requests) may interact with each other. These interactions are affected by each session’s [transaction isolation level](https://dev.mysql.com/doc/refman/en/innodb-transaction-isolation-levels.html). You can set a connection’s isolation level with an `'isolation_level'` entry in the [`OPTIONS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-OPTIONS) part of your database configuration in [`DATABASES`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATABASES). Valid values for this entry are the four standard isolation levels:

*   `'read uncommitted'`

*   `'read committed'`

*   `'repeatable read'`

*   `'serializable'`

or `None` to use the server’s configured isolation level. However, Django works best with and defaults to read committed rather than MySQL’s default, repeatable read. Data loss is possible with repeatable read. In particular, you may see cases where [`get_or_create()`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet.get_or_create "django.db.models.query.QuerySet.get_or_create") will raise an [`IntegrityError`](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.db.IntegrityError "django.db.IntegrityError") but the object won’t appear in a subsequent [`get()`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet.get "django.db.models.query.QuerySet.get") call.

### Creating your tables[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#creating-your-tables "Link to this heading")

When Django generates the schema, it doesn’t specify a storage engine, so tables will be created with whatever default storage engine your database server is configured for. The easiest solution is to set your database server’s default storage engine to the desired engine.

If you’re using a hosting service and can’t change your server’s default storage engine, you have a couple of options.

*   After the tables are created, execute an `ALTER TABLE` statement to convert a table to a new storage engine (such as InnoDB):

ALTER TABLE <tablename> ENGINE=INNODB;  
This can be tedious if you have a lot of tables.

*   Another option is to use the `init_command` option for MySQLdb prior to creating your tables:

"OPTIONS": {
    "init_command": "SET default_storage_engine=INNODB",
}  
This sets the default storage engine upon connecting to the database. After your tables have been created, you should remove this option as it adds a query that is only needed during table creation to each database connection.

### Table names[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#table-names "Link to this heading")

There are [known issues](https://bugs.mysql.com/bug.php?id=48875) in even the latest versions of MySQL that can cause the case of a table name to be altered when certain SQL statements are executed under certain conditions. It is recommended that you use lowercase table names, if possible, to avoid any problems that might arise from this behavior. Django uses lowercase table names when it auto-generates table names from models, so this is mainly a consideration if you are overriding the table name via the [`db_table`](https://docs.djangoproject.com/en/6.0/ref/models/options/#django.db.models.Options.db_table "django.db.models.Options.db_table") parameter.

### Savepoints[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#savepoints "Link to this heading")

Both the Django ORM and MySQL (when using the InnoDB [storage engine](https://docs.djangoproject.com/en/6.0/ref/databases/#mysql-storage-engines)) support database [savepoints](https://docs.djangoproject.com/en/6.0/topics/db/transactions/#topics-db-transactions-savepoints).

If you use the MyISAM storage engine please be aware of the fact that you will receive database-generated errors if you try to use the [savepoint-related methods of the transactions API](https://docs.djangoproject.com/en/6.0/topics/db/transactions/#topics-db-transactions-savepoints). The reason for this is that detecting the storage engine of a MySQL database/table is an expensive operation so it was decided it isn’t worth to dynamically convert these methods in no-op’s based in the results of such detection.

### Notes on specific fields[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#notes-on-specific-fields "Link to this heading")

#### Character fields[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#character-fields "Link to this heading")

Any fields that are stored with `VARCHAR` column types may have their `max_length` restricted to 255 characters if you are using `unique=True` for the field. This affects [`CharField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.CharField "django.db.models.CharField"), [`SlugField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.SlugField "django.db.models.SlugField"). See [the MySQL documentation](https://dev.mysql.com/doc/refman/en/create-index.html#create-index-column-prefixes) for more details.

#### `TextField` limitations[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#textfield-limitations "Link to this heading")

MySQL can index only the first N chars of a `BLOB` or `TEXT` column. Since `TextField` doesn’t have a defined length, you can’t mark it as `unique=True`. MySQL will report: “BLOB/TEXT column ‘<db_column>’ used in key specification without a key length”.

#### Fractional seconds support for Time and DateTime fields[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#fractional-seconds-support-for-time-and-datetime-fields "Link to this heading")

MySQL can store fractional seconds, provided that the column definition includes a fractional indication (e.g. `DATETIME(6)`).

Django will not upgrade existing columns to include fractional seconds if the database server supports it. If you want to enable them on an existing database, it’s up to you to either manually update the column on the target database, by executing a command like:

ALTER TABLE `your_table` MODIFY `your_datetime_column` DATETIME(6)

or using a [`RunSQL`](https://docs.djangoproject.com/en/6.0/ref/migration-operations/#django.db.migrations.operations.RunSQL "django.db.migrations.operations.RunSQL") operation in a [data migration](https://docs.djangoproject.com/en/6.0/topics/migrations/#data-migrations).

#### `TIMESTAMP` columns[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#timestamp-columns "Link to this heading")

If you are using a legacy database that contains `TIMESTAMP` columns, you must set [`USE_TZ = False`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-USE_TZ) to avoid data corruption. [`inspectdb`](https://docs.djangoproject.com/en/6.0/ref/django-admin/#django-admin-inspectdb) maps these columns to [`DateTimeField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.DateTimeField "django.db.models.DateTimeField") and if you enable timezone support, both MySQL and Django will attempt to convert the values from UTC to local time.

### Row locking with `QuerySet.select_for_update()`[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#row-locking-with-queryset-select-for-update "Link to this heading")

MySQL and MariaDB do not support some options to the `SELECT ... FOR UPDATE` statement. If `select_for_update()` is used with an unsupported option, then a [`NotSupportedError`](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.db.NotSupportedError "django.db.NotSupportedError") is raised.

| Option | MariaDB | MySQL |
| --- | --- | --- |
| `SKIP LOCKED` | X | X |
| `NOWAIT` | X | X |
| `OF` |  | X |
| `NO KEY` |  |  |

When using `select_for_update()` on MySQL, make sure you filter a queryset against at least a set of fields contained in unique constraints or only against fields covered by indexes. Otherwise, an exclusive write lock will be acquired over the full table for the duration of the transaction.

### Automatic typecasting can cause unexpected results[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#automatic-typecasting-can-cause-unexpected-results "Link to this heading")

When performing a query on a string type, but with an integer value, MySQL will coerce the types of all values in the table to an integer before performing the comparison. If your table contains the values `'abc'`, `'def'` and you query for `WHERE mycolumn=0`, both rows will match. Similarly, 
```
WHERE
mycolumn=1
```
 will match the value `'abc1'`. Therefore, string type fields included in Django will always cast the value to a string before using it in a query.

If you implement custom model fields that inherit from [`Field`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field "django.db.models.Field") directly, are overriding [`get_prep_value()`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.get_prep_value "django.db.models.Field.get_prep_value"), or use [`RawSQL`](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.expressions.RawSQL "django.db.models.expressions.RawSQL"), [`extra()`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet.extra "django.db.models.query.QuerySet.extra"), or [`raw()`](https://docs.djangoproject.com/en/6.0/topics/db/sql/#django.db.models.Manager.raw "django.db.models.Manager.raw"), you should ensure that you perform appropriate typecasting.

SQLite notes[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#sqlite-notes "Link to this heading")
---------------------------------------------------------------------------------------------------------

Django supports SQLite 3.31.0 and later.

[SQLite](https://www.sqlite.org/) provides an excellent development alternative for applications that are predominantly read-only or require a smaller installation footprint. As with all database servers, though, there are some differences that are specific to SQLite that you should be aware of.

### Substring matching and case sensitivity[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#substring-matching-and-case-sensitivity "Link to this heading")

For all SQLite versions, there is some slightly counterintuitive behavior when attempting to match some types of strings. These are triggered when using the [`iexact`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#std-fieldlookup-iexact) or [`contains`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#std-fieldlookup-contains) filters in querysets. The behavior splits into two cases:

1. For substring matching, all matches are done case-insensitively. That is a filter such as `filter(name__contains="aa")` will match a name of `"Aabb"`.

2. For strings containing characters outside the ASCII range, all exact string matches are performed case-sensitively, even when the case-insensitive options are passed into the query. So the [`iexact`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#std-fieldlookup-iexact) filter will behave exactly the same as the [`exact`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#std-fieldlookup-exact) filter in these cases.

Some possible workarounds for this are [documented at sqlite.org](https://www.sqlite.org/faq.html#q18), but they aren’t utilized by the default SQLite backend in Django, as incorporating them would be fairly difficult to do robustly. Thus, Django exposes the default SQLite behavior and you should be aware of this when doing case-insensitive or substring filtering.

### Decimal handling[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#decimal-handling "Link to this heading")

SQLite has no real decimal internal type. Decimal values are internally converted to the `REAL` data type (8-byte IEEE floating point number), as explained in the [SQLite datatypes documentation](https://www.sqlite.org/datatype3.html#storage_classes_and_datatypes), so they don’t support correctly-rounded decimal floating point arithmetic.

### “Database is locked” errors[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#database-is-locked-errors "Link to this heading")

SQLite is meant to be a lightweight database, and thus can’t support a high level of concurrency. `OperationalError: database is locked` errors indicate that your application is experiencing more concurrency than `sqlite` can handle in default configuration. This error means that one thread or process has an exclusive lock on the database connection and another thread timed out waiting for the lock the be released.

Python’s SQLite wrapper has a default timeout value that determines how long the second thread is allowed to wait on the lock before it times out and raises the `OperationalError: database is locked` error.

If you’re getting this error, you can solve it by:

*   Switching to another database backend. At a certain point SQLite becomes too “lite” for real-world applications, and these sorts of concurrency errors indicate you’ve reached that point.

*   Rewriting your code to reduce concurrency and ensure that database transactions are short-lived.

*   Increase the default timeout value by setting the `timeout` database option:

"OPTIONS": {
    # ...
    "timeout": 20,
    # ...
}  
This will make SQLite wait a bit longer before throwing “database is locked” errors; it won’t really do anything to solve them.

#### Transactions behavior[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#transactions-behavior "Link to this heading")

SQLite supports three transaction modes: `DEFERRED`, `IMMEDIATE`, and `EXCLUSIVE`.

The default is `DEFERRED`. If you need to use a different mode, set it in the [`OPTIONS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-OPTIONS) part of your database configuration in [`DATABASES`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATABASES), for example:

"OPTIONS": {
    # ...
    "transaction_mode": "IMMEDIATE",
    # ...
}

To make sure your transactions wait until `timeout` before raising “Database is Locked”, change the transaction mode to `IMMEDIATE`.

For the best performance with `IMMEDIATE` and `EXCLUSIVE`, transactions should be as short as possible. This might be hard to guarantee for all of your views so the usage of [`ATOMIC_REQUESTS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATABASE-ATOMIC_REQUESTS) is discouraged in this case.

For more information see [Transactions in SQLite](https://www.sqlite.org/lang_transaction.html#deferred_immediate_and_exclusive_transactions).

### `QuerySet.select_for_update()` not supported[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#queryset-select-for-update-not-supported "Link to this heading")

SQLite does not support the `SELECT ... FOR UPDATE` syntax. Calling it will have no effect.

### Isolation when using `QuerySet.iterator()`[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#isolation-when-using-queryset-iterator "Link to this heading")

There are special considerations described in [Isolation In SQLite](https://www.sqlite.org/isolation.html) when modifying a table while iterating over it using [`QuerySet.iterator()`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet.iterator "django.db.models.query.QuerySet.iterator"). If a row is added, changed, or deleted within the loop, then that row may or may not appear, or may appear twice, in subsequent results fetched from the iterator. Your code must handle this.

### Enabling JSON1 extension on SQLite[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#enabling-json1-extension-on-sqlite "Link to this heading")

To use [`JSONField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.JSONField "django.db.models.JSONField") on SQLite, you need to enable the [JSON1 extension](https://www.sqlite.org/json1.html) on Python’s [`sqlite3`](https://docs.python.org/3/library/sqlite3.html#module-sqlite3 "(in Python v3.14)") library. If the extension is not enabled on your installation, a system error (`fields.E180`) will be raised.

To enable the JSON1 extension you can follow the instruction on [the wiki page](https://code.djangoproject.com/wiki/JSON1Extension).

Note

The JSON1 extension is enabled by default on SQLite 3.38+.

### Setting pragma options[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#setting-pragma-options "Link to this heading")

[Pragma options](https://www.sqlite.org/pragma.html) can be set upon connection by using the `init_command` in the [`OPTIONS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-OPTIONS) part of your database configuration in [`DATABASES`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATABASES). The example below shows how to enable extra durability of synchronous writes and change the `cache_size`:

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        # ...
        "OPTIONS": {
            "init_command": "PRAGMA synchronous=3; PRAGMA cache_size=2000;",
        },
    }
}

Oracle notes[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#oracle-notes "Link to this heading")
---------------------------------------------------------------------------------------------------------

Django supports [Oracle Database Server](https://www.oracle.com/) versions 19c and higher. Version 2.3.0 or higher of the [oracledb](https://oracle.github.io/python-oracledb/) Python driver is required.

In order for the `python manage.py migrate` command to work, your Oracle database user must have privileges to run the following commands:

*   CREATE TABLE

*   CREATE SEQUENCE

*   CREATE PROCEDURE

*   CREATE TRIGGER

To run a project’s test suite, the user usually needs these _additional_ privileges:

*   CREATE USER

*   ALTER USER

*   DROP USER

*   CREATE TABLESPACE

*   DROP TABLESPACE

*   CREATE SESSION WITH ADMIN OPTION

*   CREATE TABLE WITH ADMIN OPTION

*   CREATE SEQUENCE WITH ADMIN OPTION

*   CREATE PROCEDURE WITH ADMIN OPTION

*   CREATE TRIGGER WITH ADMIN OPTION

While the `RESOURCE` role has the required `CREATE TABLE`, `CREATE SEQUENCE`, `CREATE PROCEDURE`, and `CREATE TRIGGER` privileges, and a user granted `RESOURCE WITH ADMIN OPTION` can grant `RESOURCE`, such a user cannot grant the individual privileges (e.g. `CREATE TABLE`), and thus `RESOURCE WITH ADMIN OPTION` is not usually sufficient for running tests.

Some test suites also create views or materialized views; to run these, the user also needs `CREATE VIEW WITH ADMIN OPTION` and `CREATE MATERIALIZED VIEW WITH ADMIN OPTION` privileges. In particular, this is needed for Django’s own test suite.

All of these privileges are included in the DBA role, which is appropriate for use on a private developer’s database.

The Oracle database backend uses the `SYS.DBMS_LOB` and `SYS.DBMS_RANDOM` packages, so your user will require execute permissions on it. It’s normally accessible to all users by default, but in case it is not, you’ll need to grant permissions like so:

GRANT EXECUTE ON SYS.DBMS_LOB TO user;
GRANT EXECUTE ON SYS.DBMS_RANDOM TO user;

### Connecting to the database[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#id13 "Link to this heading")

To connect using the service name of your Oracle database, your `settings.py` file should look something like this:

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.oracle",
        "NAME": "xe",
        "USER": "a_user",
        "PASSWORD": "a_password",
        "HOST": "",
        "PORT": "",
    }
}

In this case, you should leave both [`HOST`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-HOST) and [`PORT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-PORT) empty. However, if you don’t use a `tnsnames.ora` file or a similar naming method and want to connect using the SID (“xe” in this example), then fill in both [`HOST`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-HOST) and [`PORT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-PORT) like so:

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.oracle",
        "NAME": "xe",
        "USER": "a_user",
        "PASSWORD": "a_password",
        "HOST": "dbprod01ned.mycompany.com",
        "PORT": "1540",
    }
}

You should either supply both [`HOST`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-HOST) and [`PORT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-PORT), or leave both as empty strings. Django will use a different connect descriptor depending on that choice.

#### Full DSN and Easy Connect[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#full-dsn-and-easy-connect "Link to this heading")

A Full DSN or Easy Connect string can be used in [`NAME`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-NAME) if both [`HOST`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-HOST) and [`PORT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-PORT) are empty. This format is required when using RAC or pluggable databases without `tnsnames.ora`, for example.

Example of an Easy Connect string:

"NAME": "localhost:1521/orclpdb1"

Example of a full DSN string:

"NAME": (
    "(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))"
    "(CONNECT_DATA=(SERVICE_NAME=orclpdb1)))"
)

### Connection pool[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#oracle-pool "Link to this heading")

New in Django 5.2.

To use a connection pool with [oracledb](https://oracle.github.io/python-oracledb/), set `"pool"` to `True` in the [`OPTIONS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-OPTIONS) part of your database configuration. This uses the driver’s [create_pool()](https://python-oracledb.readthedocs.io/en/latest/user_guide/connection_handling.html#connection-pooling) default values:

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.oracle",
        # ...
        "OPTIONS": {
            "pool": True,
        },
    },
}

To pass custom parameters to the driver’s [create_pool()](https://python-oracledb.readthedocs.io/en/latest/user_guide/connection_handling.html#connection-pooling) function, you can alternatively set `"pool"` to be a dict:

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.oracle",
        # ...
        "OPTIONS": {
            "pool": {
                "min": 1,
                "max": 10,
                # ...
            }
        },
    },
}

### INSERT … RETURNING INTO[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#insert-returning-into "Link to this heading")

By default, the Oracle backend uses a `RETURNING INTO` clause to efficiently retrieve the value of an `AutoField` when inserting new rows. This behavior may result in a `DatabaseError` in certain unusual setups, such as when inserting into a remote table, or into a view with an `INSTEAD OF` trigger. The `RETURNING INTO` clause can be disabled by setting the `use_returning_into` option of the database configuration to `False`:

"OPTIONS": {
    "use_returning_into": False,
}

In this case, the Oracle backend will use a separate `SELECT` query to retrieve `AutoField` values.

### Naming issues[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#naming-issues "Link to this heading")

Oracle imposes a name length limit of 30 characters. To accommodate this, the backend truncates database identifiers to fit, replacing the final four characters of the truncated name with a repeatable MD5 hash value. Additionally, the backend turns database identifiers to all-uppercase.

To prevent these transformations (this is usually required only when dealing with legacy databases or accessing tables which belong to other users), use a quoted name as the value for `db_table`:

class LegacyModel(models.Model):
    class Meta:
        db_table = '"name_left_in_lowercase"'

class ForeignModel(models.Model):
    class Meta:
        db_table = '"OTHER_USER"."NAME_ONLY_SEEMS_OVER_30"'

Quoted names can also be used with Django’s other supported database backends; except for Oracle, however, the quotes have no effect.

When running `migrate`, an `ORA-06552` error may be encountered if certain Oracle keywords are used as the name of a model field or the value of a `db_column` option. Django quotes all identifiers used in queries to prevent most such problems, but this error can still occur when an Oracle datatype is used as a column name. In particular, take care to avoid using the names `date`, `timestamp`, `number` or `float` as a field name.

### NULL and empty strings[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#null-and-empty-strings "Link to this heading")

Django generally prefers to use the empty string (`''`) rather than `NULL`, but Oracle treats both identically. To get around this, the Oracle backend ignores an explicit `null` option on fields that have the empty string as a possible value and generates DDL as if `null=True`. When fetching from the database, it is assumed that a `NULL` value in one of these fields really means the empty string, and the data is silently converted to reflect this assumption.

### `TextField` limitations[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#id15 "Link to this heading")

The Oracle backend stores each `TextField` as an `NCLOB` column. Oracle imposes some limitations on the usage of such LOB columns in general:

*   LOB columns may not be used as primary keys.

*   LOB columns may not be used in indexes.

*   LOB columns may not be used in a `SELECT DISTINCT` list. This means that attempting to use the `QuerySet.distinct` method on a model that includes `TextField` columns will result in an `ORA-00932` error when run against Oracle. As a workaround, use the `QuerySet.defer` method in conjunction with `distinct()` to prevent `TextField` columns from being included in the `SELECT DISTINCT` list.

Subclassing the built-in database backends[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#subclassing-the-built-in-database-backends "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Django comes with built-in database backends. You may subclass an existing database backend to modify its behavior, features, or configuration.

Consider, for example, that you need to change a single database feature. First, you have to create a new directory with a `base` module in it. For example:

mysite/
    ...
    mydbengine/
        __init__.py
        base.py

The `base.py` module must contain a class named `DatabaseWrapper` that subclasses an existing engine from the `django.db.backends` module. Here’s an example of subclassing the PostgreSQL engine to change a feature class `allows_group_by_selected_pks_on_model`:

`mysite/mydbengine/base.py`[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#id19 "Link to this code")

from django.db.backends.postgresql import base, features

class DatabaseFeatures(features.DatabaseFeatures):
    def allows_group_by_selected_pks_on_model(self, model):
        return True

class DatabaseWrapper(base.DatabaseWrapper):
    features_class = DatabaseFeatures

Finally, you must specify a [`DATABASE-ENGINE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATABASE-ENGINE) in your `settings.py` file:

DATABASES = {
    "default": {
        "ENGINE": "mydbengine",
        # ...
    },
}

You can see the current list of database engines by looking in [django/db/backends](https://github.com/django/django/blob/main/django/db/backends).

Using a 3rd-party database backend[¶](https://docs.djangoproject.com/en/6.0/ref/databases/#using-a-3rd-party-database-backend "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------

In addition to the officially supported databases, there are backends provided by 3rd parties that allow you to use other databases with Django:

*   [CockroachDB](https://pypi.org/project/django-cockroachdb/)

*   [Firebird](https://pypi.org/project/django-firebird/)

*   [Google Cloud Spanner](https://pypi.org/project/django-google-spanner/)

*   [Microsoft SQL Server](https://pypi.org/project/mssql-django/)

*   [MongoDB](https://pypi.org/project/django-mongodb-backend/)

*   [Snowflake](https://pypi.org/project/django-snowflake/)

*   [TiDB](https://pypi.org/project/django-tidb/)

*   [YugabyteDB](https://pypi.org/project/django-yugabytedb/)

The Django versions and ORM features supported by these unofficial backends vary considerably. Queries regarding the specific capabilities of these unofficial backends, along with any support queries, should be directed to the support channels provided by each 3rd party project.

Previous page and next page

[Cross Site Request Forgery protection](https://docs.djangoproject.com/en/6.0/ref/csrf/)

[`django-admin` and `manage.py`](https://docs.djangoproject.com/en/6.0/ref/django-admin/)

[Back to Top](https://docs.djangoproject.com/en/6.0/ref/databases/#top)

Additional Information
----------------------

### Support Django!

![Image 1: Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)

*   [Bostjan Kaluza donated to the Django Software Foundation to support Django development. Donate today!](https://www.djangoproject.com/fundraising/)

### Contents

*   [Databases](https://docs.djangoproject.com/en/6.0/ref/databases/#)
    *   [General notes](https://docs.djangoproject.com/en/6.0/ref/databases/#general-notes)
        *   [Persistent connections](https://docs.djangoproject.com/en/6.0/ref/databases/#persistent-connections)
            *   [Connection management](https://docs.djangoproject.com/en/6.0/ref/databases/#connection-management)
            *   [Caveats](https://docs.djangoproject.com/en/6.0/ref/databases/#caveats)

        *   [Encoding](https://docs.djangoproject.com/en/6.0/ref/databases/#encoding)

    *   [PostgreSQL notes](https://docs.djangoproject.com/en/6.0/ref/databases/#postgresql-notes)
        *   [PostgreSQL connection settings](https://docs.djangoproject.com/en/6.0/ref/databases/#postgresql-connection-settings)
        *   [Optimizing PostgreSQL’s configuration](https://docs.djangoproject.com/en/6.0/ref/databases/#optimizing-postgresql-s-configuration)
        *   [Isolation level](https://docs.djangoproject.com/en/6.0/ref/databases/#isolation-level)
        *   [Role](https://docs.djangoproject.com/en/6.0/ref/databases/#role)
        *   [Connection pool](https://docs.djangoproject.com/en/6.0/ref/databases/#connection-pool)
        *   [Server-side parameters binding](https://docs.djangoproject.com/en/6.0/ref/databases/#server-side-parameters-binding)
        *   [Indexes for `varchar` and `text` columns](https://docs.djangoproject.com/en/6.0/ref/databases/#indexes-for-varchar-and-text-columns)
        *   [Migration operation for adding extensions](https://docs.djangoproject.com/en/6.0/ref/databases/#migration-operation-for-adding-extensions)
        *   [Server-side cursors](https://docs.djangoproject.com/en/6.0/ref/databases/#server-side-cursors)
            *   [Transaction pooling and server-side cursors](https://docs.djangoproject.com/en/6.0/ref/databases/#transaction-pooling-and-server-side-cursors)

        *   [Manually-specifying values of auto-incrementing primary keys](https://docs.djangoproject.com/en/6.0/ref/databases/#manually-specifying-values-of-auto-incrementing-primary-keys)
        *   [Test database templates](https://docs.djangoproject.com/en/6.0/ref/databases/#test-database-templates)
        *   [Speeding up test execution with non-durable settings](https://docs.djangoproject.com/en/6.0/ref/databases/#speeding-up-test-execution-with-non-durable-settings)

    *   [MariaDB notes](https://docs.djangoproject.com/en/6.0/ref/databases/#mariadb-notes)
    *   [MySQL notes](https://docs.djangoproject.com/en/6.0/ref/databases/#mysql-notes)
        *   [Version support](https://docs.djangoproject.com/en/6.0/ref/databases/#version-support)
        *   [Storage engines](https://docs.djangoproject.com/en/6.0/ref/databases/#storage-engines)
        *   [MySQL DB API Drivers](https://docs.djangoproject.com/en/6.0/ref/databases/#mysql-db-api-drivers)
            *   [mysqlclient](https://docs.djangoproject.com/en/6.0/ref/databases/#mysqlclient)
            *   [MySQL Connector/Python](https://docs.djangoproject.com/en/6.0/ref/databases/#id8)

        *   [Time zone definitions](https://docs.djangoproject.com/en/6.0/ref/databases/#time-zone-definitions)
        *   [Creating your database](https://docs.djangoproject.com/en/6.0/ref/databases/#creating-your-database)
            *   [Collation settings](https://docs.djangoproject.com/en/6.0/ref/databases/#collation-settings)

        *   [Connecting to the database](https://docs.djangoproject.com/en/6.0/ref/databases/#connecting-to-the-database)
            *   [Setting `sql_mode`](https://docs.djangoproject.com/en/6.0/ref/databases/#setting-sql-mode)
            *   [Isolation level](https://docs.djangoproject.com/en/6.0/ref/databases/#mysql-isolation-level)

        *   [Creating your tables](https://docs.djangoproject.com/en/6.0/ref/databases/#creating-your-tables)
        *   [Table names](https://docs.djangoproject.com/en/6.0/ref/databases/#table-names)
        *   [Savepoints](https://docs.djangoproject.com/en/6.0/ref/databases/#savepoints)
        *   [Notes on specific fields](https://docs.djangoproject.com/en/6.0/ref/databases/#notes-on-specific-fields)
            *   [Character fields](https://docs.djangoproject.com/en/6.0/ref/databases/#character-fields)
            *   [`TextField` limitations](https://docs.djangoproject.com/en/6.0/ref/databases/#textfield-limitations)
            *   [Fractional seconds support for Time and DateTime fields](https://docs.djangoproject.com/en/6.0/ref/databases/#fractional-seconds-support-for-time-and-datetime-fields)
            *   [`TIMESTAMP` columns](https://docs.djangoproject.com/en/6.0/ref/databases/#timestamp-columns)

        *   [Row locking with `QuerySet.select_for_update()`](https://docs.djangoproject.com/en/6.0/ref/databases/#row-locking-with-queryset-select-for-update)
        *   [Automatic typecasting can cause unexpected results](https://docs.djangoproject.com/en/6.0/ref/databases/#automatic-typecasting-can-cause-unexpected-results)

    *   [SQLite notes](https://docs.djangoproject.com/en/6.0/ref/databases/#sqlite-notes)
        *   [Substring matching and case sensitivity](https://docs.djangoproject.com/en/6.0/ref/databases/#substring-matching-and-case-sensitivity)
        *   [Decimal handling](https://docs.djangoproject.com/en/6.0/ref/databases/#decimal-handling)
        *   [“Database is locked” errors](https://docs.djangoproject.com/en/6.0/ref/databases/#database-is-locked-errors)
            *   [Transactions behavior](https://docs.djangoproject.com/en/6.0/ref/databases/#transactions-behavior)

        *   [`QuerySet.select_for_update()` not supported](https://docs.djangoproject.com/en/6.0/ref/databases/#queryset-select-for-update-not-supported)
        *   [Isolation when using `QuerySet.iterator()`](https://docs.djangoproject.com/en/6.0/ref/databases/#isolation-when-using-queryset-iterator)
        *   [Enabling JSON1 extension on SQLite](https://docs.djangoproject.com/en/6.0/ref/databases/#enabling-json1-extension-on-sqlite)
        *   [Setting pragma options](https://docs.djangoproject.com/en/6.0/ref/databases/#setting-pragma-options)

    *   [Oracle notes](https://docs.djangoproject.com/en/6.0/ref/databases/#oracle-notes)
        *   [Connecting to the database](https://docs.djangoproject.com/en/6.0/ref/databases/#id13)
            *   [Full DSN and Easy Connect](https://docs.djangoproject.com/en/6.0/ref/databases/#full-dsn-and-easy-connect)

        *   [Connection pool](https://docs.djangoproject.com/en/6.0/ref/databases/#oracle-pool)
        *   [INSERT … RETURNING INTO](https://docs.djangoproject.com/en/6.0/ref/databases/#insert-returning-into)
        *   [Naming issues](https://docs.djangoproject.com/en/6.0/ref/databases/#naming-issues)
        *   [NULL and empty strings](https://docs.djangoproject.com/en/6.0/ref/databases/#null-and-empty-strings)
        *   [`TextField` limitations](https://docs.djangoproject.com/en/6.0/ref/databases/#id15)

    *   [Subclassing the built-in database backends](https://docs.djangoproject.com/en/6.0/ref/databases/#subclassing-the-built-in-database-backends)
    *   [Using a 3rd-party database backend](https://docs.djangoproject.com/en/6.0/ref/databases/#using-a-3rd-party-database-backend)

### Browse

*   Prev: [Cross Site Request Forgery protection](https://docs.djangoproject.com/en/6.0/ref/csrf/)
*   Next: [`django-admin` and `manage.py`](https://docs.djangoproject.com/en/6.0/ref/django-admin/)
*   [Table of contents](https://docs.djangoproject.com/en/6.0/contents/)
*   [General Index](https://docs.djangoproject.com/en/6.0/genindex/)
*   [Python Module Index](https://docs.djangoproject.com/en/6.0/py-modindex/)

### You are here:

*   [Django 6.0 documentation](https://docs.djangoproject.com/en/6.0/)
    *   [API Reference](https://docs.djangoproject.com/en/6.0/ref/)
        *   Databases

### Getting help

[FAQ](https://docs.djangoproject.com/en/6.0/faq/)Try the FAQ — it's got answers to many common questions.[Index](https://docs.djangoproject.com/en/stable/genindex/), [Module Index](https://docs.djangoproject.com/en/stable/py-modindex/), or [Table of Contents](https://docs.djangoproject.com/en/stable/contents/)Handy when looking for specific information.[Django Discord Server](https://chat.djangoproject.com/)Join the Django Discord Community.[Official Django Forum](https://forum.djangoproject.com/)Join the community on the Django Forum.[Ticket tracker](https://code.djangoproject.com/)Report bugs with Django or Django documentation in our ticket tracker.
### Download:

Offline (Django 6.0): [HTML](https://media.djangoproject.com/docs/django-docs-6.0-en.zip) | [PDF](https://media.readthedocs.org/pdf/django/6.0.x/django.pdf) | [ePub](https://media.readthedocs.org/epub/django/6.0.x/django.epub)

 Provided by [Read the Docs](https://readthedocs.org/).

### Diamond and Platinum Members

[![Image 2: JetBrains](https://media.djangoproject.com/cache/c0/ea/c0ea128467983e64aab91cd27e7918c0.png)](https://jb.gg/ybja10 "JetBrains")

*   **JetBrains**
*   [JetBrains delivers intelligent software solutions that make developers more productive by simplifying their challenging tasks, automating the routine, and helping them adopt the best development practices. PyCharm is the Python IDE for Professional Developers by JetBrains providing a complete set of tools for productive Python, Web and scientific development.](https://jb.gg/ybja10 "JetBrains")

[![Image 3: Sentry](https://media.djangoproject.com/cache/7a/f9/7af9c770dc49465739a82c91a0eb3d51.png)](https://sentry.io/for/django/ "Sentry")

*   **Sentry**
*   [Monitor your Django Code Resolve performance bottlenecks and errors using monitoring, replays, logs and Seer an AI agent for debugging.](https://sentry.io/for/django/ "Sentry")

[![Image 4: Kraken Tech](https://media.djangoproject.com/cache/71/4b/714b3473ed0cf3665f6b894d3be9491e.png)](https://kraken.tech/ "Kraken Tech")

*   **Kraken Tech**
*   [Kraken is the most-loved operating system for energy. Powered by our Utility-Grade AI™ and deep industry know-how, we help utilities transform their technology and operations so they can lead the energy transition. Delivering better outcomes from generation through distribution to supply, Kraken powers 70+ million accounts worldwide, and is on a mission to make a big, green dent in the universe.](https://kraken.tech/ "Kraken Tech")

Django Links
------------

### Learn More

*   [About Django](https://www.djangoproject.com/start/overview/)
*   [Getting Started with Django](https://www.djangoproject.com/start/)
*   [Team Organization](https://www.djangoproject.com/foundation/teams/)
*   [Django Software Foundation](https://www.djangoproject.com/foundation/)
*   [Code of Conduct](https://www.djangoproject.com/conduct/)
*   [Diversity Statement](https://www.djangoproject.com/diversity/)

### Get Involved

*   [Join a Group](https://www.djangoproject.com/community/)
*   [Contribute to Django](https://docs.djangoproject.com/en/dev/internals/contributing/)
*   [Submit a Bug](https://docs.djangoproject.com/en/dev/internals/contributing/bugs-and-features/)
*   [Report a Security Issue](https://docs.djangoproject.com/en/dev/internals/security/#reporting-security-issues)
*   [Individual membership](https://www.djangoproject.com/foundation/individual-members/)

### Get Help

*   [Getting Help FAQ](https://docs.djangoproject.com/en/stable/faq/)
*   [Django Discord](https://chat.djangoproject.com/)
*   [Official Django Forum](https://forum.djangoproject.com/)

### Follow Us

*   [GitHub](https://github.com/django)
*   [X](https://x.com/djangoproject)
*   [Fediverse (Mastodon)](https://fosstodon.org/@django)
*   [Bluesky](https://bsky.app/profile/djangoproject.com)
*   [LinkedIn](https://www.linkedin.com/company/django-software-foundation)
*   [News RSS](https://www.djangoproject.com/rss/weblog/)

### Support Us

*   [Sponsor Django](https://www.djangoproject.com/fundraising/)
*   [Corporate membership](https://www.djangoproject.com/foundation/corporate-members/)
*   [Official merchandise store](https://django.threadless.com/)
*   [Benevity Workplace Giving Program](https://www.djangoproject.com/fundraising/#benevity-giving)

[Django](https://www.djangoproject.com/)

*   Hosting by[In-kind donors](https://www.djangoproject.com/fundraising/#in-kind-donors)
*   Design by[Threespot](https://www.threespot.com/)&[andrevv](http://andrevv.com/)

© 2005-2026 [Django Software Foundation](https://www.djangoproject.com/foundation/) and individual contributors. Django is a [registered trademark](https://www.djangoproject.com/trademarks/) of the Django Software Foundation.
