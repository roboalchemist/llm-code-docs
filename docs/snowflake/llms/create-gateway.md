# Source: https://docs.snowflake.com/en/sql-reference/sql/create-gateway.md

# CREATE GATEWAY

Creates a new [gateway](../../developer-guide/snowpark-container-services/gateway.md)
in the current schema. A gateway enables traffic splitting across multiple service endpoints.

See also:
:   [ALTER GATEWAY](alter-gateway.md) , [DESCRIBE GATEWAY](desc-gateway.md), [DROP GATEWAY](drop-gateway.md) , [SHOW GATEWAYS](show-gateways.md)

## Syntax

```sqlsyntax
CREATE [ OR REPLACE ] GATEWAY [ IF NOT EXISTS ] <name>
  FROM SPECIFICATION <specification_text>
```

## Required parameters

`name`
:   String that specifies the identifier for the gateway; it must be unique for the schema in which the gateway is created.

`FROM SPECIFICATION`
:   Specifies the gateway specification inline. The specification defines the traffic split configuration.

    The specification uses the following format:

    ```yaml
    spec:
      type: traffic_split
      split_type: custom
      targets:
      - type: endpoint
        value: <db>.<schema>.<service>!<endpoint>
        weight: <weight>
      - type: endpoint
        value: <db>.<schema>.<service>!<endpoint>
        weight: <weight>
    ```

## Specification parameters

`type`
:   Fixed value. Must be set to `traffic_split`.

`split_type`
:   Fixed value. Must be set to `custom`.

`targets`
:   A list of target endpoints to route traffic to. Each target must specify:

    `type`
    :   Fixed value. Must be set to `endpoint`.

    `value`
    :   The fully qualified endpoint name in the format `db.schema.service!endpoint`. Each target endpoint must exist.

    `weight`
    :   The traffic weight for this endpoint, specified as an integer. All weights must add up to 100.

> **Note:**
>
> * Maximum number of endpoints per gateway is 5 by default.

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| CREATE GATEWAY | Schema | Required to create a gateway in the schema. |
| BIND SERVICE ENDPOINT | Account | Required to bind service endpoints to the gateway. |
| USAGE | Database | Required on the database containing the gateway. |
| USAGE | Schema | Required on the schema containing the gateway. |
| USAGE | Service endpoints | Required on the target service endpoints. Grant the service role `ALL_ENDPOINTS_USAGE` to provide access. |

To grant the required privileges, use the following commands:

```sqlexample
-- Grant CREATE GATEWAY privilege in the schema
GRANT CREATE GATEWAY ON SCHEMA <schema_name> TO ROLE <role_name>;

-- Grant BIND SERVICE ENDPOINT privilege on the account
GRANT BIND SERVICE ENDPOINT ON ACCOUNT TO ROLE <role_name>;

-- Grant USAGE on target endpoints via service role
GRANT SERVICE ROLE <db_name>.<schema_name>.<service_name>!ALL_ENDPOINTS_USAGE TO ROLE <role_name>;
```

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).

## Examples

Create a gateway that splits traffic between two service endpoints:

```sqlexample
CREATE GATEWAY split_gateway
  FROM SPECIFICATION $$
spec:
  type: traffic_split
  split_type: custom
  targets:
  - type: endpoint
    value: db.schema.s2!ep1
    weight: 60
  - type: endpoint
    value: db.schema.s1!ep1
    weight: 40
$$;
```

Create or replace a gateway with a new traffic split configuration:

```sqlexample
CREATE OR REPLACE GATEWAY split_gateway
  FROM SPECIFICATION $$
spec:
  type: traffic_split
  split_type: custom
  targets:
  - type: endpoint
    value: db.schema.service1!endpoint1
    weight: 70
  - type: endpoint
    value: db.schema.service2!endpoint1
    weight: 30
$$;
```
