# Source: https://docs.snowflake.com/en/sql-reference/sql/create-hybrid-table.md

# CREATE HYBRID TABLE

Creates a new hybrid table in the current/specified schema or replaces an existing table. A table can have multiple columns,
with each column definition consisting of a name, data type, and optionally whether the column:

* Requires a NOT NULL value.
* Has a default value or is an identity column.
* Has any inline constraints.

> **Note:**
>
> When you create a hybrid table, you must define a PRIMARY KEY constraint on one or more columns.

You can also use the following CREATE TABLE variants to create hybrid tables:

* CREATE HYBRID TABLE … AS SELECT (CTAS) (creates a populated table; also referred to as CTAS)
* CREATE HYBRID TABLE … LIKE (creates an empty copy of an existing hybrid table)

For the full CREATE TABLE syntax used for standard Snowflake tables, see [CREATE TABLE](create-table.md).

> **Tip:**
>
> Before creating and using hybrid tables, you should become familiar with some
> [unsupported features and limitations](../../user-guide/tables-hybrid-limitations.md).

See also:
:   [CREATE INDEX](create-index.md) [DROP INDEX](drop-index.md), [SHOW INDEXES](show-indexes.md), [ALTER TABLE](alter-table.md) , [DROP TABLE](drop-table.md) , [SHOW TABLES](show-tables.md)

## Syntax

```sqlsyntax
CREATE [ OR REPLACE ] HYBRID TABLE [ IF NOT EXISTS ] <table_name>
  ( <col_name> <col_type>
    [
      {
        DEFAULT <expr>
        | { AUTOINCREMENT | IDENTITY }
          [
            {
              ( <start_num> , <step_num> )
              | START <num> INCREMENT <num>
            }
          ]
          [ { ORDER | NOORDER } ]
      }
    ]
    [ NOT NULL ]
    [ inlineConstraint ]
    [ COLLATE '<collation_specification>' ]
    [ COMMENT '<string_literal>' ]
    [ , <col_name> <col_type> [ ... ] ]
    [ , outoflineConstraint ]
    [ , outoflineIndex ]
    [ , ... ]
  )
  [ COMMENT = '<string_literal>' ]
```

Where:

> ```sqlsyntax
> inlineConstraint ::=
>   [ CONSTRAINT <constraint_name> ]
>   { UNIQUE | PRIMARY KEY | { [ FOREIGN KEY ] REFERENCES <ref_table_name> [ ( <ref_col_name> ) ] } }
>   [ <constraint_properties> ]
>
> outoflineConstraint ::=
>   [ CONSTRAINT <constraint_name> ]
>   { UNIQUE [ ( <col_name> [ , <col_name> , ... ] ) ]
>     | PRIMARY KEY [ ( <col_name> [ , <col_name> , ... ] ) ]
>     | [ FOREIGN KEY ] [ ( <col_name> [ , <col_name> , ... ] ) ]
>       REFERENCES <ref_table_name> [ ( <ref_col_name> [ , <ref_col_name> , ... ] ) ]
>   }
>   [ <constraint_properties> ]
>   [ COMMENT '<string_literal>' ]
>
> outoflineIndex ::=
>   INDEX <index_name> ( <col_name> [ , <col_name> , ... ] )
>     [ INCLUDE ( <col_name> [ , <col_name> , ... ] ) ]
> ```
>
> For inline and out-of-line constraint details, see [CREATE | ALTER TABLE … CONSTRAINT](create-table-constraint.md).

## Required parameters

`name`
:   Specifies the identifier (i.e. name) for the table; must be unique for the schema in which the table is created.

    In addition, the identifier must start with an alphabetic character and cannot contain spaces or special characters unless the
    entire identifier string is enclosed in double quotes (for example, `"My object"`). Identifiers enclosed in double quotes are also
    case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

`col_name`
:   Specifies the column identifier (i.e. name). All the requirements for table identifiers also apply to column identifiers.

    For more details, see [Identifier requirements](../identifiers-syntax.md) and [Reserved & limited keywords](../reserved-keywords.md).

    > **Note:**
    >
    > In addition to the standard reserved keywords, the following keywords cannot be used as column identifiers because they are reserved for ANSI-standard context functions:
    >
    > * `CURRENT_DATE`
    > * `CURRENT_ROLE`
    > * `CURRENT_TIME`
    > * `CURRENT_TIMESTAMP`
    > * `CURRENT_USER`
    >
    > For the list of reserved keywords, see [Reserved & limited keywords](../reserved-keywords.md).

`col_type`
:   Specifies the data type for the column.

    For details about the data types that can be specified for table columns, see [SQL data types reference](../../sql-reference-data-types.md).

`PRIMARY KEY ( col_name [ , col_name , ... ] )`
:   Specifies the required primary key constraint for the table, either within a column definition (inline) or separately (out-of-line).
    See also Constraints for hybrid tables.

    For complete syntax details, see [CREATE | ALTER TABLE … CONSTRAINT](create-table-constraint.md). For general information about constraints, see
    [Constraints](../constraints.md).

## Optional parameters

`DEFAULT ...` or . `AUTOINCREMENT ...`
:   Specifies whether a default value is automatically inserted in the column if a value is not explicitly specified via an INSERT or
    CREATE HYBRID TABLE AS SELECT statement:

    > `DEFAULT expr`
    > :   Column default value is defined by the specified expression which can be any of the following:
    >
    >     * Constant value.
    >     * Simple expression.
    >     * Sequence reference (`seq_name.NEXTVAL`).
    >
    >     A simple expression is an expression that returns a scalar value; however, the expression cannot contain
    >     references to:
    >
    >     * Subqueries.
    >     * Aggregates.
    >     * Window functions.
    >     * External functions.
    >
    > `{ AUTOINCREMENT | IDENTITY }` . `[ { ( start_num , step_num ) | START num INCREMENT num } ]` . `[ { ORDER | NOORDER } ]`
    > :   When `AUTOINCREMENT` is used, the default value for the column starts with a specified number and each successive
    >     value is automatically generated. Values generated by an `AUTOINCREMENT` column are guaranteed to be unique. The
    >     difference between any pair of the generated values is guaranteed to be a multiple of the increment amount.
    >
    >     The optional `ORDER` and `NOORDER` parameters specify whether or not the generated values provide ordering
    >     guarantees as specified in [Sequence Semantics](../../user-guide/querying-sequences.md). `NOORDER` is the default option for `AUTOINCREMENT`
    >     columns on hybrid tables. `NOORDER` typically provides significantly better performance for point writes.
    >
    >     These parameters can only be used for columns with numeric data types (NUMBER, INT, FLOAT, etc.)
    >
    >     `AUTOINCREMENT` and `IDENTITY` are synonymous. If either is specified for a column, Snowflake utilizes a
    >     sequence to generate the values for the column. For more information about sequences, see
    >     [Using Sequences](../../user-guide/querying-sequences.md).
    >
    >     The default value for both start and step/increment is `1`.

    Default: No value (the column has no default value)

    > **Note:**
    >
    > * `DEFAULT` and `AUTOINCREMENT` are mutually exclusive; only one can be specified for a column.
    > * For performance-sensitive workloads, `NOORDER` is the recommended option for `AUTOINCREMENT` columns.

`CONSTRAINT ...`
:   Defines an inline or out-of-line constraint for the specified column(s) in the table. UNIQUE and FOREIGN KEY constraints
    are optional for hybrid table columns. See also Constraints for hybrid tables.

    For complete syntax details, see [CREATE | ALTER TABLE … CONSTRAINT](create-table-constraint.md). For general information about constraints, see
    [Constraints](../constraints.md).

`COLLATE 'collation_specification'`
:   Specifies the collation to use for column operations such as string comparisons. This parameter applies only to
    [text columns](../data-types-text.md) that are not indexed. For more information,
    see Collations on hybrid table columns and [Collation specifications](../collation.md).

`INDEX index_name ( col_name [ , col_name , ... ]`
:   Specifies a secondary index on one or more columns in the table. (When you define constraints on hybrid table columns,
    indexes are automatically created on those columns.)

    Indexes cannot be defined on the following columns:

    * [Semi-structured columns](../data-types-semistructured.md) (VARIANT, OBJECT, ARRAY)
      because of space constraints associated with the underlying storage engines for the key of each record.
    * [Geospatial columns](../data-types-geospatial.md) (GEOGRAPHY, GEOMETRY) or
      [VECTOR columns](../data-types-vector.md).
    * [TIMESTAMP_TZ](../data-types-datetime.md) columns (or [TIMESTAMP](../data-types-datetime.md)
      columns that resolve to TIMESTAMP_TZ). TIMESTAMP_NTZ columns are supported.

    Indexes can be defined when the table is created, or with the CREATE INDEX command. For more information about creating indexes for
    hybrid tables, see [Index hybrid tables](../../user-guide/tables-hybrid-index.md) and [CREATE INDEX](create-index.md).

`INCLUDE ( col_name [ , col_name , ... ] )`
:   Specifies one or more included columns for a secondary index. Using included columns with a secondary index is
    particularly useful when queries frequently contain a set of columns in the SELECT list but not in
    the list of WHERE predicates. See [INCLUDE columns](../../user-guide/tables-hybrid-index.md).

    INCLUDE columns cannot be semi-structured columns (VARIANT, OBJECT, ARRAY) or geospatial columns (GEOGRAPHY, GEOMETRY).

`COMMENT = 'string_literal'`
:   Specifies a comment at the column, constraint, or table level. For details, see [Comments on constraints](create-table-constraint.md).

    Default: No value

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| CREATE TABLE | Schema | Note that there is no CREATE HYBRID TABLE privilege. |
| SELECT | Table, external table, view | Required on queried tables and/or views only when cloning a table or executing CTAS statements. |
| APPLY | Masking policy, row access policy, tag | Required only when applying a masking policy, row access policy, object tags, or any combination of these [governance](../../guides-overview-govern.md) features when creating tables. |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

## Usage notes

* To recreate or replace a hybrid table, call the [GET_DDL](../functions/get_ddl.md) function to see the definition of the
  hybrid table before running a CREATE OR REPLACE HYBRID TABLE command.
* You cannot create hybrid tables that are [temporary or transient](../../user-guide/tables-temp-transient.md). In turn, you cannot
  create hybrid tables within transient schemas or databases.
* A schema cannot contain tables and/or views with the same name. When creating a table:

  * If a view with the same name already exists in the schema, an error is returned and the table is not created.
  * If a table with the same name already exists in the schema, an error is returned and the table is not created, unless the
    optional `OR REPLACE` keyword is included in the command.
  > **Important:**
  >
  > Using `OR REPLACE` is the equivalent of using [DROP TABLE](drop-table.md) on the existing table and then
  > creating a new table with the same name.
  >
  > Note that the drop and create actions occur in a single atomic operation. This means that any queries concurrent with the
  > CREATE OR REPLACE TABLE operation use either the old or new table version.
  >
  > Recreating or swapping a table drops its change data.
* The `OR REPLACE` and `IF NOT EXISTS` clauses are mutually exclusive. They can’t both be used in the same statement.
* For information about cloning hybrid tables, see [Clone databases that contain hybrid tables](../../user-guide/tables-hybrid-clone.md).
* Similar to [reserved keywords](../reserved-keywords.md), ANSI-reserved function names
  ([CURRENT_DATE](../functions/current_date.md), [CURRENT_TIMESTAMP](../functions/current_timestamp.md), etc.) cannot be used as
  column names.
* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).

## Constraints for hybrid tables

The following rules apply to constraints that are defined on hybrid tables.

* A hybrid table must be created with a PRIMARY KEY constraint.

  Multi-column (or composite) primary keys are supported. To define a multi-column primary key, use the
  syntax shown in the following example, where the constraint is defined “out of line” and refers to
  multiple columns that were previously defined for the table:

  ```sqlexample
  CREATE OR REPLACE HYBRID TABLE ht2pk (
    col1 INTEGER NOT NULL,
    col2 INTEGER NOT NULL,
    col3 VARCHAR,
    CONSTRAINT pkey_1 PRIMARY KEY (col1, col2)
    );
  ```

* PRIMARY KEY, UNIQUE, and FOREIGN KEY constraints are all enforced on hybrid tables, and you cannot set the NOT ENFORCED
  property on these constraints.
* PRIMARY KEY, UNIQUE, and FOREIGN KEY constraints build their own underlying indexes. The creation of indexes results in
  additional data being stored. Secondary (or covering) indexes can also be defined explicitly when the table is created,
  using the `outoflineIndex` syntax.
* Constraints are enforced at the row level, not at the statement or transaction level (that is, deferred constraints).
* Constraints can only be defined at table creation.
* You cannot alter a column to be UNIQUE.

The following rules apply specifically to FOREIGN KEY constraints:

* A foreign key in a hybrid table that references a primary key cannot be NULL. If you attempt to
  load a NULL value into a column that has a FOREIGN KEY constraint, the load operation fails with a constraint error.
  See Create two hybrid tables with a primary-key/foreign-key relationship.
* FOREIGN KEY constraints are supported only among hybrid tables that belong to the same database.
* The referenced table from a FOREIGN KEY constraint cannot be truncated as long as the FOREIGN KEY relationship exists.
* FOREIGN KEY constraints do not support partial matching.
* FOREIGN KEY constraints do not support deferrable behavior.
* FOREIGN KEY constraints only support [RESTRICT and NO ACTION properties](create-table-constraint.md)
  for DELETE and UPDATE operations.

## Collations on hybrid table columns

Collations are not supported on PRIMARY KEY columns and other indexed columns in hybrid tables. However, if you do not intend to
index a column, and the column has a [character data type](../data-types-text.md), you can specify a COLLATE clause for
that column.

For example:

```sqlexample
CREATE OR REPLACE HYBRID TABLE ht1 (c1 INT PRIMARY KEY, c2 VARCHAR(10) COLLATE 'de');

DESCRIBE TABLE ht1;
```

```output
+------+--------------------------+--------+-------+---------+-------------+------------+-------+------------+---------+-------------+----------------+
| name | type                     | kind   | null? | default | primary key | unique key | check | expression | comment | policy name | privacy domain |
|------+--------------------------+--------+-------+---------+-------------+------------+-------+------------+---------+-------------+----------------|
| C1   | NUMBER(38,0)             | COLUMN | N     | NULL    | Y           | N          | NULL  | NULL       | NULL    | NULL        | NULL           |
| C2   | VARCHAR(10) COLLATE 'de' | COLUMN | Y     | NULL    | N           | N          | NULL  | NULL       | NULL    | NULL        | NULL           |
+------+--------------------------+--------+-------+---------+-------------+------------+-------+------------+---------+-------------+----------------+
```

In some cases, you might need to disable collation for hybrid table columns by using the `DEFAULT_DDL_COLLATION = ''` syntax,
which applies to all columns in the table. You might need to do this when a default collation is set at the account level or for all columns
in all tables in a schema or database.

For example:

```sqlexample
ALTER SCHEMA ht SET DEFAULT_DDL_COLLATION = 'de';

CREATE OR REPLACE HYBRID TABLE ht2 (c1 INT PRIMARY KEY, c2 VARCHAR(10),
  INDEX idx_c2 (c2));
```

```output
391464 (0A000): SQL compilation error: Collations are not supported on primary keys or indexed columns.
```

```sqlexample
CREATE OR REPLACE HYBRID TABLE ht2 (c1 INT PRIMARY KEY, c2 VARCHAR(10),
  INDEX idx_c2 (c2))
  DEFAULT_DDL_COLLATION = '';
```

```output
+---------------------------------+
| status                          |
|---------------------------------|
| Table HT2 successfully created. |
+---------------------------------+
```

Table `ht2` is defined without a collation setting on the indexed column `c2`, despite the fact that
the DEFAULT_DDL_COLLATION parameter is set to `'de'` at the schema level.

For general information about collations, see [Collation control](../collation.md).

## CREATE HYBRID TABLE … AS SELECT (CTAS)

Creates a new hybrid table that contains the results of a query:

> ```sqlsyntax
> CREATE [ OR REPLACE ] HYBRID TABLE <table_name> [ ( <col_name> [ <col_type> ] , <col_name> [ <col_type> ] , ... ) ]
>   [ ... ]
>   AS <query>
> ```
>
> > **Note:**
> >
> > When you use a CTAS statement to create a hybrid table, you must define the table schema explicitly. You must specify the
> > following table properties in the syntax before the definition of the query:
> >
> > * Column definitions
> > * A PRIMARY KEY constraint
> > * Other constraints, as needed (UNIQUE, NOT NULL, FOREIGN KEY)
> > * Secondary indexes (and any INCLUDE columns)
> >
> > The schema of the new hybrid table can’t be inferred from a SELECT statement.

The number of column names specified must match the number of [SELECT](select.md) list items in the query.

To create the table with rows in a specific order, use an ORDER BY clause at the end of the query.

For information about loading hybrid tables, see [Loading data](../../user-guide/tables-hybrid-create.md).

## CREATE HYBRID TABLE … LIKE

Creates a new hybrid table with the same column definitions as an existing hybrid table, but without copying data from the
existing table.

Column names, types, defaults, constraints, and indexes are copied to the new table:

> ```sqlsyntax
> CREATE [ OR REPLACE ] HYBRID TABLE <table_name> LIKE <source_hybrid_table>
>   [ ... ]
> ```
>
> > **Note:**
> >
> > CREATE HYBRID TABLE … LIKE only supports another hybrid table as the source table type.
> >
> > CREATE HYBRID TABLE … LIKE for a table with an auto-increment sequence accessed through a data share is
> > not supported.

## Examples

Create a hybrid table in the current database with `customer_id` as the primary key, a unique constraint on `email`,
and a secondary index on `full_name`:

```sqlexample
CREATE HYBRID TABLE mytable (
  customer_id INT AUTOINCREMENT PRIMARY KEY,
  full_name VARCHAR(255),
  email VARCHAR(255) UNIQUE,
  extended_customer_info VARIANT,
  INDEX index_full_name (full_name)
);
```

```output
+-------------------------------------+
| status                              |
|-------------------------------------|
| Table MYTABLE successfully created. |
+-------------------------------------+
```

Insert a row into this table:

```sqlexample
INSERT INTO mytable (customer_id, full_name, email, extended_customer_info)
  SELECT 100, 'Jane Doe', 'jdoe@example.com',
    parse_json('{"address": "1234 Main St", "city": "San Francisco", "state": "CA", "zip":"94110"}');
```

```output
+-------------------------+
| number of rows inserted |
|-------------------------|
|                       1 |
+-------------------------+
```

The primary key must be unique. For example, if you try to insert the same primary key from the previous example a second time,
the command fails with the following error:

```output
200001 (22000): Primary key already exists
```

The email address must also follow the inline UNIQUE constraint. For example, if you attempt to insert two records with the
same email address, the statement fails with the following error:

```output
Duplicate key value violates unique constraint "SYS_INDEX_MYTABLE_UNIQUE_EMAIL"
```

View table properties and metadata. Note the value of the `is_hybrid` column:

```sqlexample
SHOW TABLES LIKE 'mytable';
```

```output
+-------------------------------+---------+---------------+-------------+-------+-----------+---------+------------+------+-------+--------+----------------+----------------------+-----------------+---------------------+------------------------------+---------------------------+-------------+
| created_on                    | name    | database_name | schema_name | kind  | is_hybrid | comment | cluster_by | rows | bytes | owner  | retention_time | automatic_clustering | change_tracking | search_optimization | search_optimization_progress | search_optimization_bytes | is_external |
|-------------------------------+---------+---------------+-------------+-------+-----------+---------+------------+------+-------+--------+----------------+----------------------+-----------------+---------------------+------------------------------+---------------------------+-------------|
| 2022-02-23 23:53:19.707 +0000 | MYTABLE | MYDB          | PUBLIC      | TABLE | Y         |         |            | NULL |  NULL | MYROLE | 10             | OFF                  | OFF             | OFF                 |                         NULL |                      NULL | N           |
+-------------------------------+---------+---------------+-------------+-------+-----------+---------+------------+------+-------+--------+----------------+----------------------+-----------------+---------------------+------------------------------+---------------------------+-------------+
```

View details for all hybrid tables:

```sqlexample
SHOW HYBRID TABLES;
```

```output
+-------------------------------+---------------------------+---------------+-------------+--------------+--------------+------+-------+---------+
| created_on                    | name                      | database_name | schema_name | owner        | datastore_id | rows | bytes | comment |
|-------------------------------+---------------------------+---------------+-------------+--------------+--------------+------+-------+---------|
| 2022-02-24 02:07:31.877 +0000 | MYTABLE                   | DEMO_DB       | PUBLIC      | ACCOUNTADMIN |         2002 | NULL |  NULL |         |
+-------------------------------+---------------------------+---------------+-------------+--------------+--------------+------+-------+---------+
```

Display information about the columns in the table:

```sqlexample
DESCRIBE TABLE mytable;
```

```output
+-------------------+--------------+--------+-------+---------+-------------+------------+-------+------------+---------+-------------+
| name              | type         | kind   | null? | default | primary key | unique key | check | expression | comment | policy name |
|-------------------+--------------+--------+-------+---------+-------------+------------+-------+------------+---------+-------------|
| CUSTOMER_ID       | NUMBER(38,0) | COLUMN | N     | NULL    | Y           | N          | NULL  | NULL       | NULL    | NULL        |
| FULL_NAME         | VARCHAR(256) | COLUMN | Y     | NULL    | N           | N          | NULL  | NULL       | NULL    | NULL        |
| APPLICATION_STATE | VARIANT      | COLUMN | Y     | NULL    | N           | N          | NULL  | NULL       | NULL    | NULL        |
+-------------------+--------------+--------+-------+---------+-------------+------------+-------+------------+---------+-------------+
```

Select data from the table:

```sqlexample
SELECT customer_id, full_name, email, extended_customer_info
  FROM mytable
  WHERE extended_customer_info['state'] = 'CA';
```

```output
+-------------+-----------+------------------+------------------------------+
| CUSTOMER_ID | FULL_NAME | EMAIL            | EXTENDED_CUSTOMER_INFO       |
|-------------+-----------+------------------+------------------------------|
|         100 | Jane Doe  | jdoe@example.com | {                            |
|             |           |                  |   "address": "1234 Main St", |
|             |           |                  |   "city": "San Francisco",   |
|             |           |                  |   "state": "CA",             |
|             |           |                  |   "zip": "94110"             |
|             |           |                  | }                            |
+-------------+-----------+------------------+------------------------------+
```

### Create two hybrid tables with a primary-key/foreign-key relationship

This example shows the creation of two hybrid tables that reference each other. The first table, `team`, has a
PRIMARY KEY constraint on its `team_id` column. The second table, `player`, has a FOREIGN KEY constraint on
its `team_id` column, which references the `team_id` column in the `team` table.

```sqlexample
CREATE OR REPLACE HYBRID TABLE team
  (team_id INT PRIMARY KEY,
  team_name VARCHAR(40),
  stadium VARCHAR(40));

CREATE OR REPLACE HYBRID TABLE player
  (player_id INT PRIMARY KEY,
  first_name VARCHAR(40),
  last_name VARCHAR(40),
  team_id INT,
  FOREIGN KEY (team_id) REFERENCES team(team_id));
```

You can verify that referential integrity is enforced by inserting some rows into both tables. You can also
confirm that NULL values are not allowed in columns defined as foreign keys.

The first insert into the `player` table succeeds as expected. The second insert fails because `3`
does not exist as an ID in the `team` table. The third insert fails because NULL is not allowed as a foreign key.

```sqlexample
INSERT INTO team VALUES (1, 'Bayern Munich', 'Allianz Arena');
INSERT INTO player VALUES (100, 'Harry', 'Kane', 1);
INSERT INTO player VALUES (301, 'Gareth', 'Bale', 3);
```

```output
200009 (22000): Foreign key constraint "SYS_INDEX_PLAYER_FOREIGN_KEY_TEAM_ID_TEAM_TEAM_ID" was violated.
```

```sqlexample
INSERT INTO player VALUES (200, 'Tommy', 'Atkins', NULL);
```

```output
200009 (22000): Foreign key constraint "SYS_INDEX_PLAYER_FOREIGN_KEY_TEAM_ID_TEAM_TEAM_ID" was violated.
```

```sqlexample
SELECT * FROM team t, player p WHERE t.team_id=p.team_id;
```

```output
+---------+---------------+---------------+-----------+------------+-----------+---------+
| TEAM_ID | TEAM_NAME     | STADIUM       | PLAYER_ID | FIRST_NAME | LAST_NAME | TEAM_ID |
|---------+---------------+---------------+-----------+------------+-----------+---------|
|       1 | Bayern Munich | Allianz Arena |       100 | Harry      | Kane      |       1 |
+---------+---------------+---------------+-----------+------------+-----------+---------+
```

A possible workaround for the rejection of NULL in this case is to insert a “dummy” row into the
`team` table with a team ID of `0`. Then you can insert rows into the `player` table that use a
matching placeholder value of `0` instead of NULL. For example:

```sqlexample
INSERT INTO team VALUES (0, 'Unknown', 'Unknown');
INSERT INTO player VALUES (200, 'Tommy', 'Atkins', 0);

SELECT * FROM team t, player p WHERE t.team_id=p.team_id;
```

```output
+---------+---------------+---------------+-----------+------------+-----------+---------+
| TEAM_ID | TEAM_NAME     | STADIUM       | PLAYER_ID | FIRST_NAME | LAST_NAME | TEAM_ID |
|---------+---------------+---------------+-----------+------------+-----------+---------|
|       1 | Bayern Munich | Allianz Arena |       100 | Harry      | Kane      |       1 |
|       0 | Unknown       | Unknown       |       200 | Tommy      | Atkins    |       0 |
+---------+---------------+---------------+-----------+------------+-----------+---------+
```

### Create a hybrid table with a comment on the primary key column

Create a hybrid table that includes a comment within the column definition for the primary key.

```sqlexample
CREATE OR REPLACE HYBRID TABLE ht1pk
  (COL1 NUMBER(38,0) NOT NULL COMMENT 'Primary key',
  COL2 NUMBER(38,0) NOT NULL,
  COL3 VARCHAR(16777216),
  CONSTRAINT PKEY_1 PRIMARY KEY (COL1));

DESCRIBE TABLE ht1pk;
```

```output
+------+-------------------+--------+-------+---------+-------------+------------+-------+------------+-------------+-------------+----------------+
| name | type              | kind   | null? | default | primary key | unique key | check | expression | comment     | policy name | privacy domain |
|------+-------------------+--------+-------+---------+-------------+------------+-------+------------+-------------+-------------+----------------|
| COL1 | NUMBER(38,0)      | COLUMN | N     | NULL    | Y           | N          | NULL  | NULL       | Primary key | NULL        | NULL           |
| COL2 | NUMBER(38,0)      | COLUMN | N     | NULL    | N           | N          | NULL  | NULL       | NULL        | NULL        | NULL           |
| COL3 | VARCHAR(16777216) | COLUMN | Y     | NULL    | N           | N          | NULL  | NULL       | NULL        | NULL        | NULL           |
+------+-------------------+--------+-------+---------+-------------+------------+-------+------------+-------------+-------------+----------------+
```

Note that if you put this comment in the CONSTRAINT clause, the comment will not be visible in the DESCRIBE TABLE output. You can query
the [TABLE_CONSTRAINTS view](../info-schema/table_constraints.md) to see complete information about constraints.
