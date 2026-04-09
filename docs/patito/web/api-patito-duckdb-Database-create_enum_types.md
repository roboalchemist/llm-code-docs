# patito.duckdb.Database.create_enum_types

Database.create_enum_types(*model*)

Define SQL enum types in DuckDB database.

Parameters:

**model** (`Type`[`TypeVar`(`ModelType`, bound= Model)]) – Model for which all Literal-annotated or enum-annotated string fields
will get respective DuckDB enum types.

Return type:

`None`

Example

```
>>> import patito as pt
>>> class EnumModel(pt.Model):
...     enum_column: Literal["A", "B", "C"]
...
>>> db = pt.duckdb.Database()
>>> db.create_enum_types(EnumModel)
>>> db.enum_types
{'enum__7ba49365cc1b0fd57e61088b3bc9aa25'}

```