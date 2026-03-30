# databricks.koalas.DataFrame.ge

`DataFrame.``ge`(*other*) → databricks.koalas.frame.DataFrame

Compare if the current value is greater than or equal to the other.

```
>>> df = ks.DataFrame({'a': [1, 2, 3, 4],
...                    'b': [1, np.nan, 1, np.nan]},
...                   index=['a', 'b', 'c', 'd'], columns=['a', 'b'])

```