# databricks.koalas.DataFrame.assign

`DataFrame.``assign`(***kwargs*) → databricks.koalas.frame.DataFrame

Assign new columns to a DataFrame.

Returns a new object with all original columns in addition to new ones.
Existing columns that are re-assigned will be overwritten.

Parameters

****kwargs**dict of {str: callable, Series or Index}

The column names are keywords. If the values are
callable, they are computed on the DataFrame and
assigned to the new columns. The callable must not
change input DataFrame (though Koalas doesn’t check it).
If the values are not callable, (e.g. a Series or a literal),
they are simply assigned.

Returns

DataFrame

A new DataFrame with the new columns in addition to
all the existing columns.

Notes

Assigning multiple columns within the same `assign` is possible
but you cannot refer to newly created or modified columns. This
feature is supported in pandas for Python 3.6 and later but not in
Koalas. In Koalas, all items are computed first, and then assigned.

Examples

```
>>> df = ks.DataFrame({'temp_c': [17.0, 25.0]},
...                   index=['Portland', 'Berkeley'])
>>> df
          temp_c
Portland    17.0
Berkeley    25.0

```