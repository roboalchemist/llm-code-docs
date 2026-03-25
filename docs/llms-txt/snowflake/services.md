# Source: https://docs.snowflake.com/en/sql-reference/info-schema/services.md

# Source: https://docs.snowflake.com/en/sql-reference/account-usage/services.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# SERVICES view

This SERVICES view in the Account Usage schema is similar to SERVICES view in information schema except this view includes deleted Snowpark Container Services services. For more information about difference in these schemas, see
[Differences between Account Usage and Information Schema](../account-usage.md).

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| SERVICE_ID | NUMBER | Internal/system-generated identifier for the service. |
| SERVICE_NAME | VARCHAR | Name of the service. |
| SERVICE_CATALOG_ID | NUMBER | Internal, Snowflake-generated identifier of the database for the service. |
| SERVICE_CATALOG | VARCHAR | Database that the service belongs to. |
| SERVICE_SCHEMA_ID | NUMBER | Internal, Snowflake-generated identifier of the schema for the service. |
| SERVICE_SCHEMA | VARCHAR | Schema that the service belongs to. |
| SERVICE_OWNER | VARCHAR | Name of the role that owns the service. App instance name if in an app. |
| SERVICE_OWNER_ROLE_TYPE | VARCHAR | Type of the owner role. |
| COMPUTE_POOL_ID | NUMBER | Identifier of the compute pool that runs the service. |
| COMPUTE_POOL_NAME | VARCHAR | Compute pool where the job was executed. |
| DNS_NAME | VARCHAR | DNS name associated with the service. |
| MIN_READY_INSTANCES | NUMBER | Minimum service instances that must be ready for Snowflake to consider the service is ready to process requests. |
| MIN_INSTANCES | NUMBER | Minimum instances for the service. |
| MAX_INSTANCES | NUMBER | Maximum instances for the service. |
| AUTO_RESUME | BOOLEAN | Flag that determines if the service can be auto resumed. |
| QUERY_WAREHOUSE | VARCHAR | Name of the default query warehouse of the service. |
| CREATED | TIMESTAMP_LTZ | Creation time of the service. |
| LAST_ALTERED | TIMESTAMP_LTZ | Last altered time of the service. |
| LAST_RESUMED | TIMESTAMP_LTZ | Last resumed time of the service. |
| DELETED | TIMESTAMP_LTZ | Deletion time of the service. |
| COMMENT | VARCHAR | Comment for this service. |
| IS_JOB | BOOLEAN | `true` if the service is a job service; `false` otherwise. |

## Example

```sqlexample
SELECT *
FROM snowflake.account_usage.services
WHERE service_name LIKE '%myservice%';
```
