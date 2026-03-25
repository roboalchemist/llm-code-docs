# patito.Database.Query

*class *patito.database.DatabaseQuery(*query_constructor*, *cache_directory*, *query_handler*, *ttl*, *lazy=False*, *cache=False*, *model=None*, *query_handler_kwargs=None*)

A class acting as a function that returns a polars.DataFrame when called.

Methods

- cache_path

- clear_caches

- query_string

- refresh_cache

- __call__