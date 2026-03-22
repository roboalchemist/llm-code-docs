# databricks.koalas.DataFrame.count

`DataFrame.``count`(*axis: Union[int, str] = None*, *numeric_only: bool = False*) → Union[int, float, str, bytes, decimal.Decimal, datetime.date, None, Series]

Count non-NA cells for each column.

The values None, NaN are considered NA.

Parameters

**axis**{0 or ‘index’, 1 or ‘columns’}, default 0

If 0 or ‘index’ counts are generated for each column. If 1 or ‘columns’ counts are
generated for each row.

**numeric_only**bool, default False

If True, include only float, int, boolean columns. This parameter is mainly for
pandas compatibility.

Returns

**max**scalar for a Series, and a Series for a DataFrame.

See also

`DataFrame.shape`

Number of DataFrame rows and columns (including NA elements).

`DataFrame.isna`

Boolean same-sized DataFrame showing places of NA elements.