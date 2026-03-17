# databricks.koalas.DataFrame.last_valid_index

`DataFrame.``last_valid_index`() → Union[int, float, str, bytes, decimal.Decimal, datetime.date, None, Tuple[Union[int, float, str, bytes, decimal.Decimal, datetime.date, None], …]]

Return index for last non-NA/null value.

Returns

scalar, tuple, or None

Notes

This API only works with PySpark >= 3.0.

Examples

Support for DataFrame

```
>>> kdf = ks.DataFrame({'a': [1, 2, 3, None],
...                     'b': [1.0, 2.0, 3.0, None],
...                     'c': [100, 200, 400, None]},
...                     index=['Q', 'W', 'E', 'R'])
>>> kdf
     a    b      c
Q  1.0  1.0  100.0
W  2.0  2.0  200.0
E  3.0  3.0  400.0
R  NaN  NaN    NaN

```