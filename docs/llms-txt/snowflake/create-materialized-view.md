# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/translation-references/oracle/sql-translation-reference/create-materialized-view.md

# Source: https://docs.snowflake.com/en/sql-reference/sql/create-materialized-view.md

# CREATE MATERIALIZED VIEW

Creates a new materialized view in the current/specified schema, based on a query of an existing table, and populates the view with data.

For more details, see [Working with Materialized Views](../../user-guide/views-materialized.md).

See also:
:   [ALTER MATERIALIZED VIEW](alter-materialized-view.md) , [DROP MATERIALIZED VIEW](drop-materialized-view.md) , [SHOW MATERIALIZED VIEWS](show-materialized-views.md) , [DESCRIBE MATERIALIZED VIEW](desc-materialized-view.md)

## Syntax

```sqlsyntax
CREATE [ OR REPLACE ] [ SECURE ] [ INTERACTIVE ] MATERIALIZED VIEW [ IF NOT EXISTS ] <name>
  [ COPY GRANTS ]
  ( <column_list> )
  [ <col1> [ WITH ] MASKING POLICY <policy_name> [ USING ( <col1> , <cond_col1> , ... ) ]
           [ WITH ] PROJECTION POLICY <policy_name>
           [ WITH ] TAG ( <tag_name> = '<tag_value>' [ , <tag_name> = '<tag_value>' , ... ] ) ]
  [ , <col2> [ ... ] ]
  [ COMMENT = '<string_literal>' ]
  [ [ WITH ] ROW ACCESS POLICY <policy_name> ON ( <col_name> [ , <col_name> ... ] ) ]
  [ [ WITH ] AGGREGATION POLICY <policy_name> [ ENTITY KEY ( <col_name> [ , <col_name> ... ] ) ] ]
  [ CLUSTER BY ( <expr1> [, <expr2> ... ] ) ]
  [ [ WITH ] TAG ( <tag_name> = '<tag_value>' [ , <tag_name> = '<tag_value>' , ... ] ) ]
  [ WITH CONTACT ( <purpose> = <contact_name> [ , <purpose> = <contact_name> ... ] ) ]
  AS <select_statement>
```

## Required parameters

`name`
:   Specifies the identifier for the view; must be unique for the schema in which the view is created.

    In addition, the identifier must start with an alphabetic character and cannot contain spaces or special characters unless the entire
    identifier string is enclosed in double quotes (e.g. `"My object"`). Identifiers enclosed in double quotes are also case-sensitive.

    For more details, see [Identifier requirements](../identifiers-syntax.md).

`select_statement`
:   Specifies the query used to create the view. This query serves as the text/definition for the view. This query is displayed in the output
    of [SHOW VIEWS](show-views.md) and [SHOW MATERIALIZED VIEWS](show-materialized-views.md).

    There are limitations on the `select_statement`. For details, see:

    * Usage notes.
    * [Limitations on Creating Materialized Views](../../user-guide/views-materialized.md).

## Optional parameters

`column_list`
:   If you do not want the column names in the view to be the same as the column names of the underlying table, you may include a column list in
    which you specify the column names. (You do not need to specify the data types of the columns.)

    If you include a CLUSTER BY clause for the materialized view, then you
    must include the column name list.

`MASKING POLICY = policy_name`
:   Specifies the [masking policy](../../user-guide/security-column-intro.md) to set on a column.

`USING ( col_name , cond_col_1 ... )`
:   Specifies the arguments to pass into the conditional masking policy SQL expression.

    The first column in the list specifies the column for the policy conditions to mask or tokenize the data and must match the
    column to which the masking policy is set.

    The additional columns specify the columns to evaluate to determine whether to mask or tokenize the data in each row of the query result
    when a query is made on the first column.

    If the USING clause is omitted, Snowflake treats the conditional masking policy as a normal
    [masking policy](../../user-guide/security-column-intro.md).

`PROJECTION POLICY policy_name`
:   Specifies the [projection policy](../../user-guide/projection-policies.md) to set on a column.

`string_literal`
:   Specifies a comment for the view. The string literal should be in single quotes. (The string literal should not contain single
    quotes unless they are escaped.)

    Default: No value.

`INTERACTIVE`
:   Creates an interactive materialized view, which is optimized for low-latency queries on [interactive tables](../../user-guide/interactive.md).
    An interactive materialized view must be based on a single interactive table. After you create the interactive materialized view,
    you must add both the materialized view and its underlying base table to the interactive warehouse.

    For more information, see [Materialized view support for interactive tables](../../user-guide/interactive.md).

    Default: No value (creates a standard materialized view)

`SECURE`
:   Specifies that the view is secure. For more information about secure views, see [Working with Secure Views](../../user-guide/views-secure.md).

    Default: No value (view is not secure)

`COPY GRANTS`
:   If you are replacing an existing view by using the `OR REPLACE` clause, then the replacement view retains the access permissions
    from the original view. This parameter copies all privileges, except OWNERSHIP, from the existing view to the new view. The
    new view does not inherit any future grants defined for the object type in the schema. By default, the role that executes
    the CREATE MATERIALIZED VIEW statement owns the new view.

    If the parameter is not included in the CREATE VIEW statement, then the new view does not inherit any explicit access privileges
    granted on the original view but does inherit any future grants defined for the object type in the schema.

    Note that the operation to copy grants occurs atomically with the CREATE VIEW statement (i.e. within the same transaction).

    Default: No value (grants are not copied).

`ROW ACCESS POLICY policy_name ON ( col_name [ , col_name ... ] )`
:   Specifies the [row access policy](../../user-guide/security-row-intro.md) to set on the materialized view.

`AGGREGATION POLICY policy_name`
:   Specifies the [aggregation policy](../../user-guide/aggregation-policies.md) to set on the materialized view.

`expr#`
:   Specifies an expression on which to cluster the materialized view. Typically, each expression is the name of a column in the
    materialized view.

    For more information about clustering materialized views, see [Materialized Views and Clustering](../../user-guide/views-materialized.md). For more
    information about clustering in general, see [What is Data Clustering?](../../user-guide/tables-clustering-micropartitions.md).

`TAG ( tag_name = 'tag_value' [ , tag_name = 'tag_value' , ... ] )`
:   Specifies the [tag](../../user-guide/object-tagging/introduction.md) name and the tag string value.

    The tag value is always a string, and the maximum number of characters for the tag value is 256.

    For information about specifying tags in a statement, see [Tag quotas](../../user-guide/object-tagging/introduction.md).

`WITH CONTACT ( purpose = contact [ , purpose = contact ...] )`
:   Associate the new object with one or more [contacts](../../user-guide/contacts-using.md).

    Specify the WITH CONTACT clause after all other clauses except the AS clause (if that clause is supported by this command).

## Usage notes

* Creating a materialized view requires CREATE MATERIALIZED VIEW privilege on the schema, and SELECT privilege on
  the base table. For more information about privileges and materialized views, see [Privileges on a Materialized View’s Schema](../../user-guide/views-materialized.md).
* If you specify the [CURRENT_DATABASE](../functions/current_database.md) or [CURRENT_SCHEMA](../functions/current_schema.md) function in the
  definition of the view, the function returns the database or schema that contains the view, not the database or schema in
  use for the session.
* When you choose a name for the materialized view, note that a schema cannot contain a table and view with the same name. CREATE
  [ MATERIALIZED ] VIEW produces an error if a table with the same name already exists in the schema.
* When specifying the `select_statement`, note the following:

  * You cannot specify a HAVING clause or an ORDER BY clause.
  * If you include a CLUSTER BY clause for the materialized view, you must include the `column_list` clause.
  * If you refer to the base table more than once in the `select_statement`, use the same
    [qualifier](../identifiers.md) for all references for the base table.

    For example, don’t use a mix of `base_table`, `schema.base_table`, and `database.schema.base_table` in the
    same `select_statement`. Instead, choose one of these forms (e.g. `database.schema.base_table`), and use this
    consistently throughout the `select_statement`.
  * Do not query stream objects in the SELECT statement. Streams are not designed to serve as source objects for views or materialized
    views.
* Some column names are not allowed in materialized views. If a column name is not allowed, you can define an alias for the
  column. For details, see [Handling Column Names That Are Not Allowed in Materialized Views](../../user-guide/views-materialized.md).
* If the materialized view queries external tables, you must refresh the file-level metadata
  for the external tables to reflect changes in the referenced cloud storage location, including
  new, updated, and removed files.

  You can refresh the metadata for an external table
  [automatically](../../user-guide/tables-external-auto.md) using the event notification service
  for your cloud storage service or manually using
  [ALTER EXTERNAL TABLE … REFRESH](alter-external-table.md) statements.
* Materialized views have a number of other restrictions. For details, see
  [Limitations on Creating Materialized Views](../../user-guide/views-materialized.md) and [Limitations on Working With Materialized Views](../../user-guide/views-materialized.md).
* When you create an interactive materialized view (using the INTERACTIVE keyword):

  * The materialized view must be based on a single [interactive table](../../user-guide/interactive.md).
    You can’t create an interactive materialized view based on a standard table.
  * Joins aren’t supported in interactive materialized views, just like standard materialized views.
  * After creating the interactive materialized view, you must add both the materialized view
    **and** its underlying base table to the interactive warehouse using
    [ALTER WAREHOUSE … ADD TABLES](alter-warehouse.md).
  * You can’t use an interactive materialized view as the source for another materialized view
    or a dynamic table.

  For more information, see [Materialized view support for interactive tables](../../user-guide/interactive.md).
* View definitions are not updated if the schema of the underlying source table is changed so that the view definition becomes
  invalid. For example:

  * A view is created from a base table, and a column is subsequently dropped from that base table.
  * The base table for the materialized view is dropped.

  In these scenarios, querying the view returns an error that includes the reason why the view was invalidated. For example:

  ```output
  Failure during expansion of view 'MV1':
    SQL compilation error: Materialized View MV1 is invalid.
    Invalidation reason: DDL Statement was executed on the base table 'MY_INVENTORY'.
    Marked Materialized View as invalid.
  ```

  When this occurs, you can do the following:

  * If the base table has been dropped and this is within the
    [data retention period for Time Travel](../../user-guide/data-time-travel.md), you can
    [undrop the base table](undrop-table.md) to make the materialized view valid again.
  * Use the CREATE OR REPLACE MATERIALIZED VIEW command to recreate the view.
* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).
* Using `OR REPLACE` is the equivalent of using [DROP MATERIALIZED VIEW](drop-materialized-view.md) on the existing materialized view and then creating a
  new view with the same name.

  CREATE OR REPLACE *<object>* statements are atomic. That is, when an object is replaced, the old object is deleted and the new object is created in a single transaction.

  This means that any queries concurrent with the CREATE OR REPLACE MATERIALIZED VIEW operation use either the old or new materialized
  view version.
* The `OR REPLACE` and `IF NOT EXISTS` clauses are mutually exclusive. They can’t both be used in the same statement.
* When creating a materialized view with a masking policy on one or more materialized view columns, or a row access policy added to the
  materialized view, use the [POLICY_CONTEXT](../functions/policy_context.md) function to simulate a query on the column(s) protected by a
  masking policy and the materialized view protected by a row access policy.

## Examples

Create a materialized view in the current schema, with a comment, that selects all the rows from a table:

> ```sqlexample
> CREATE MATERIALIZED VIEW mymv
>     COMMENT='Test view'
>     AS
>     SELECT col1, col2 FROM mytable;
> ```

Create an interactive materialized view based on an interactive table, then add both the materialized view and its
base table to an interactive warehouse:

> ```sqlexample
> CREATE INTERACTIVE MATERIALIZED VIEW IF NOT EXISTS mv_summary
>     AS
>     SELECT SUM(quantity) AS total_quantity, SUM(net_paid) AS total_net_paid
>     FROM my_interactive_table
>     WHERE call_center_id = 52;
>
> ALTER WAREHOUSE interactive_wh ADD TABLES (mv_summary, my_interactive_table);
> ```

For more examples, see the examples in [Working with Materialized Views](../../user-guide/views-materialized.md).
