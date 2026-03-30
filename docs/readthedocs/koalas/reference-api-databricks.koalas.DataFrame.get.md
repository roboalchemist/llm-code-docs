# databricks.koalas.DataFrame.get

`DataFrame.``get`(*key*, *default=None*) → Any

Get item from object for given key (DataFrame column, Panel slice,
etc.). Returns default value if not found.

Parameters

**key**object

Returns

**value**same type as items contained in object

Examples

```
>>> df = ks.DataFrame({'x':range(3), 'y':['a','b','b'], 'z':['a','b','b']},
...                   columns=['x', 'y', 'z'], index=[10, 20, 20])
>>> df
    x  y  z
10  0  a  a
20  1  b  b
20  2  b  b

```