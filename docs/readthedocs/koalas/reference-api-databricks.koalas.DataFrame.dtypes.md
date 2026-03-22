# databricks.koalas.DataFrame.dtypes

*property *`DataFrame.``dtypes`

Return the dtypes in the DataFrame.

This returns a Series with the data type of each column. The result’s index is the original
DataFrame’s columns. Columns with mixed types are stored with the object dtype.

Returns

pd.Series

The data type of each column.

Examples

```
>>> df = ks.DataFrame({'a': list('abc'),
...                    'b': list(range(1, 4)),
...                    'c': np.arange(3, 6).astype('i1'),
...                    'd': np.arange(4.0, 7.0, dtype='float64'),
...                    'e': [True, False, True],
...                    'f': pd.date_range('20130101', periods=3)},
...                   columns=['a', 'b', 'c', 'd', 'e', 'f'])
>>> df.dtypes
a            object
b             int64
c              int8
d           float64
e              bool
f    datetime64[ns]
dtype: object

```