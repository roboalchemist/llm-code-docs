# patito.duckdb.Relation.add_suffix

Relation.add_suffix(*suffix*, *include=None*, *exclude=None*)

Add a suffix to all the columns of the relation.

Parameters:

- 

**suffix** (`str`) – A string to append to add to all columns names.

- 

**include** (`Optional`[`Collection`[`str`]]) – If provided, only the given columns will be renamed.

- 

**exclude** (`Optional`[`Collection`[`str`]]) – If provided, the given columns will not be renamed.

Raises:

**TypeError** – If both include and exclude are provided at the same time.

Return type:

`Relation`

Examples

```
>>> import patito as pt
>>> relation = pt.duckdb.Relation("select 1 as column_1, 2 as column_2")
>>> relation.add_suffix("_renamed").to_df()
shape: (1, 2)
┌──────────────────┬──────────────────┐
│ column_1_renamed ┆ column_2_renamed │
│ ---              ┆ ---              │
│ i64              ┆ i64              │
╞══════════════════╪══════════════════╡
│ 1                ┆ 2                │
└──────────────────┴──────────────────┘

```