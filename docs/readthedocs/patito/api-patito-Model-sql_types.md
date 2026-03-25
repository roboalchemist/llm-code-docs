# patito.Model.sql_types

*property *Model.sql_types*: dict[str, str]*

Return compatible DuckDB SQL types for all model fields.

Returns:

Dictionary with column name keys and SQL type identifier strings.

Example

```
>>> from typing import Literal
>>> import patito as pt

```