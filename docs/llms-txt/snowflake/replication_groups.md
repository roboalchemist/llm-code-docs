# Source: https://docs.snowflake.com/en/sql-reference/info-schema/replication_groups.md

# Source: https://docs.snowflake.com/en/sql-reference/account-usage/replication_groups.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# REPLICATION_GROUPS view

This Account Usage view displays a row for each
[replication group and failover group](../../user-guide/account-replication-intro.md) in the account.

The returned results include details such as the replication or failover group name,
the types of objects that it applies to, and its schedule for replication refresh operations.

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| CREATED | TIMESTAMP_LTZ | Date and time the replication or failover group was created. |
| DELETED | TIMESTAMP_LTZ | Date and time the replication or failover group was deleted. |
| NAME | VARCHAR | Name of the replication or failover group. |
| TYPE | VARCHAR | Type of group. Valid values are REPLICATION or FAILOVER. |
| COMMENT | VARCHAR | Comment string. |
| OBJECT_TYPES | VARCHAR | List of specified object types enabled for replication (and failover in the case of a FAILOVER group). |
| ALLOWED_INTEGRATION_TYPES | VARCHAR | List of integration types that are enabled for replication. Snowflake always includes this column in the output, even if integrations weren’t specified in the CREATE or ALTER command. |
| REPLICATION_SCHEDULE | VARCHAR | Scheduled interval for refresh; NULL if no replication schedule is set. |
| OWNER | VARCHAR | Name of the role with the OWNERSHIP privilege on the replication or failover group. |
| IS_LISTING_AUTO_FULFILLMENT_GROUP | BOOLEAN | TRUE if the replication group is used for Cross-Cloud Auto-Fulfillment. FALSE otherwise. |
| ERROR_INTEGRATION | VARCHAR | The name of the notification integration for the replication group or failover group to which the error notification is sent in cases of refresh failures. |

## Usage notes

* Latency for the view may be up to 120 minutes (2 hours).

## Examples

The following example returns the active failover groups for your Snowflake account:

```sqlexample
SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.REPLICATION_GROUPS
  WHERE type = 'FAILOVER' AND deleted IS NULL
  ORDER BY name;
```
