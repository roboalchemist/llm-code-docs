# patito.duckdb.Relation.aggregate

Relation.aggregate(**aggregations*, *group_by*, ***named_aggregations*)

Return relation formed by `GROUP BY` SQL aggregation(s).

Parameters:

- 

**aggregations** (`str`) – Zero or more aggregation expressions such as
“sum(column_name)” and “count(distinct column_name)”.

- 

**named_aggregations** (`str`) – Zero or more aggregated expressions where the keyword is
used to name the given aggregation. For example,
`my_column="sum(column_name)"` is inserted as
`"sum(column_name) as my_column"` in the executed SQL query.

- 

**group_by** (`Union`[`str`, `Iterable`[`str`]]) – A single column name or iterable collection of column names to
group by.

Return type:

`Relation`

Examples

```
>>> import patito as pt
>>> df = pt.DataFrame({"a": [1, 2, 3], "b": ["X", "Y", "X"]})
>>> relation = pt.duckdb.Relation(df)
>>> relation.aggregate(
...     "b",
...     "sum(a)",
...     "greatest(b)",
...     max_a="max(a)",
...     group_by="b",
... ).to_df()
shape: (2, 4)
┌─────┬────────┬─────────────┬───────┐
│ b   ┆ sum(a) ┆ greatest(b) ┆ max_a │
│ --- ┆ ---    ┆ ---         ┆ ---   │
│ str ┆ f64    ┆ str         ┆ i64   │
╞═════╪════════╪═════════════╪═══════╡
│ X   ┆ 4.0    ┆ X           ┆ 3     │
│ Y   ┆ 2.0    ┆ Y           ┆ 2     │
└─────┴────────┴─────────────┴───────┘

```