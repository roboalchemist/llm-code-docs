# databricks.koalas.DataFrame.expanding

`DataFrame.``expanding`(*min_periods=1*) → databricks.koalas.window.Expanding

Provide expanding transformations.

Note

‘min_periods’ in Koalas works as a fixed window size unlike pandas.
Unlike pandas, NA is also counted as the period. This might be changed
in the near future.