# patito.duckdb.Relation.get

Relation.get(**filters*, ***equalities*)

Fetch the single row that matches the given filter(s).

If you expect a relation to already return one row, you can use get() without
any arguments to return that row.

Raises:

**RuntimeError** – RuntimeError is thrown if not exactly one single row matches
    the given filter.

Parameters:

- 

**filters** (*str*) – A conjunction of SQL where clauses.

- 

**equalities** (*Any*) – A conjunction of SQL equality clauses. The keyword name
is the column and the parameter is the value of the equality.

Returns:

A Patito model representing the given row.

Return type:

Model

Examples

```
>>> import patito as pt
>>> import polars as pl
>>> df = pt.DataFrame({"product_id": [1, 2, 3], "price": [10, 10, 20]})
>>> relation = pt.duckdb.Relation(df).set_alias("my_relation")

```