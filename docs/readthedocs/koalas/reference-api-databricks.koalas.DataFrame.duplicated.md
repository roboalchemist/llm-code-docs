# databricks.koalas.DataFrame.duplicated

`DataFrame.``duplicated`(*subset=None*, *keep='first'*) → Series

Return boolean Series denoting duplicate rows, optionally only considering certain columns.

Parameters

**subset**column label or sequence of labels, optional

Only consider certain columns for identifying duplicates,
by default use all of the columns

**keep**{‘first’, ‘last’, False}, default ‘first’

- 

`first` : Mark duplicates as `True` except for the first occurrence.

- 

`last` : Mark duplicates as `True` except for the last occurrence.

- 

False : Mark all duplicates as `True`.

Returns

**duplicated**Series

Examples

```
>>> df = ks.DataFrame({'a': [1, 1, 1, 3], 'b': [1, 1, 1, 4], 'c': [1, 1, 1, 5]},
...                   columns = ['a', 'b', 'c'])
>>> df
   a  b  c
0  1  1  1
1  1  1  1
2  1  1  1
3  3  4  5

```