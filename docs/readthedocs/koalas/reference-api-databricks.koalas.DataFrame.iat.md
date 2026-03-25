# databricks.koalas.DataFrame.iat

*property *`DataFrame.``iat`

Access a single value for a row/column pair by integer position.

Similar to `iloc`, in that both provide integer-based lookups. Use
`iat` if you only need to get or set a single value in a DataFrame
or Series.

Raises

KeyError

When label does not exist in DataFrame

Examples

```
>>> df = ks.DataFrame([[0, 2, 3], [0, 4, 1], [10, 20, 30]],
...                   columns=['A', 'B', 'C'])
>>> df
    A   B   C
0   0   2   3
1   0   4   1
2  10  20  30

```