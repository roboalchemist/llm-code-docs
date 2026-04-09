# databricks.koalas.DataFrame.add_suffix

`DataFrame.``add_suffix`(*suffix*) → databricks.koalas.frame.DataFrame

Suffix labels with string suffix.

For Series, the row labels are suffixed.
For DataFrame, the column labels are suffixed.

Parameters

**suffix**str

The string to add before each label.

Returns

DataFrame

New DataFrame with updated labels.

See also

`Series.add_prefix`

Prefix row labels with string prefix.

`Series.add_suffix`

Suffix row labels with string suffix.

`DataFrame.add_prefix`

Prefix column labels with string prefix.