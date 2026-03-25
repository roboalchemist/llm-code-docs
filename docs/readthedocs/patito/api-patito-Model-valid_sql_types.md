# patito.Model.valid_sql_types

*property *Model.valid_sql_types*: dict[str, List[Literal['BIGINT', 'INT8', 'LONG', 'BLOB', 'BYTEA', 'BINARY', 'VARBINARY', 'BOOLEAN', 'BOOL', 'LOGICAL', 'DATE', 'DOUBLE', 'FLOAT8', 'NUMERIC', 'DECIMAL', 'HUGEINT', 'INTEGER', 'INT4', 'INT', 'SIGNED', 'INTERVAL', 'REAL', 'FLOAT4', 'FLOAT', 'SMALLINT', 'INT2', 'SHORT', 'TIME', 'TIMESTAMP', 'DATETIME', 'TIMESTAMP WITH TIMEZONE', 'TIMESTAMPTZ', 'TINYINT', 'INT1', 'UBIGINT', 'UINTEGER', 'USMALLINT', 'UTINYINT', 'UUID', 'VARCHAR', 'CHAR', 'BPCHAR', 'TEXT', 'STRING']]]*

Return a list of DuckDB SQL types which Patito considers valid for each field.

The first item of each list is the default dtype chosen by Patito.

Returns:

A dictionary mapping each column string name to a list of DuckDB SQL types
represented as strings.

Raises:

**NotImplementedError** – If one or more model fields are annotated with types
    not compatible with DuckDB.

Example

```
>>> import patito as pt
>>> from pprint import pprint

```