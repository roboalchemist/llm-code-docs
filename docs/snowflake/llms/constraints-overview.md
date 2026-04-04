# Source: https://docs.snowflake.com/en/sql-reference/constraints-overview.md

# Overview of Constraints

Snowflake provides the following constraint functionality:

* Unique, primary, and foreign keys, and NOT NULL columns.
* Named constraints.
* Single-column and multi-column constraints.
* Creation of constraints inline and out-of-line.
* Creation, modification, and deletion of constraints.

## Supported Constraint Types

Snowflake supports the following constraint types from the ANSI SQL standard:

* PRIMARY KEY
* FOREIGN KEY
* UNIQUE
* NOT NULL

A table can have multiple unique keys and foreign keys, but only one primary key. A PRIMARY KEY constraint implies that the
column is both NOT NULL and UNIQUE.

All foreign keys must reference a corresponding primary or unique key that matches the column types of each column in the foreign key.
The primary key for a foreign key can be on a different table or the same table as the foreign key. When you define foreign key constraints across [hybrid tables](../user-guide/tables-hybrid.md), the tables must be in the same database.

The following table summarizes the differences in behavior between standard tables and hybrid tables,
with respect to the enforcement of constraints and whether constraints are required.

* A constraint is *enforced* when it protects a column from being updated in certain ways.
  For example, a column that is declared NOT NULL cannot contain a NULL value. An attempt to copy or insert a NULL value into a NOT NULL column always results in an error.
  For hybrid tables, you cannot set the NOT ENFORCED property on PRIMARY KEY, FOREIGN KEY, and UNIQUE constraints. Setting this property results in an “invalid constraint property” error.
* A constraint is *required* when one or more columns in a table must have such a constraint, which is only true for
  PRIMARY KEY constraints on hybrid tables.

| Feature | Hybrid tables | Standard tables |
| --- | --- | --- |
| PRIMARY KEY constraints | Required, enforced | Optional, not enforced |
| FOREIGN KEY constraints | Optional, enforced (referential integrity) | Optional, not enforced |
| UNIQUE constraints | Optional, enforced | Optional, not enforced |
| NOT NULL constraints | Optional, enforced | Optional, enforced |

See also [CREATE | ALTER TABLE … CONSTRAINT](sql/create-table-constraint.md).

## Table Constraints

Snowflake supports constraints on permanent, transient, temporary, and hybrid
tables. You can define constraints on columns of all data types, and you can
include any number of columns in a single constraint.

* When you copy a table by using CREATE TABLE … LIKE or CREATE TABLE … CLONE,
  all existing constraints on the table, including foreign keys, are copied to the
  new table. (CREATE TABLE … CLONE is not supported for hybrid tables.)
* Additional commands and functions, such as DROP/UNDROP and GET_DDL are
  supported for tables with constraints. They are also supported for schemas
  and databases.

  For Snowflake Time Travel, when previous versions of a table are copied, the
  current version of the constraints on the table are used because Snowflake
  does not store previous versions of constraints in table metadata.

## Single-Column and Multi-Column Constraints

Constraints can be defined on a single column or on multiple columns in the same
table.

For multi-column constraints (composite primary keys or unique keys), the
columns are ordered, and each column has a corresponding key sequence.

## Inline and Out-of-Line Constraints

Constraints are defined either inline or out-of-line during table creation or
modification:

* Inline constraints are created as part of the column definition and can only
  be used for single-column constraints.
* Out-of-line constraints are defined using a separate clause that specifies the
  column or columns on which the constraint is created. They can be used for creating
  either single-column or multi-column constraints, as well as for creating
  constraints on existing columns.

## Constraints in GET_DDL

The SQL statements that [GET_DDL](functions/get_ddl.md) returns includes the
clauses that define constraints; however, note the following:

* Single-column constraints, such as `NOT NULL` and `DEFAULT`, are
  reconstructed inline with the definition of the column.
* Table constraints, such as unique/primary/foreign keys, are always reconstructed as
  out-of-line constraints, even if they consist of a single column.
* For unnamed constraints (that is, constraints with a system-generated name),
  [GET_DDL](functions/get_ddl.md) does not return the system-generated name.
