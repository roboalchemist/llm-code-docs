# databricks.koalas.DataFrame.itertuples

`DataFrame.``itertuples`(*index: bool = True*, *name: Optional[str] = 'Koalas'*) → Iterator

Iterate over DataFrame rows as namedtuples.

Parameters

**index**bool, default True

If True, return the index as the first element of the tuple.

**name**str or None, default “Koalas”

The name of the returned namedtuples or None to return regular
tuples.

Returns

iterator

An object to iterate over namedtuples for each row in the
DataFrame with the first field possibly being the index and
following fields being the column values.

See also

`DataFrame.iterrows`

Iterate over DataFrame rows as (index, Series) pairs.

`DataFrame.items`

Iterate over (column name, Series) pairs.