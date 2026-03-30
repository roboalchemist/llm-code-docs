# Source: https://docs.snowflake.com/en/sql-reference/functions/spcs_wait_for.md

Categories:
:   [Snowpark Container Services functions](../functions-spcs.md)

# <service_name>!SPCS_WAIT_FOR

Waits for the [Snowpark Container Services service](../../developer-guide/snowpark-container-services/working-with-services.md) to reach the specified state, with a timeout.

* When you execute an asynchronous job, use this helper function to wait for the job to complete.
* When you create a service, use this helper function to wait until the service is running.

See also:
:   [Snowpark Container Services: Working with services](../../developer-guide/snowpark-container-services/working-with-services.md)

## Syntax

```sqlsyntax
<service_name>!SPCS_WAIT_FOR( <status>, <timeout_sec> );
```

## Arguments

**Required arguments**

`'status'`
:   Status to wait for. For a list of service status values, see the output section of the [DESCRIBE SERVICE](../sql/desc-service.md) command.

`timeout_sec`
:   The maximum duration, in seconds, to wait for the specified status. If specified status isn’t reached within the timeout, the function returns an error message that includes the current service status.

## Returns

If the service doesn’t reach the specified status within the timeout or Snowflake determines that the status can never be reached, the function returns an error message that also provides the current service status. Otherwise, it returns a success message.

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this SQL command must have at least one of the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| Any one of these privileges: OWNERSHIP, USAGE, MONITOR or OPERATE | Service |  |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Examples

Wait for two minutes for the specified job to complete (job status is DONE).

```sqlexample
CALL my_job!spcs_wait_for('DONE', 120)
```

Wait for three minutes for the specified service to start (service status is RUNNING).

```sqlexample
CALL my_service!SPCS_WAIT_FOR('RUNNING', 180)
```
