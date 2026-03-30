# databricks.koalas.DataFrame.koalas.transform_batch

`koalas.``transform_batch`(*func*, **args*, ***kwargs*) → Union[DataFrame, Series]

Transform chunks with a function that takes pandas DataFrame and outputs pandas DataFrame.
The pandas DataFrame given to the function is of a batch used internally. The length of
each input and output should be the same.

See also Transform and apply a function [https://koalas.readthedocs.io/en/latest/user_guide/transform_apply.html].

Note

the func is unable to access to the whole input frame. Koalas internally
splits the input series into multiple batches and calls func with each batch multiple
times. Therefore, operations such as global aggregations are impossible. See the example
below.

```
>>> # This case does not return the length of whole frame but of the batch internally
... # used.
... def length(pdf) -> ks.DataFrame[int]:
...     return pd.DataFrame([len(pdf)] * len(pdf))
...
>>> df = ks.DataFrame({'A': range(1000)})
>>> df.koalas.transform_batch(length)  
    c0
0   83
1   83
2   83
...

```