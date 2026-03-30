# databricks.koalas.DataFrame.groupby

`DataFrame.``groupby`(*by*, *axis=0*, *as_index: bool = True*, *dropna: bool = True*) → Union[DataFrameGroupBy, SeriesGroupBy]

Group DataFrame or Series using a Series of columns.

A groupby operation involves some combination of splitting the
object, applying a function, and combining the results. This can be
used to group large amounts of data and compute operations on these
groups.

Parameters

**by**Series, label, or list of labels

Used to determine the groups for the groupby.
If Series is passed, the Series or dict VALUES
will be used to determine the groups. A label or list of
labels may be passed to group by the columns in `self`.

**axis**int, default 0 or ‘index’

Can only be set to 0 at the moment.

**as_index**bool, default True

For aggregated output, return object with group labels as the
index. Only relevant for DataFrame input. as_index=False is
effectively “SQL-style” grouped output.

**dropna**bool, default True

If True, and if group keys contain NA values,
NA values together with row/column will be dropped.
If False, NA values will also be treated as the key in groups.

Returns

DataFrameGroupBy or SeriesGroupBy

Depends on the calling object and returns groupby object that
contains information about the groups.

See also

`koalas.groupby.GroupBy`