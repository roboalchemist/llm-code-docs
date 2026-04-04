# Source: https://docs.snowflake.com/en/sql-reference/sql/create-share.md

# CREATE SHARE

Creates a new, empty [share](../../user-guide/data-sharing-intro.md). Once the share is created, you can include a database and
objects from the database (schemas, tables, and views) in the share using the [GRANT <privilege> … TO SHARE](grant-privilege-share.md) command. You can then use
[ALTER SHARE](alter-share.md) to add one or more accounts to the share.

See also:
:   [DROP SHARE](drop-share.md) , [ALTER SHARE](alter-share.md) , [SHOW SHARES](show-shares.md) , [DESCRIBE SHARE](desc-share.md)

## Syntax

```sqlsyntax
CREATE [ OR REPLACE ] SHARE [ IF NOT EXISTS ] <name>
  [ COMMENT = '<string_literal>' ]
```

## Required parameters

`name`
:   Specifies the identifier for the share; must be unique for the account in which the share is created.

    In addition, the identifier must start with an alphabetic character and cannot contain spaces or special characters unless the entire
    identifier string is enclosed in double quotes (e.g. `"My object"`). Identifiers enclosed in double quotes are also case-sensitive.

    For more details, see [Identifier requirements](../identifiers-syntax.md).

## Optional parameters

`COMMENT = 'string_literal'`
:   Specifies a comment for the share.

    Default: No value

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| CREATE SHARE | Account | Only the ACCOUNTADMIN role has this privilege by default. The privilege can be granted to additional roles as needed. |

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

For more information about access control requirements for Snowflake Secure Data Sharing specifically, see
[Enable non-ACCOUNTADMIN roles to perform data sharing tasks](../../user-guide/security-access-privileges-shares.md).

## Usage notes

* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).

* The OR REPLACE and IF NOT EXISTS clauses are mutually exclusive. They can’t both be used in the same statement.
* CREATE OR REPLACE *<object>* statements are atomic. That is, when an object is replaced, the old object is deleted and the new object is created in a single transaction.

## Examples

Create an empty share named `sales_s`:

> ```sqlexample
> CREATE SHARE sales_s;
> ```
>
> ```output
> +-----------------------------------------+
> | status                                  |
> |-----------------------------------------|
> | Share SALES_S successfully created.     |
> +-----------------------------------------+
> ```

After you create the share, complete it by running the following commands:

> 1. Run the [GRANT <privilege> … TO SHARE](grant-privilege-share.md) command to add a database (and objects in the database) to the share.
> 2. Run the [ALTER SHARE](alter-share.md) command to add accounts to the share.
