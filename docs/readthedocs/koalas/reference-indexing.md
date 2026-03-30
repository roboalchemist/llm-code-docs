# Index objects

## Index

`Index`

Koalas Index that corresponds to pandas Index logically.

### Properties

`Index.is_monotonic`

Return boolean if values in the object are monotonically increasing.

`Index.is_monotonic_increasing`

Return boolean if values in the object are monotonically increasing.

`Index.is_monotonic_decreasing`

Return boolean if values in the object are monotonically decreasing.

`Index.is_unique`

Return if the index has unique values.

`Index.has_duplicates`

If index has duplicates, return True, otherwise False.

`Index.hasnans`

Return True if it has any missing values.

`Index.dtype`

Return the dtype object of the underlying data.

`Index.inferred_type`

Return a string of the type inferred from the values.

`Index.is_all_dates`

Return if all data types of the index are datetime.

`Index.shape`

Return a tuple of the shape of the underlying data.

`Index.name`

Return name of the Index.

`Index.names`

Return names of the Index.

`Index.ndim`

Return an int representing the number of array dimensions.

`Index.size`

Return an int representing the number of elements in this object.

`Index.nlevels`

Number of levels in Index & MultiIndex.

`Index.empty`

Returns true if the current object is empty.

`Index.T`

Return the transpose, For index, It will be index itself.

`Index.values`

Return an array representing the data in the Index.