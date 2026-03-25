# databricks.koalas.DataFrame.idxmin

`DataFrame.``idxmin`(*axis=0*) → Series

Return index of first occurrence of minimum over requested axis.
NA/null values are excluded.

Note

This API collect all rows with minimum value using to_pandas()
because we suppose the number of rows with min values are usually small in general.