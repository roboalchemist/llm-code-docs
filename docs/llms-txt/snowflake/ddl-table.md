# Source: https://docs.snowflake.com/en/sql-reference/ddl-table.md

# Table, view, & sequence DDL

Tables and views are the primary objects created and maintained in database schemas:

* All data in Snowflake is stored in tables.
* Views can be used to display selected rows and columns in one or more tables.

Sequences are also schema-level objects. Sequences can be used to generate unique numbers across sessions and statements or to generate
values for a primary key or any column that requires a unique value.

## Table management

* [CREATE TABLE](sql/create-table.md)
* [CREATE TABLE … CLONE](sql/create-clone.md)
* [CREATE TABLE … CONSTRAINT](sql/create-table-constraint.md)
* [ALTER TABLE](sql/alter-table.md)
* [ALTER TABLE … ALTER COLUMN](sql/alter-table-column.md)
* [ALTER TABLE … CONSTRAINT](sql/create-table-constraint.md)
* [DROP TABLE](sql/drop-table.md)
* [UNDROP TABLE](sql/undrop-table.md)
* [SHOW TABLES](sql/show-tables.md) (also [SHOW OBJECTS](sql/show-objects.md))
* [SHOW COLUMNS](sql/show-columns.md)
* [DESCRIBE TABLE](sql/desc-table.md)
* [DESCRIBE SEARCH OPTIMIZATION](sql/desc-search-optimization.md)

## Event table management

* [CREATE EVENT TABLE](sql/create-event-table.md)
* [ALTER TABLE (event tables)](sql/alter-table-event-table.md)
* [DROP TABLE](sql/drop-table.md)
* [SHOW EVENT TABLES](sql/show-event-tables.md)
* [DESCRIBE EVENT TABLE](sql/desc-event-table.md)

## External table management

* [CREATE EXTERNAL TABLE](sql/create-external-table.md)
* [ALTER EXTERNAL TABLE](sql/alter-external-table.md)
* [DROP EXTERNAL TABLE](sql/drop-external-table.md)
* [SHOW EXTERNAL TABLES](sql/show-external-tables.md) (also [SHOW OBJECTS](sql/show-objects.md))
* [DESCRIBE EXTERNAL TABLE](sql/desc-external-table.md)

## Standard view management

* [CREATE VIEW](sql/create-view.md)
* [ALTER VIEW](sql/alter-view.md)
* [DROP VIEW](sql/drop-view.md)
* [SHOW VIEWS](sql/show-views.md) (also [SHOW OBJECTS](sql/show-objects.md))
* [SHOW COLUMNS](sql/show-columns.md)
* [DESCRIBE VIEW](sql/desc-view.md)

## Materialized view management

* [CREATE MATERIALIZED VIEW](sql/create-materialized-view.md)
* [ALTER MATERIALIZED VIEW](sql/alter-materialized-view.md)
* [DROP MATERIALIZED VIEW](sql/drop-materialized-view.md)
* [SHOW MATERIALIZED VIEWS](sql/show-materialized-views.md)
* [DESCRIBE MATERIALIZED VIEW](sql/desc-materialized-view.md)

## Sequence management

* [CREATE SEQUENCE](sql/create-sequence.md)
* [CREATE SEQUENCE … CLONE](sql/create-clone.md)
* [ALTER SEQUENCE](sql/alter-sequence.md)
* [DROP SEQUENCE](sql/drop-sequence.md)
* [SHOW SEQUENCES](sql/show-sequences.md)
* [DESCRIBE SEQUENCE](sql/desc-sequence.md)

## Column-level security management

Use these commands for Dynamic Data Masking and External Tokenization.

* [CREATE MASKING POLICY](sql/create-masking-policy.md)
* [ALTER MASKING POLICY](sql/alter-masking-policy.md) (see also: [ALTER TABLE](sql/alter-table.md), [ALTER TABLE … ALTER COLUMN](sql/alter-table-column.md), and [ALTER VIEW](sql/alter-view.md))
* [DROP MASKING POLICY](sql/drop-masking-policy.md)
* [SHOW MASKING POLICIES](sql/show-masking-policies.md)
* [DESCRIBE MASKING POLICY](sql/desc-masking-policy.md)

## Row access policy management

Snowflake supports the following DDL commands and operations to manage row access policies:

* [CREATE ROW ACCESS POLICY](sql/create-row-access-policy.md)
* [ALTER ROW ACCESS POLICY](sql/alter-row-access-policy.md)
* [DROP ROW ACCESS POLICY](sql/drop-row-access-policy.md)
* [SHOW ROW ACCESS POLICIES](sql/show-row-access-policies.md)
* [DESCRIBE ROW ACCESS POLICY](sql/desc-row-access-policy.md)
* [ALTER TABLE](sql/alter-table.md), [ALTER EXTERNAL TABLE](sql/alter-external-table.md), and [ALTER VIEW](sql/alter-view.md) (to add/drop a policy on a table or view)
