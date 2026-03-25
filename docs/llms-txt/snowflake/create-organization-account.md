# Source: https://docs.snowflake.com/en/sql-reference/sql/create-organization-account.md

# CREATE ORGANIZATION ACCOUNT

Creates a new [organization account](../../user-guide/organization-accounts.md).

See also:
:   [ALTER ORGANIZATION ACCOUNT](alter-organization-account.md), [SHOW ORGANIZATION ACCOUNTS](show-organization-accounts.md)

## Syntax

```sqlsyntax
CREATE ORGANIZATION ACCOUNT <name>
    ADMIN_NAME = <string>
    { ADMIN_PASSWORD = '<string_literal>' | ADMIN_RSA_PUBLIC_KEY = <string> }
    [ FIRST_NAME = <string> ]
    [ LAST_NAME = <string> ]
    EMAIL = '<string>'
    [ MUST_CHANGE_PASSWORD = { TRUE | FALSE } ]
    EDITION = { ENTERPRISE | BUSINESS_CRITICAL }
    [ REGION_GROUP = <region_group_id> ]
    [ REGION = <snowflake_region_id> ]
    [ COMMENT = '<string_literal>' ]
```

## Required Parameters

`name`
:   Specifies the identifier (that is, name) for the organization account. It must conform to the following:

    * Must be unique within an organization, regardless of which Snowflake Region the
      organization account is in.
    * Must start with an alphabetic character and cannot contain spaces or special characters except for
      underscores (`_`).

`ADMIN_NAME = string`
:   Login name of the initial administrative user of the organization account. A new user is created in the new organization account with this
    name and password and granted the GLOBALORGADMIN role in the organization account.

    A login name can be any string consisting of letters, numbers, and underscores. Login names are always case-insensitive.

`ADMIN_PASSWORD = 'string_literal'`
:   Password for the initial administrative user of the organization account. The password for the user must be enclosed in single or double quotes.

    Optional if the `ADMIN_RSA_PUBLIC_KEY` parameter is specified.

    For more information about passwords in Snowflake, see [Snowflake-provided password policy](../../user-guide/password-authentication.md).

`ADMIN_RSA_PUBLIC_KEY = string`
:   Assigns a public key to the initial administrative user of the organization account in order to implement
    [key pair authentication](../../user-guide/key-pair-auth.md) for the user.

    Optional if the `ADMIN_PASSWORD` parameter is specified.

`EMAIL = 'string_literal'`
:   Email address of the initial administrative user of the organization account. This email address is used to send any notifications about the
    organization account.

`EDITION = ENTERPRISE | BUSINESS_CRITICAL`
:   [Snowflake Edition](../../user-guide/intro-editions.md) of the organization account.

## Optional Parameters

`FIRST_NAME = string` , . `LAST_NAME = string`
:   First and last name of the initial administrative user of the organization account.

    Default: `NULL`

`MUST_CHANGE_PASSWORD = TRUE | FALSE`
:   Specifies whether the new user created to administer the organization is forced to change their password upon first login into the
    organization account.

    Default: `FALSE`

`REGION_GROUP = region_group_id`
:   ID of the region group where the organization account is created. To retrieve the region group ID for existing accounts in your
    organization, execute the [SHOW REGIONS](show-regions.md) command. For information about when you might need to specify region
    group, see [Region groups](../../user-guide/admin-account-identifier.md).

    Default: Current region group.

`REGION = snowflake_region_id`
:   [Snowflake Region ID](../../user-guide/admin-account-identifier.md) of the region where the organization account is created. If no value is provided,
    Snowflake creates the organization account in the same Snowflake Region as the current account (that is, the account in which the CREATE
    ORGANIZATION ACCOUNT statement is executed.)

    To obtain a list of the regions that are available for an organization, execute the [SHOW REGIONS](show-regions.md) command.

    Default: Current Snowflake Region.

`COMMENT = 'string_literal'`
:   Specifies a comment for the organization account.

    Default: No value

## Access Control Requirements

Only users with the ORGADMIN role can execute the command.

## Examples

Create an organization account in the same region group and Snowflake Region in which the CREATE ORGANIZATION ACCOUNT statement is executed.
The new organization administrator must change their password upon first login:

> ```sqlexample
> CREATE ORGANIZATION ACCOUNT myorgaccount
>   ADMIN_NAME = admin
>   ADMIN_PASSWORD = 'TestPassword1'
>   EMAIL = 'myemail@myorg.org'
>   MUST_CHANGE_PASSWORD = true
>   EDITION = enterprise;
> ```
