# patito.duckdb.Relation.to_series

Relation.to_series()

Convert the given relation to a polars Series.

Raises:

**TypeError** – If the given relation does not contain exactly one column.

Returns: A `polars.Series` object containing the data of the relation.

Return type:

`Series`

Example

```
>>> import patito as pt
>>> relation = pt.duckdb.Relation("select 1 as a union select 2 as a")
>>> relation.order(by="a").to_series()
shape: (2,)
Series: 'a' [i32]
[
            1
            2
]

```