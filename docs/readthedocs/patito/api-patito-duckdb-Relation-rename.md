# patito.duckdb.Relation.rename

Relation.rename(***columns*)

Rename columns as specified.

Parameters:

****columns** (`str`) – A set of keyword arguments where the keyword is the old column
name and the value is the new column name.

Raises:

**ValueError** – If any of the given keywords do not exist as columns in the
    relation.

Examples

Return type:

`Relation`

```
>>> import patito as pt
>>> relation = pt.duckdb.Relation("select 1 as a, 2 as b")
>>> relation.rename(b="c").to_df().select(["a", "c"])
shape: (1, 2)
┌─────┬─────┐
│ a   ┆ c   │
│ --- ┆ --- │
│ i64 ┆ i64 │
╞═════╪═════╡
│ 1   ┆ 2   │
└─────┴─────┘

```