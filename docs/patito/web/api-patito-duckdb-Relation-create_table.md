# patito.duckdb.Relation.create_table

Relation.create_table(*name*)

Create new database table based on relation.

If `self.model` is set with
Relation.set_model(), then the model is used
to infer the table schema. Otherwise, a permissive table schema is created based
on the relation data.

Returns:

A relation pointing to the newly created table.

Return type:

Relation

Examples

```
>>> from typing import Literal
>>> import patito as pt

```