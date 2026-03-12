# Source: https://docs.snowflake.com/en/developer-guide/native-apps/connector-sdk/reference/core_reference.md

# Core SQL reference

File: `core.sql`

## Database objects and procedures

### STATE SCHEMA

An un-versioned schema containing the internal state of the Connector. This schema is persisted between different versions of the application.

### STATE.APP_STATE

Table to store the current status of the connector. This table is only accessible internally.
The table contains the following columns:

1. key STRING
2. value VARIANT
3. updated_at TIMESTAMP_NTZ

The following status is set as a default value during the installation:

```json
{
    "status": "CONFIGURING",
    "configurationStatus": "INSTALLED"
}
```

To retrieve the status use the `GET_CONNECTOR_STATUS` procedure below.

### PUBLIC.GET_CONNECTOR_STATUS()

This procedure retrieves the current status from the `APP_STATE` table. An exception will be thrown when status does not exist in the table.

### PUBLIC.RECOVER_CONNECTOR_STATE(NEW_CONNECTOR_STATUS STRING)

This procedure allows the user to force a change of the connector status. It should only be used as
a last resort, when all other means of fixing the connector have failed and the connector is ‘stuck’
in an unchangeable state.

The procedure can only be used by a user with the `ADMIN` role, to force connector status change
from `STARTING`, `PAUSING` or `ERROR` status into `STARTED` or `PAUSED` status.

## Roles

The `core.sql` file introduces the following roles into the application:

* `ADMIN` - has access to all publicly exposed procedures and views
* `VIEWER` - has access to all read only procedures and views
* `DATA_READER` - no access to anything by default. Should be used to access sink database only

## Related Java objects

The following Java objects are tightly connected with the `APP_STATE` table:

* `ConnectorStatusService`
* `ConnectorStatusRepository`
* `KeyValueTable`
* `FullConnectorStatus`
* `ConnectorStatus`
