# patito.Database.Query.cache_path

Database.Query.cache_path(**args*, ***kwargs*)

Return the path to the parquet cache that would store the result of the query.

Parameters:

- 

**args** (`ParamSpecArgs`) – The positional arguments passed to the wrapped function.

- 

**kwargs** (`ParamSpecKwargs`) – The keyword arguments passed to the wrapped function.

Return type:

`Optional`[`Path`]

Returns:

A deterministic path to a parquet cache. None if caching is disabled.