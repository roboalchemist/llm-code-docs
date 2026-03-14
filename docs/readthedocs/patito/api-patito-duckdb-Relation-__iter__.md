# patito.duckdb.Relation.__iter__

Relation.__iter__()

Iterate over rows in relation.

If Relation.set_model() has been invoked
first, the given model will be used to deserialize each row. Otherwise a Patito
model is dynamically constructed which fits the schema of the relation.

Returns:

An iterator of patito Model objects representing each row.

Return type:

Iterator[Model]

Example

```
>>> from typing import Literal
>>> import patito as pt
>>> df = pt.DataFrame({"float_column": [1, 2], "enum_column": ["A", "B"]})
>>> relation = pt.duckdb.Relation(df).set_alias("my_relation")
>>> for row in relation:
...     print(row)
...
float_column=1 enum_column='A'
float_column=2 enum_column='B'
>>> list(relation)
[my_relation(float_column=1, enum_column='A'),
 my_relation(float_column=2, enum_column='B')]

```