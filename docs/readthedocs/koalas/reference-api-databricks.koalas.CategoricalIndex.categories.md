# databricks.koalas.CategoricalIndex.categories

*property *`CategoricalIndex.``categories`

The categories of this categorical.

Examples

```
>>> idx = ks.CategoricalIndex(list("abbccc"))
>>> idx  
CategoricalIndex(['a', 'b', 'b', 'c', 'c', 'c'],
                 categories=['a', 'b', 'c'], ordered=False, dtype='category')

```