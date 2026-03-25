# databricks.koalas.DataFrame.keys

`DataFrame.``keys`() → pandas.core.indexes.base.Index

Return alias for columns.

Returns

Index

Columns of the DataFrame.

Examples

```
>>> df = ks.DataFrame([[1, 2], [4, 5], [7, 8]],
...                   index=['cobra', 'viper', 'sidewinder'],
...                   columns=['max_speed', 'shield'])
>>> df
            max_speed  shield
cobra               1       2
viper               4       5
sidewinder          7       8

```