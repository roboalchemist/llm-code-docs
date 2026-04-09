# patito.duckdb.Relation.filter

Relation.filter(**filters*, ***equalities*)

Return subset of rows of relation that satisfy the given predicates.

The method returns self if no filters are provided.

Parameters:

- 

**filters** (`str`) – A conjunction of SQL `WHERE` clauses.

- 

**equalities** (`Union`[`str`, `int`, `float`]) – A conjunction of SQL equality clauses. The keyword name
is the column and the parameter is the value of the equality.

Returns:

A new relation where all rows satisfy the given criteria.

Return type:

Relation

Examples

```
>>> import patito as pt
>>> df = pt.DataFrame(
...     {
...         "number": [1, 2, 3, 4],
...         "string": ["A", "A", "B", "B"],
...     }
... )
>>> relation = pt.duckdb.Relation(df)
>>> relation.filter("number % 2 = 0").to_df()
shape: (2, 2)
┌────────┬────────┐
│ number ┆ string │
│ ---    ┆ ---    │
│ i64    ┆ str    │
╞════════╪════════╡
│ 2      ┆ A      │
│ 4      ┆ B      │
└────────┴────────┘

```