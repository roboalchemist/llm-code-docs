# patito.duckdb.Relation.set_model

Relation.set_model(*model*)

Associate a give Patito model with the relation.

The returned relation has an associated `.model` attribute which can in turn
be used by several methods such as Relation.get(),
Relation.create_table(), and
Relation.__iter__.

Parameters:

**model** – A Patito Model class specifying the intended schema of the relation.

Returns:

A new relation with the associated model.

Return type:

Relation[model]

Example

```
>>> from typing import Literal
>>> import patito as pt
>>> class MySchema(pt.Model):
...     float_column: float
...     enum_column: Literal["A", "B", "C"]
...
>>> relation = pt.duckdb.Relation(
...     "select 1 as float_column, 'A' as enum_column"
... )
>>> relation.get()
query_relation(float_column=1, enum_column='A')
>>> relation.set_model(MySchema).get()
MySchema(float_column=1.0, enum_column='A')
>>> relation.create_table("unmodeled_table").types
{'float_column': INTEGER, 'enum_column': VARCHAR}
>>> relation.set_model(MySchema).create_table("modeled_table").types
{'float_column': DOUBLE,
 'enum_column': enum__7ba49365cc1b0fd57e61088b3bc9aa25}

```