# patito.Database.Query.refresh_cache

Database.Query.refresh_cache(**args*, ***kwargs*)

Force query execution by refreshing the cache.

Parameters:

- 

***args** (`ParamSpecArgs`) – Positional arguments used to construct the SQL query string.

- 

***kwargs** (`ParamSpecKwargs`) – Keyword arguments used to construct the SQL query string.

Return type:

`TypeVar`(`DF`, bound= `Union`[`DataFrame`, `LazyFrame`], covariant=True)

Returns:

A DataFrame representing the result of the newly executed query.