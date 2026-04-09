# databricks.koalas.DataFrame.diff

`DataFrame.``diff`(*periods: int = 1*, *axis: Union[int, str] = 0*) → databricks.koalas.frame.DataFrame

First discrete difference of element.

Calculates the difference of a DataFrame element compared with another element in the
DataFrame (default is the element in the same column of the previous row).

Note

the current implementation of diff uses Spark’s Window without
specifying partition specification. This leads to move all data into
single partition in single machine and could cause serious
performance degradation. Avoid this method against very large dataset.