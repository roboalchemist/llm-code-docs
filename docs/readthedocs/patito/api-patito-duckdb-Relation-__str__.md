# patito.duckdb.Relation.__str__

Relation.__str__()

Return string representation of Relation object.

Includes an expression tree, the result columns, and a result preview.

Return type:

`str`

Example

```
>>> import patito as pt
>>> products = pt.duckdb.Relation(
...     pt.DataFrame(
...         {
...             "product_name": ["apple", "red_apple", "banana", "oranges"],
...             "supplier_id": [2, 2, 1, 3],
...         }
...     )
... ).set_alias("products")
>>> print(str(products))  # xdoctest: +SKIP
---------------------
--- Relation Tree ---
---------------------
arrow_scan(94609350519648, 140317161740928, 140317161731168, 1000000)
---------------------
-- Result Columns  --
---------------------
- product_name (VARCHAR)
- supplier_id (BIGINT)
---------------------
-- Result Preview  --
---------------------
product_name    supplier_id
VARCHAR BIGINT
[ Rows: 4]
apple   2
red_apple       2
banana  1
oranges 3

```