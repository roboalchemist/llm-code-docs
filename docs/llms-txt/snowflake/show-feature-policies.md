# Source: https://docs.snowflake.com/en/sql-reference/sql/show-feature-policies.md

# SHOW FEATURE POLICIES

Lists the [feature policies](../../developer-guide/native-apps/ui-consumer-feature-policies.md) for which you have access privileges.

See also:
:   [CREATE FEATURE POLICY](create-feature-policy.md) , [ALTER FEATURE POLICY](alter-feature-policy.md), [DESCRIBE FEATURE POLICY](desc-feature-policy.md), [DROP FEATURE POLICY](drop-feature-policy.md)

## Syntax

```sqlsyntax
SHOW FEATURE POLICIES
  [ IN
    {
      ACCOUNT                                        |
      APPLICATION {app_name}                         |
      APPLICATION PACKAGE {app_package_name}         |
      DATABASE {database_name}                       |
      SCHEMA {schema_name}                           |
    }
  ]

SHOW FEATURE POLICIES ON ACCOUNT

SHOW FEATURE POLICIES ON APPLICATION <application_name>
```

## Parameters

`[ IN ... ]`
:   Optionally specifies the scope of the command. Specify one of the following:

    `ACCOUNT`
    :   Returns information about feature policies created in the specified account.

    `APPLICATION app_name`
    :   Returns information about feature policies created in the specified app.

    `APPLICATION PACKAGE app_package_name`
    :   Returns information about feature policies created in the specified application package.

    `DATABASE database_name`
    :   Returns information about feature policies created in the specified database.

    `SCHEMA schema_name`
    :   Returns information about feature policies created in the specified schema.

`ON ACCOUNT`
:   Shows the feature policies that have been applied to the current account.

`ON APPLICATION app_name`
:   Shows the feature policies that have been applied on the specified app. This command also
    displays feature policies that are inherited from those applied on the account.

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP | Feature policy | This privilege is required to use this command. |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Output

| Column | Description |
| --- | --- |
| `created_on` | The timestamp when the policy was created. |
| `name` | The name of the policy. |
| `database_name` | The name of the database containing the policy. |
| `schema_name` | The name of the schema containing the policy. |
| `kind` | The type of feature policy. Currently, only `FEATURE_POLICY` is supported. |
| `owner` | The role that owns the feature policy. |
| `comment` | A comment containing information about the policy. |
| `owner_role_type` | The type of the role that owns the feature policy. |
| `options` | Currently, always NULL. |

## Examples

The following example lists the feature policies that you have the privileges to view
in the current account:

```sqlexample
SHOW FEATURE POLICIES;
```

The following example lists the feature policies that you have the privileges to view
in an app named `hello_snowflake_app`:

```sqlexample
SHOW FEATURE POLICIES IN APPLICATION hello_snowflake_app;
```

The following example lists the feature policies that have been applied on the current account:

```sqlexample
SHOW FEATURE POLICIES ON ACCOUNT
```
