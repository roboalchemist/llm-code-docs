# databricks.koalas.DataFrame.axes

*property *`DataFrame.``axes`

Return a list representing the axes of the DataFrame.

It has the row axis labels and column axis labels as the only members.
They are returned in that order.

Examples

```
>>> df = ks.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
>>> df.axes
[Int64Index([0, 1], dtype='int64'), Index(['col1', 'col2'], dtype='object')]

```