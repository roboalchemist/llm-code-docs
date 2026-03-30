# patito.duckdb.Database.from_connection

*classmethod *Database.from_connection(*connection*)

Create database from native DuckDB connection object.

Parameters:

**connection** (`DuckDBPyConnection`) – A native DuckDB connection object created with
`duckdb.connect()`.

Return type:

`Database`

Returns:

A Database object wrapping around the given
connection.

Example

```
>>> import duckdb
>>> import patito as pt
>>> connection = duckdb.connect()
>>> database = pt.duckdb.Database.from_connection(connection)

```