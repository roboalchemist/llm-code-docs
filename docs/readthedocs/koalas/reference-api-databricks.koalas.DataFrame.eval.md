# databricks.koalas.DataFrame.eval

`DataFrame.``eval`(*expr*, *inplace=False*) → Union[DataFrame, Series, None]

Evaluate a string describing operations on DataFrame columns.

Operates on columns only, not specific rows or elements. This allows
eval to run arbitrary code, which can make you vulnerable to code
injection if you pass user input to this function.

Parameters

**expr**str

The expression string to evaluate.

**inplace**bool, default False

If the expression contains an assignment, whether to perform the
operation inplace and mutate the existing DataFrame. Otherwise,
a new DataFrame is returned.

Returns

The result of the evaluation.

See also

`DataFrame.query`

Evaluates a boolean expression to query the columns of a frame.

`DataFrame.assign`

Can evaluate an expression or function to create new values for a column.

`eval`

Evaluate a Python expression as a string using various backends.