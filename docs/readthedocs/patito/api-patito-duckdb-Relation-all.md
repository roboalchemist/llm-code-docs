# patito.duckdb.Relation.all

Relation.all(**filters*, ***equalities*)

Return `True` if the given predicate(s) are true for all rows in the relation.

See `Relation.filter()` for additional information regarding the
parameters.

Parameters:

- 

**filters** (`str`) – SQL predicates to satisfy.

- 

**equalities** (`Union`[`int`, `float`, `str`]) – SQL equality predicates to satisfy.

Return type:

`bool`

Examples

```
>>> import patito as pt
>>> df = pt.DataFrame(
...     {
...         "even_number": [2, 4, 6],
...         "odd_number": [1, 3, 5],
...         "zero": [0, 0, 0],
...     }
... )
>>> relation = pt.duckdb.Relation(df)
>>> relation.all(zero=0)
True
>>> relation.all(
...     "even_number % 2 = 0",
...     "odd_number % 2 = 1",
...     zero=0,
... )
True
>>> relation.all(zero=1)
False
>>> relation.all("odd_number % 2 = 0")
False

```