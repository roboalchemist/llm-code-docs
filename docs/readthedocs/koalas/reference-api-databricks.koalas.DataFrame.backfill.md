# databricks.koalas.DataFrame.backfill

`DataFrame.``backfill`(*axis=None*, *inplace=False*, *limit=None*) → Union[DataFrame, Series]

Synonym for DataFrame.fillna() or Series.fillna() with `method=`bfill``.

Note

the current implementation of ‘bfill’ uses Spark’s Window
without specifying partition specification. This leads to move all data into
single partition in single machine and could cause serious
performance degradation. Avoid this method against very large dataset.