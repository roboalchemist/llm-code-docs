# Source: https://docs.snowflake.com/en/sql-reference/ddl-database.md

# Database, schema, & share DDL

Databases and schemas are used to organize data stored in Snowflake:

* A database is a logical grouping of schemas. Each database belongs to a single Snowflake account.
* A schema is a logical grouping of database objects (tables, views, etc.). Each schema belongs to a single database.

Together, a database and schema comprise a *namespace* in Snowflake. When performing any operations on database objects in Snowflake, the
namespace is inferred from the current database and schema in use for the session. If a database and schema are not in use for the session,
the namespace must be explicitly specified when performing any operations on the objects.

Snowflake provides a full set of DDL commands for creating and managing databases and schemas.

In addition, Snowflake provides DDL for creating and managing shares. A share specifies a set of database objects (schemas, tables, and
secure views) containing data you wish to share with other Snowflake accounts.

## Database management

* [CREATE DATABASE](sql/create-database.md)
* [CREATE DATABASE (catalog-linked)](sql/create-database-catalog-linked.md)
* [CREATE DATABASE … CLONE](sql/create-clone.md)
* [ALTER DATABASE](sql/alter-database.md)
* [ALTER DATABASE (catalog-linked)](sql/alter-database-catalog-linked.md)
* [DESCRIBE DATABASE](sql/desc-database.md)
* [DROP DATABASE](sql/drop-database.md)
* [UNDROP DATABASE](sql/undrop-database.md)
* [USE DATABASE](sql/use-database.md)
* [SHOW DATABASES](sql/show-databases.md)

## Schema management

* [CREATE SCHEMA](sql/create-schema.md)
* [CREATE SCHEMA … CLONE](sql/create-clone.md)
* [ALTER SCHEMA](sql/alter-schema.md)
* [DROP SCHEMA](sql/drop-schema.md)
* [UNDROP SCHEMA](sql/undrop-schema.md)
* [USE SCHEMA](sql/use-schema.md)
* [SHOW SCHEMAS](sql/show-schemas.md)

## Share management

* [CREATE SHARE](sql/create-share.md)
* [ALTER SHARE](sql/alter-share.md)
* [DROP SHARE](sql/drop-share.md)
* [SHOW SHARES](sql/show-shares.md)
* [DESCRIBE SHARE](sql/desc-share.md)
