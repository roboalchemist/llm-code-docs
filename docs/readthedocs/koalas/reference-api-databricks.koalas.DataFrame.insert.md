# databricks.koalas.DataFrame.insert

`DataFrame.``insert`(*loc: int*, *column*, *value: Union[int, float, decimal.Decimal, datetime.date, None, Series, Iterable]*, *allow_duplicates: bool = False*) → None

Insert column into DataFrame at specified location.

Raises a ValueError if column is already contained in the DataFrame,
unless allow_duplicates is set to True.

Parameters

**loc**int

Insertion index. Must verify 0 <= loc <= len(columns).

**column**str, number, or hashable object

Label of the inserted column.

**value**int, Series, or array-like
**allow_duplicates**bool, optional

Examples

```
>>> kdf = ks.DataFrame([1, 2, 3])
>>> kdf.sort_index()
   0
0  1
1  2
2  3
>>> kdf.insert(0, 'x', 4)
>>> kdf.sort_index()
   x  0
0  4  1
1  4  2
2  4  3

```