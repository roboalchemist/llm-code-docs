# databricks.koalas.DataFrame.first_valid_index

`DataFrame.``first_valid_index`() → Union[int, float, str, bytes, decimal.Decimal, datetime.date, None, Tuple[Union[int, float, str, bytes, decimal.Decimal, datetime.date, None], …]]

Retrieves the index of the first valid value.

Returns

scalar, tuple, or None

Examples

Support for DataFrame

```
>>> kdf = ks.DataFrame({'a': [None, 2, 3, 2],
...                     'b': [None, 2.0, 3.0, 1.0],
...                     'c': [None, 200, 400, 200]},
...                     index=['Q', 'W', 'E', 'R'])
>>> kdf
     a    b      c
Q  NaN  NaN    NaN
W  2.0  2.0  200.0
E  3.0  3.0  400.0
R  2.0  1.0  200.0

```