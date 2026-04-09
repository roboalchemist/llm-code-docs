# patito.duckdb.Relation.coalesce

Relation.coalesce(***column_expressions*)

Replace null-values in given columns with respective values.

For example, `coalesce(column_name=value)` is compiled to:
`f"coalesce({column_name}, {repr(value)}) as column_name"` in the resulting
SQL.

Parameters:

**column_expressions** (`Union`[`str`, `int`, `float`]) – Keywords indicate which columns to coalesce, while the
string representation of the respective arguments are used as the
null-replacement.

Returns:

Relation where values have been filled in for nulls in the given
columns.

Return type:

Relation

Examples

```
>>> import patito as pt
>>> df = pt.DataFrame(
...     {
...         "a": [1, None, 3],
...         "b": ["four", "five", None],
...         "c": [None, 8.0, 9.0],
...     }
... )
>>> relation = pt.duckdb.Relation(df)
>>> relation.coalesce(a=2, b="six").to_df()
shape: (3, 3)
┌─────┬──────┬──────┐
│ a   ┆ b    ┆ c    │
│ --- ┆ ---  ┆ ---  │
│ i64 ┆ str  ┆ f64  │
╞═════╪══════╪══════╡
│ 1   ┆ four ┆ null │
│ 2   ┆ five ┆ 8.0  │
│ 3   ┆ six  ┆ 9.0  │
└─────┴──────┴──────┘

```