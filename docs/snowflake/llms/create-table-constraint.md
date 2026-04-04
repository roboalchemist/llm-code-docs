# Source: https://docs.snowflake.com/en/sql-reference/sql/create-table-constraint.md

# CREATE | ALTER TABLE … CONSTRAINT

This topic describes how to create constraints by specifying a CONSTRAINT clause in a
[CREATE TABLE](create-table.md), [CREATE HYBRID TABLE](create-hybrid-table.md),
or [ALTER TABLE](alter-table.md) statement:

* An inline constraint is specified as part of the individual column definition.
* An out-of-line constraint is specified as an independent clause:

  * When creating a table, the clause is part of the column definitions for the table.
  * When altering a table, the clause is specified as an explicit `ADD` action for the table.

For more information, see [Constraints](../constraints.md).

If you are creating or altering [hybrid tables](../../user-guide/tables-hybrid.md), the syntax for defining constraints is the same; however, the rules and requirements are different.

## Syntax for inline constraints

```sqlsyntax
CREATE TABLE <name> ( <col1_name> <col1_type>    [ NOT NULL ] { inlineUniquePK | inlineFK }
                     [ , <col2_name> <col2_type> [ NOT NULL ] { inlineUniquePK | inlineFK } ]
                     [ , ... ] )

ALTER TABLE <name> ADD COLUMN <col_name> <col_type> [ NOT NULL ] { inlineUniquePK | inlineFK }
```

Where:

> ```sqlsyntax
> inlineUniquePK ::=
>   [ CONSTRAINT <constraint_name> ]
>   { UNIQUE | PRIMARY KEY }
>   [ [ NOT ] ENFORCED ]
>   [ [ NOT ] DEFERRABLE ]
>   [ INITIALLY { DEFERRED | IMMEDIATE } ]
>   [ { ENABLE | DISABLE } ]
>   [ { VALIDATE | NOVALIDATE } ]
>   [ { RELY | NORELY } ]
> ```
>
> ```sqlsyntax
> inlineFK :=
>   [ CONSTRAINT <constraint_name> ]
>   [ FOREIGN KEY ]
>   REFERENCES <ref_table_name> [ ( <ref_col_name> ) ]
>   [ MATCH { FULL | SIMPLE | PARTIAL } ]
>   [ ON [ UPDATE { CASCADE | SET NULL | SET DEFAULT | RESTRICT | NO ACTION } ]
>        [ DELETE { CASCADE | SET NULL | SET DEFAULT | RESTRICT | NO ACTION } ] ]
>   [ [ NOT ] ENFORCED ]
>   [ [ NOT ] DEFERRABLE ]
>   [ INITIALLY { DEFERRED | IMMEDIATE } ]
>   [ { ENABLE | DISABLE } ]
>   [ { VALIDATE | NOVALIDATE } ]
>   [ { RELY | NORELY } ]
> ```

## Syntax for out-of-line constraints

```sqlsyntax
CREATE TABLE <name> ... ( <col1_name> <col1_type>
                         [ , <col2_name> <col2_type> , ... ]
                         [ , { outoflineUniquePK | outoflineFK } ]
                         [ , { outoflineUniquePK | outoflineFK } ]
                         [ , ... ] )

ALTER TABLE <name> ... ADD { outoflineUniquePK | outoflineFK }
```

Where:

> ```sqlsyntax
> outoflineUniquePK ::=
>   [ CONSTRAINT <constraint_name> ]
>   { UNIQUE | PRIMARY KEY } ( <col_name> [ , <col_name> , ... ] )
>   [ [ NOT ] ENFORCED ]
>   [ [ NOT ] DEFERRABLE ]
>   [ INITIALLY { DEFERRED | IMMEDIATE } ]
>   [ { ENABLE | DISABLE } ]
>   [ { VALIDATE | NOVALIDATE } ]
>   [ { RELY | NORELY } ]
>   [ COMMENT '<string_literal>' ]
> ```
>
> ```sqlsyntax
> outoflineFK :=
>   [ CONSTRAINT <constraint_name> ]
>   FOREIGN KEY ( <col_name> [ , <col_name> , ... ] )
>   REFERENCES <ref_table_name> [ ( <ref_col_name> [ , <ref_col_name> , ... ] ) ]
>   [ MATCH { FULL | SIMPLE | PARTIAL } ]
>   [ ON [ UPDATE { CASCADE | SET NULL | SET DEFAULT | RESTRICT | NO ACTION } ]
>        [ DELETE { CASCADE | SET NULL | SET DEFAULT | RESTRICT | NO ACTION } ] ]
>   [ [ NOT ] ENFORCED ]
>   [ [ NOT ] DEFERRABLE ]
>   [ INITIALLY { DEFERRED | IMMEDIATE } ]
>   [ { ENABLE | DISABLE } ]
>   [ { VALIDATE | NOVALIDATE } ]
>   [ { RELY | NORELY } ]
>   [ COMMENT '<string_literal>' ]
> ```

## Constraint properties

For compatibility with other databases, and for use with hybrid tables, Snowflake provides constraint properties.
The properties that can be specified for a constraint depend on the type:

* Some properties apply to all keys (unique, primary, and foreign).
* Other properties apply only to foreign keys.

> **Important:**
>
> For standard Snowflake tables, these properties are provided to facilitate migrating from other databases. They are not
> enforced or maintained by Snowflake. This means that the defaults can be changed for these properties, but changing the
> defaults results in Snowflake not creating the constraint.
>
> An exception is the RELY property. If you have ensured that the data in your standard tables complies with UNIQUE, PRIMARY
> KEY, and FOREIGN KEY constraints, you can set the RELY property for those constraints. See also
> [Setting the RELY Constraint Property to Eliminate Unnecessary Joins](../../user-guide/join-elimination.md).
>
> If you are creating or altering [hybrid tables](../../user-guide/tables-hybrid.md), the rules and requirements are different.
> See [Overview of Constraints](../constraints-overview.md).

Most of the supported constraint properties are ANSI SQL standard properties; however, the following properties are Snowflake extensions:

* ENABLE | DISABLE
* VALIDATE | NOVALIDATE
* RELY | NORELY

You can also define a comment within an out-of-line constraint definition; see Comments on constraints.

### Properties (for all constraints)

The following properties apply to all constraints (the order of the properties is interchangeable):

```sqlsyntax
[ NOT ] ENFORCED
[ NOT ] DEFERRABLE
INITIALLY { DEFERRED | IMMEDIATE }
{ ENABLE | DISABLE }
{ VALIDATE | NOVALIDATE }
{ RELY | NORELY }
```

`{ ENFORCED | NOT ENFORCED }`
:   Specifies whether the constraint is enforced in a transaction. For standard tables, NOT NULL is the
    *only* type of constraint that is enforced by Snowflake, regardless of this property.

    For hybrid tables, you cannot set the NOT ENFORCED property on PRIMARY KEY, FOREIGN KEY, and UNIQUE constraints.
    Setting this property results in an “invalid constraint property” error.

    See also [Referential Integrity Constraints](../../user-guide/table-considerations.md).

    Default: NOT ENFORCED

`{ DEFERRABLE | NOT DEFERRABLE }`
:   Specifies whether, in subsequent transactions, the constraint check can be deferred until the end of the transaction.

    Default: NOT DEFERRABLE

`INITIALLY { DEFERRED | IMMEDIATE }`
:   For DEFERRABLE constraints, specifies whether the check for the constraints can be deferred, starting from the next transaction.

    Default: INITIALLY DEFERRED

`{ ENABLE | DISABLE }`
:   Specifies whether the constraint is enabled or disabled. These properties are provided for compatibility with Oracle.

    Default: DISABLE

`{ VALIDATE | NOVALIDATE }`
:   Specifies whether to validate existing data on the table when a constraint is created. Applies only when either
    `{ ENFORCED | NOT ENFORCED }` or `{ ENABLE | DISABLE }` is specified.

    Default: NOVALIDATE

`{ RELY | NORELY }`
:   Specifies whether a constraint in NOVALIDATE mode is taken into account during query rewrite.

    If you have ensured that the data in the table complies with the constraints, you can change this property
    to RELY to indicate that the query optimizer should expect such data integrity. For standard tables, it is your responsibility to
    enforce RELY constraints; otherwise, you might risk unintended behavior and unexpected results.

    If the RELY property is set for a constraint and a violation of referential integrity occurs, DML and CTAS statements might insert
    incorrect data.

    Setting the RELY property might improve query
    performance (for example, by [eliminating unnecessary joins](../../user-guide/join-elimination.md)).

    For related PRIMARY KEY and FOREIGN KEY constraints, set this property on both constraints. For example:

    ```sqlexample
    ALTER TABLE table_with_primary_key ALTER CONSTRAINT a_primary_key_constraint RELY;
    ALTER TABLE table_with_foreign_key ALTER CONSTRAINT a_foreign_key_constraint RELY;
    ```

    Default: NORELY

### Properties (for foreign key constraints only)

The following constraint properties apply only to foreign keys (the order of the properties is interchangeable):

```sqlsyntax
MATCH { FULL | SIMPLE | PARTIAL }
ON [ UPDATE { CASCADE | SET NULL | SET DEFAULT | RESTRICT | NO ACTION } ]
   [ DELETE { CASCADE | SET NULL | SET DEFAULT | RESTRICT | NO ACTION } ]
```

`MATCH { FULL | PARTIAL | SIMPLE }`
:   Specifies whether the foreign key constraint is satisfied with regard to NULL values in one or more of the columns.

    Default: MATCH FULL

`UPDATE { CASCADE | SET NULL | SET DEFAULT | RESTRICT | NO ACTION }`
:   Specifies the action performed when the primary/unique key for the foreign key is updated.

    Default: UPDATE NO ACTION

`DELETE { CASCADE | SET NULL | SET DEFAULT | RESTRICT | NO ACTION }`
:   Specifies the action performed when the primary/unique key for the foreign key is deleted.

    Default: DELETE NO ACTION

### Non-default values for ENABLE and VALIDATE properties

For syntax compatibility with other databases, Snowflake supports specifying non-default values for constraint properties.

However, if you specify ENABLE or VALIDATE (the non-default values for these properties) when creating a new
constraint, *the constraint is not created*. This does not apply to RELY. Specifying RELY does result in
the creation of the new constraint.

Note that Snowflake provides a session parameter, [UNSUPPORTED_DDL_ACTION](../parameters.md), which determines whether specifying non-default
values during constraint creation generates an error.

## Comments on constraints

Similar to other database objects and constructs, Snowflake supports comments on constraints:

* Out-of-line constraints support the COMMENT clause within the constraint definition.

  ```sqlexample
  CREATE OR REPLACE TABLE uni (c1 INT, c2 int, CONSTRAINT uni1 UNIQUE(C1) COMMENT 'Unique column');
  ```

* A COMMENT clause within the column definition can be used to comment on the column itself or its constraint:

  ```sqlexample
  CREATE OR REPLACE TABLE uni (c1 INT UNIQUE COMMENT 'Unique column', c2 int);
  ```

Note the following limitations:

* You cannot set comments on constraints by using the [COMMENT](comment.md) command.
* The [DESCRIBE TABLE](desc-table.md) command shows comments defined on columns, but not comments defined on constraints.
  To see comments on constraints, select from the [TABLE_CONSTRAINTS view](../info-schema/table_constraints.md) or the
  [REFERENTIAL_CONSTRAINTS view](../info-schema/referential_constraints.md).
* The COMMENT clause within column and constraint definitions does not support the equals sign (`=`). Do not specify:

  ```sqlexample
  COMMENT = 'My comment'
  ```

  Use the syntax shown in the previous examples:

  ```sqlexample
  COMMENT 'My comment'
  ```

## Usage notes

* NOT NULL specifies that the column does not allow NULL values:

  > * For standard Snowflake tables, this is the only constraint that is enforced. See [Referential Integrity Constraints](../../user-guide/table-considerations.md).
  > * It can be specified only as an inline constraint within the column definition.
  > * The default is to allow NULL values in columns.
* Multi-column constraints (composite unique or primary keys) can only be defined out-of-line.
* When defining foreign keys, either inline or out-of-line, column name(s) for the referenced table do not need to be specified if the
  signature (name and data type) of the foreign key column(s) and the referenced table’s primary key column(s) exactly match.

* If you create a foreign key, the columns in the REFERENCES clause must be listed in the same order as they were
  listed for the primary key. For example:

  ```sqlexample
  CREATE TABLE parent ... CONSTRAINT primary_key_1 PRIMARY KEY (c_1, c_2) ...
  CREATE TABLE child  ... CONSTRAINT foreign_key_1 FOREIGN KEY (...) REFERENCES parent (c_1, c_2) ...
  ```

  In both cases, the order of the columns is `c_1, c_2`. If the order of the columns in the foreign key had been different
  (for example, `c_2, c_1`), the attempt to create the foreign key would have failed.

## Access control requirements

For creating primary key or unique constraints:

* When altering an existing table to add the constraint, you must use a role that has the OWNERSHIP privilege on the table.
* When creating a new table, you must use a role that has the CREATE TABLE privilege on the schema where the table will be created.

For creating foreign key constraints:

* You must use a role that has the OWNERSHIP privilege on the foreign key table.
* You must use a role that has the REFERENCES privilege on the unique/primary key table.

The REFERENCES privilege can be granted to and revoked from roles using the [GRANT <privileges> … TO ROLE](grant-privilege.md) and
[REVOKE <privileges> … FROM ROLE](revoke-privilege.md) commands:

> ```sqlsyntax
> GRANT REFERENCES ON TABLE <pk_table_name> TO ROLE <role_name>
>
> REVOKE REFERENCES ON TABLE <pk_table_name> FROM ROLE <role_name>
> ```

## Examples with standard tables

For examples of constraints with hybrid tables, see [CREATE HYBRID TABLE](create-hybrid-table.md).

The example below shows how to create a simple NOT NULL constraint while creating a table, and another NOT NULL
constraint while altering a table:

Create a table and create a constraint at the same time:

```sqlexample
CREATE TABLE table1 (col1 INTEGER NOT NULL);
```

Alter the table to add a column with a constraint:

```sqlexample
ALTER TABLE table1 ADD COLUMN col2 VARCHAR NOT NULL;
```

The following example specifies that the intent of the column is to hold unique values, but makes clear that the
constraint is not actually enforced. This example also demonstrates how to specify a name for the constraint
(“uniq_col3” in this case.)

```sqlexample
ALTER TABLE table1
  ADD COLUMN col3 VARCHAR NOT NULL CONSTRAINT uniq_col3 UNIQUE NOT ENFORCED;
```

The following creates a parent table with a primary key constraint and another table with a foreign key constraint
that points to the same columns as the first table’s primary key constraint.

```sqlexample
CREATE TABLE table2 (
  col1 INTEGER NOT NULL,
  col2 INTEGER NOT NULL,
  CONSTRAINT pkey_1 PRIMARY KEY (col1, col2) NOT ENFORCED
);
CREATE TABLE table3 (
  col_a INTEGER NOT NULL,
  col_b INTEGER NOT NULL,
  CONSTRAINT fkey_1 FOREIGN KEY (col_a, col_b) REFERENCES table2 (col1, col2) NOT ENFORCED
);
```
