# patito.duckdb.Relation.left_join

Relation.left_join(*other*, *on*)

Left join relation with other relation source based on condition.

Parameters:

- 

**other** (`Union`[`DataFrame`, `DataFrame`, `DataFrame`, `Path`, `str`, `DuckDBPyRelation`, `Relation`]) – A source which can be casted to a Relation object, and be used as
the right table in the join.

- 

**on** (`str`) – Join condition following the `LEFT JOIN ... ON` in the SQL query.

Returns:

New relation based on the joined tables.

Return type:

Relation

Example

```
>>> import patito as pt
>>> products_df = pt.DataFrame(
...     {
...         "product_name": ["apple", "banana", "oranges"],
...         "supplier_id": [2, 1, 3],
...     }
... )
>>> products = pt.duckdb.Relation(products_df)
>>> supplier_df = pt.DataFrame(
...     {
...         "id": [1, 2],
...         "supplier_name": ["Banana Republic", "Applies Inc."],
...     }
... )
>>> suppliers = pt.duckdb.Relation(supplier_df)
>>> products.set_alias("p").left_join(
...     suppliers.set_alias("s"),
...     on="p.supplier_id = s.id",
... ).to_df()
shape: (3, 4)
┌──────────────┬─────────────┬──────┬─────────────────┐
│ product_name ┆ supplier_id ┆ id   ┆ supplier_name   │
│ ---          ┆ ---         ┆ ---  ┆ ---             │
│ str          ┆ i64         ┆ i64  ┆ str             │
╞══════════════╪═════════════╪══════╪═════════════════╡
│ apple        ┆ 2           ┆ 2    ┆ Applies Inc.    │
│ banana       ┆ 1           ┆ 1    ┆ Banana Republic │
│ oranges      ┆ 3           ┆ null ┆ null            │
└──────────────┴─────────────┴──────┴─────────────────┘

```