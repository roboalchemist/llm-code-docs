# databricks.koalas.DataFrame.append

`DataFrame.``append`(*other: databricks.koalas.frame.DataFrame*, *ignore_index: bool = False*, *verify_integrity: bool = False*, *sort: bool = False*) → databricks.koalas.frame.DataFrame

Append rows of other to the end of caller, returning a new object.

Columns in other that are not in the caller are added as new columns.

Parameters

**other**DataFrame or Series/dict-like object, or list of these

The data to append.

**ignore_index**boolean, default False

If True, do not use the index labels.

**verify_integrity**boolean, default False

If True, raise ValueError on creating index with duplicates.

**sort**boolean, default False

Currently not supported.

Returns

**appended**DataFrame

Examples

```
>>> df = ks.DataFrame([[1, 2], [3, 4]], columns=list('AB'))

```