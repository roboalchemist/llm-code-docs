# Source: https://docs.snowflake.com/en/sql-reference/sql/create-maintenance-policy.md

# CREATE MAINTENANCE POLICY

Creates a new [maintenance policy](../../developer-guide/native-apps/consumer-maintenance-policies.md) in the current or specified schema.

See also:
:   [ALTER MAINTENANCE POLICY](alter-maintenance-policy.md), [DROP MAINTENANCE POLICY](drop-maintenance-policy.md), [SHOW MAINTENANCE POLICIES](show-maintenance-policies.md)

## Syntax

```sqlsyntax
CREATE [ OR REPLACE ] MAINTENANCE POLICY [ IF NOT EXISTS ] <name>
  SCHEDULE = 'USING CRON <cron_spec> <timezone>'
  [ COMMENT = '<comment>' ]
```

## Required parameters

`name`
:   Specifies the identifier of the maintenance policy. The identifier must be
    unique within the schema.

`SCHEDULE = 'USING CRON cron_spec timezone`
:   Specifies the schedule for the maintenance policy. This parameter uses the
    same syntax as the `SCHEDULE` parameter of the [CREATE TASK](create-task.md) command.

## Optional parameters

`COMMENT = 'comment'`
:   Specifies an optional comment for the maintenance policy.

## Usage notes

* Each app or account can have only one maintenance policy.

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this SQL command must have at least one of the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| CREATE MAINTENANCE POLICY | Schema |  |

## Examples

The following example creates a maintenance policy that schedules
upgrades for Saturdays at 2 AM UTC:

```sqlexample
CREATE MAINTENANCE POLICY my_maintenance_policy
  SCHEDULE = 'USING CRON 0 2 * * SAT UTC'
  COMMENT = 'Weekly Saturday maintenance window';
```
