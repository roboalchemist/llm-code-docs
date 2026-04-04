# Source: https://docs.snowflake.com/en/sql-reference/sql/create-packages-policy.md

# CREATE PACKAGES POLICY

Creates a new [packages policy](../../developer-guide/udf/python/packages-policy.md) or replaces an
existing packages policy.

After creating a packages policy, apply the packages policy to your Snowflake account using
an ALTER ACCOUNT statement.

## Syntax

```sqlsyntax
CREATE [ OR REPLACE ] PACKAGES POLICY [ IF NOT EXISTS ] <name>
  LANGUAGE PYTHON
  [ ALLOWLIST = ( [ '<packageSpec>' ] [ , '<packageSpec>' ... ] ) ]
  [ BLOCKLIST = ( [ '<packageSpec>' ] [ , '<packageSpec>' ... ] ) ]
  [ ADDITIONAL_CREATION_BLOCKLIST = ( [ '<packageSpec>' ] [ , '<packageSpec>' ... ] ) ]
  [ COMMENT = '<string_literal>' ]
```

## Required parameters

`name`
:   Specifies the identifier (i.e. name) for the packages policy; must be unique for the schema in which the packages policy is created.

    In addition, the identifier must start with an alphabetic character and cannot contain spaces or special characters unless the
    entire identifier string is enclosed in double quotes (for example, `"My object"`). Identifiers enclosed in double quotes are also
    case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

`LANGUAGE PYTHON`
:   Specifies the language that this packages policy will apply to.

## Optional parameters

`ALLOWLIST = ( [ 'packageSpec' ] [ , 'packageSpec' ... ] )`
:   Specifies a list of package specs that are allowed.

    Default: `('*')` (i.e. allow all packages).

`BLOCKLIST = ( [ 'packageSpec' ] [ , 'packageSpec' ... ] )`
:   Specifies a list of package specs that are blocked. To unset this parameter, specify an empty list.

    Default: `()` (i.e. do not block any packages).

`ADDITIONAL_CREATION_BLOCKLIST = ( [ 'packageSpec' ] [ , 'packageSpec' ... ] )`
:   Specifies a list of package specs that are blocked at creation time. To unset this parameter, specify an empty list.
    If the `ADDITIONAL_CREATION_BLOCKLIST` is set, it is appended to the basic BLOCKLIST at the creation time.
    For temporary UDFs and anonymous stored procedures, the `ADDITIONAL_CREATION_BLOCKLIST` is appended to the basic BLOCKLIST at both creation and execution time.

    Default: `()` (i.e. do not block any packages).

`COMMENT = 'string_literal'`
:   Adds a comment or overwrites an existing comment for the packages policy.

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| CREATE PACKAGES POLICY | Schema |  |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* The OR REPLACE and IF NOT EXISTS clauses are mutually exclusive. They can’t both be used in the same statement.
* CREATE OR REPLACE *<object>* statements are atomic. That is, when an object is replaced, the old object is deleted and the new object is created in a single transaction.

* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).

## Examples

Create a packages policy for your current account:

> ```sqlexample
> CREATE PACKAGES POLICY yourdb.yourschema.packages_policy_prod_1
>   LANGUAGE PYTHON
>   ALLOWLIST = ('numpy', 'pandas==1.2.3', ...)
>   BLOCKLIST = ('numpy==1.2.3', 'bad_package', ...)
>   COMMENT = 'Packages policy for the prod_1 environment';
> ```
