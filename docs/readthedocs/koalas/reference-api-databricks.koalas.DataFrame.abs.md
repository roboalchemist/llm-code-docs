# databricks.koalas.DataFrame.abs

`DataFrame.``abs`() → Union[DataFrame, Series]

Return a Series/DataFrame with absolute numeric value of each element.

Returns

**abs**Series/DataFrame containing the absolute value of each element.

Examples

Absolute numeric values in a Series.

```
>>> s = ks.Series([-1.10, 2, -3.33, 4])
>>> s.abs()
0    1.10
1    2.00
2    3.33
3    4.00
dtype: float64

```