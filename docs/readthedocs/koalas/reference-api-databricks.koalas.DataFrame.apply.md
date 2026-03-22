# databricks.koalas.DataFrame.apply

`DataFrame.``apply`(*func*, *axis=0*, *args=()*, ***kwds*) → Union[Series, DataFrame, Index]

Apply a function along an axis of the DataFrame.

Objects passed to the function are Series objects whose index is
either the DataFrame’s index (`axis=0`) or the DataFrame’s columns
(`axis=1`).

See also Transform and apply a function [https://koalas.readthedocs.io/en/latest/user_guide/transform_apply.html].

Note

when axis is 0 or ‘index’, the func is unable to access
to the whole input series. Koalas internally splits the input series into multiple
batches and calls func with each batch multiple times. Therefore, operations
such as global aggregations are impossible. See the example below.

```
>>> # This case does not return the length of whole series but of the batch internally
... # used.
... def length(s) -> int:
...     return len(s)
...
>>> df = ks.DataFrame({'A': range(1000)})
>>> df.apply(length, axis=0)  
0     83
1     83
2     83
...
10    83
11    83
dtype: int32

```