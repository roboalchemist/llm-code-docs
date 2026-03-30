# databricks.koalas.DataFrame.align

`DataFrame.``align`(*other: Union[DataFrame, Series]*, *join: str = 'outer'*, *axis: Union[str, int, None] = None*, *copy: bool = True*) → Tuple[DataFrame, Union[DataFrame, Series]]

Align two objects on their axes with the specified join method.

Join method is specified for each axis Index.

Parameters

**other**DataFrame or Series
**join**{{‘outer’, ‘inner’, ‘left’, ‘right’}}, default ‘outer’
**axis**allowed axis of the other object, default None

Align on index (0), columns (1), or both (None).

**copy**bool, default True

Always returns new objects. If copy=False and no reindexing is
required then original objects are returned.

Returns

**(left, right)**(DataFrame, type of other)

Aligned objects.

Examples

```
>>> ks.set_option("compute.ops_on_diff_frames", True)
>>> df1 = ks.DataFrame({"a": [1, 2, 3], "b": ["a", "b", "c"]}, index=[10, 20, 30])
>>> df2 = ks.DataFrame({"a": [4, 5, 6], "c": ["d", "e", "f"]}, index=[10, 11, 12])

```