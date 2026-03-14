# patito.Database.as_query

Database.as_query(***, *lazy=False*, *cache=False*, *ttl=None*, *model=None*, ***kwargs*)

Execute the returned query string and return a polars dataframe.

Parameters:

- 

**lazy** (`bool`) – If the result should be returned as a LazyFrame rather than a
DataFrame. Allows more efficient reading from parquet caches if caching
is enabled.

- 

**cache** (`Union`[`str`, `Path`, `bool`]) – If queries should be cached in order to save time and costs.
The cache will only be used if the exact same SQL string has
been executed before.
If the parameter is specified as `True`, a parquet file is
created for each unique query string, and is located at:
artifacts/query_cache/<function_name>/<query_md5_hash>.parquet
If the a string or `pathlib.Path` object is provided, the given path
will be used, but it must have a ‘.parquet’ file extension.
Relative paths are interpreted relative to artifacts/query_cache/
in the workspace root. The given parquet path will be overwritten
if the query string changes, so only the latest query string value
will be cached.

- 

**ttl** (`Optional`[`timedelta`]) – The Time to Live (TTL) of the cache specified as a datetime.timedelta
object. When the cache becomes older than the specified TTL, the query
will be re-executed on the next invocation of the query function
and the cache will refreshed.

- 

**model** (`Optional`[`Type`[`Model`]]) – An optional Patito model used to validate the content of the
dataframe before return.

- 

****kwargs** (`Any`) – Connection parameters forwarded to sql_to_polars, for example
db_params.

Return type:

`Callable`[[`QueryConstructor`[`ParamSpec`(`P`)]], `DatabaseQuery`[`ParamSpec`(`P`), `Union`[`DataFrame`, `LazyFrame`]]]

Returns:

A new function which returns a polars DataFrame based on the query
specified by the original function’s return string.