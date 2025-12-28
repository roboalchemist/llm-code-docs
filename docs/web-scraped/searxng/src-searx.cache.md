# Source: https://docs.searxng.org/src/searx.cache.html

[][]

# Caches[¶](#module-searx.cache "Link to this heading")

Implementation of caching solutions.

-   [[`searx.cache.ExpireCache`]](#searx.cache.ExpireCache "searx.cache.ExpireCache") and its [[`searx.cache.ExpireCacheCfg`]](#searx.cache.ExpireCacheCfg "searx.cache.ExpireCacheCfg")

------------------------------------------------------------------------

*[[class]][ ]*[[searx.cache.]][[ExpireCacheCfg]][(]*[[name]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *[[db_url]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")][ ][[=]][ ][[\'\']]*, *[[MAX_VALUE_LEN]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[10240]]*, *[[MAXHOLD_TIME]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[604800]]*, *[[MAINTENANCE_PERIOD]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[3600]]*, *[[MAINTENANCE_MODE]][[:]][ ][[[Literal]](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[[\[]][[\'auto\']][[,]][ ][[\'off\']][[\]]]][ ][[=]][ ][[\'auto\']]*, *[[password]][[:]][ ][[[bytes]](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")][ ][[=]][ ][[b\'ultrasecretkey\']]*[)][[[\[source\]]]](../_modules/searx/cache.html#ExpireCacheCfg)[¶](#searx.cache.ExpireCacheCfg "Link to this definition")

:   Configuration of a [[`ExpireCache`]](#searx.cache.ExpireCache "searx.cache.ExpireCache") cache.

    [[name]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*[¶](#searx.cache.ExpireCacheCfg.name "Link to this definition")

    :   Name of the cache.

    [[db_url]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*[¶](#searx.cache.ExpireCacheCfg.db_url "Link to this definition")

    :   URL of the SQLite DB, the path to the database file. If unset a default DB will be created in /tmp/sxng_cache\_.db

    [[MAX_VALUE_LEN]]*[[:]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*[¶](#searx.cache.ExpireCacheCfg.MAX_VALUE_LEN "Link to this definition")

    :   Max length of a *serialized* value.

    [[MAXHOLD_TIME]]*[[:]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*[¶](#searx.cache.ExpireCacheCfg.MAXHOLD_TIME "Link to this definition")

    :   Hold time (default in sec.), after which a value is removed from the cache.

    [[MAINTENANCE_PERIOD]]*[[:]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*[¶](#searx.cache.ExpireCacheCfg.MAINTENANCE_PERIOD "Link to this definition")

    :   Maintenance period in seconds / when [[`MAINTENANCE_MODE`]](#searx.cache.ExpireCacheCfg.MAINTENANCE_MODE "searx.cache.ExpireCacheCfg.MAINTENANCE_MODE") is set to [`auto`].

    [[MAINTENANCE_MODE]]*[[:]][ ][[Literal]](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[[\[]][[\'auto\']][[,]][ ][[\'off\']][[\]]]*[¶](#searx.cache.ExpireCacheCfg.MAINTENANCE_MODE "Link to this definition")

    :   Type of maintenance mode

        [`auto`]:

        :   Maintenance is carried out automatically as part of the maintenance intervals ([[`MAINTENANCE_PERIOD`]](#searx.cache.ExpireCacheCfg.MAINTENANCE_PERIOD "searx.cache.ExpireCacheCfg.MAINTENANCE_PERIOD")); no external process is required.

        [`off`]:

        :   Maintenance is switched off and must be carried out by an external process if required.

    [[password]]*[[:]][ ][[bytes]](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")*[¶](#searx.cache.ExpireCacheCfg.password "Link to this definition")

    :   Password used by [[`ExpireCache.secret_hash`]](#searx.cache.ExpireCache.secret_hash "searx.cache.ExpireCache.secret_hash").

        The default password is taken from [[secret_key]](../admin/settings/settings_server.html#server-secret-key). When the password is changed, the hashed keys in the cache can no longer be used, which is why all values in the cache are deleted when the password is changed.

```
<!-- -->
```

*[[class]][ ]*[[searx.cache.]][[ExpireCacheStats]][(]*[[cached_items]][[:]][ ][[[dict]](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][[list]](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[\[]][[tuple]](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][[Any]](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")[[,]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[\]]][[\]]][[\]]]]*[)][[[\[source\]]]](../_modules/searx/cache.html#ExpireCacheStats)[¶](#searx.cache.ExpireCacheStats "Link to this definition")

:   Dataclass which provides information on the status of the cache.

    [[cached_items]]*[[:]][ ][[dict]](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][[list]](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[\[]][[tuple]](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][[Any]](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")[[,]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[\]]][[\]]][[\]]]*[¶](#searx.cache.ExpireCacheStats.cached_items "Link to this definition")

    :   Values in the cache mapped by context name.

```
<!-- -->
```

*[[class]][ ]*[[searx.cache.]][[ExpireCache]][[[\[source\]]]](../_modules/searx/cache.html#ExpireCache)[¶](#searx.cache.ExpireCache "Link to this definition")

:   Abstract base class for the implementation of a key/value cache with expire date.

    *[[abstractmethod]][ ]*[[set]][(]*[[key]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *[[value]][[:]][ ][[[Any]](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")]*, *[[expire]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*, *[[ctx]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*[)] [[→] [[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")]][[[\[source\]]]](../_modules/searx/cache.html#ExpireCache.set)[¶](#searx.cache.ExpireCache.set "Link to this definition")

    :   Set *key* to *value*. To set a timeout on key use argument [`expire`] (in sec.). If expire is unset the default is taken from [[`ExpireCacheCfg.MAXHOLD_TIME`]](#searx.cache.ExpireCacheCfg.MAXHOLD_TIME "searx.cache.ExpireCacheCfg.MAXHOLD_TIME"). After the timeout has expired, the key will automatically be deleted.

        The [`ctx`] argument specifies the context of the [`key`]. A key is only unique in its context.

        The concrete implementations of this abstraction determine how the context is mapped in the connected database. In SQL databases, for example, the context is a DB table or in a Key/Value DB it could be a prefix for the key.

        If the context is not specified (the default is [`None`]) then a default context should be used, e.g. a default table for SQL databases or a default prefix in a Key/Value DB.

    *[[abstractmethod]][ ]*[[get]][(]*[[key]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *[[default]][[:]][ ][[[Any]](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[ctx]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*[)] [[→] [[[Any]](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")]][[[\[source\]]]](../_modules/searx/cache.html#ExpireCache.get)[¶](#searx.cache.ExpireCache.get "Link to this definition")

    :   Return *value* of *key*. If key is unset, [`None`] is returned.

    *[[abstractmethod]][ ]*[[maintenance]][(]*[[force]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[False]]*, *[[truncate]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[False]]*[)] [[→] [[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")]][[[\[source\]]]](../_modules/searx/cache.html#ExpireCache.maintenance)[¶](#searx.cache.ExpireCache.maintenance "Link to this definition")

    :   Performs maintenance on the cache.

        [`force`]:

        :   Maintenance should be carried out even if the maintenance interval has not yet been reached.

        [`truncate`]:

        :   Truncate the entire cache, which is necessary, for example, if the password has changed.

    *[[abstractmethod]][ ]*[[state]][(][)] [[→] [[[ExpireCacheStats]](#searx.cache.ExpireCacheStats "searx.cache.ExpireCacheStats")]][[[\[source\]]]](../_modules/searx/cache.html#ExpireCache.state)[¶](#searx.cache.ExpireCache.state "Link to this definition")

    :   Returns a [[`ExpireCacheStats`]](#searx.cache.ExpireCacheStats "searx.cache.ExpireCacheStats"), which provides information about the status of the cache.

    *[[static]][ ]*[[build_cache]][(]*[[cfg]][[:]][ ][[[ExpireCacheCfg]](#searx.cache.ExpireCacheCfg "searx.cache.ExpireCacheCfg")]*[)] [[→] [[[ExpireCacheSQLite]](#searx.cache.ExpireCacheSQLite "searx.cache.ExpireCacheSQLite")]][[[\[source\]]]](../_modules/searx/cache.html#ExpireCache.build_cache)[¶](#searx.cache.ExpireCache.build_cache "Link to this definition")

    :   Factory to build a caching instance.

        ::: 
        Note

        Currently, only the SQLite adapter is available, but other database types could be implemented in the future, e.g. a Valkey (Redis) adapter.
        :::

    *[[static]][ ]*[[normalize_name]][(]*[[name]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*[)] [[→] [[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]][[[\[source\]]]](../_modules/searx/cache.html#ExpireCache.normalize_name)[¶](#searx.cache.ExpireCache.normalize_name "Link to this definition")

    :   Returns a normalized name that can be used as a file name or as a SQL table name (is used, for example, to normalize the context name).

    [[secret_hash]][(]*[[name]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[\|]][ ][[bytes]](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")]*[)] [[→] [[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]][[[\[source\]]]](../_modules/searx/cache.html#ExpireCache.secret_hash)[¶](#searx.cache.ExpireCache.secret_hash "Link to this definition")

    :   Creates a hash of the argument [`name`]. The hash value is formed from the [`name`] combined with the [[`password`]](#searx.cache.ExpireCacheCfg.password "searx.cache.ExpireCacheCfg.password"). Can be used, for example, to make the [`key`] stored in the DB unreadable for third parties.

```
<!-- -->
```

*[[class]][ ]*[[searx.cache.]][[ExpireCacheSQLite]][(]*[[cfg]][[:]][ ][[[ExpireCacheCfg]](#searx.cache.ExpireCacheCfg "searx.cache.ExpireCacheCfg")]*[)][[[\[source\]]]](../_modules/searx/cache.html#ExpireCacheSQLite)[¶](#searx.cache.ExpireCacheSQLite "Link to this definition")

:   Cache that manages key/value pairs in a SQLite DB. The DB model in the SQLite DB is implemented in abstract class [[`SQLiteAppl`]](searx.sqlitedb.html#searx.sqlitedb.SQLiteAppl "searx.sqlitedb.SQLiteAppl").

    The following configurations are required / supported:

    -   [[`ExpireCacheCfg.db_url`]](#searx.cache.ExpireCacheCfg.db_url "searx.cache.ExpireCacheCfg.db_url")

    -   [[`ExpireCacheCfg.MAXHOLD_TIME`]](#searx.cache.ExpireCacheCfg.MAXHOLD_TIME "searx.cache.ExpireCacheCfg.MAXHOLD_TIME")

    -   [[`ExpireCacheCfg.MAINTENANCE_PERIOD`]](#searx.cache.ExpireCacheCfg.MAINTENANCE_PERIOD "searx.cache.ExpireCacheCfg.MAINTENANCE_PERIOD")

    -   [[`ExpireCacheCfg.MAINTENANCE_MODE`]](#searx.cache.ExpireCacheCfg.MAINTENANCE_MODE "searx.cache.ExpireCacheCfg.MAINTENANCE_MODE")

    [[DB_SCHEMA]]*[[:]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[=]][ ][1]*[¶](#searx.cache.ExpireCacheSQLite.DB_SCHEMA "Link to this definition")

    :   As soon as changes are made to the DB schema, the version number must be increased. Changes to the version number require the DB to be recreated (or migrated / if an migration path exists and is implemented).

    [[init]][(]*[[conn]][[:]][ ][[[Connection]](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection "(in Python v3.14)")]*[)] [[→] [[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")]][[[\[source\]]]](../_modules/searx/cache.html#ExpireCacheSQLite.init)[¶](#searx.cache.ExpireCacheSQLite.init "Link to this definition")

    :   Initializes the DB schema and properties, is only executed once even if called several times.

        If the initialization has not yet taken place, it is carried out and a True is returned to the caller at the end. If the initialization has already been carried out in the past, False is returned.

    [[maintenance]][(]*[[force]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[False]]*, *[[truncate]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[False]]*[)] [[→] [[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")]][[[\[source\]]]](../_modules/searx/cache.html#ExpireCacheSQLite.maintenance)[¶](#searx.cache.ExpireCacheSQLite.maintenance "Link to this definition")

    :   Performs maintenance on the cache.

        [`force`]:

        :   Maintenance should be carried out even if the maintenance interval has not yet been reached.

        [`truncate`]:

        :   Truncate the entire cache, which is necessary, for example, if the password has changed.

    [[create_table]][(]*[[table]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*[)] [[→] [[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")]][[[\[source\]]]](../_modules/searx/cache.html#ExpireCacheSQLite.create_table)[¶](#searx.cache.ExpireCacheSQLite.create_table "Link to this definition")

    :   Create DB [`table`] if it has not yet been created, no recreates are initiated if the table already exists.

    *[[property]][ ]*[[table_names]]*[[:]][ ][[list]](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[\]]]*[¶](#searx.cache.ExpireCacheSQLite.table_names "Link to this definition")

    :   List of key/value tables already created in the DB.

    *[[property]][ ]*[[next_maintenance_time]]*[[:]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*[¶](#searx.cache.ExpireCacheSQLite.next_maintenance_time "Link to this definition")

    :   Returns (unix epoch) time of the next maintenance.

    [[set]][(]*[[key]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *[[value]][[:]][ ][[[Any]](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")]*, *[[expire]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*, *[[ctx]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*[)] [[→] [[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")]][[[\[source\]]]](../_modules/searx/cache.html#ExpireCacheSQLite.set)[¶](#searx.cache.ExpireCacheSQLite.set "Link to this definition")

    :   Set key/value in DB table given by argument [`ctx`]. If expire is unset the default is taken from [[`ExpireCacheCfg.MAXHOLD_TIME`]](#searx.cache.ExpireCacheCfg.MAXHOLD_TIME "searx.cache.ExpireCacheCfg.MAXHOLD_TIME"). If [`ctx`] argument is [`None`] (the default), a table name is generated from the [[`ExpireCacheCfg.name`]](#searx.cache.ExpireCacheCfg.name "searx.cache.ExpireCacheCfg.name"). If DB table does not exists, it will be created (on demand) by [[`self.create_table`]](#searx.cache.ExpireCacheSQLite.create_table "searx.cache.ExpireCacheSQLite.create_table").

    [[setmany]][(]*[[opt_list]][[:]][ ][[[list]](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[\[]][[tuple]](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][[Any]](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")[[,]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[\]]][[\]]]]*, *[[ctx]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*[)] [[→] [[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]][[[\[source\]]]](../_modules/searx/cache.html#ExpireCacheSQLite.setmany)[¶](#searx.cache.ExpireCacheSQLite.setmany "Link to this definition")

    :   Efficient bootload of the cache from a list of options. The list contains tuples with the arguments described in [[`ExpireCacheSQLite.set`]](#searx.cache.ExpireCacheSQLite.set "searx.cache.ExpireCacheSQLite.set").

    [[get]][(]*[[key]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *[[default]][[:]][ ][[[Any]](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[ctx]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*[)] [[→] [[[Any]](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")]][[[\[source\]]]](../_modules/searx/cache.html#ExpireCacheSQLite.get)[¶](#searx.cache.ExpireCacheSQLite.get "Link to this definition")

    :   Get value of [`key`] from table given by argument [`ctx`]. If [`ctx`] argument is [`None`] (the default), a table name is generated from the [[`ExpireCacheCfg.name`]](#searx.cache.ExpireCacheCfg.name "searx.cache.ExpireCacheCfg.name"). If [`key`] not exists (in table), the [`default`] value is returned.

    [[pairs]][(]*[[ctx]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*[)] [[→] [[[Iterator]](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "(in Python v3.14)")[[\[]][[tuple]](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][[Any]](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")[[\]]][[\]]]]][[[\[source\]]]](../_modules/searx/cache.html#ExpireCacheSQLite.pairs)[¶](#searx.cache.ExpireCacheSQLite.pairs "Link to this definition")

    :   Iterate over key/value pairs from table given by argument [`ctx`]. If [`ctx`] argument is [`None`] (the default), a table name is generated from the [[`ExpireCacheCfg.name`]](#searx.cache.ExpireCacheCfg.name "searx.cache.ExpireCacheCfg.name").

    [[state]][(][)] [[→] [[[ExpireCacheStats]](#searx.cache.ExpireCacheStats "searx.cache.ExpireCacheStats")]][[[\[source\]]]](../_modules/searx/cache.html#ExpireCacheSQLite.state)[¶](#searx.cache.ExpireCacheSQLite.state "Link to this definition")

    :   Returns a [[`ExpireCacheStats`]](#searx.cache.ExpireCacheStats "searx.cache.ExpireCacheStats"), which provides information about the status of the cache.