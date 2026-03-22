# databricks.koalas.CategoricalIndex.codes

*property *`CategoricalIndex.``codes`

The category codes of this categorical.

Codes are an Index of integers which are the positions of the actual
values in the categories Index.

There is no setter, use the other categorical methods and the normal item
setter to change values in the categorical.

Returns

Index

A non-writable view of the codes Index.

Examples

```
>>> idx = ks.CategoricalIndex(list("abbccc"))
>>> idx  
CategoricalIndex(['a', 'b', 'b', 'c', 'c', 'c'],
                 categories=['a', 'b', 'c'], ordered=False, dtype='category')

```