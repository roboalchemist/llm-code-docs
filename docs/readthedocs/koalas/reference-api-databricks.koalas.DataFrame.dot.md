# databricks.koalas.DataFrame.dot

`DataFrame.``dot`(*other: Series*) → Series

Compute the matrix multiplication between the DataFrame and other.

This method computes the matrix product between the DataFrame and the
values of an other Series

It can also be called using `self @ other` in Python >= 3.5.

Note

This method is based on an expensive operation due to the nature
of big data. Internally it needs to generate each row for each value, and
then group twice - it is a huge operation. To prevent misusage, this method
has the ‘compute.max_rows’ default limit of input length, and raises a ValueError.

```
>>> from databricks.koalas.config import option_context
>>> with option_context(
...     'compute.max_rows', 1000, "compute.ops_on_diff_frames", True
... ):  
...     kdf = ks.DataFrame({'a': range(1001)})
...     kser = ks.Series([2], index=['a'])
...     kdf.dot(kser)
Traceback (most recent call last):
  ...
ValueError: Current DataFrame has more then the given limit 1000 rows.
Please set 'compute.max_rows' by using 'databricks.koalas.config.set_option'
to retrieve to retrieve more than 1000 rows. Note that, before changing the
'compute.max_rows', this operation is considerably expensive.

```