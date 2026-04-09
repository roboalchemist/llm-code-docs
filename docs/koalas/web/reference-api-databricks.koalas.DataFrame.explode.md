# databricks.koalas.DataFrame.explode

`DataFrame.``explode`(*column*) → databricks.koalas.frame.DataFrame

Transform each element of a list-like to a row, replicating index values.

Parameters

**column**str or tuple

Column to explode.

Returns

DataFrame

Exploded lists to rows of the subset columns;
index will be duplicated for these rows.

See also

`DataFrame.unstack`

Pivot a level of the (necessarily hierarchical) index labels.

`DataFrame.melt`

Unpivot a DataFrame from wide format to long format.