# databricks.koalas.DataFrame.describe

`DataFrame.``describe`(*percentiles: Optional[List[float]] = None*) → databricks.koalas.frame.DataFrame

Generate descriptive statistics that summarize the central tendency,
dispersion and shape of a dataset’s distribution, excluding
`NaN` values.

Analyzes both numeric and object series, as well
as `DataFrame` column sets of mixed data types. The output
will vary depending on what is provided. Refer to the notes
below for more detail.

Parameters

**percentiles**list of `float` in range [0.0, 1.0], default [0.25, 0.5, 0.75]

A list of percentiles to be computed.

Returns

DataFrame

Summary statistics of the Dataframe provided.

See also

`DataFrame.count`

Count number of non-NA/null observations.

`DataFrame.max`

Maximum of the values in the object.

`DataFrame.min`

Minimum of the values in the object.

`DataFrame.mean`

Mean of the values.

`DataFrame.std`

Standard deviation of the observations.