# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/translation-references/oracle/sql-translation-reference/create-table.md

# Source: https://docs.snowflake.com/en/sql-reference/sql/create-table.md

# CREATE TABLE

Creates a new table in the current/specified schema, replaces an existing table, or alters an existing table. A table can have multiple
columns, with each column definition consisting of a name, data type, and optionally whether the column:

* Requires a value (NOT NULL).
* Has a default value.
* Has any referential integrity constraints (primary key, foreign key, etc.).

In addition, this command supports the following variants:

* CREATE OR ALTER TABLE (creates a table if it doesn’t exist, or alters it according to the table definition)
* CREATE TABLE … AS SELECT (creates a populated table; also referred to as CTAS)
* CREATE TABLE … USING TEMPLATE (creates a table with the column definitions derived from a set of staged files)
* CREATE TABLE … LIKE (creates an empty copy of an existing table)
* CREATE TABLE … CLONE (creates a clone of an existing table)
* CREATE TABLE … FROM ARCHIVE OF (creates a table from archived data)
* CREATE TABLE … FROM BACKUP SET (restores a table from a backup under a new name)

See also:
:   [ALTER TABLE](alter-table.md) , [DROP TABLE](drop-table.md) , [SHOW TABLES](show-tables.md) , [DESCRIBE TABLE](desc-table.md)

## Syntax

```sqlsyntax
CREATE [ OR REPLACE ]
    [ { [ { LOCAL | GLOBAL } ] TEMP | TEMPORARY | VOLATILE | TRANSIENT } ]
  TABLE [ IF NOT EXISTS ] <table_name>

  (
    -- Column definition
    <col_name> <col_type>
      [ inlineConstraint ]
      [ NOT NULL ]
      [ COLLATE '<collation_specification>' ]
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
      [ [ WITH ] MASKING POLICY <policy_name> [ USING ( <col_name> , <cond_col1> , ... ) ] ]
      [ [ WITH ] PROJECTION POLICY <policy_name> ]
      [ [ WITH ] TAG ( <tag_name> = '<tag_value>' [ , <tag_name> = '<tag_value>' , ... ] ) ]
      [ COMMENT '<string_literal>' ]

    -- Additional column definitions
    [ , <col_name> <col_type> [ ... ] ]

    -- Out-of-line constraints
    [ , outoflineConstraint [ ... ] ]
  )

  [ CLUSTER BY ( <expr> [ , <expr> , ... ] ) ]
  [ ENABLE_SCHEMA_EVOLUTION = { TRUE | FALSE } ]
  [ DATA_RETENTION_TIME_IN_DAYS = <integer> ]
  [ MAX_DATA_EXTENSION_TIME_IN_DAYS = <integer> ]
  [ CHANGE_TRACKING = { TRUE | FALSE } ]
  [ DEFAULT_DDL_COLLATION = '<collation_specification>' ]
  [ COPY GRANTS ]
  [ COPY TAGS ]
  [ COMMENT = '<string_literal>' ]
  [ [ WITH ] ROW ACCESS POLICY <policy_name> ON ( <col_name> [ , <col_name> ... ] ) ]
  [ [ WITH ] AGGREGATION POLICY <policy_name> [ ENTITY KEY ( <col_name> [ , <col_name> ... ] ) ] ]
  [ [ WITH ] JOIN POLICY <policy_name> [ ALLOWED JOIN KEYS ( <col_name> [ , ... ] ) ] ]
  [ [ WITH ] STORAGE LIFECYCLE POLICY <policy_name> ON ( <col_name> [ , <col_name> ... ] ) ]
  [ [ WITH ] TAG ( <tag_name> = '<tag_value>' [ , <tag_name> = '<tag_value>' , ... ] ) ]
  [ WITH CONTACT ( <purpose> = <contact_name> [ , <purpose> = <contact_name> ... ] ) ]
  [ ROW_TIMESTAMP = { TRUE | FALSE } ]
```

Where:

> `col_name` is an [object identifier](../identifiers.md). It must follow the [requirements for Snowflake identifiers](../identifiers-syntax.md).
>
> `col_type` is one of the [Snowflake data types](../../sql-reference-data-types.md), such as
> [NUMBER](../data-types-numeric.md) or [VARCHAR](../data-types-text.md).
>
> ```sqlsyntax
> inlineConstraint ::=
>   [ CONSTRAINT <constraint_name> ]
>   { UNIQUE
>     | PRIMARY KEY
>     | [ FOREIGN KEY ] REFERENCES <ref_table_name> [ ( <ref_col_name> ) ]
>   }
>   [ <constraint_properties> ]
> ```
>
> For additional inline constraint details, see [CREATE | ALTER TABLE … CONSTRAINT](create-table-constraint.md).
>
> ```sqlsyntax
> outoflineConstraint ::=
>   [ CONSTRAINT <constraint_name> ]
>   { UNIQUE [ ( <col_name> [ , <col_name> , ... ] ) ]
>     | PRIMARY KEY [ ( <col_name> [ , <col_name> , ... ] ) ]
>     | [ FOREIGN KEY ] [ ( <col_name> [ , <col_name> , ... ] ) ]
>       REFERENCES <ref_table_name> [ ( <ref_col_name> [ , <ref_col_name> , ... ] ) ]
>   }
>   [ <constraint_properties> ]
>   [ COMMENT '<string_literal>' ]
> ```
>
> For additional out-of-line constraint details, see [CREATE | ALTER TABLE … CONSTRAINT](create-table-constraint.md).

> **Note:**
>
> Do not specify copy options using the CREATE STAGE, ALTER STAGE, CREATE TABLE, or ALTER TABLE commands. We recommend that you use the [COPY INTO <table>](copy-into-table.md) command to specify copy options.

**Restored table (from a backup)**

```sqlsyntax
CREATE TABLE <name> FROM BACKUP SET <backup_set> IDENTIFIER '<backup_id>'
```

## Variant syntax

### CREATE OR ALTER TABLE

Creates a table if it doesn’t exist, or alters it according to the table definition. The CREATE OR ALTER TABLE syntax follows the
rules of a CREATE TABLE statement and has the same limitations as an ALTER TABLE statement. If the table is transformed, existing
data in the table is preserved when possible. If a column must be dropped, data loss might occur.

The following changes are supported when altering a table:

* Change table properties and parameters. For example, ENABLE_SCHEMA_EVOLUTION, DATA_RETENTION_TIME_IN_DAYS, or CLUSTER BY.
* Change column data type, default value, nullability, comment, or autoincrement.
* Add new columns to the end of the column list.
* Drop columns.
* Add, drop, or modify inline or out-of-line constraints.
* Add, drop, or modify clustering keys.

For more information, see CREATE OR ALTER TABLE usage notes.

```sqlsyntax
CREATE OR ALTER
    [ { [ { LOCAL | GLOBAL } ] TEMP | TEMPORARY | TRANSIENT } ]
  TABLE <table_name> (
    -- Column definition
    <col_name> <col_type>
      [ inlineConstraint ]
      [ NOT NULL ]
      [ COLLATE '<collation_specification>' ]
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
      [ COMMENT '<string_literal>' ]

    -- Additional column definitions
    [ , <col_name> <col_type> [ ... ] ]

    -- Out-of-line constraints
    [ , outoflineConstraint [ ... ] ]
  )
  [ CLUSTER BY ( <expr> [ , <expr> , ... ] ) ]
  [ ENABLE_SCHEMA_EVOLUTION = { TRUE | FALSE } ]
  [ DATA_RETENTION_TIME_IN_DAYS = <integer> ]
  [ MAX_DATA_EXTENSION_TIME_IN_DAYS = <integer> ]
  [ CHANGE_TRACKING = { TRUE | FALSE } ]
  [ DEFAULT_DDL_COLLATION = '<collation_specification>' ]
  [ COMMENT = '<string_literal>' ]
  [ ROW_TIMESTAMP = { TRUE | FALSE } ]
```

### CREATE TABLE … AS SELECT (also referred to as CTAS)

Creates a new table populated with the data returned by a query:

> ```sqlsyntax
> CREATE [ OR REPLACE ] TABLE <table_name> [ ( <col_name> [ <col_type> ] , <col_name> [ <col_type> ] , ... ) ]
>   [ CLUSTER BY ( <expr> [ , <expr> , ... ] ) ]
>   [ COPY GRANTS ]
>   [ COPY TAGS ]
>   [ ... ]
>   AS <query>
> ```

A masking policy can be applied to a column in a CTAS statement. Specify the masking policy after the column data type. Similarly, a
row access policy can be applied to the table. For example:

> ```sqlsyntax
> CREATE TABLE <table_name> ( <col1> <data_type> [ WITH ] MASKING POLICY <policy_name> [ , ... ] )
>   ...
>   [ WITH ] ROW ACCESS POLICY <policy_name> ON ( <col1> [ , ... ] )
>   [ ... ]
>   AS <query>
> ```

> **Note:**
>
> In a CTAS statement, the COPY GRANTS clause is valid only when combined with the OR REPLACE clause. COPY GRANTS copies
> permissions from the table being replaced with CREATE OR REPLACE (if it already exists), not from the source
> table(s) being queried in the SELECT statement. CTAS with COPY GRANTS allows you to overwrite a table with a new
> set of data while keeping existing grants on that table.
>
> For more details about COPY GRANTS, see COPY GRANTS in this document.

### CREATE TABLE … USING TEMPLATE

Creates a new table with the column definitions derived from a set of staged files using the [INFER_SCHEMA](../functions/infer_schema.md) function.
This feature supports Apache Parquet, Apache Avro, ORC, JSON, and CSV files.

> ```sqlsyntax
> CREATE [ OR REPLACE ] TABLE <table_name>
>   [ COPY GRANTS ]
>   USING TEMPLATE <query>
>   [ ... ]
> ```

> **Note:**
>
> If the statement is replacing an existing table of the same name, then the grants are copied from the table
> being replaced. If there is no existing table of that name, then the grants are copied from the source table
> being cloned.

For more details about COPY GRANTS, see COPY GRANTS in this document.

### CREATE TABLE … LIKE

Creates a new table with the same column definitions as an existing table, but without copying data from the existing table. Column
names, types, defaults, and constraints are copied to the new table:

> ```sqlsyntax
> CREATE [ OR REPLACE ] TABLE <table_name> LIKE <source_table>
>   [ CLUSTER BY ( <expr> [ , <expr> , ... ] ) ]
>   [ COPY GRANTS ]
>   [ ... ]
> ```

For more details about COPY GRANTS, see COPY GRANTS in this document.

> > **Note:**
> >
> > CREATE TABLE … LIKE for a table with an auto-increment sequence accessed through a data share is currently not
> > supported.

### CREATE TABLE … CLONE

Creates a new table with the same column definitions and containing all the existing data from the source table, without actually
copying the data. This variant can also be used to clone a table at a specific time/point in the past (using
[Time Travel](../../user-guide/data-time-travel.md)):

> ```sqlsyntax
> CREATE [ OR REPLACE ]
>     [ {
>           [ { LOCAL | GLOBAL } ] TEMP [ READ ONLY ] |
>           TEMPORARY [ READ ONLY ] |
>           VOLATILE |
>           TRANSIENT
>     } ]
>   TABLE <name> CLONE <source_table>
>     [ { AT | BEFORE } ( { TIMESTAMP => <timestamp> | OFFSET => <time_difference> | STATEMENT => <id> } ) ]
>     [ COPY GRANTS ]
>     [ ... ]
> ```

> **Note:**
>
> * If the statement is replacing an existing table of the same name,
>   then the grants are copied from the table being replaced.
>   If there is no existing table of that name, then the grants are
>   copied from the source table being cloned.
> * If you directly clone a table, any streams on that table are not cloned.
> * If you clone a schema including tables with streams, then the streams are also cloned.

For more details about COPY GRANTS, see COPY GRANTS in this document.

For more details about cloning, see [CREATE <object> … CLONE](create-clone.md).

For details about cloning dynamic tables to tables, see [Clone a dynamic table to a new table](../../user-guide/dynamic-tables-clone.md).

### CREATE TABLE … FROM ARCHIVE OF

Creates a new table containing rows that were archived by a
[storage lifecycle policy](../../user-guide/storage-management/storage-lifecycle-policies.md).
You can specify filter conditions to retrieve specific archived data.

```sqlsyntax
CREATE [ TRANSIENT ] TABLE [ IF NOT EXISTS ] <name>
  FROM ARCHIVE OF <source_table> [ [ AS ] <alias_name> ]
  WHERE <expression>
```

For more information, see FROM ARCHIVE OF parameters and
the Usage notes.

## Required parameters

`name`
:   Specifies the identifier (i.e. name) for the table; must be unique for the schema in which the table is created.

    In addition, the identifier must start with an alphabetic character and cannot contain spaces or special characters unless the
    entire identifier string is enclosed in double quotes (e.g. `"My object"`). Identifiers enclosed in double quotes are also
    case-sensitive.

    For more details, see [Identifier requirements](../identifiers-syntax.md).

`col_name`
:   Specifies the column identifier (i.e. name). All the requirements for table identifiers also apply to column identifiers.

    For more details, see [Identifier requirements](../identifiers-syntax.md) and [Reserved & limited keywords](../reserved-keywords.md).

    > **Note:**
    >
    > In addition to the standard reserved keywords, the following keywords cannot be used as column identifiers because they are
    > reserved for ANSI-standard context functions:
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

`query`
:   Required for CTAS and USING TEMPLATE.

    * For CTAS, specifies the [SELECT statement](../constructs.md) that populates the table. This query must be
      specified last in the CTAS statement, regardless of the other parameters that you include.
    * For CREATE TABLE … USING TEMPLATE, specifies the subquery that calls the [INFER_SCHEMA](../functions/infer_schema.md) function and
      formats the output as an array. Alternatively, `USING TEMPLATE` accepts the INFER_SCHEMA output as a string
      literal or variable.

`source_table`
:   Required for LIKE, CLONE, and FROM ARCHIVE OF.

    * For CREATE TABLE … LIKE, specifies the table from which properties and column definitions are copied.
    * For CREATE TABLE … CLONE, specifies the table to use as the source for the clone.
    * For CREATE TABLE … FROM ARCHIVE OF, see FROM ARCHIVE OF parameters.

## Backup parameters

The FROM BACKUP SET clause restores a table from a backup. You don’t specify other table
properties because they’re all the same as in the backed-up table.

> **Note:**
>
> The FROM SNAPSHOT SET clause is deprecated. Use FROM BACKUP SET instead.

This form doesn’t have a CREATE OR REPLACE clause. You typically either restore the
table under a new name and recover any data or other objects from this new table,
or rename the original table and then restore the table under the original name.

> **Note:**
>
> The restored table is independent of the original table from the backup.
> There isn’t any cloning relationship between the restored and original tables.
> Therefore, all the micro-partitions in the restored table are owned by that table.
>
> If you want to make backups of the newly restored table, create a new backup set for it.

For more information about backups, see [Backups for disaster recovery and immutable storage](../../user-guide/backups.md).

`backup_set`
:   Specifies the name of a backup set created for a specific table.
    You can use the SHOW BACKUP SETS command to locate the right backup set.

`backup_id`
:   Specifies the identifier of a specific backup within that backup set.
    You can use the SHOW BACKUPS IN BACKUP SET command to locate the right identifier within the backup
    set, based on the creation date and time for the backup.

## FROM ARCHIVE OF parameters

`source_table`
:   Specifies the table whose rows have been archived by a
    [storage lifecycle policy](../../user-guide/storage-management/storage-lifecycle-policies.md). This is the table from which
    archived data is retrieved.

`[ AS ] alias_name`
:   Specifies an optional alias name for the source table reference. Use this alias when referencing columns
    in the WHERE clause.

    Alias names must follow the rules for [Object identifiers](../identifiers.md).

`WHERE expression`
:   Specifies a required condition that filters the archived rows to retrieve. The expression can reference columns
    from the source table (using the alias if specified).

    For more information about WHERE expressions, see [WHERE](../constructs/where.md).

## Optional parameters

`{ [ { LOCAL | GLOBAL } ] TEMP [ READ ONLY] |` . `TEMPORARY [ READ ONLY] |` . `VOLATILE |` . `TRANSIENT }`
:   Specifies that the table persists only for the duration of the [session](../../user-guide/session-policies.md) that you created it in. A
    temporary table and all its contents are dropped at the end of the session.

    The synonyms and abbreviations for `TEMPORARY` (e.g. `GLOBAL TEMPORARY`) are provided for compatibility with other databases
    (e.g. to prevent errors when migrating CREATE TABLE statements). Tables created with any of these keywords appear and behave identically
    to a table created with the `TEMPORARY` keyword.

    Default: No value. If a table is not declared as `TEMPORARY` or `TRANSIENT`, the table is permanent.

    If you want to avoid unexpected conflicts, avoid naming temporary tables after tables that already exist in the schema.

    If you created a temporary table with the same name as another table in the schema, all queries and operations used on the table only
    affect the temporary table in the session, until you drop the temporary table. If you drop the table, you drop the temporary table, and
    not the table that already exists in the schema.

    For information about temporary or transient tables, and how they can affect storage and cost, refer to the following resources:

    * [Working with Temporary and Transient Tables](../../user-guide/tables-temp-transient.md)
    * [Storage costs for Time Travel and Fail-safe](../../user-guide/data-cdp-storage-costs.md)

    `READ ONLY`
    :   Specifies that the table is read-only. READ ONLY is valid only for a temporary table that is being created with the
        CREATE TABLE … CLONE variant of the CREATE TABLE command.

        A read-only table does not allow DML operations and only allows the following subset of DDL operations:

        * ALTER TABLE … { ALTER | MODIFY } COLUMN … { SET | UNSET } COMMENT
        * ALTER TABLE … { ALTER | MODIFY } COLUMN … { SET | UNSET } MASKING POLICY
        * ALTER TABLE … { ALTER | MODIFY } COLUMN … { SET | UNSET } TAG
        * ALTER TABLE … RENAME COLUMN … TO
        * ALTER TABLE … RENAME TO
        * ALTER TABLE … { SET | UNSET } COMMENT
        * ALTER TABLE … { SET | UNSET } TAG
        * COMMENT
        * DESCRIBE
        * DROP
        * SHOW
        * UNDROP

        Read-only tables have a `METADATA$ROW_POSITION` column. This metadata column assigns a row number to each row in
        the table that is continuous and starts from 0. The row number assigned to each row remains unchanged until the
        read-only table is dropped.

`TRANSIENT`
:   Specifies that the table is transient.

    Like a permanent table, a transient table exists until explicitly dropped and is visible to any
    user with the appropriate privileges. However, transient tables have a lower level of data protection than permanent tables, meaning
    that data in a transient table might be lost in the event of a system failure. As such, transient tables should only be used for data
    that can be recreated externally to Snowflake.

    Default: No value. If a table is not declared as `TRANSIENT` or `TEMPORARY`, the table is permanent.

    > **Note:**
    >
    > Transient tables have some storage considerations.
    >
    > For more information about these and other considerations when deciding whether to create temporary or transient tables, see
    > [Working with Temporary and Transient Tables](../../user-guide/tables-temp-transient.md) and [Storage costs for Time Travel and Fail-safe](../../user-guide/data-cdp-storage-costs.md).

`CONSTRAINT ...`
:   Defines an inline or out-of-line constraint for the specified column(s) in the table.

    For syntax details, see [CREATE | ALTER TABLE … CONSTRAINT](create-table-constraint.md). For more information about constraints, see [Constraints](../constraints.md).

`COLLATE 'collation_specification'`
:   Specifies the collation to use for column operations such as string comparisons. This parameter applies only to
    [text columns](../data-types-text.md): VARCHAR, STRING, TEXT, and so on. For more information,
    see [Collation specifications](../collation.md).

`DEFAULT ...` or . `AUTOINCREMENT ...`
:   Specifies whether a default value is automatically inserted in the column if a value is not explicitly specified via an INSERT
    or CREATE TABLE AS SELECT statement:

    > `DEFAULT expr`
    > :   Column default value is defined by the specified expression which can be any of the following:
    >
    >     * Constant value.
    >     * [Sequence reference](../../user-guide/querying-sequences.md) (`seq_name.NEXTVAL`).
    >     * Simple expression that returns a scalar value.
    >
    >       The simple expression can include a SQL UDF (user-defined function) if the UDF is not a
    >       [secure UDF](../../developer-guide/secure-udf-procedure.md).
    >
    >       > **Note:**
    >       >
    >       > If a default expression refers to a SQL UDF, then the function is replaced by its
    >       > definition at table creation time. If the user-defined function is redefined in the future, this does not
    >       > update the column’s default expression.
    >
    >       The simple expression cannot contain references to:
    >
    >       > + Subqueries.
    >       > + Aggregates.
    >       > + Window functions.
    >       > + Secure UDFs.
    >       > + UDFs written in languages other than SQL (e.g. Java, JavaScript).
    >       > + External functions.
    >
    > `{ AUTOINCREMENT | IDENTITY }` . `[ { ( start_num , step_num ) | START num INCREMENT num } ]` . `[ { ORDER | NOORDER } ]`
    > :   When you specify AUTOINCREMENT or IDENTITY, the default value for the column starts with a specified number and each
    >     successive value automatically increments by the specified amount.
    >
    >     AUTOINCREMENT and IDENTITY are synonymous and can be used only for columns with numeric data types, such as NUMBER, INT,
    >     FLOAT.
    >
    >     > **Caution:**
    >     >
    >     > Snowflake uses a sequence to generate the values for an auto-incremented column. Sequences have limitations;
    >     > see [Sequence Semantics](../../user-guide/querying-sequences.md).
    >
    >     The default value for both the start value and the step/increment value is `1`.
    >
    >     > **Note:**
    >     >
    >     > Manually inserting values into an AUTOINCREMENT or IDENTITY column can result in duplicate values. If you manually insert the
    >     > value `5` into an AUTOINCREMENT or IDENTITY column, a subsequently inserted row might use the same value `5` as the
    >     > default value for the column.
    >
    >     Use ORDER or NOORDER to specify whether or not the values are generated for the auto-incremented column in
    >     [increasing or decreasing order](../../user-guide/querying-sequences.md).
    >
    >     * ORDER specifies that the values generated for a sequence or auto-incremented column are in increasing order (or, if the interval
    >       is a negative value, in decreasing order).
    >
    >       For example, if a sequence or auto-incremented column has `START 1 INCREMENT 2`, the generated values might be
    >       `1`, `3`, `5`, `7`, `9`, etc.
    >     * NOORDER specifies that the values are not guaranteed to be in increasing order.
    >
    >       For example, if a sequence has `START 1 INCREMENT 2`, the generated values might be `1`, `3`, `101`, `5`, `103`, etc.
    >
    >       NOORDER can improve performance when multiple INSERT operations are performed concurrently (for example, when multiple
    >       clients are executing multiple INSERT statements).
    >
    >     If you do not specify ORDER or NOORDER, the [NOORDER_SEQUENCE_AS_DEFAULT](../parameters.md) parameter determines which property is
    >     set.

    > **Note:**
    >
    > DEFAULT and AUTOINCREMENT are mutually exclusive; only one can be specified for a column.

`MASKING POLICY = policy_name`
:   Specifies the [masking policy](../../user-guide/security-column-intro.md) to set on a column.

    This parameter is not supported by the CREATE OR ALTER variant syntax.

`PROJECTION POLICY policy_name`
:   Specifies the [projection policy](../../user-guide/projection-policies.md) to set on a column.

    This parameter is not supported by the CREATE OR ALTER variant syntax.

`COMMENT 'string_literal'`
:   Specifies a comment for the column.

    (Note that comments can be specified at the column level or the table level. The syntax for each is slightly different.)

`USING ( col_name , cond_col_1 ... )`
:   Specifies the arguments to pass into the conditional masking policy SQL expression.

    The first column in the list specifies the column for the policy conditions to mask or tokenize the data and must match the
    column to which the masking policy is set.

    The additional columns specify the columns to evaluate to determine whether to mask or tokenize the data in each row of the query result
    when a query is made on the first column.

    If the USING clause is omitted, Snowflake treats the conditional masking policy as a normal
    [masking policy](../../user-guide/security-column-intro.md).

`CLUSTER BY ( expr [ , expr , ... ] )`
:   Specifies one or more columns or column expressions in the table as the clustering key. For more details, see
    [Clustering Keys & Clustered Tables](../../user-guide/tables-clustering-keys.md).

    Default: No value (no clustering key is defined for the table)

    > **Important:**
    >
    > Clustering keys are not intended or recommended for all tables; they typically benefit very large (i.e. multi-terabyte)
    > tables.
    >
    > Before you specify a clustering key for a table, you should understand micro-partitions. For more information, see [Understanding Snowflake Table Structures](../../user-guide/tables-micro-partitions.md).

`ENABLE_SCHEMA_EVOLUTION = { TRUE | FALSE }`
:   Enables or disables automatic changes to the table schema from data loaded into the table from source files, including:

    > * Added columns.
    >
    >   By default, schema evolution is limited to a maximum of 100 added columns per load operation. To request more than 100 added columns per load operation, contact [Snowflake Support](https://docs.snowflake.com/user-guide/contacting-support).
    > * The NOT NULL constraint can be dropped from any number of columns missing in new data files.

    Setting it to `TRUE` enables automatic table schema evolution. The default `FALSE` disables automatic table schema evolution.

    > **Note:**
    >
    > Loading data from files evolves the table columns when all of the following are true:
    >
    > * The [COPY INTO <table>](copy-into-table.md) statement includes the `MATCH_BY_COLUMN_NAME` option.
    > * The role used to load the data has the EVOLVE SCHEMA or OWNERSHIP privilege on the table.
    >
    > Additionally, for schema evolution with CSV, when used with `MATCH_BY_COLUMN_NAME` and `PARSE_HEADER`, `ERROR_ON_COLUMN_COUNT_MISMATCH` must be set to false.

`DATA_RETENTION_TIME_IN_DAYS = integer`
:   Specifies the retention period for the table so that Time Travel actions (SELECT, CLONE, UNDROP) can be performed on historical
    data in the table. For more details, see [Understanding & using Time Travel](../../user-guide/data-time-travel.md) and [Working with Temporary and Transient Tables](../../user-guide/tables-temp-transient.md).

    For a detailed description of this object-level parameter, as well as more information about object parameters, see
    [Parameters](../parameters.md).

    Values:

    > * Standard Edition: `0` or `1`
    > * Enterprise Edition:
    >
    >   + `0` to `90` for permanent tables
    >   + `0` or `1` for temporary and transient tables

    Default:

    > * Standard Edition: `1`
    > * Enterprise Edition (or higher): `1` (unless a different default value was specified at the schema, database, or account level)

    > **Note:**
    >
    > A value of `0` effectively disables Time Travel for the table.

`MAX_DATA_EXTENSION_TIME_IN_DAYS = integer`
:   Object parameter that specifies the maximum number of days for which Snowflake can extend the data retention period for the table to
    prevent streams on the table from becoming stale.

    For a detailed description of this parameter, see [MAX_DATA_EXTENSION_TIME_IN_DAYS](../parameters.md).

`CHANGE_TRACKING = { TRUE | FALSE }`
:   Specifies whether to enable change tracking on the table.

    * `TRUE` enables change tracking on the table. This setting adds a pair of hidden columns to the source table and begins
      storing change-tracking metadata in the columns. These columns consume a small amount of storage.

      The change-tracking metadata can be queried using the [CHANGES](../constructs/changes.md) clause for
      [SELECT](select.md) statements, or by creating and querying one or more streams on the table.
    * `FALSE` does not enable change tracking on the table.

    Default: FALSE

`DEFAULT_DDL_COLLATION = 'collation_specification'`
:   Specifies a default [collation specification](../collation.md) for the columns in the table, including columns
    added to the table in the future.

    For more details about the parameter, see [DEFAULT_DDL_COLLATION](../parameters.md).

`COPY GRANTS`
:   Specifies to retain the access privileges from the original table when a new table is created using any of the following
    CREATE TABLE variants:

    > * CREATE OR REPLACE TABLE
    > * CREATE TABLE … LIKE
    > * CREATE TABLE … CLONE

    The parameter copies all privileges, except OWNERSHIP, from the existing table to the new table. The new table does not
    inherit any future grants defined for the object type in the schema. By default, the role that executes the CREATE TABLE statement
    owns the new table.

    If the parameter is not included in the CREATE TABLE statement, then the new table does not inherit any explicit access
    privileges granted on the original table, but does inherit any future grants defined for the object type in the schema.

    Note:

    > * With [data sharing](../../guides-overview-sharing.md):
    >
    >   > + If the existing table was shared to another account, the replacement table is also shared.
    >   > + If the existing table was shared with your account as a data consumer, and access was further granted to other roles in
    >   >   the account (using `GRANT IMPORTED PRIVILEGES` on the parent database), access is also granted to the replacement
    >   >   table.
    > * The [SHOW GRANTS](show-grants.md) output for the replacement table lists the grantee for the copied privileges as the
    >   role that executed the CREATE TABLE statement, with the current timestamp when the statement was executed.
    > * The operation to copy grants occurs atomically in the CREATE TABLE command (i.e. within the same transaction).
    > * This parameter is not supported by the CREATE OR ALTER variant syntax.

`COPY TAGS`
:   [Preview Feature](../../release-notes/preview-features.md) — Open

    Available to all accounts.

    Retains [tags](../../user-guide/object-tagging/introduction.md) when executing a CREATE OR REPLACE statement. If the original table or its
    columns had a tag, the newly created table and its columns will still have the tag.

    For information about using the parameter, including its effect when altering columns in the CREATE OR REPLACE statement, see
    the usage notes for COPY TAGS.

`COMMENT = 'string_literal'`
:   Specifies a comment for the table.

    Default: No value

    (Note that comments can be specified at the column level, constraint level, or table level. The syntax for each is slightly different.)

`ROW ACCESS POLICY policy_name ON ( col_name [ , col_name ... ] )`
:   Specifies the [row access policy](../../user-guide/security-row-intro.md) to set on a table.

    This parameter is not supported by the CREATE OR ALTER variant syntax.

`AGGREGATION POLICY policy_name [ ENTITY KEY ( col_name [ , col_name ... ] ) ]`
:   Specifies an [aggregation policy](../../user-guide/aggregation-policies.md) to set on a table. You can apply one or more aggregation
    policies on a table.

    Use the optional ENTITY KEY parameter to define which columns uniquely identity an entity within the table. For more information, see
    [Implementing entity-level privacy with aggregation policies](../../user-guide/aggregation-policies-entity-privacy.md). You can specify one or more entity keys for an aggregation policy.

    This parameter is not supported by the CREATE OR ALTER variant syntax.

`JOIN POLICY policy_name [ ALLOWED JOIN KEYS ( col_name [ , ... ] ) ]`
:   Specifies the [join policy](../../user-guide/join-policies.md) to set on a table.

    Use the optional ALLOWED JOIN KEYS parameter to define which columns are allowed to be used as joining columns when
    this policy is in effect. For more information, see [Join policies](../../user-guide/join-policies.md).

    This parameter is not supported by the CREATE OR ALTER variant syntax.

`STORAGE LIFECYCLE POLICY policy_name ON ( col_name [ , col_name ... ] )`
:   Specifies a [storage lifecycle policy](../../user-guide/storage-management/storage-lifecycle-policies.md) to attach to the table.

    The columns specified in the ON clause must match the argument count and data types defined in the policy function signature.
    Snowflake uses these columns to evaluate the policy expression and determine which rows to archive or expire.

    > **Important:**
    >
    > If you attach an archival storage policy to a table, the table is permanently assigned to the specified archive tier for its lifetime. You can’t change the archive tier by applying a new policy. For example, you can’t specify a policy created with a COOL archive tier in ALTER TABLE…DROP STORAGE LIFECYCLE POLICY and then subsequently alter the table to add a policy created with a COLD archive tier. To alter the archive tier for a table, contact Snowflake Support to request deletion of the currently archived data. For additional considerations, see [Archival storage policies](../../user-guide/storage-management/storage-lifecycle-policies.md).

    For more information about creating and managing storage lifecycle policies, see
    [Create and manage storage lifecycle policies](../../user-guide/storage-management/storage-lifecycle-policies-create-manage.md).

    This parameter is not supported by the CREATE OR ALTER variant syntax.

`ROW_TIMESTAMP = { TRUE | FALSE }`
:   Specifies whether to enable row timestamps on the table. You must use a role with the OWNERSHIP privilege.

    For more information, see [Use row timestamps to measure latency in your pipelines](../../user-guide/data-engineering/row-timestamps.md).

`TAG ( tag_name = 'tag_value' [ , tag_name = 'tag_value' , ... ] )`
:   Specifies the [tag](../../user-guide/object-tagging/introduction.md) name and the tag string value.

    The tag value is always a string, and the maximum number of characters for the tag value is 256.

    For information about specifying tags in a statement, see [Tag quotas](../../user-guide/object-tagging/introduction.md).

    This parameter is not supported by the CREATE OR ALTER variant syntax.

`WITH CONTACT ( purpose = contact [ , purpose = contact ...] )`
:   Associate the new object with one or more [contacts](../../user-guide/contacts-using.md).

    Specify the WITH CONTACT clause after all other clauses except the AS clause (if that clause is supported by this command).

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| CREATE TABLE | Schema | Note that creating a temporary table does not require the CREATE TABLE privilege. |
| SELECT | Table, external table, view | Required on queried tables and/or views only when cloning a table or executing CTAS statements. |
| APPLY | Masking policy, row access policy, tag, storage lifecycle policy | Required only when applying a masking policy, row access policy, object tags, storage lifecycle policy, or any combination of these [governance](../../guides-overview-govern.md) features when creating tables. |
| USAGE (external stage) or READ (internal stage) | Stage | Required to derive table column definitions from staged files using CREATE TABLE … USING TEMPLATE statements. |
| OWNERSHIP | Table | *A role must be granted or inherit the OWNERSHIP privilege on the object to create a temporary object that has the same name as the object   that already exists in the schema.* Required to execute a CREATE OR ALTER TABLE statement for an *existing* table.   OWNERSHIP is a special privilege on an object that is automatically granted to the role that created the object, but can also be transferred using the [GRANT OWNERSHIP](grant-ownership.md) command to a different role by the owning role (or any role with the MANAGE GRANTS privilege).  Note that in a [managed access schema](../../user-guide/security-access-control-configure.md), only the schema owner (i.e. the role with the OWNERSHIP privilege on the schema) or a role with the MANAGE GRANTS privilege can grant or revoke privileges on objects in the schema, including future grants. |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* A schema cannot contain tables and/or views with the same name. When creating a table:

  > * If a view with the same name already exists in the schema, an error is returned and the table is not created.
  > * If a table with the same name already exists in the schema, an error is returned and the table is not created, unless the
  >   optional `OR REPLACE` keyword is included in the command.
  >
  >   > **Important:**
  >   >
  >   > Using `OR REPLACE` is the equivalent of using [DROP TABLE](drop-table.md) on the existing table and then creating a new table
  >   > with the same name; however, the dropped table is not permanently removed from the system. Instead, it is retained in
  >   > Time Travel. This is important to note because dropped tables in Time Travel can be recovered, but they also contribute to data
  >   > storage for your account. For more information, see [Storage costs for Time Travel and Fail-safe](../../user-guide/data-cdp-storage-costs.md).
  >   >
  >   > CREATE OR REPLACE *<object>* statements are atomic. That is, when an object is replaced, the old object is deleted and the new object is created in a single transaction.
  >   >
  >   > This means that any queries concurrent with the CREATE OR REPLACE TABLE operation use either the old or new table version.
  >   >
  >   > Recreating or swapping a table drops its change data. Any stream on the table becomes [stale](../../user-guide/streams-intro.md). In
  >   > addition, any stream on a view that has this table as an underlying table, becomes stale. A stale stream is unreadable.
* The `OR REPLACE` and `IF NOT EXISTS` clauses are mutually exclusive. They can’t both be used in the same statement.
* Similar to [reserved keywords](../reserved-keywords.md), ANSI-reserved function names
  ([CURRENT_DATE](../functions/current_date.md), [CURRENT_TIMESTAMP](../functions/current_timestamp.md), etc.) cannot be used as column
  names.
* CREATE OR ALTER TABLE:

  For more information, see CREATE OR ALTER TABLE usage notes.
* CREATE TABLE … CLONE:

  If the source table has clustering keys, then the new table has clustering keys. By default, Automatic Clustering is suspended
  for the new table – even if Automatic Clustering was not suspended for the source table.

* CREATE TABLE … FROM ARCHIVE OF:

  * Using this command requires the OWNERSHIP privilege on the source table.
  * Specifying column definitions, policies, tags, or other constraints isn’t supported. Snowflake automatically retrieves
    the table schema, policies, tags, and constraints from the source table.
  * The WHERE clause is required. Reading archived data is expensive, and should be performed infrequently.
    Filtering results using the WHERE clause helps you minimize costs by ensuring that Snowflake reads only the data that you
    require from archival storage.
  * To estimate the number of files that Snowflake will retrieve from archive storage, run the [EXPLAIN](explain.md) command before
    this operation. The output includes a `createTableFromArchiveData` operation and displays `ARCHIVE OF <table>` in
    the `objects` column for the TableScan operation. For more information, see [Estimate retrieval costs with EXPLAIN](../../user-guide/storage-management/storage-lifecycle-policies-retrieving-archived-data.md).
  * To see a history of data retrieval from archive storage, use the [ARCHIVE_STORAGE_DATA_RETRIEVAL_USAGE_HISTORY view](../account-usage/archive_storage_data_retrieval_usage_history.md).
  * To retrieve data from the COLD tier of archive storage, Snowflake must first restore the files from external cloud storage. This process
    can take up to 48 hours.

    To support this process, set the following parameters appropriately:

    * [STATEMENT_TIMEOUT_IN_SECONDS](../parameters.md) must be at least 48 hours.
    * [ABORT_DETACHED_QUERY](../parameters.md) must be FALSE.

    COLD storage tier restore operations support a maximum of 1 million files per restore operation.
  * If you cancel a CREATE TABLE operation that retrieves data from archive storage, you might still incur retrieval costs.
* CREATE TABLE … CHANGE_TRACKING = TRUE:

  When change tracking is enabled, the table is locked for the duration of the operation.
  Locks can cause latency with some associated DDL/DML operations.
  For more information, refer to [Resource locking](../transactions.md).
* CREATE TABLE … LIKE:

  If the source table has clustering keys, then the new table has clustering keys. By default, Automatic Clustering is not
  suspended for the new table – even if Automatic Clustering was suspended for the source table.
* CREATE TABLE … AS SELECT (CTAS):

  * If the aliases for the column names in the [SELECT](select.md) list are valid columns, then the column definitions
    are not required in the CTAS statement; if omitted, the column names and types are inferred from the underlying query:

    > ```sqlsyntax
    > CREATE TABLE <table_name> AS SELECT ...
    > ```

    Alternatively, the names can be explicitly specified using the following syntax:

    > ```sqlsyntax
    > CREATE TABLE <table_name> ( <col1_name> , <col2_name> , ... ) AS SELECT ...
    > ```

    The number of column names specified must match the number of [SELECT](select.md) list items in the query; the
    types of the columns are inferred from the types produced by the query.
  * When clustering keys are specified in a CTAS statement:

    * Column definitions are required and must be explicitly specified in the statement.
    * By default, [Automatic Clustering](../../user-guide/tables-auto-reclustering.md) is enabled for the new table even if Automatic Clustering is
      suspended for the source table.
    * The data is clustered when the new table is created. A clustered table generates a query plan
      that includes a sort operation and takes longer to create than an equivalent table that is not clustered. For example, the
      second of these commands is likely to take longer than the first:

      ```sqlexample
      CREATE TABLE ctas_large_table
        AS SELECT * FROM large_table;

      CREATE TABLE ctas_clustered_large_table CLUSTER BY (timestamp)
        AS SELECT * FROM large_table;
      ```

      Alternatively, you can create a table with rows in sorted order by using an ORDER BY clause in the CTAS query.

* CREATE OR REPLACE … COPY TAGS

  * You can’t use COPY TAGS with a CREATE TABLE … LIKE or CREATE TABLE … CLONE statement.
  * You can’t use COPY TAGS with a WITH TAG clause.
  * You don’t need privileges on the tags to use COPY TAGS.
  * If you rename a tagged column in the statement, the column in the new table doesn’t have the tag.
  * If you change the data type of a tagged column — for example, changing `NUMBER(8)` to `NUMBER(16)` — the column in the new table
    doesn’t have the tag.
  * If you swap column names in the statement, the tag stays with the column based on its name. For example, suppose only column `a` has a
    tag and you run the following command to swap the names of columns `a` and `b`:

    ```sqlexample
    CREATE OR REPLACE TABLE dst1 COPY TAGS AS SELECT b AS a, a AS b FROM src1
    ```

    Only column `a` is still tagged in the new table, although it contains the data from column `b` in the source table.
* Inside a transaction, any DDL statement (including CREATE TEMPORARY/TRANSIENT TABLE) commits
  the transaction before executing the DDL statement itself. The DDL statement then runs in its own transaction. The
  next statement after the DDL statement starts a new transaction. Therefore, you can’t create, use, and drop a
  temporary or transient table within a single transaction. If you want to use a temporary or transient table inside a
  transaction, then create the table before the transaction, and drop the table after the transaction.
* Recreating a table (using the optional `OR REPLACE` keyword) drops its history, which makes any stream on the table stale.
  A stale stream is unreadable.
* A single masking policy that uses conditional columns can be applied to multiple tables provided that the column structure of the table
  matches the columns specified in the policy.
* When creating a table with a masking policy on one or more table columns, or a row access policy added to the table, use the
  [POLICY_CONTEXT](../functions/policy_context.md) function to simulate a query on the column(s) protected by a masking policy and the table
  protected by a row access policy.

* For creating a table with the WITH STORAGE LIFECYCLE POLICY clause:

  * You must have the necessary privileges to apply the policy. For information about required privileges, see
    [Storage lifecycle policy privileges](../../user-guide/security-access-control-privileges.md).
  * A table can have only one attached storage lifecycle policy.
  * The number of columns must match the argument count in the policy function signature, and the column data must be compatible with the argument types.
  * Associated policies aren’t affected if you rename table columns. Snowflake associates policies to tables by using the column IDs.
  * In order to evaluate and apply storage lifecycle policy expressions, Snowflake internally and temporarily bypasses any governance policies on a table.
* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).

## CREATE OR ALTER TABLE usage notes

* **Limitations**

  * Currently only supports permanent, temporary, and transient tables. Read-only, external, dynamic, Apache Iceberg™, and hybrid tables
    are *not* supported.
  * All limitations of the [ALTER TABLE](alter-table.md) command apply.
  * Currently does *not* support the following:

    * CREATE TABLE … AS SELECT (CTAS) variant syntax.
    * CREATE TABLE … USING TEMPLATE variant syntax.
    * CREATE TABLE … LIKE variant syntax.
    * CREATE TABLE … CLONE variant syntax.
* **Table parameters and properties**

  * The absence of a property or parameter that was previously set in the modified table definition results in unsetting it.
  * Unsetting an explicit [parameter](../parameters.md) value results in setting it to the default parameter value.
    If the parameter is set on the schema or database that contain the table, the table inherits the parameter value set on
    the schema or database.
* **Data governance**

  * Setting or unsetting a tag or policy on a table or column using a CREATE OR ALTER TABLE statement is not supported.

    Existing policies or tags are *not* altered by a CREATE OR ALTER statement and remain unchanged.
* **Constraints**

  > Setting or unsetting an inline primary key changes the nullability of the column accordingly. This aligns with the behavior of
  > the CREATE TABLE command, but is different from the behavior of the ALTER TABLE command.
* **Columns**

  * New columns can only be added to the end of the column list.
  * Columns cannot be renamed. If you attempt to rename a column, the column is dropped and a new column is added.
  * The default value for a column can only be modified to use a sequence.
  * The default sequence for a column (for example, `SET DEFAULT seq_name.NEXTVAL`) can only be changed if the column
    already has a sequence.
  * For more information about modifying columns, see [ALTER TABLE … ALTER COLUMN](alter-table-column.md).
* **Collation**

  * Collation specifications cannot be altered.
  * Setting the [DEFAULT_DDL_COLLATION](../parameters.md) parameter in the CREATE OR ALTER TABLE command
    sets the default collation specification for existing columns, which ensures the CREATE OR ALTER TABLE command
    yields the same results as the CREATE TABLE command. Therefore, you can’t use the CREATE OR ALTER TABLE command to set the
    DEFAULT_DDL_COLLATION parameter on a table that has existing text columns. You can, however, make collations explicit
    for existing columns when changing the DEFAULT_DDL_COLLATION parameter for a table.

    For example, create a new table `my_table` and set the default collation specification for the table to ‘fr’:

    ```sqlexample
    CREATE OR ALTER TABLE my_table (
      a INT PRIMARY KEY,
      b VARCHAR(20)
    )
    DEFAULT_DDL_COLLATION = 'fr';
    ```

    The collation specification for column `b` is ‘fr’ and cannot be changed. To change the default collation specification for
    table `my_table`, you must explicitly set the collation for text column `b` in the CREATE OR ALTER statement:

    ```sqlexample
    CREATE OR ALTER TABLE my_table (
      a INT PRIMARY KEY,
      b VARCHAR(200) COLLATE 'fr'
    )
    DEFAULT_DDL_COLLATION = 'de';
    ```

* **Atomicity**

  The CREATE OR ALTER TABLE command currently does not guarantee atomicity. This means that if a CREATE OR ALTER TABLE statement
  fails during execution, it is possible that a subset of changes might have been applied to the table. If there is a possibility
  of partial changes, the error message, in most cases, includes the following text:

  ```output
  CREATE OR ALTER execution failed. Partial updates may have been applied.
  ```

  For example, if the statement is attempting to drop column `A` and add a new column `B` to a table, and the
  statement is aborted, it is possible that column `A` was dropped but column `B` was not added.

  > **Note:**
  >
  > If changes are partially applied, the resulting table is still in a valid state, and you can use additional ALTER TABLE
  > statements to complete the original set of changes.

  To recover from partial updates, Snowflake recommends the following recovery mechanisms:

  * Fix forward

    * Re-execute the CREATE OR ALTER TABLE statement. If the statements succeeds on the second attempt, the target
      state is achieved.
    * Investigate the error message. If possible, fix the error and re-execute the CREATE OR ALTER TABLE statement.
  * Roll back

    If it is not possible to fix forward, Snowflake recommends manually rolling back partial changes:

    * Investigate the state of the table using the [DESCRIBE TABLE](desc-table.md) and [SHOW TABLES](show-tables.md) commands. Determine which partial
      changes were applied, if any.
    * If any partial changes were applied, execute the appropriate ALTER TABLE statements to transform the table back to its
      original state.

      > **Note:**
      >
      > In some cases, you might not be able to undo partial changes. For more information, see the supported and unsupported
      > actions for modifying column properties in the [ALTER TABLE … ALTER COLUMN](alter-table-column.md) topic.
  * If you need help recovering from a partial update, contact [Snowflake Support](https://docs.snowflake.com/user-guide/contacting-support).

## Examples

### Basic examples

Create a simple table in the current database and insert a row in the table:

> ```sqlexample
> CREATE TABLE mytable (amount NUMBER);
>
> +-------------------------------------+
> | status                              |
> |-------------------------------------|
> | Table MYTABLE successfully created. |
> +-------------------------------------+
>
> INSERT INTO mytable VALUES(1);
>
> SHOW TABLES like 'mytable';
>
> +---------------------------------+---------+---------------+-------------+-------+---------+------------+------+-------+--------------+----------------+
> | created_on                      | name    | database_name | schema_name | kind  | comment | cluster_by | rows | bytes | owner        | retention_time |
> |---------------------------------+---------+---------------+-------------+-------+---------+------------+------+-------+--------------+----------------|
> | Mon, 11 Sep 2017 16:32:28 -0700 | MYTABLE | TESTDB        | PUBLIC      | TABLE |         |            |    1 |  1024 | ACCOUNTADMIN | 1              |
> +---------------------------------+---------+---------------+-------------+-------+---------+------------+------+-------+--------------+----------------+
>
> DESC TABLE mytable;
>
> +--------+--------------+--------+-------+---------+-------------+------------+-------+------------+---------+
> | name   | type         | kind   | null? | default | primary key | unique key | check | expression | comment |
> |--------+--------------+--------+-------+---------+-------------+------------+-------+------------+---------|
> | AMOUNT | NUMBER(38,0) | COLUMN | Y     | NULL    | N           | N          | NULL  | NULL       | NULL    |
> +--------+--------------+--------+-------+---------+-------------+------------+-------+------------+---------+
> ```

Create a simple table and specify comments for both the table and the column in the table:

> ```sqlexample
> CREATE TABLE example (col1 NUMBER COMMENT 'a column comment') COMMENT='a table comment';
>
> +-------------------------------------+
> | status                              |
> |-------------------------------------|
> | Table EXAMPLE successfully created. |
> +-------------------------------------+
>
> SHOW TABLES LIKE 'example';
>
> +---------------------------------+---------+---------------+-------------+-------+-----------------+------------+------+-------+--------------+----------------+
> | created_on                      | name    | database_name | schema_name | kind  | comment         | cluster_by | rows | bytes | owner        | retention_time |
> |---------------------------------+---------+---------------+-------------+-------+-----------------+------------+------+-------+--------------+----------------|
> | Mon, 11 Sep 2017 16:35:59 -0700 | EXAMPLE | TESTDB        | PUBLIC      | TABLE | a table comment |            |    0 |     0 | ACCOUNTADMIN | 1              |
> +---------------------------------+---------+---------------+-------------+-------+-----------------+------------+------+-------+--------------+----------------+
>
> DESC TABLE example;
>
> +------+--------------+--------+-------+---------+-------------+------------+-------+------------+------------------+
> | name | type         | kind   | null? | default | primary key | unique key | check | expression | comment          |
> |------+--------------+--------+-------+---------+-------------+------------+-------+------------+------------------|
> | COL1 | NUMBER(38,0) | COLUMN | Y     | NULL    | N           | N          | NULL  | NULL       | a column comment |
> +------+--------------+--------+-------+---------+-------------+------------+-------+------------+------------------+
> ```

### CTAS examples

Create a table by selecting from an existing table:

> ```sqlexample
> CREATE TABLE mytable_copy (b) AS SELECT * FROM mytable;
>
> DESC TABLE mytable_copy;
>
> +------+--------------+--------+-------+---------+-------------+------------+-------+------------+---------+
> | name | type         | kind   | null? | default | primary key | unique key | check | expression | comment |
> |------+--------------+--------+-------+---------+-------------+------------+-------+------------+---------|
> | B    | NUMBER(38,0) | COLUMN | Y     | NULL    | N           | N          | NULL  | NULL       | NULL    |
> +------+--------------+--------+-------+---------+-------------+------------+-------+------------+---------+
>
> CREATE TABLE mytable_copy2 AS SELECT b+1 AS c FROM mytable_copy;
>
> DESC TABLE mytable_copy2;
>
> +------+--------------+--------+-------+---------+-------------+------------+-------+------------+---------+
> | name | type         | kind   | null? | default | primary key | unique key | check | expression | comment |
> |------+--------------+--------+-------+---------+-------------+------------+-------+------------+---------|
> | C    | NUMBER(39,0) | COLUMN | Y     | NULL    | N           | N          | NULL  | NULL       | NULL    |
> +------+--------------+--------+-------+---------+-------------+------------+-------+------------+---------+
>
> SELECT * FROM mytable_copy2;
>
> +---+
> | C |
> |---|
> | 2 |
> +---+
> ```

More advanced example of creating a table by selecting from an existing table; in this example, the values in the `summary_amount`
column in the new table are derived from two columns in the source table:

> ```sqlexample
> CREATE TABLE testtable_summary (name, summary_amount) AS SELECT name, amount1 + amount2 FROM testtable;
> ```

Create a table by selecting columns from a staged Parquet data file:

> ```sqlexample
> CREATE OR REPLACE TABLE parquet_col (
>   custKey NUMBER DEFAULT NULL,
>   orderDate DATE DEFAULT NULL,
>   orderStatus VARCHAR(100) DEFAULT NULL,
>   price VARCHAR(255)
> )
> AS SELECT
>   $1:o_custkey::number,
>   $1:o_orderdate::date,
>   $1:o_orderstatus::text,
>   $1:o_totalprice::text
> FROM @my_stage;
>
> +-----------------------------------------+
> | status                                  |
> |-----------------------------------------|
> | Table PARQUET_COL successfully created. |
> +-----------------------------------------+
>
> DESC TABLE parquet_col;
>
> +-------------+--------------+--------+-------+---------+-------------+------------+-------+------------+---------+
> | name        | type         | kind   | null? | default | primary key | unique key | check | expression | comment |
> |-------------+--------------+--------+-------+---------+-------------+------------+-------+------------+---------|
> | CUSTKEY     | NUMBER(38,0) | COLUMN | Y     | NULL    | N           | N          | NULL  | NULL       | NULL    |
> | ORDERDATE   | DATE         | COLUMN | Y     | NULL    | N           | N          | NULL  | NULL       | NULL    |
> | ORDERSTATUS | VARCHAR(100) | COLUMN | Y     | NULL    | N           | N          | NULL  | NULL       | NULL    |
> | PRICE       | VARCHAR(255) | COLUMN | Y     | NULL    | N           | N          | NULL  | NULL       | NULL    |
> +-------------+--------------+--------+-------+---------+-------------+------------+-------+------------+---------+
> ```

### CREATE TABLE … LIKE examples

Create a table with the same column definitions as another table, but with no rows:

> ```sqlexample
> CREATE TABLE mytable (amount NUMBER);
>
> INSERT INTO mytable VALUES(1);
>
> SELECT * FROM mytable;
>
> +--------+
> | AMOUNT |
> |--------|
> |      1 |
> +--------+
>
> CREATE TABLE mytable_2 LIKE mytable;
>
> DESC TABLE mytable_2;
>
> +--------+--------------+--------+-------+---------+-------------+------------+-------+------------+---------+
> | name   | type         | kind   | null? | default | primary key | unique key | check | expression | comment |
> |--------+--------------+--------+-------+---------+-------------+------------+-------+------------+---------|
> | AMOUNT | NUMBER(38,0) | COLUMN | Y     | NULL    | N           | N          | NULL  | NULL       | NULL    |
> +--------+--------------+--------+-------+---------+-------------+------------+-------+------------+---------+
>
> SELECT * FROM mytable_2;
>
> +--------+
> | AMOUNT |
> |--------|
> +--------+
> ```

### CREATE TABLE examples that set parameters and properties

Create a table with a multi-column clustering key:

> ```sqlexample
> CREATE TABLE mytable (date TIMESTAMP_NTZ, id NUMBER, content VARIANT) CLUSTER BY (date, id);
>
> SHOW TABLES LIKE 'mytable';
>
> +---------------------------------+---------+---------------+-------------+-------+---------+------------------+------+-------+--------------+----------------+
> | created_on                      | name    | database_name | schema_name | kind  | comment | cluster_by       | rows | bytes | owner        | retention_time |
> |---------------------------------+---------+---------------+-------------+-------+---------+------------------+------+-------+--------------+----------------|
> | Mon, 11 Sep 2017 16:20:41 -0700 | MYTABLE | TESTDB        | PUBLIC      | TABLE |         | LINEAR(DATE, ID) |    0 |     0 | ACCOUNTADMIN | 1              |
> +---------------------------------+---------+---------------+-------------+-------+---------+------------------+------+-------+--------------+----------------+
> ```

Specify collation for columns in a table:

> ```sqlexample
> CREATE OR REPLACE TABLE collation_demo (
>   uncollated_phrase VARCHAR,
>   utf8_phrase VARCHAR COLLATE 'utf8',
>   english_phrase VARCHAR COLLATE 'en',
>   spanish_phrase VARCHAR COLLATE 'es');
>
> INSERT INTO collation_demo (
>       uncollated_phrase,
>       utf8_phrase,
>       english_phrase,
>       spanish_phrase)
>    VALUES (
>      'pinata',
>      'pinata',
>      'pinata',
>      'piñata');
> ```

### CREATE TABLE … USING TEMPLATE examples

Create a table where the column definitions are derived from a set of staged files that contain Avro, Parquet, or ORC data.

Note that the `mystage` stage and `my_parquet_format` file format referenced in the statement must already exist. A set of files
must already be staged in the cloud storage location referenced in the stage definition.

The following example creates a table using the detected schema from staged files and sorts the columns by `order_id`.
It builds on an example in the [INFER_SCHEMA](../functions/infer_schema.md) topic.

> ```sqlexample
> CREATE TABLE mytable
>   USING TEMPLATE (
>     SELECT ARRAY_AGG(OBJECT_CONSTRUCT(*))
>     WITHIN GROUP (ORDER BY order_id)
>       FROM TABLE(
>         INFER_SCHEMA(
>           LOCATION=>'@mystage',
>           FILE_FORMAT=>'my_parquet_format'
>         )
>       ));
> ```

Note that sorting the columns by `order_id` only applies if all staged files share a single schema. If the set of staged data
files includes multiple schemas with shared column names, the order represented in the `order_id` column might not match any
single file.

> **Note:**
>
> Using `*` for `ARRAY_AGG(OBJECT_CONSTRUCT())` might result in an error if the returned result is larger than 128 MB.
> We recommend that you avoid using `*` for larger result sets, and only use the required columns, `COLUMN NAME`,
> `TYPE`, and `NULLABLE`, for the query. Optional column `ORDER_ID` can be included when using
> `WITHIN GROUP (ORDER BY order_id)`.

### Temporary table examples

Create a temporary table that is dropped automatically at the end of the session:

> ```sqlexample
> CREATE TEMPORARY TABLE demo_temporary (i INTEGER);
> CREATE TEMP TABLE demo_temp (i INTEGER);
> ```

For compatibility with other vendors, Snowflake also supports using the keywords below as synonyms for TEMPORARY:

> ```sqlexample
> CREATE LOCAL TEMPORARY TABLE demo_local_temporary (i INTEGER);
> CREATE LOCAL TEMP TABLE demo_local_temp (i INTEGER);
>
> CREATE GLOBAL TEMPORARY TABLE demo_global_temporary (i INTEGER);
> CREATE GLOBAL TEMP TABLE demo_global_temp (i INTEGER);
>
> CREATE VOLATILE TABLE demo_volatile (i INTEGER);
> ```

### CREATE OR ALTER TABLE examples

Create a table `my_table` using the CREATE OR ALTER TABLE command:

```sqlexample
CREATE OR ALTER TABLE my_table(a INT);
```

> **Note:**
>
> CREATE OR ALTER TABLE statements for existing tables can only be executed by a role
> with the OWNERSHIP privilege on table `my_table`.

Alter table `my_table` to add and modify columns and set the DATA_RETENTION_TIME_IN_DAYS and
DEFAULT_DDL_COLLATION parameters:

```sqlexample
CREATE OR ALTER TABLE my_table(
    a INT PRIMARY KEY,
    b VARCHAR(200)
  )
  DATA_RETENTION_TIME_IN_DAYS = 5
  DEFAULT_DDL_COLLATION = 'de';
```

Unset the DATA_RETENTION_TIME_IN_DAYS parameter. The absence of a parameter in the modified table definition results in unsetting it.
In this case, unsetting the DATA_RETENTION_TIME_IN_DAYS parameter for the table resets it to the default value of `1`:

```sqlexample
CREATE OR ALTER TABLE my_table(
    a INT PRIMARY KEY,
    c VARCHAR(200)
  )
  DEFAULT_DDL_COLLATION = 'de';
```

The CREATE OR ALTER TABLE command supports adding columns at the end of the column list. If you attempt to rename an existing column, the existing
column is dropped, and a new column with the new column name is added. This might result in data loss if data exists in the original column.

The following example illustrates this behavior.

1. Create a table:

   ```sqlexample
   CREATE OR ALTER TABLE my_table(
       a INT PRIMARY KEY,
       b INT
     );
   ```

2. Insert data into table `my_table`:

   ```sqlexample
   INSERT INTO my_table VALUES (1, 2), (2, 3);

   SELECT * FROM my_table;
   ```

   Returns:

   ```output
   +---+---+
   | A | B |
   |---+---|
   | 1 | 2 |
   | 2 | 3 |
   +---+---+
   ```

3. Attempt to rename column `b`:

   ```sqlexample
   CREATE OR ALTER TABLE my_table(
       a INT PRIMARY KEY,
       c INT
     );
   ```

   Column `b` is dropped and column `c` is added:

   ```sqlexample
   SELECT * FROM my_table;
   ```

   Returns:

   ```output
   +---+------+
   | A | C    |
   |---+------|
   | 1 | NULL |
   | 2 | NULL |
   +---+------+
   ```

   > **Note:**
   >
   > You can recover dropped columns using [Time Travel](../../user-guide/data-time-travel.md).

Setting or unsetting an inline primary key changes the nullability of the column in a way that aligns with the behavior of the
CREATE TABLE command, but is different from the behavior of the ALTER TABLE command. For example, adding a primary key constraint
on a column using an ALTER TABLE statement does not change column nullability.

The following example illustrates this behavior.

1. Create a table:

   ```sqlexample
   CREATE TABLE t(a INT);
   ```

2. Alter the table to add a PRIMARY KEY constraint:

   ```sqlexample
   CREATE OR ALTER TABLE t(a INT PRIMARY KEY);
   ```

   Column `a` is now the primary key and is set to NOT NULL:

   ```sqlexample
   DESC TABLE t;
   ```

   Returns:

   ```output
   +------+--------------+--------+-------+---------+-------------+------------+-------+------------+---------+-------------+----------------+
   | name | type         | kind   | null? | default | primary key | unique key | check | expression | comment | policy name | privacy domain |
   |------+--------------+--------+-------+---------+-------------+------------+-------+------------+---------+-------------+----------------|
   | A    | NUMBER(38,0) | COLUMN | N     | NULL    | Y           | N          | NULL  | NULL       | NULL    | NULL        | NULL           |
   +------+--------------+--------+-------+---------+-------------+------------+-------+------------+---------+-------------+----------------+
   ```

3. Replace table `t`:

   ```sqlexample
   CREATE OR REPLACE TABLE t(a INT);
   ```

4. Insert a NULL value:

   ```sqlexample
   INSERT INTO t VALUES (null);
   ```

5. Add primary key constraint to column `a`.

   The NULL value in column `a` causes the following statement to fail:

   ```sqlexample
   CREATE OR ALTER TABLE t(a INT PRIMARY KEY);
   ```

   Returns:

   ```output
   001471 (42601): SQL compilation error:
   Column 'A' contains null values. Not null constraint cannot be added.
   ```
