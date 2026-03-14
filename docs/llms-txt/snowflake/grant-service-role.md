# Source: https://docs.snowflake.com/en/sql-reference/sql/grant-service-role.md

# GRANT SERVICE ROLE

Assigns a service role to an account role, application role, or database role. For more information, see [Managing service-related privileges](../../developer-guide/snowpark-container-services/working-with-services.md).

See also:
:   [REVOKE SERVICE ROLE](revoke-service-role.md), [SHOW ROLES IN SERVICE](show-roles-in-service.md),
    [SHOW GRANTS](show-grants.md)

## Syntax

```sqlsyntax
GRANT SERVICE ROLE <name> TO
{
  ROLE <role_name>                     |
  APPLICATION ROLE <application_role_name>  |
  DATABASE ROLE <database_role_name>
}
```

## Parameters

`name`
:   Specifies the identifier for the service role to grant. If the identifier contains spaces or
    special characters, the entire string must be enclosed in double quotes. Identifiers enclosed in
    double quotes are also case-sensitive.

    Specify the service role name in the following format:

    > `service-name!service-role-name`

    For example, `echo_service!echoendpoint_role`.

`ROLE role_name`
:   Name of the account role to grant the service role to.

`APPLICATION ROLE application_role_name`
:   Name of the application role to grant the service role to.

`DATABASE ROLE database_role_name`
:   Name of the database role to grant the service role to.

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege or role | Object | Notes |
| --- | --- | --- |
| OWNERSHIP | Service | Only the service owner can grant the service role. |

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Examples

The following command grants the `echoendpoint_role` service role defined in the `echo_service` service specification to the `service_function_user_role` role.

```sqlexample
GRANT SERVICE ROLE echo_service!echoendpoint_role TO ROLE service_function_user_role;
```
