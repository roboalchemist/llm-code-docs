# patito.duckdb.Relation.case

Relation.case(***, *from_column*, *to_column*, *mapping*, *default*)

Map values of one column over to a new column.

Parameters:

- 

**from_column** (`str`) – Name of column defining the domain of the mapping.

- 

**to_column** (`str`) – Name of column to insert the mapped values into.

- 

**mapping** (`Dict`[`Union`[`str`, `float`, `int`, `None`], `Union`[`str`, `float`, `int`, `None`]]) – Dictionary defining the mapping. The dictionary keys represent the
input values, while the dictionary values represent the output values.
Items are inserted into the SQL case statement by their repr() string
value.

- 

**default** (`Union`[`str`, `float`, `int`, `None`]) – Default output value for inputs which have no provided mapping.

Return type:

`Relation`

Examples

The following case statement…

```
>>> import patito as pt
>>> db = pt.duckdb.Database()
>>> relation = db.to_relation("select 1 as a union select 2 as a")
>>> relation.case(
...     from_column="a",
...     to_column="b",
...     mapping={1: "one", 2: "two"},
...     default="three",
... ).order(by="a").to_df()
shape: (2, 2)
┌─────┬─────┐
│ a   ┆ b   │
│ --- ┆ --- │
│ i64 ┆ str │
╞═════╪═════╡
│ 1   ┆ one │
│ 2   ┆ two │
└─────┴─────┘

```