# databricks.koalas.DataFrame.iterrows

`DataFrame.``iterrows`() → Iterator

Iterate over DataFrame rows as (index, Series) pairs.

Yields

**index**label or tuple of label

The index of the row. A tuple for a MultiIndex.

**data**pandas.Series

The data of the row as a Series.

**it**generator

A generator that iterates over the rows of the frame.

Notes

- 

Because `iterrows` returns a Series for each row,
it does **not** preserve dtypes across the rows (dtypes are
preserved across columns for DataFrames). For example,

```
>>> df = ks.DataFrame([[1, 1.5]], columns=['int', 'float'])
>>> row = next(df.iterrows())[1]
>>> row
int      1.0
float    1.5
Name: 0, dtype: float64
>>> print(row['int'].dtype)
float64
>>> print(df['int'].dtype)
int64

```