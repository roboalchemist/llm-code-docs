# patito.duckdb.Database.__contains__

Database.__contains__(*table*)

Return `True` if the database contains a table with the given name.

Parameters:

**table** (`str`) – The name of the table to be checked for.

Return type:

`bool`

Examples

```
>>> import patito as pt
>>> db = pt.duckdb.Database()
>>> "my_table" in db
False
>>> db.to_relation("select 1 as a, 2 as b").create_table(name="my_table")
>>> "my_table" in db
True

```