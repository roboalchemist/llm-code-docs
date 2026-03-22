# databricks.koalas.DataFrame.iloc

*property *`DataFrame.``iloc`

Purely integer-location based indexing for selection by position.

`.iloc[]` is primarily integer position based (from `0` to
`length-1` of the axis), but may also be used with a conditional boolean Series.

Allowed inputs are:

- 

An integer for column selection, e.g. `5`.

- 

A list or array of integers for row selection with distinct index values,
e.g. `[3, 4, 0]`

- 

A list or array of integers for column selection, e.g. `[4, 3, 0]`.

- 

A boolean array for column selection.

- 

A slice object with ints for row and column selection, e.g. `1:7`.

Not allowed inputs which pandas allows are:

- 

A list or array of integers for row selection with duplicated indexes,
e.g. `[4, 4, 0]`.

- 

A boolean array for row selection.

- 

A `callable` function with one argument (the calling Series, DataFrame
or Panel) and that returns valid output for indexing (one of the above).
This is useful in method chains, when you don’t have a reference to the
calling object, but would like to base your selection on some value.

`.iloc` will raise `IndexError` if a requested indexer is
out-of-bounds, except *slice* indexers which allow out-of-bounds
indexing (this conforms with python/numpy *slice* semantics).

See also

`DataFrame.loc`

Purely label-location based indexer for selection by label.

`Series.iloc`

Purely integer-location based indexing for selection by position.