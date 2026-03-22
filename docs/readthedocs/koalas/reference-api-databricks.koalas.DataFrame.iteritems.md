# databricks.koalas.DataFrame.iteritems

`DataFrame.``iteritems`() → Iterator

Iterator over (column name, Series) pairs.

Iterates over the DataFrame columns, returning a tuple with
the column name and the content as a Series.

Returns

**label**object

The column names for the DataFrame being iterated over.

**content**Series

The column entries belonging to each label, as a Series.

Examples

```
>>> df = ks.DataFrame({'species': ['bear', 'bear', 'marsupial'],
...                    'population': [1864, 22000, 80000]},
...                   index=['panda', 'polar', 'koala'],
...                   columns=['species', 'population'])
>>> df
         species  population
panda       bear        1864
polar       bear       22000
koala  marsupial       80000

```