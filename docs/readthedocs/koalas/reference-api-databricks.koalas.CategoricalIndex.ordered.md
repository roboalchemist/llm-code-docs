# databricks.koalas.CategoricalIndex.ordered

*property *`CategoricalIndex.``ordered`

Whether the categories have an ordered relationship.

Examples

```
>>> idx = ks.CategoricalIndex(list("abbccc"))
>>> idx  
CategoricalIndex(['a', 'b', 'b', 'c', 'c', 'c'],
                 categories=['a', 'b', 'c'], ordered=False, dtype='category')

```