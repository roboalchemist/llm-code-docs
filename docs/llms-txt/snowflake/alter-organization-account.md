# Source: https://docs.snowflake.com/en/sql-reference/sql/alter-organization-account.md

# ALTER ORGANIZATION ACCOUNT

Modifies the properties of an existing [organization account](../../user-guide/organization-accounts.md).

See also:
:   [CREATE ORGANIZATION ACCOUNT](create-organization-account.md), [SHOW ORGANIZATION ACCOUNTS](show-organization-accounts.md)

## Syntax

```sqlsyntax
ALTER ORGANIZATION ACCOUNT SET { [ accountParams ] | [ objectParams ] | [ sessionParams ] }

ALTER ORGANIZATION ACCOUNT UNSET <param_name> [ , ... ]

ALTER ORGANIZATION ACCOUNT SET RESOURCE_MONITOR = <monitor_name>

ALTER ORGANIZATION ACCOUNT SET { PASSWORD | SESSION } POLICY <policy_name>

ALTER ORGANIZATION ACCOUNT UNSET { PASSWORD | SESSION } POLICY

ALTER ORGANIZATION ACCOUNT SET TAG <tag_name> = '<tag_value>' [ , <tag_name> = '<tag_value>' ... ]

ALTER ORGANIZATION ACCOUNT UNSET TAG <tag_name> [ , <tag_name> ... ]
```

> **Note:**
>
> The accountParams, objectParams, and sessionParams for the organization account are identical to the parameters for other accounts. See [ALTER ACCOUNT](alter-account.md) for their syntax.

## Parameters

`name`
:   Specifies the identifier for the organization account to alter.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

`SET ...`
:   Specifies one (or more) account, session, and object parameters to set for your organization account (separated by blank spaces, commas, or new lines):

    * Account parameters cannot be changed by any other users.
    * Session and object parameters set at the account level serve only as defaults and can be changed by other users.

    For descriptions of the parameters you can set for your organization account, see [Parameters](../parameters.md).

`UNSET ...`
:   Specifies one (or more) account, session, and object parameters to unset for your account, which resets them to the system defaults.

    You can reset multiple properties with a single ALTER statement; however, each property must be separated by a comma. When resetting a
    property, specify only the name; specifying a value for the property will return an error.

`SET RESOURCE_MONITOR resource_monitor_name`
:   Special parameter that specifies the name of the resource monitor used to control all virtual warehouses created in the account.

    The organization account is not intended to be heavily used for analytics or other workloads.

`{ PASSWORD | SESSION } POLICY policy_name`
:   Specifies the [password policy](../../user-guide/password-authentication.md) or the [session policy](../../user-guide/session-policies.md) to set for the
    account.

`TAG tag_name = 'tag_value' [ , tag_name = 'tag_value' , ... ]`
:   Specifies the [tag](../../user-guide/object-tagging/introduction.md) name and the tag string value.

    The tag value is always a string, and the maximum number of characters for the tag value is 256.

    For information about specifying tags in a statement, see [Tag quotas](../../user-guide/object-tagging/introduction.md).

## Access Control Requirements

Only a user with the GLOBALORGADMIN role can execute this command.

## Examples

Rename the organization account while allowing users to use either the new or the old account URL to access the account.

> ```sqlexample
> ALTER ORGANIZATION ACCOUNT original_acctname RENAME TO new_acctname;
> ```
