# databricks.koalas.DataFrame.isna

`DataFrame.``isna`() → databricks.koalas.frame.DataFrame

Detects missing values for items in the current Dataframe.

Return a boolean same-sized Dataframe indicating if the values are NA.
NA values, such as None or numpy.NaN, gets mapped to True values.
Everything else gets mapped to False values.

See also

`DataFrame.notnull`