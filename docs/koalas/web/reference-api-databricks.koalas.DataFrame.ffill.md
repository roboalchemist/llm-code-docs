# databricks.koalas.DataFrame.ffill

`DataFrame.``ffill`(*axis=None*, *inplace=False*, *limit=None*) → Union[DataFrame, Series]

Synonym for DataFrame.fillna() or Series.fillna() with `method=`ffill``.

Note

the current implementation of ‘ffill’ uses Spark’s Window
without specifying partition specification. This leads to move all data into
single partition in single machine and could cause serious
performance degradation. Avoid this method against very large dataset.