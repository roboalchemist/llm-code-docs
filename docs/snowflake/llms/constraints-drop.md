# Source: https://docs.snowflake.com/en/sql-reference/constraints-drop.md

# Dropping Constraints

Constraints are dropped using the [ALTER TABLE](sql/alter-table.md) command:

* ALTER TABLE … DROP CONSTRAINT explicitly drops the specified constraint. Similar to modifying constraints, the constraint can be identified by the constraint name or column definition along with
  the constraint type. For a primary key, they can also be identified using the PRIMARY KEY keyword.
* ALTER TABLE … DROP COLUMN drops a column and its associated constraints.

By default, when a primary/unique key is dropped, all foreign keys referencing the key being dropped are also dropped, unless the RESTRICT drop option is specified.

Constraints are also dropped when the associated tables/schemas/databases are dropped. The DROP commands support the CASCADE | RESTRICT drop options.

> **Note:**
>
> Dropped tables, schemas, and databases can be restored using the UNDROP command; dropped columns and constraints cannot be restored.

## Dropping Constraints

Unique/primary/foreign key constraints can be explicitly dropped (using ALTER TABLE … DROP CONSTRAINT):

> ```sqlsyntax
> ALTER TABLE <table_name> DROP { CONSTRAINT <name> | PRIMARY KEY | { UNIQUE | FOREIGN KEY } (<column>, [ ... ] ) } [ CASCADE | RESTRICT ]
> ```

For these constraints, when dropping a foreign key constraint or a primary/unique key constraint with no foreign key references, the constraints are dropped directly.

The default drop option is CASCADE, which means that dropping a unique/primary key with foreign key references drops all the referencing foreign keys together with the unique/primary key.

* If the RESTRICT drop option is specified, when dropping a primary/unique key, an error is returned if there exist foreign keys that reference the keys being dropped.

## Dropping Columns

Dropping columns using ALTER TABLE … DROP COLUMN behaves similarly to dropping constraints:

> ```sqlsyntax
> ALTER TABLE <table_name> DROP COLUMN <name> [ CASCADE | RESTRICT ]
> ```

The default drop option is CASCADE, which means any constraint that contains the column being dropped is also dropped. If a primary/unique key involving the column is referenced by other foreign key
constraints, all referencing foreign keys are dropped.

* If the RESTRICT option is specified, an error is returned if the column has primary/unique keys with foreign keys references. The drop command only succeeds if there are no constraints defined on or
  referring to the column being dropped.

## Dropping Tables/Schemas/Databases

The DROP command drops the specified table, schema, or database and can also be specified to drop all constraints associated with the object:

> ```sqlsyntax
> DROP { TABLE | SCHEMA | DATABASE } <name> [ CASCADE | RESTRICT ]
> ```

Similar to dropping columns and constraints, CASCADE is the default drop option, and all constraints that belong to or references the object being dropped will also be dropped.

For example, when dropping a database, if the database contains a primary/unique key which is referenced by a foreign key from another database, the referencing foreign keys are also dropped.

If the object is later undropped, all relevant constraints previously dropped will be restored.

If the RESTRICT option is specified, an error is returned if any primary/unique constraints under the object has foreign key references.
