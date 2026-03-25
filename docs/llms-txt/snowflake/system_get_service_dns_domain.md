# Source: https://docs.snowflake.com/en/sql-reference/functions/system_get_service_dns_domain.md

Categories:
:   [System functions](../functions-system.md) (System Information)

# SYSTEM$GET_SERVICE_DNS_DOMAIN

Given a schema name, returns that schema’s DNS namespace hash as a string.

See also:
:   [Working with Services](../../developer-guide/snowpark-container-services/working-with-services.md)

## Syntax

```sqlsyntax
SYSTEM$GET_SERVICE_DNS_DOMAIN( <schema_name> )
```

## Arguments

`schema_name`
:   Schema name. If the schema is not in the current database, specify the fully qualified name of the schema.

## Returns

Returns the schema’s DNS namespace hash as a string.

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| USAGE | Schema |  |

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Examples

If TUTORIAL_DB is the current database, then both of the following return the same result. This is the same DNS domain that appears in the DNS name (as reported by [SHOW SERVICES](../sql/show-services.md)) for any service in the DATA_SCHEMA schema.

```sqlexample
SELECT SYSTEM$GET_SERVICE_DNS_DOMAIN('DATA_SCHEMA');
SELECT SYSTEM$GET_SERVICE_DNS_DOMAIN('TUTORIAL_DB.DATA_SCHEMA');
```

Example output:

```output
+----------------------------------------------+
| SYSTEM$GET_SERVICE_DNS_DOMAIN('DATA_SCHEMA') |
|----------------------------------------------|
| k3m6.svc.spcs.internal                       |
+----------------------------------------------+
```
