# databricks.koalas.DataFrame.fillna

`DataFrame.``fillna`(*value=None*, *method=None*, *axis=None*, *inplace=False*, *limit=None*) → Optional[databricks.koalas.frame.DataFrame]

Fill NA/NaN values.

Note

the current implementation of ‘method’ parameter in fillna uses Spark’s Window
without specifying partition specification. This leads to move all data into
single partition in single machine and could cause serious
performance degradation. Avoid this method against very large dataset.