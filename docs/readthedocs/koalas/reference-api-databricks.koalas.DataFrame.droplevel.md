# databricks.koalas.DataFrame.droplevel

`DataFrame.``droplevel`(*level*, *axis=0*) → databricks.koalas.frame.DataFrame

Return DataFrame with requested index / column level(s) removed.

Parameters

**level: int, str, or list-like**

If a string is given, must be the name of a level If list-like, elements must
be names or positional indexes of levels.

**axis: {0 or ‘index’, 1 or ‘columns’}, default 0**

Returns

DataFrame with requested index / column level(s) removed.

Examples

```
>>> df = ks.DataFrame(
...     [[3, 4], [7, 8], [11, 12]],
...     index=pd.MultiIndex.from_tuples([(1, 2), (5, 6), (9, 10)], names=["a", "b"]),
... )

```