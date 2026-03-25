# databricks.koalas.DataFrame.applymap

`DataFrame.``applymap`(*func*) → databricks.koalas.frame.DataFrame

Apply a function to a Dataframe elementwise.

This method applies a function that accepts and returns a scalar
to every element of a DataFrame.

Note

this API executes the function once to infer the type which is
potentially expensive, for instance, when the dataset is created after
aggregations or sorting.

To avoid this, specify return type in `func`, for instance, as below:

```
>>> def square(x) -> np.int32:
...     return x ** 2

```