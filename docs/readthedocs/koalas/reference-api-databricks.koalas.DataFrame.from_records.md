# databricks.koalas.DataFrame.from_records

*static *`DataFrame.``from_records`(*data: Union[numpy.array, List[tuple], dict, pandas.core.frame.DataFrame]*, *index: Union[str, list, numpy.array] = None*, *exclude: list = None*, *columns: list = None*, *coerce_float: bool = False*, *nrows: int = None*) → databricks.koalas.frame.DataFrame

Convert structured or record ndarray to DataFrame.

Parameters

**data**ndarray (structured dtype), list of tuples, dict, or DataFrame
**index**string, list of fields, array-like

Field of array to use as the index, alternately a specific set of input labels to use

**exclude**sequence, default None

Columns or fields to exclude

**columns**sequence, default None

Column names to use. If the passed data do not have names associated with them, this
argument provides names for the columns. Otherwise this argument indicates the order of
the columns in the result (any names not found in the data will become all-NA columns)

**coerce_float**boolean, default False

Attempt to convert values of non-string, non-numeric objects (like decimal.Decimal) to
floating point, useful for SQL result sets

**nrows**int, default None

Number of rows to read if data is an iterator

Returns

**df**DataFrame

Examples

Use dict as input

```
>>> ks.DataFrame.from_records({'A': [1, 2, 3]})
   A
0  1
1  2
2  3

```