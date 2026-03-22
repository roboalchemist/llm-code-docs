# databricks.koalas.DataFrame.T

*property *`DataFrame.``T`

Transpose index and columns.

Reflect the DataFrame over its main diagonal by writing rows as columns
and vice-versa. The property `T` is an accessor to the method
`transpose()`.

Note

This method is based on an expensive operation due to the nature
of big data. Internally it needs to generate each row for each value, and
then group twice - it is a huge operation. To prevent misusage, this method
has the ‘compute.max_rows’ default limit of input length, and raises a ValueError.

```
>>> from databricks.koalas.config import option_context
>>> with option_context('compute.max_rows', 1000):  
...     ks.DataFrame({'a': range(1001)}).transpose()
Traceback (most recent call last):
  ...
ValueError: Current DataFrame has more then the given limit 1000 rows.
Please set 'compute.max_rows' by using 'databricks.koalas.config.set_option'
to retrieve to retrieve more than 1000 rows. Note that, before changing the
'compute.max_rows', this operation is considerably expensive.

```