# Source: https://docs.snowflake.com/en/sql-reference/sql/show-endpoints.md

# SHOW ENDPOINTS

> **Note:**
>
> This operation is not currently covered by the Service Level set forth in
> [Snowflake’s Support Policy and Service Level Agreement](https://www.snowflake.com/legal/support-policy-and-service-level-agreement/).

Lists the endpoints in a
[Snowpark Container Services service](../../developer-guide/snowpark-container-services/working-with-services.md) (or a job service). Use the command to list endpoints in a service or service running as a job.

See also:
:   [CREATE SERVICE](create-service.md) , [ALTER SERVICE](alter-service.md), [DROP SERVICE](drop-service.md) , [SHOW SERVICES](show-services.md)

## Syntax

```sqlsyntax
SHOW ENDPOINTS IN SERVICE <name>
```

## Parameters

`name`
:   Specifies the identifier for the service whose endpoints to list.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

## Output

The command output provides service properties and metadata in the following columns:

| Column | Description |
| --- | --- |
| `name` | User-friendly endpoint name that represents the corresponding port. |
| `port` | The network port the service is listening on. NULL, when `portRange` is specified. |
| `port_range` | The network port range the service is listening on. NULL, when `port` is specified. |
| `protocol` | Supported network protocol (TCP, HTTP, or HTTPS). The default is HTTP. Public endpoints and service functions (see [Using a service](../../developer-guide/snowpark-container-services/working-with-services.md)) require HTTP or HTTPS. |
| `is_public` | True, if the endpoint is public, accessible from internet. |
| `ingress_url` | Endpoint URL accessible from the internet. |
| `privatelink_ingress_url` | Endpoint URL accessible via Private Connectivity. The column is returned only for [Business Critical](../../user-guide/intro-editions.md) accounts. |

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| USAGE | Service |  |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* The command doesn’t require a running warehouse to execute.
* The command only returns objects for which the current user’s current role has been granted at least one access privilege.
* The MANAGE GRANTS access privilege implicitly allows its holder to see every object in the account. By default, only the account
  administrator (users with the ACCOUNTADMIN role) and security administrator (users with the SECURITYADMIN role) have the
  MANAGE GRANTS privilege.

* To post-process the output of this command, you can use the [pipe operator](../operators-flow.md)
  (`->>`) or the [RESULT_SCAN](../functions/result_scan.md) function. Both constructs treat the output as a
  result set that you can query.

  For example, you can use the pipe operator or RESULT_SCAN function to select specific columns from the SHOW
  command output or filter the rows.

  When you refer to the output columns, use [double-quoted identifiers](../identifiers-syntax.md) for
  the column names. For example, to select the output column `type`, specify `SELECT "type"`.

  You must use double-quoted identifiers because the output column names for SHOW commands are in lowercase.
  The double quotes ensure that the column names in the SELECT list or WHERE clause match the column names
  in the SHOW command output that was scanned.

## Examples

The following example lists endpoints exposed by `echo_service` service:

```sqlexample
SHOW ENDPOINTS IN SERVICE echo_service;
```

```output
+--------------+------+------------+----------+-----------+------------------------------------------------------------------------------+-----------------------------------------------+
| name         | port | port_range | protocol | is_public | ingress_url                                                                  | privatelink_ingress_url                       |
|--------------+------+------------+----------+-----------+------------------------------------------------------------------------------|-----------------------------------------------*
| echoendpoint | 8080 |            | HTTP     | true      | d7qoajz-orgname-acctname.pp-snowflakecomputing.app                           | d7qoajz.spcs.pdxaac.privatelink.snowflake.app |
+--------------+------+------------+----------+-----------+------------------------------------------------------------------------------+-----------------------------------------------*
```
