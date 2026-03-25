# Source: https://docs.snowflake.com/en/sql-reference/constraints-alter.md

# Modifying Constraints

After a constraint is created:

* The constraint can be renamed.
* Some properties can be modified, e.g. RELY.
* Some properties cannot be modified, e.g. such as DEFERRABLE. To modify these properties, the constraint must be dropped and recreated.
* The column definition for a constraint cannot be modified, e.g. add new columns, drop existing columns, or change the order of columns. To make these types of changes, the constraint must be dropped
  and recreated.

When modifying a constraint, the constraint can be identified using either the constraint name or the columns in the constraint definition along with the type of the constraint. Primary keys can also be
identified using the PRIMARY KEY keyword, because each table can have only a single primary key.

If a table with constraints is modified, e.g. rename table or swap table with another table, the constraints are updated to reflect the changes.

## Renaming a Constraint

Use the following syntax for the [ALTER TABLE](sql/alter-table.md) command to rename a constraint:

```sqlsyntax
ALTER TABLE <table_name> RENAME CONSTRAINT <old_name> TO <new_name>;
```

## Modifying Properties of a Constraint

Use the following syntax for the [ALTER TABLE](sql/alter-table.md) command to modify the properties of a constraint:

```sqlsyntax
ALTER TABLE <table_name>
    { ALTER | MODIFY } { CONSTRAINT <name> | PRIMARY KEY | { UNIQUE | FOREIGN KEY } (<column_name>, [ ... ] ) }
    { [ [ NOT ] ENFORCED ] [ VALIDATE | NOVALIDATE ] [ RELY | NORELY ] };
```

Currently, Snowflake only supports setting the following constraint properties:

* NOT ENFORCED
* NOVALIDATE
* RELY and NORELY

Note that Snowflake does not support setting ENFORCED and VALIDATE. See also [Non-default values for ENABLE and VALIDATE properties](sql/create-table-constraint.md).

For descriptions of the constraint properties, see [Constraint properties](sql/create-table-constraint.md).

## Modifying a Table with Constraints

If a table with constraints is renamed, the constraints for the table, as well as any foreign key constraints that reference the table are updated to reference the new name.

Likewise, if a table is swapped with another, existing table, all the constraints on the table are maintained on the swapped table.

For more details about renaming or swapping tables, see [ALTER TABLE](sql/alter-table.md).
