# databricks.koalas.DataFrame.cumprod

`DataFrame.``cumprod`(*skipna: bool = True*) → Union[Series, DataFrame]

Return cumulative product over a DataFrame or Series axis.

Returns a DataFrame or Series of the same size containing the cumulative product.

Note

the current implementation of cumprod uses Spark’s Window without
specifying partition specification. This leads to move all data into
single partition in single machine and could cause serious
performance degradation. Avoid this method against very large dataset.