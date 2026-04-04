# Source: https://docs.snowflake.com/en/developer-guide/native-apps/event-about.md

# Use logging and event tracing for an app

This topic describes how providers can configure a Snowflake Native App to record log messages and trace events.

## About log messages and trace events in an app

The Snowflake Native App Framework supports using the Snowflake [logging and tracing](../logging-tracing/logging-tracing-overview.md)
functionality to gather information about an app. Providers can configure an app to record and analyze the following:

* [Log messages](../logging-tracing/logging.md) — Independent, detailed messages with information about
  the state of a specific piece app code.
* [Trace events](../logging-tracing/tracing.md) — Structured data that providers can
  use to get information spanning and grouping multiple parts of your code. Trace events allows an app to emit information related
  to its performance and behavior.
* [Metrics](../logging-tracing/metrics.md) - Information about stored procedure and UDF resource consumption
  based on the CPU and memory metrics that Snowflake generates.

To configure an app to emit log messages and trace events, providers set the log and trace levels in the manifest file.
See [Set the log and trace levels for an app](event-definition.md).

Providers can also configure an app to use event sharing to allow the consumer to share the log messages
and trace events with the provider. See About event sharing for
more information.

## About application lifecycle events

Snowflake records events that provide visibility into the status and history of a
Snowflake Native App. These Snowflake-provided events are referred to as
*application lifecycle events*.

For example, if a consumer’s app instance transitions to a failed state due to an
error during an upgrade, you can use application lifecycle events to view this
historical event.

Snowflake logs these application lifecycle events in the
[event table](../logging-tracing/event-table-setting-up.md) in the
account. By default, application lifecycle events are not logged. To enable logging of
application lifecycle events, set the log and trace levels in the [log level property in the manifest file](manifest-reference.md) manifest file. See
[Set the log and trace levels for an app](event-definition.md) for more information.

The value of the `log_level` property in the manifest file determines the
severity of events recorded in the event table. Application lifecycle events support
the following severity levels:

* `TRACE`
* `DEBUG`
* `INFO`
* `WARN`
* `ERROR`
* `FATAL`
* `OFF`

> **Note:**
>
> Each logging level includes records from all lower levels. For example, setting the log level
> to `WARN` also records `ERROR` and `FATAL` events.

### Query application lifecycle events

After you configure the log level for your app, Snowflake records application
lifecycle events in the active event table in your Snowflake account. You can query
the event table to view these events.

The following SELECT statement retrieves application lifecycle events for a specific
app recorded in the past hour:

```sqlexample
SELECT TIMESTAMP, RESOURCE_ATTRIBUTES, RECORD, VALUE
  FROM <your_event_table>
  WHERE TIMESTAMP > DATEADD(hour, -1, CURRENT_TIMESTAMP())
    AND RESOURCE_ATTRIBUTES:"snow.application.name" = '<your_app_name>'
    AND RECORD_TYPE = 'EVENT'
  ORDER BY TIMESTAMP DESC
  LIMIT 10;
```

## About event sharing

Event sharing allows the provider to collect information about an app’s performance and behavior.
A provider can configure an app to request that the consumers share the log messages
and trace events with the provider. Event sharing requires that the provider and consumer configure an
event table in their account to store the log messages and trace events emitted by the app.

When event sharing is enabled, the log messages and trace events that are inserted into the event table in the
consumer account are also inserted into the event table in provider account.

> **Note:**
>
> The only events with a `RECORD_TYPE` of `EVENT` that support event
> sharing are Snowflake Native Apps application lifecycle events and Snowpark Container Services platform events.

## Considerations when using event sharing

Before configuring logging and event sharing for an app, providers must consider the following:

* Providers are responsible for all costs associated with event sharing on the provider side, including data
  ingestion and storage.
* Providers must have [an account to store shared events](event-manage-provider.md)
  in each region where you want to support event sharing.
* Providers must define the default log level and trace level for an app in the manifest file.

## Considerations when migrating from the previous event sharing functionality

When migrating from the existing event sharing functionality to use event definitions, providers
should consider the following.

* The previous event sharing functionality is equivalent to the OPTIONAL ALL event definition.
* Published versions and patches of an app that used the previous functionality will have the
  OPTIONAL ALL event definition by default. Providers do not need to add this event definition
  to the manifest file.

To begin using event definitions, providers can add supported event definitions to the manifest
file. This is applicable to new apps as well as new versions and patches of existing apps.

> **Note:**
>
> To being begin requesting more granular log and event sharing, providers only have to add
> event definitions to the manifest file. No other actions are required for providers.

## Workflow - Set up event sharing for an app

Event sharing allows consumers to share log messages and trace events with the provider.

The following workflow shows how to set up and enable event sharing for an app:

1. The provider [sets the log and trace levels](event-definition.md)
   for the app.
2. The provider [adds event definitions](event-definition.md) to the manifest file.

   Event definitions act as filters on the log messages and trace events emitted by the app.
   Providers can configure event definitions to be required or optional.
3. The provider [sets up an event table](event-manage-provider.md)
   in their organization.
4. The provider publishes the app.

When a consumer installs an app, they can set up an event table and enable event sharing.
See [Enable logging and event sharing for an app](https://other-docs.snowflake.com/en/native-apps/consumer-enable-logging)
for more information on the consumer requirements for event sharing.

## Monitor consumer application health

You can use the `LAST_HEALTH_STATUS` and `LAST_HEALTH_STATUS_UPDATED_ON` columns
of the [APPLICATION_STATE view](../../sql-reference/data-sharing-usage/application-state-view.md) to monitor the health of consumer instances of your
app. The `LAST_HEALTH_STATUS` column has the following possible values:

* `OK`: The consumer instance is healthy.
* `FAILED`: The consumer instance is in an error state.
* `PAUSED`: The consumer manually paused the app.

The following code sample demonstrates using the `APPLICATION_STATE` view
to retrieve the health status of all consumer instances of your app:

```sqlexample
SELECT
    CONSUMER_ORGANIZATION_NAME,
    CONSUMER_ACCOUNT_NAME,
    LAST_HEALTH_STATUS,
    LAST_HEALTH_STATUS_UPDATE_TIME
FROM
    SNOWFLAKE.ACCOUNT_USAGE.APPLICATION_STATE
WHERE
    PROVIDER_ORG_NAME = '<your_provider_org_name>'
    AND APPLICATION_NAME = '<your_app_name>'
ORDER BY
    LAST_HEALTH_STATUS_UPDATE_TIME DESC;
```

The preceding query may return results similar to the following:

```output
CONSUMER_ORG_NAME    CONSUMER_ACCOUNT_NAME    LAST_HEALTH_STATUS    LAST_HEALTH_STATUS_UPDATE_TIME
------------------   ---------------------    ------------------    -------------------------------
consumer_org_1      consumer_account_1       OK                    2024-01-15 10:30:00.000
consumer_org_2      consumer_account_2       FAILED                2024-01-15 09:45:00.000
consumer_org_3      consumer_account_3       PAUSED                2024-01-14 16:20:00.000
```
