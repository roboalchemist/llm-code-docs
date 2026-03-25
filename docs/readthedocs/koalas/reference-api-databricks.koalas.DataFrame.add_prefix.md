# databricks.koalas.DataFrame.add_prefix

`DataFrame.``add_prefix`(*prefix*) → databricks.koalas.frame.DataFrame

Prefix labels with string prefix.

For Series, the row labels are prefixed.
For DataFrame, the column labels are prefixed.

Parameters

**prefix**str

The string to add before each label.

Returns

DataFrame

New DataFrame with updated labels.

See also

`Series.add_prefix`

Prefix row labels with string prefix.

`Series.add_suffix`

Suffix row labels with string suffix.

`DataFrame.add_suffix`

Suffix column labels with string suffix.