# databricks.koalas.DataFrame.idxmax

`DataFrame.``idxmax`(*axis=0*) → Series

Return index of first occurrence of maximum over requested axis.
NA/null values are excluded.

Note

This API collect all rows with maximum value using to_pandas()
because we suppose the number of rows with max values are usually small in general.