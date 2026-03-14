# patito.duckdb.Database.create_table

Database.create_table(*name*, *model*)

Create table with schema matching the provided Patito model.

See Relation.insert_into() for how to insert
data into the table after creation.
The Relation.create_table() method can also
be used to create a table from a given relation and insert the data at the
same time.

Parameters:

- 

**name** (`str`) – Name of new database table.

- 

**model** (*Type**[**Model**]*) – Patito model indicating names and types of table
columns.

Returns:

Relation pointing to the new table.

Return type:

Relation[ModelType]

Example

```
>>> from typing import Optional
>>> import patito as pt
>>> class MyModel(pt.Model):
...     str_column: str
...     nullable_string_column: Optional[str]
...
>>> db = pt.duckdb.Database()
>>> db.create_table(name="my_table", model=MyModel)
>>> db.table("my_table").types
{'str_column': VARCHAR, 'nullable_string_column': VARCHAR}

```