# databricks.koalas.DataFrame.info

`DataFrame.``info`(*verbose=None*, *buf=None*, *max_cols=None*, *null_counts=None*) → None

Print a concise summary of a DataFrame.

This method prints information about a DataFrame including
the index dtype and column dtypes, non-null values and memory usage.

Parameters

**verbose**bool, optional

Whether to print the full summary.

**buf**writable buffer, defaults to sys.stdout

Where to send the output. By default, the output is printed to
sys.stdout. Pass a writable buffer if you need to further process
the output.

**max_cols**int, optional

When to switch from the verbose to the truncated output. If the
DataFrame has more than max_cols columns, the truncated output
is used.

**null_counts**bool, optional

Whether to show the non-null counts.

Returns

None

This method prints a summary of a DataFrame and returns None.

See also

`DataFrame.describe`

Generate descriptive statistics of DataFrame columns.