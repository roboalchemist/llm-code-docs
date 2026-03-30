# Source: https://docs.snowflake.com/en/sql-reference/functions/spcs_cancel_job.md

Categories:
:   [Table functions](../functions-table.md)

# <service_name>!SPCS_CANCEL_JOB

Cancels a [Snowpark Container Services job](../../developer-guide/snowpark-container-services/working-with-services.md); also referred to as job service. When you cancel a job, Snowflake stops the job from running and removes the resources allocated for running the job.

See also:
:   [Run a job service](../../developer-guide/snowpark-container-services/working-with-services.md), [Working with services](../../developer-guide/snowpark-container-services/working-with-services.md)

## Syntax

```sqlsyntax
<service_name>!SPCS_CANCEL_JOB();
```

## Returns

Returns a string that indicates whether or not the job was canceled.

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| OPERATE | Service | To cancel the job service, you must use a role that was granted this privilege. |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Examples

Cancel the `my_job` job.

```sqlexample
SELECT my_job!SPCS_CANCEL_JOB();
```
