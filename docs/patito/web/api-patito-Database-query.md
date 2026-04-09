# patito.Database.query

Database.query(*query*, ***, *lazy=False*, *cache=False*, *ttl=None*, *model=None*, ***kwargs*)

Execute the given query and return the query result as a DataFrame or LazyFrame.

See patito.Database.as_query for a more powerful way to build and execute
queries.

Parameters:

- 

**query** (`str`) – The query string to be executed, for instance an SQL query.

- 

**lazy** (`bool`) – If the query  result should be returned in the form of a LazyFrame
instead of a DataFrame.

- 

**cache** (`Union`[`str`, `Path`, `bool`]) – If the query result should be saved and re-used the next time the
same query is executed. Can also be provided as a path. See
`Database.as_query()` for full documentation.

- 

**ttl** (`Optional`[`timedelta`]) – How long to use cached results until the query is re-executed anyway.

- 

**model** (`Optional`[`Type`[`Model`]]) – A patito.Model to optionally validate the query result.

- 

****kwargs** (`Any`) – All additional keyword arguments are forwarded to the query
handler which executes the given query.

Return type:

`Union`[`DataFrame`, `LazyFrame`]

Returns:

The result of the query in the form of a `DataFrame` if `lazy=False`, or
a `LazyFrame` otherwise.

Examples

We will use DuckDB as our example database.

```
>>> import duckdb
>>> import patito as pt

```