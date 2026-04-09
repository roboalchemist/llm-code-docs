# databricks.koalas.DataFrame.any

`DataFrame.``any`(*axis: Union[int, str] = 0*) → Series

Return whether any element is True.

Returns False unless there is at least one element within a series that is
True or equivalent (e.g. non-zero or non-empty).

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
...    'col1': [False, False, False],
...    'col2': [True, False, False],
...    'col3': [0, 0, 1],
...    'col4': [0, 1, 2],
...    'col5': [False, False, None],
...    'col6': [True, False, None]},
...    columns=['col1', 'col2', 'col3', 'col4', 'col5', 'col6'])

```