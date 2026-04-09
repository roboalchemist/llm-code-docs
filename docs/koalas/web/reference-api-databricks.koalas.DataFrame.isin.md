# databricks.koalas.DataFrame.isin

`DataFrame.``isin`(*values*) → databricks.koalas.frame.DataFrame

Whether each element in the DataFrame is contained in values.

Parameters

**values**iterable or dict

The sequence of values to test. If values is a dict,
the keys must be the column names, which must match.
Series and DataFrame are not supported.

Returns

DataFrame

DataFrame of booleans showing whether each element in the DataFrame
is contained in values.

Examples

```
>>> df = ks.DataFrame({'num_legs': [2, 4], 'num_wings': [2, 0]},
...                   index=['falcon', 'dog'],
...                   columns=['num_legs', 'num_wings'])
>>> df
        num_legs  num_wings
falcon         2          2
dog            4          0

```