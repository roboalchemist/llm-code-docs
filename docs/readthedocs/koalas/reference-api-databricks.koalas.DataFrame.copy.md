# databricks.koalas.DataFrame.copy

`DataFrame.``copy`(*deep=None*) → databricks.koalas.frame.DataFrame

Make a copy of this object’s indices and data.

Parameters

**deep**None

this parameter is not supported but just dummy parameter to match pandas.

Returns

**copy**DataFrame

Examples

```
>>> df = ks.DataFrame({'x': [1, 2], 'y': [3, 4], 'z': [5, 6], 'w': [7, 8]},
...                   columns=['x', 'y', 'z', 'w'])
>>> df
   x  y  z  w
0  1  3  5  7
1  2  4  6  8
>>> df_copy = df.copy()
>>> df_copy
   x  y  z  w
0  1  3  5  7
1  2  4  6  8

```