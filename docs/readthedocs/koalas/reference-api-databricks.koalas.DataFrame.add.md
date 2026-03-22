# databricks.koalas.DataFrame.add

`DataFrame.``add`(*other*) → databricks.koalas.frame.DataFrame

Get Addition of dataframe and other, element-wise (binary operator +).

Equivalent to `dataframe + other`. With reverse version, radd.

Among flexible wrappers (add, sub, mul, div) to
arithmetic operators: +, -, *, /, //.

Parameters

**other**scalar

Any single data

Returns

DataFrame

Result of the arithmetic operation.

Examples

```
>>> df = ks.DataFrame({'angles': [0, 3, 4],
...                    'degrees': [360, 180, 360]},
...                   index=['circle', 'triangle', 'rectangle'],
...                   columns=['angles', 'degrees'])
>>> df
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360

```