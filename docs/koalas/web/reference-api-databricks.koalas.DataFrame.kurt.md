# databricks.koalas.DataFrame.kurt

`DataFrame.``kurt`(*axis: Union[int, str] = None*, *numeric_only: bool = None*) → Union[int, float, str, bytes, decimal.Decimal, datetime.date, None, Series]

Return unbiased kurtosis using Fisher’s definition of kurtosis (kurtosis of normal == 0.0).
Normalized by N-1.

Parameters

**axis**{index (0), columns (1)}

Axis for the function to be applied on.

**numeric_only**bool, default None

Include only float, int, boolean columns. False is not supported. This parameter
is mainly for pandas compatibility.

Returns

**kurt**scalar for a Series, and a Series for a DataFrame.

Examples

```
>>> df = ks.DataFrame({'a': [1, 2, 3, np.nan], 'b': [0.1, 0.2, 0.3, np.nan]},
...                   columns=['a', 'b'])

```