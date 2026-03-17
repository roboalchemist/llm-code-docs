# databricks.koalas.DataFrame.dropna

`DataFrame.``dropna`(*axis=0*, *how='any'*, *thresh=None*, *subset=None*, *inplace=False*) → Optional[databricks.koalas.frame.DataFrame]

Remove missing values.

Parameters

**axis**{0 or ‘index’}, default 0

Determine if rows or columns which contain missing values are
removed.

- 

0, or ‘index’ : Drop rows which contain missing values.

**how**{‘any’, ‘all’}, default ‘any’

Determine if row or column is removed from DataFrame, when we have
at least one NA or all NA.

- 

‘any’ : If any NA values are present, drop that row or column.

- 

‘all’ : If all values are NA, drop that row or column.

**thresh**int, optional

Require that many non-NA values.

**subset**array-like, optional

Labels along other axis to consider, e.g. if you are dropping rows
these would be a list of columns to include.

**inplace**bool, default False

If True, do operation inplace and return None.

Returns

DataFrame

DataFrame with NA entries dropped from it.

See also

`DataFrame.drop`

Drop specified labels from columns.

`DataFrame.isnull`

Indicate missing values.

`DataFrame.notnull`

Indicate existing (non-missing) values.