# Source: https://docs.snowflake.com/en/sql-reference/sql/alter-packages-policy.md

# ALTER PACKAGES POLICY

Modifies the properties for an existing [packages policy](../../developer-guide/udf/python/packages-policy.md).

Any changes made to the packages policy properties go into effect when the next SQL query that uses the packages policy runs.

## Syntax

```sqlsyntax
ALTER PACKAGES POLICY [ IF EXISTS ] <name> SET
  [ ALLOWLIST = ( [ '<packageSpec>' ] [ , '<packageSpec>' ... ] ) ]
  [ BLOCKLIST = ( [ '<packageSpec>' ] [ , '<packageSpec>' ... ] ) ]
  [ ADDITIONAL_CREATION_BLOCKLIST = ( [ '<packageSpec>' ] [ , '<packageSpec>' ... ] ) ]
  [ COMMENT = '<string_literal>' ]

ALTER PACKAGES POLICY [ IF EXISTS ] <name> UNSET
  [ ALLOWLIST ]
  [ BLOCKLIST ]
  [ ADDITIONAL_CREATION_BLOCKLIST ]
  [ COMMENT ]
```

## Parameters

`name`
:   Specifies the identifier for the packages policy to alter. If the identifier contains spaces or special characters,
    the entire string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive.

    For more details, see [Identifier requirements](../identifiers-syntax.md).

`SET ...`
:   Specifies one or more properties to set for the packages policy.

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

`UNSET ...`
:   Specifies one or more properties to unset for the packages policy, which resets them to the defaults:

    > * `ALLOWLIST`
    > * `BLOCKLIST`
    > * `ADDITIONAL_CREATION_BLOCKLIST`
    > * `COMMENT`
    >
    > You can reset multiple properties with a single ALTER statement; however, each property must be separated by a comma. When resetting
    > a property, specify only the name; specifying a value for the property will return an error.

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP | Packages policy | OWNERSHIP is a special privilege on an object that is automatically granted to the role that created the object, but can also be transferred using the [GRANT OWNERSHIP](grant-ownership.md) command to a different role by the owning role (or any role with the MANAGE GRANTS privilege). |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* If you want to update an existing packages policy and need to see the current definition of the policy, call the
  [GET_DDL](../functions/get_ddl.md) function or run
  the [DESCRIBE PACKAGES POLICY](desc-packages-policy.md) command.
* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).

## Examples

The following example updates the packages policy.

> ```sqlexample
> ALTER PACKAGES POLICY packages_policy_prod_1 SET ALLOWLIST = ('pandas==1.2.3');
> ```
