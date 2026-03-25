# patito.duckdb.Relation.add_prefix

Relation.add_prefix(*prefix*, *include=None*, *exclude=None*)

Add a prefix to all the columns of the relation.

Parameters:

- 

**prefix** (`str`) – A string to prepend to add to all the columns names.

- 

**include** (`Optional`[`Iterable`[`str`]]) – If provided, only the given columns will be renamed.

- 

**exclude** (`Optional`[`Iterable`[`str`]]) – If provided, the given columns will not be renamed.

Raises:

**TypeError** – If both include and exclude are provided at the same time.

Return type:

`Relation`

Examples

```
>>> import patito as pt
>>> relation = pt.duckdb.Relation("select 1 as column_1, 2 as column_2")
>>> relation.add_prefix("renamed_").to_df()
shape: (1, 2)
┌──────────────────┬──────────────────┐
│ renamed_column_1 ┆ renamed_column_2 │
│ ---              ┆ ---              │
│ i64              ┆ i64              │
╞══════════════════╪══════════════════╡
│ 1                ┆ 2                │
└──────────────────┴──────────────────┘

```