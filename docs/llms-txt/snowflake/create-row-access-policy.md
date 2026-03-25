# Source: https://docs.snowflake.com/en/sql-reference/sql/create-row-access-policy.md

# CREATE ROW ACCESS POLICY

Creates a new row access policy in the current/specified schema or replaces an existing row access policy.

After creating a row access policy, add the policy to a table using an [ALTER TABLE](alter-table.md) command or a view using an [ALTER VIEW](alter-view.md)
command.

See also:
:   [Row access policy DDL](../../user-guide/security-row-intro.md)

## Syntax

Snowflake supports the following syntax to create a row access policy.

```sqlsyntax
CREATE [ OR REPLACE ] ROW ACCESS POLICY [ IF NOT EXISTS ] <name> AS
( <arg_name> <arg_type> [ , ... ] ) RETURNS BOOLEAN -> <body>
[ COMMENT = '<string_literal>' ]
```

## Required parameters

`name`
:   Identifier for the row access policy; must be unique for your schema.

    The identifier value must start with an alphabetic character and cannot contain spaces or special characters unless the entire
    identifier string is enclosed in double quotes (e.g. “My object”). Identifiers enclosed in double quotes are also case-sensitive.

    For more details, see [Identifier requirements](../identifiers-syntax.md)

`AS ( <arg_name> <arg_type> [ , ... ] )`
:   The signature for the row access policy.

    A signature specifies a set of attributes that must be considered to determine whether the row is accessible. The attribute values come
    from the database object (e.g. table or view) to be protected by the row access policy.

`RETURNS BOOLEAN`
:   A row access policy must evaluate to true or false. A user that queries a table protected by a row access policy sees rows in the output
    based on how the `body` is written.

`body`
:   SQL expression that operates on the argument values in the signature to determine which rows to return for a query on a table that is
    protected by a row access policy.

    The `body` can be any boolean-valued SQL expression. Snowflake supports expressions that invoke
    [User-defined functions overview](../../developer-guide/udf/udf-overview.md), [Writing external functions](../external-functions.md), and expressions that use sub-queries.

## Optional parameters

`COMMENT = 'string_literal'`
:   Specifies a comment for the row access policy.

    Default: No value

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| CREATE ROW ACCESS POLICY | Schema |  |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

For additional details on masking policy DDL and privileges, see [Managing Column-level Security](../../user-guide/security-column-intro.md).

## Usage notes

* Including one or more [subqueries](../../user-guide/querying-subqueries.md) in the policy body may cause errors. When possible, limit the
  number of subqueries, limit the number of JOIN operations, and simplify WHERE clause conditions.
* If a database object has both a row access policy and one or more [masking policy](../../user-guide/security-column-intro.md), the row access
  policy is evaluated first.

  For more information on row access policies during query runtime, see [Understanding row access policies](../../user-guide/security-row-intro.md).
* A given table or view column can be specified in either a masking policy signature or a row access policy signature. In other words, the
  same column cannot be specified in both a masking policy signature and a row access policy signature at the same time.

  For more information, see [CREATE MASKING POLICY](create-masking-policy.md).
* You cannot change the policy signature (i.e. argument name or input/output data type) using
  CREATE OR REPLACE ROW ACCESS POLICY if the policy is attached to a table or view, or using
  [ALTER ROW ACCESS POLICY](alter-row-access-policy.md). If you need to change the signature, execute a
  [DROP ROW ACCESS POLICY](drop-row-access-policy.md) statement on the policy and create a new row access policy.
* If the policy `body` contains a mapping table lookup, create a centralized mapping table and store the mapping table
  in the same database as the protected table. This is particularly important if the `body` calls the
  [IS_DATABASE_ROLE_IN_SESSION](../functions/is_database_role_in_session.md) function. For details, see the function usage notes.
* A data sharing provider cannot create a row access policy in a [reader account](../../user-guide/data-sharing-reader-create.md).
* If you specify the [CURRENT_DATABASE](../functions/current_database.md) or [CURRENT_SCHEMA](../functions/current_schema.md) function in the
  body of a masking or row access policy, the function returns the database or schema that contains the protected table, not the database or
  schema in use for the session.
* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).

* The OR REPLACE and IF NOT EXISTS clauses are mutually exclusive. They can’t both be used in the same statement.
* CREATE OR REPLACE *<object>* statements are atomic. That is, when an object is replaced, the old object is deleted and the new object is created in a single transaction.

## Examples

These examples use the [CURRENT_ROLE](../functions/current_role.md) context function. If role activation and role hierarchy is
necessary in the policy conditions, use [IS_ROLE_IN_SESSION](../functions/is_role_in_session.md).

The following row access policy allows users whose CURRENT_ROLE is the `it_admin` custom role to see rows that contain the
employee ID number (i.e. `empl_id`) in the query result.

> ```sqlexample
> create or replace row access policy rap_it as (empl_id varchar) returns boolean ->
>   case
>       when 'it_admin' = current_role() then true
>       else false
>   end
> ;
> ```

The following row access policy allows users to view rows in the query result if either of the following two conditions are true:

1. The current role is the `sales_executive_role` custom role. Call the [CURRENT_ROLE](../functions/current_role.md) function to
   determine the current role.
2. The current role is the `sales_manager` custom role and the query specifies a `sales_region` that corresponds to the
   `salesmanageregions` mapping table.

> ```sqlexample
> use role securityadmin;
>
> create or replace row access policy rap_sales_manager_regions_1 as (sales_region varchar) returns boolean ->
>   'sales_executive_role' = current_role()
>       or exists (
>             select 1 from salesmanagerregions
>               where sales_manager = current_role()
>                 and region = sales_region
>           )
> ;
> ```
>
> Where:
>
> > `rap_sales_manager_regions_1`
> > :   The name of the row access policy.
> >
> > `as (sales_region varchar)`
> > :   The signature for the row access policy.
> >
> >     A signature specifies a set of attributes that must be considered to determine whether the row is accessible. The attribute values
> >     come from the table to be protected by the row access policy.
> >
> > `returns boolean ->`
> > :   Specifies the application of the row access policy.
> >
> >     Note that the `<expression>` of the row access policy immediately follows the right-arrow (i.e. `->`).
> >
> >     The expression can be any boolean-valued SQL expression. Snowflake supports expressions that invoke UDFs, External Functions, and
> >     expressions that use subqueries.
> >
> > `'sales_executive_role' = current_role()`
> > :   The first condition of the row access policy expression that allows users with the sales_executive_role custom role to view data.
> >
> > `or exists (select 1 from salesmanagerregions where sales_manager = current_role() and region = sales_region)`
> > :   The second condition of the row access policy expression that uses a subquery.
> >
> >     The subquery requires the [CURRENT_ROLE](../functions/current_role.md) to be the sales_manager custom role with the executed query on
> >     the data to specify a region listed in the `salesmanagerregions` mapping table.

The following row access policy specifies two attributes in the policy signature:

> ```sqlexample
> create or replace row access policy rap_test2 as (n number, v varchar)
>   returns boolean -> true;
> ```
>
> Where:
>
> > `rap_test2`
> > :   The name of the row access policy.
> >
> > `(n number, v varchar)`
> > :   The signature for the row access policy.
> >
> >     A signature specifies a set of attributes that must be considered to determine whether the row is accessible. The attribute values
> >     come from the table to be protected by the row access policy.
> >
> > `returns boolean -> true`
> > :   Determines the application of the row access policy.
> >
> >     The returned value determines whether the user has access to a given row on the database object to which the row access policy is
> >     added.

For additional examples, see [Use row access policies](../../user-guide/security-row-using.md).
