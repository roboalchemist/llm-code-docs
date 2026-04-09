# patito.Database

*class *patito.Database(*query_handler*, *cache_directory=None*, *default_ttl=datetime.timedelta(days=364)*)

Construct manager for executing SQL queries and caching the results.

Parameters:

- 

**query_handler** (`Callable`[`...`, `Table`]) – The function that the Database object should use for executing
SQL queries. Its first argument should be the SQL query string to execute,
and it should return the query result as an arrow table, for instance
pyarrow.Table.

- 

**cache_directory** (`Optional`[`Path`]) – Path to the directory where caches should be stored as parquet
files. If not provided, the XDG [https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html] Base Directory Specification will be
used to determine the suitable cache directory, by default
`~/.cache/patito` or `${XDG_CACHE_HOME}/patito`.

- 

**default_ttl** (`timedelta`) – The default Time To Live (TTL), or with other words, how long to
wait until caches are refreshed due to old age. The given default TTL can be
overwritten by specifying the `ttl` parameter in
`Database.query()`. The default is 52 weeks.

Examples

We start by importing the necessary modules:

```
>>> from pathlib import Path
...
>>> import patito as pt
>>> import pyarrow as pa

```