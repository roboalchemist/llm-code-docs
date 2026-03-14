# Source: https://docs.snowflake.com/en/sql-reference/sql-ddl-summary.md

# Data Definition Language (DDL) commands

DDL commands are used to create, manipulate, and modify objects in Snowflake, such as users, virtual warehouses, databases, schemas,
tables, views, columns, functions, and stored procedures.

They are also used to perform many account-level and session operations, such as setting parameters, initializing variables, and
initiating transactions.

The following commands serve as the base for all DDL commands:

* [ALTER <object>](sql/alter.md)
* [COMMENT](sql/comment.md)
* [CREATE <object>](sql/create.md)
* [CREATE OR ALTER <object>](sql/create-or-alter.md)
* [DESCRIBE <object>](sql/desc.md)
* [DROP <object>](sql/drop.md)
* [SHOW <objects>](sql/show.md)
* [USE <object>](sql/use.md)

Each command takes an *object type* and *identifier*, as well as additional parameters and options. The descriptions for the
[individual commands](sql-all.md) provide the syntax and full list of parameters that can be specified for each
command. The descriptions also provide detailed usage notes and examples.

The commands are grouped into the following categories:

* [Account & session DDL](ddl-other.md)
* [User & security DDL](ddl-user-security.md)
* [Warehouse & resource monitor DDL](ddl-virtual-warehouse.md)
* [Database, schema, & share DDL](ddl-database.md)
* [Table, view, & sequence DDL](ddl-table.md)
* [Data loading / unloading DDL](ddl-stage.md)
* [DDL for user-defined functions, external functions, and stored procedures](ddl-udf.md)
* [Data pipeline DDL](ddl-pipeline.md)
* [Listings DDL](ddl-listings.md)
* [Machine learning model DDL](ddl-model.md)
