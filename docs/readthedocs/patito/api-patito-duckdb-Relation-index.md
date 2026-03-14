# patito.duckdb.Relation

Relation.__init__(*derived_from*, *database=None*, *model=None*)

Create a new relation object containing data to be queried with DuckDB.

Parameters:

- 

**derived_from** (`Union`[`DataFrame`, `DataFrame`, `DataFrame`, `Path`, `str`, `DuckDBPyRelation`, `Relation`]) – 

Data to be represented as a DuckDB relation object.
Can be one of the following types:

  - 

A pandas or polars DataFrame.

  - 

An SQL query represented as a string.

  - 

A `Path` object pointing to a CSV or a parquet file.
The path must point to an existing file with either a `.csv`
or `.parquet` file extension.

  - 

A native DuckDB relation object (`duckdb.DuckDBPyRelation`).

  - 

A `patito.duckdb.Relation` object.

- 

**database** (`Optional`[`Database`]) – Which database to load the relation into. If not provided,
the default DuckDB database will be used.

- 

**model** (`Optional`[`Type`[`TypeVar`(`ModelType`, bound= Model)]]) – 

Sub-class of `patito.Model` which specifies how to deserialize rows
when fetched with methods such as
Relation.get() and `__iter__()`.

Will also be used to create a strict table schema if
Relation.create_table().
schema should be constructed.

If not provided, a dynamic model fitting the relation schema will be
created when required.

Can also be set later dynamically by invoking
Relation.set_model().

Raises:

- 

**ValueError** – If any one of the following cases are encountered:
    
    - If a provided `Path` object does not have a `.csv` or
      `.parquet` file extension.
    - If a database and relation object is provided, but the relation object
      does not belong to the database.

- 

**TypeError** – If the type of `derived_from` is not supported.

Examples

Instantiated from a dataframe:

```
>>> import patito as pt
>>> df = pt.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
>>> pt.duckdb.Relation(df).filter("a > 2").to_df()
shape: (1, 2)
┌─────┬─────┐
│ a   ┆ b   │
│ --- ┆ --- │
│ i64 ┆ i64 │
╞═════╪═════╡
│ 3   ┆ 6   │
└─────┴─────┘

```