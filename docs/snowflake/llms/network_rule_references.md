# Source: https://docs.snowflake.com/en/sql-reference/account-usage/network_rule_references.md

# Source: https://docs.snowflake.com/en/sql-reference/functions/network_rule_references.md

Categories:
:   [Information Schema](../info-schema.md) , [Table functions](../functions-table.md)

# NETWORK_RULE_REFERENCES

Returns a row for each object with which the specified network rule is associated or returns a row for each network rule associated
with the specified container.

See also:
:   [NETWORK_RULE_REFERENCES view](../account-usage/network_rule_references.md) (Account Usage View)

## Syntax

```sqlsyntax
NETWORK_RULE_REFERENCES(
  NETWORK_RULE_NAME => '<string>'
)

NETWORK_RULE_REFERENCES(
  CONTAINER_NAME => '<container_name>' ,
  CONTAINER_TYPE => { 'INTEGRATION' | 'NETWORK_POLICY' }
)
```

## Arguments

`NETWORK_RULE_NAME => 'string'`
:   Specifies the identifier for the [network rule](../sql/create-network-rule.md).

    * The entire network rule name must be enclosed in single quotes.
    * If the network rule name is case-sensitive or includes any special characters or spaces, double quotes are required to process the
      case/characters. The double quotes must be enclosed within the single quotes, such as `'"name"'`.

`CONTAINER_NAME => 'container_name'`
:   Specifies the name of the external access integration or network policy to which the network rule is associated.

    * The entire network rule name must be enclosed in single quotes.
    * If the object name is case-sensitive or includes any special characters or spaces, double quotes are required to process the
      case/characters. The double quotes must be enclosed within the single quote, such as `'"<name>"'`.

`CONTAINER_TYPE => { 'INTEGRATION' | 'NETWORK_POLICY' }`
:   Specifies the object type (domain) to which the network rule is associated.

## Output

The function returns the following columns:

| Column | Data Type | Description |
| --- | --- | --- |
| `container_name` | VARCHAR | The name of the container to which the network policy is associated. |
| `container_type` | VARCHAR | One of the following: `NETWORK_POLICY` or `INTEGRATION`. |
| `network_rule_name` | VARCHAR | Name of the network rule. |
| `action_type` | VARCHAR | One of the following: `ALLOW` or `BLOCK`. |
| `database_name` | VARCHAR | Name of the database that contains the network rule. |
| `schema_name` | VARCHAR | Name of the schema that contains the network rule. |

## Usage notes

Use one syntax or the other. Do not mix arguments.

## Examples

Returns a row for each object to which the specified network rule is associated:

> ```sqlexample
> USE ROLE network_admin;
> USE DATABASE securitydb;
> SELECT *
>   FROM TABLE(
>     securitydb.INFORMATION_SCHEMA.NETWORK_RULE_REFERENCES(
>       NETWORK_RULE_NAME => 'securitydb.myrules.cloud_rule'
>     )
>   );
> ```

Returns a row for each network rule associated to the specified container:

> ```sqlexample
> USE ROLE network_admin;
> USE DATABASE securitydb;
> SELECT *
>   FROM TABLE(
>     securitydb.INFORMATION_SCHEMA.NETWORK_RULE_REFERENCES(
>       CONTAINER_NAME => 'my_network_policy' ,
>       CONTAINER_TYPE => 'NETWORK_POLICY'
>     )
>   );
> ```
