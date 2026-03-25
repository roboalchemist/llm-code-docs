# Source: https://docs.snowflake.com/en/sql-reference/functions/spcs_get_events.md

Categories:
:   [Table functions](../functions-table.md) (Snowpark Container Services)

# <service_name>!SPCS_GET_EVENTS

Returns the events that Snowflake collected for the specified service.
For more information,
see [Accessing platform events](../../developer-guide/snowpark-container-services/monitoring-services.md).

See also:
:   [Monitoring Services](../../developer-guide/snowpark-container-services/monitoring-services.md)

## Syntax

```sqlsyntax
<service_name>!SPCS_GET_EVENTS(
  [ START_TIME => <constant_expr> ],
  [ END_TIME => <constant_expr> ] )
```

## Arguments

`START_TIME => constant_expr`
:   Start time (in TIMESTAMP_LTZ format) for the time range from which to
    retrieve events. For available functions to construct data, time, and timestamp data, see [Date & time functions](../functions-date-time.md).

    If the `START_TIME` is not specified, it defaults to one day ago.

`END_TIME => constant_expr`
:   End time (in TIMESTAMP_LTZ format) for the time range from which to retrieve events.

    If END_TIME is not specified, it defaults to the current timestamp.

## Output

| Column | Type | Description |
| --- | --- | --- |
| TIMESTAMP | TIMESTAMP_NTZ | Coordinated Universal Time (UTC) timestamp when Snowflake collected the event. This value maps to the TIMESTAMP column in the event table. |
| SEVERITY | VARCHAR | Severity of the event. This value maps to the `severity_text` field in the RECORD column in the event table. |
| EVENT_NAME | VARCHAR | Name of the event. This value maps to the `name` field in the RECORD column in the event table. |
| EVENT_DETAILS | OBJECT | Details about the event. This value maps to the VALUE column in the event table. |
| INSTANCE_ID | NUMBER | Identifier of the service instance if the event is related to a service instance. This value maps to the `snow.service.instance` field in the RESOURCE_ATTRIBUTES column in the event table. |
| CONTAINER_NAME | VARCHAR | Name of the container if the event is related to a container. This value maps to the `snow.service.container.name` field in the RESOURCE_ATTRIBUTES column in the event table. |
| RECORD | OBJECT | Event information in JSON format. This value maps to the RECORD column in the event table. |
| RECORD_ATTRIBUTES | OBJECT | Additional information about the event. This value maps to the RECORD_ATTRIBUTES column in the event table. |

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| MONITOR | Service | OWNERSHIP is a special privilege on an object that is automatically granted to the role that created the object, but can also be transferred using the [GRANT OWNERSHIP](../sql/grant-ownership.md) command to a different role by the owning role (or any role with the MANAGE GRANTS privilege). |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* It can take a few minutes before events show in the output.

## Examples

Retrieve the events that Snowflake recorded for the `my_test_job`
job over the past day.

```sqlexample
SELECT * FROM TABLE(mydb.myschema.my_test_job!SPCS_GET_EVENTS());
```

Example output:

```output
+-------------------------+----------+-------------------------+----------------------------------------+-------------+----------------+--------------------------------------+-------------------+
| TIMESTAMP               | SEVERITY | EVENT_NAME              | EVENT_DETAILS                          | INSTANCE_ID | CONTAINER_NAME | RECORD                               | RECORD_ATTRIBUTES |
|-------------------------+----------+-------------------------+----------------------------------------+-------------+----------------+--------------------------------------+-------------------|
| 2025-06-26 00:23:40.933 | INFO     | CONTAINER.STATUS_CHANGE | {                                      |        0    | main           | {                                    | NULL              |
|                         |          |                         |   "message": "Completed successfully", |             |                |   "name": "CONTAINER.STATUS_CHANGE", |                   |
|                         |          |                         |   "status": "DONE"                     |             |                |   "severity_text": "INFO"            |                   |
|                         |          |                         | }                                      |             |                | }                                    |                   |
| 2025-06-26 00:23:35.919 | INFO     | CONTAINER.STATUS_CHANGE | {                                      |        0    | main           | {                                    | NULL              |
|                         |          |                         |   "message": "Running",                |             |                |   "name": "CONTAINER.STATUS_CHANGE", |                   |
|                         |          |                         |   "status": "READY"                    |             |                |   "severity_text": "INFO"            |                   |
|                         |          |                         | }                                      |             |                | }                                    |                   |
| 2025-06-26 00:23:34.127 | INFO     | CONTAINER.STATUS_CHANGE | {                                      |        0    | main           | {                                    | NULL              |
|                         |          |                         |   "message": "Waiting to start",       |             |                |   "name": "CONTAINER.STATUS_CHANGE", |                   |
|                         |          |                         |   "status": "PENDING"                  |             |                |   "severity_text": "INFO"            |                   |
|                         |          |                         | }                                      |             |                | }                                    |                   |
+-------------------------+----------+-------------------------+----------------------------------------+-------------+----------------+--------------------------------------+-------------------+
```

Retrieve the events that Snowflake recorded for the `my_test_job` job over the past three days.

```sqlexample
SELECT * FROM TABLE(mydb.myschema.my_test_job!SPCS_GET_EVENTS(START_TIME => DATEADD('day', -3, CURRENT_TIMESTAMP())));
```
