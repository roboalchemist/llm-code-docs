# Source: https://docs.snowflake.com/en/sql-reference/sql/show-notification-integrations.md

# SHOW NOTIFICATION INTEGRATIONS

Lists the notification integrations in your account.

The output includes metadata and properties of each notification integration.

See also:
:   [CREATE NOTIFICATION INTEGRATION](create-notification-integration.md) , [ALTER NOTIFICATION INTEGRATION](alter-notification-integration.md) , [DESCRIBE NOTIFICATION INTEGRATION](desc-notification-integration.md),
    [DROP INTEGRATION](drop-integration.md)

## Syntax

```sqlsyntax
SHOW NOTIFICATION INTEGRATIONS [ LIKE '<pattern>' ]
```

## Parameters

`LIKE 'pattern'`
:   Optionally filters the command output by object name. The filter uses case-insensitive pattern matching, with support for SQL
    wildcard characters (`%` and `_`).

    For example, the following patterns return the same results:

    `... LIKE '%testing%' ...`

    `... LIKE '%TESTING%' ...`

    . Default: No value (no filtering is applied to the output).

## Output

The output of the command includes the following columns, which describe the properties and metadata of the object:

| Column | Description |
| --- | --- |
| `name` | Name of the notification integration. |
| `type` | Type of the notification integration. The value can be one of the following:   *`QUEUE - AZURE_STORAGE_QUEUE`: For   [inbound notifications](create-notification-integration-queue-inbound-azure.md) from Azure Event   Grid topics.* `QUEUE - GCP_PUBSUB`: For   [inbound](create-notification-integration-queue-inbound-gcp.md) and   [outbound notifications](create-notification-integration-queue-outbound-gcp.md) to and from Google   Pub/Sub topics. *`QUEUE - AWS_SNS`: For   [outbound notifications](create-notification-integration-queue-outbound-aws.md) to Amazon SNS   topics.* `QUEUE - AZURE_EVENT_GRID`: For   [outbound notifications](create-notification-integration-queue-outbound-azure.md) to Azure Event   Grid topics. *`EMAIL`: For [email notifications](create-notification-integration-email.md).* `WEBHOOK`: For [webhook notifications](create-notification-integration-webhooks.md). |
| `category` | Category of the integration. For notification integrations, this is always `NOTIFICATION`. |
| `enabled` | Indicates whether or not the notification integration is enabled:   *If `true`, the notification integration is enabled.* If `false`, the notification integration is disabled. |
| `comment` | Comment for the notification integration. |
| `created_on` | Date and time when the notification integration was created. |
| `direction` | Indicates whether the integration supports sending or receiving notifications. The value can be one of the following:   *`OUTBOUND`: Snowflake uses the integration to send notifications to a third-party messaging service.  This value appears for notification integrations with any of the following properties:    + `TYPE=QUEUE` and `DIRECTION=OUTBOUND`   + `TYPE=EMAIL`   + `TYPE=WEBHOOK`* `INBOUND`: Snowflake uses the integration to receive notifications from a third-party messaging service.  This value appears for notification integrations that do not specify DIRECTION=OUTBOUND. |

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this SQL command must have at least one of the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| USAGE | Integration |  |
| OWNERSHIP | Integration | OWNERSHIP is a special privilege on an object that is automatically granted to the role that created the object, but can also be transferred using the [GRANT OWNERSHIP](grant-ownership.md) command to a different role by the owning role (or any role with the MANAGE GRANTS privilege). |

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* The command does not require a running warehouse to execute.

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

Show all notification integrations:

```sqlexample
SHOW NOTIFICATION INTEGRATIONS;
```

```output
+-----------------------------+-----------------------------+--------------+---------+---------+-------------------------------+-----------+
| name                        | type                        | category     | enabled | comment | created_on                    | direction |
|-----------------------------+-----------------------------+--------------+---------+---------+-------------------------------+-----------|
| MY_AZURE_INBOUND_QUEUE_INT  | QUEUE - AZURE_STORAGE_QUEUE | NOTIFICATION | true    | NULL    | 2025-03-08 11:34:55.861 -0800 | INBOUND   |
| MY_GCP_INBOUND_QUEUE_INT    | QUEUE - GCP_PUBSUB          | NOTIFICATION | true    | NULL    | 2025-03-08 11:35:35.163 -0800 | INBOUND   |
| MY_GCP_OUTBOUND_QUEUE_INT   | QUEUE - GCP_PUBSUB          | NOTIFICATION | true    | NULL    | 2025-03-08 11:37:06.487 -0800 | OUTBOUND  |
| MY_AWS_OUTBOUND_QUEUE_INT   | QUEUE - AWS_SNS             | NOTIFICATION | true    | NULL    | 2025-03-08 11:36:13.072 -0800 | OUTBOUND  |
| MY_EMAIL_INT                | EMAIL                       | NOTIFICATION | true    | NULL    | 2025-03-08 11:38:55.866 -0800 | OUTBOUND  |
| MY_AZURE_OUTBOUND_QUEUE_INT | QUEUE - AZURE_EVENT_GRID    | NOTIFICATION | true    | NULL    | 2025-03-08 11:36:40.822 -0800 | OUTBOUND  |
| MY_WEBHOOK_INT              | WEBHOOK                     | NOTIFICATION | true    | NULL    | 2025-03-08 11:40:17.336 -0800 | OUTBOUND  |
+-----------------------------+-----------------------------+--------------+---------+---------+-------------------------------+-----------+
```
