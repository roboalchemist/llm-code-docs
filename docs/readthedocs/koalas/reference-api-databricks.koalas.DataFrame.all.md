# databricks.koalas.DataFrame.all

`DataFrame.``all`(*axis: Union[int, str] = 0*) → Series

Return whether all elements are True.

Returns True unless there is at least one element within a series that is
False or equivalent (e.g. zero or empty)

Parameters

**axis**{0 or ‘index’}, default 0

Indicate which axis or axes should be reduced.

- 

0 / ‘index’ : reduce the index, return a Series whose index is the
original column labels.

Returns

Series

Examples

Create a dataframe from a dictionary.

```
>>> df = ks.DataFrame({
...    'col1': [True, True, True],
...    'col2': [True, False, False],
...    'col3': [0, 0, 0],
...    'col4': [1, 2, 3],
...    'col5': [True, True, None],
...    'col6': [True, False, None]},
...    columns=['col1', 'col2', 'col3', 'col4', 'col5', 'col6'])

```