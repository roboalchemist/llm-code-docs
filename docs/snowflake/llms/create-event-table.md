# Source: https://docs.snowflake.com/en/sql-reference/sql/create-event-table.md

# CREATE EVENT TABLE

Creates an [event table](../../developer-guide/logging-tracing/event-table-setting-up.md) that captures events, including logged messages
from functions and procedures.

See also:
:   [ALTER TABLE (event tables)](alter-table-event-table.md) , [DESCRIBE EVENT TABLE](desc-event-table.md), [DROP TABLE](drop-table.md),
    [SHOW EVENT TABLES](show-event-tables.md)

## Syntax

```sqlsyntax
CREATE [ OR REPLACE ] EVENT TABLE [ IF NOT EXISTS ] <name>
  [ CLUSTER BY ( <expr> [ , <expr> , ... ] ) ]
  [ DATA_RETENTION_TIME_IN_DAYS = <integer> ]
  [ MAX_DATA_EXTENSION_TIME_IN_DAYS = <integer> ]
  [ CHANGE_TRACKING = { TRUE | FALSE } ]
  [ DEFAULT_DDL_COLLATION = '<collation_specification>' ]
  [ COPY GRANTS ]
  [ [ WITH ] COMMENT = '<string_literal>' ]
  [ [ WITH ] ROW ACCESS POLICY <policy_name> ON ( <col_name> [ , <col_name> ... ] ) ]
  [ [ WITH ] TAG ( <tag_name> = '<tag_value>' [ , <tag_name> = '<tag_value>' , ... ] ) ]
  [ WITH CONTACT ( <purpose> = <contact_name> [ , <purpose> = <contact_name> ... ] ) ]
```

## Variant syntax

### CREATE EVENT TABLE … CLONE

Creates a new event table with the same [predefined column definitions](../../developer-guide/logging-tracing/event-table-columns.md) and
containing all the existing data from the source table without actually copying the data. You can also use this variant to clone an
event table at a specific time/point in the past (using [Time Travel](../../user-guide/data-time-travel.md)):

```sqlsyntax
CREATE [ OR REPLACE ] EVENT TABLE [ IF NOT EXISTS ] <name>
  CLONE <source_table>
    [ { AT | BEFORE } ( { TIMESTAMP => <timestamp> | OFFSET => <time_difference> | STATEMENT => <id> } ) ]
    [ COPY GRANTS ]
    [ ... ]
```

> **Note:**
>
> If the statement replaces an event table of the same name, the grants are copied from the event table
> being replaced. Otherwise, the grants are copied from the source event table being cloned.

For more details about COPY GRANTS, see COPY GRANTS in this document.

For more details about cloning, see [CREATE <object> … CLONE](create-clone.md).

## Required parameters

`name`
:   Specifies the identifier (the name) for the event table; must be unique for the schema in which the event table is created.

    In addition, the identifier must start with an alphabetic character and cannot contain spaces or special characters unless the
    entire identifier string is enclosed in double quotes (e.g. `"My object"`). Identifiers enclosed in double quotes are also
    case-sensitive.

    For more details, see [Identifier requirements](../identifiers-syntax.md).

`source_table`
:   Required for CLONE.

    Specifies the event table to use as the source for the clone.

## Optional parameters

`CLUSTER BY ( expr [ , expr , ... ] )`
:   Specifies one or more columns or column expressions in the table as the clustering key. For more details, see
    [Clustering Keys & Clustered Tables](../../user-guide/tables-clustering-keys.md).

    Default: No value (no clustering key is defined for the table)

    > **Important:**
    >
    > Clustering keys are not intended or recommended for all tables; they typically benefit very large (i.e. multi-terabyte)
    > tables.
    >
    > Before you specify a clustering key for a table, please read [Understanding Snowflake Table Structures](../../user-guide/tables-micro-partitions.md).

`DATA_RETENTION_TIME_IN_DAYS = integer`
:   Specifies the retention period for the table so that Time Travel actions (SELECT, CLONE, UNDROP) can be performed on historical
    data in the table. For more details, see [Understanding & using Time Travel](../../user-guide/data-time-travel.md).

    For a detailed description of this object-level parameter, as well as more information about object parameters, see
    [Parameters](../parameters.md).

    Values:

    > * Standard Edition: `0` or `1`
    > * Enterprise Edition:
    >
    >   + `0` to `90` for permanent tables

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

`CHANGE_TRACKING = TRUE | FALSE`
:   Specifies whether to enable change tracking on the table.

    * `TRUE` enables change tracking on the table. This setting adds a pair of hidden columns to the source table and begins
      storing change tracking metadata in the columns. These columns consume a small amount of storage.

      The change tracking metadata can be queried using the [CHANGES](../constructs/changes.md) clause for
      [SELECT](select.md) statements, or by creating and querying one or more streams on the table.
    * `FALSE` does not enable change tracking on the table.

    Default: FALSE

`DEFAULT_DDL_COLLATION = 'collation_specification'`
:   Specifies a default [collation specification](../collation.md) for the columns in the table.

    For more details about the parameter, see [DEFAULT_DDL_COLLATION](../parameters.md).

`COPY GRANTS`
:   Specifies to retain the access privileges from the original table when a new table is created using any of the following
    CREATE TABLE variants:

    * CREATE OR REPLACE EVENT TABLE
    * CREATE EVENT TABLE … CLONE

    The parameter copies all privileges, except OWNERSHIP, from the existing table to the new table. The new table does not
    inherit any future grants defined for the object type in the schema. By default, the role that executes the CREATE EVENT TABLE statement
    owns the new table.

    If the parameter is not included in the CREATE EVENT TABLE statement, then the new table does not inherit any explicit access
    privileges granted on the original table, but does inherit any future grants defined for the object type in the schema.

    Note:

    > * The [SHOW GRANTS](show-grants.md) output for the replacement table lists the grantee for the copied privileges as the
    >   role that executed the CREATE EVENT TABLE statement, with the current timestamp when the statement was executed.
    > * The operation to copy grants occurs atomically in the CREATE EVENT TABLE command (in other words, within the same transaction).

`ROW ACCESS POLICY policy_name ON ( col_name [ , col_name ... ] )`
:   Specifies the [row access policy](../../user-guide/security-row-intro.md) to set on a table.

`COMMENT = 'string_literal'`
:   Specifies a comment for the table.

    Default: No value

`TAG ( tag_name = 'tag_value' [ , tag_name = 'tag_value' , ... ] )`
:   Specifies the [tag](../../user-guide/object-tagging/introduction.md) name and the tag string value.

    The tag value is always a string, and the maximum number of characters for the tag value is 256.

    For information about specifying tags in a statement, see [Tag quotas](../../user-guide/object-tagging/introduction.md).

`WITH CONTACT ( purpose = contact [ , purpose = contact ...] )`
:   Associate the new object with one or more [contacts](../../user-guide/contacts-using.md).

    Specify the WITH CONTACT clause after all other clauses except the AS clause (if that clause is supported by this command).

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| CREATE EVENT TABLE | Schema in which you plan to create the event table. |  |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* A schema cannot contain event tables, tables, and/or views with the same name. When creating an event table:

  * If a table or view with the same name already exists in the schema, an error is returned and the event table is not created.
  * If an event table with the same name already exists in the schema, an error is returned and the event table is not created,
    unless the optional `OR REPLACE` keyword is included in the command.
  > **Important:**
  >
  > Using `OR REPLACE` is the equivalent of using [DROP TABLE](drop-table.md) on the existing event table and then
  > creating a new event table with the same name; however, the dropped table is not permanently removed from the system.
  > Instead, it is retained in Time Travel. This is important to note because dropped tables in Time Travel can be recovered, but
  > they also contribute to data storage for your account. For more information, see [Storage costs for Time Travel and Fail-safe](../../user-guide/data-cdp-storage-costs.md).
  >
  > CREATE OR REPLACE *<object>* statements are atomic. That is, when an object is replaced, the old object is deleted and the new object is created in a single transaction.
  >
  > This means that any queries concurrent with the CREATE OR REPLACE EVENT TABLE operation use either the old or new table version.
* Recreating a table (using the optional `OR REPLACE` keyword) drops its history, which makes any stream on the table stale.
  A stale stream is unreadable.
* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).
* CREATE EVENT TABLE … CLONE:

  If the source event table has clustering keys, the new event table has clustering keys. By default, Automatic Clustering is suspended
  for the new event table—even if Automatic Clustering was not suspended for the source table.
* The `OR REPLACE` and `IF NOT EXISTS` clauses are mutually exclusive. They can’t both be used in the same statement.

## Examples

Create an event table named `my_events`:

> ```sqlexample
> CREATE EVENT TABLE my_events;
> ```
