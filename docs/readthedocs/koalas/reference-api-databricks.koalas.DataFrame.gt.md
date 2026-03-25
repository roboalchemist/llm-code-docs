# databricks.koalas.DataFrame.gt

`DataFrame.``gt`(*other*) → databricks.koalas.frame.DataFrame

Compare if the current value is greater than the other.

```
>>> df = ks.DataFrame({'a': [1, 2, 3, 4],
...                    'b': [1, np.nan, 1, np.nan]},
...                   index=['a', 'b', 'c', 'd'], columns=['a', 'b'])

```