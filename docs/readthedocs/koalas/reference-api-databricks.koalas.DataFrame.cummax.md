# databricks.koalas.DataFrame.cummax

`DataFrame.``cummax`(*skipna: bool = True*) → Union[Series, DataFrame]

Return cumulative maximum over a DataFrame or Series axis.

Returns a DataFrame or Series of the same size containing the cumulative maximum.

Note

the current implementation of cummax uses Spark’s Window without
specifying partition specification. This leads to move all data into
single partition in single machine and could cause serious
performance degradation. Avoid this method against very large dataset.