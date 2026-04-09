# databricks.koalas.DataFrame.astype

`DataFrame.``astype`(*dtype*) → databricks.koalas.frame.DataFrame

Cast a Koalas object to a specified dtype `dtype`.

Parameters

**dtype**data type, or dict of column name -> data type

Use a numpy.dtype or Python type to cast entire Koalas object to
the same type. Alternatively, use {col: dtype, …}, where col is a
column label and dtype is a numpy.dtype or Python type to cast one
or more of the DataFrame’s columns to column-specific types.

Returns

**casted**same type as caller

See also

`to_datetime`

Convert argument to datetime.