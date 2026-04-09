# databricks.koalas.DataFrame.aggregate

`DataFrame.``aggregate`(*func: Union[List[str], Dict[Any, List[str]]]*) → Union[Series, DataFrame, Index]

Aggregate using one or more operations over the specified axis.

Parameters

**func**dict or a list

a dict mapping from column name (string) to
aggregate functions (list of strings).
If a list is given, the aggregation is performed against
all columns.

Returns

DataFrame

See also

`DataFrame.apply`

Invoke function on DataFrame.

`DataFrame.transform`

Only perform transforming type operations.

`DataFrame.groupby`

Perform operations over groups.

`Series.aggregate`

The equivalent function for Series.