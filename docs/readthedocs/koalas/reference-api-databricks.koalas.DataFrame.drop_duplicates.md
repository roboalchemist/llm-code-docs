# databricks.koalas.DataFrame.drop_duplicates

`DataFrame.``drop_duplicates`(*subset=None*, *keep='first'*, *inplace=False*) → Optional[databricks.koalas.frame.DataFrame]

Return DataFrame with duplicate rows removed, optionally only
considering certain columns.

Parameters

**subset**column label or sequence of labels, optional

Only consider certain columns for identifying duplicates, by
default use all of the columns.

**keep**{‘first’, ‘last’, False}, default ‘first’

Determines which duplicates (if any) to keep.
- `first` : Drop duplicates except for the first occurrence.
- `last` : Drop duplicates except for the last occurrence.
- False : Drop all duplicates.

**inplace**boolean, default False

Whether to drop duplicates in place or to return a copy.

Returns

DataFrame

DataFrame with duplicates removed or None if `inplace=True`.

```
>>> df = ks.DataFrame(
    ..

```