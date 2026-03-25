# databricks.koalas.DataFrame.join

`DataFrame.``join`(*right: databricks.koalas.frame.DataFrame*, *on: Union[Any, List[Any], Tuple, List[Tuple], None] = None*, *how: str = 'left'*, *lsuffix: str = ''*, *rsuffix: str = ''*) → databricks.koalas.frame.DataFrame

Join columns of another DataFrame.

Join columns with right DataFrame either on index or on a key column. Efficiently join
multiple DataFrame objects by index at once by passing a list.

Parameters

**right: DataFrame, Series**
**on: str, list of str, or array-like, optional**

Column or index level name(s) in the caller to join on the index in right, otherwise
joins index-on-index. If multiple values given, the right DataFrame must have a
MultiIndex. Can pass an array as the join key if it is not already contained in the
calling DataFrame. Like an Excel VLOOKUP operation.

**how: {‘left’, ‘right’, ‘outer’, ‘inner’}, default ‘left’**

How to handle the operation of the two objects.

- 

left: use left frame’s index (or column if on is specified).

- 

right: use right’s index.

- 

outer: form union of left frame’s index (or column if on is specified) with
right’s index, and sort it. lexicographically.

- 

inner: form intersection of left frame’s index (or column if on is specified)
with right’s index, preserving the order of the left’s one.

**lsuffix**str, default ‘’

Suffix to use from left frame’s overlapping columns.

**rsuffix**str, default ‘’

Suffix to use from right frame’s overlapping columns.

Returns

DataFrame

A dataframe containing columns from both the left and right.

See also

`DataFrame.merge`

For column(s)-on-columns(s) operations.

`DataFrame.update`

Modify in place using non-NA values from another DataFrame.

`DataFrame.hint`

Specifies some hint on the current DataFrame.

`broadcast`

Marks a DataFrame as small enough for use in broadcast joins.