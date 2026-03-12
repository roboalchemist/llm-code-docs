# Source: https://docs.snowflake.com/en/developer-guide/logging-tracing/logging-tracing-billing.md

# Costs of telemetry data collection

When you log messages from a function or procedure, Snowflake collects the messages in batches and ingests the batches into the event table.

To perform this work, Snowflake uses Snowflake-managed resources, also referred to as the serverless compute model. As is the case with
[other serverless features](../../user-guide/cost-understanding-compute.md), Snowflake bills your account for the compute resource and cloud
services usage needed to ingest the logged messages. These costs appear on your bill as separate line items.

To determine the credit usage for logging over time, use the following views:

* [METERING_HISTORY view](../../sql-reference/account-usage/metering_history.md).
* [METERING_DAILY_HISTORY view](../../sql-reference/account-usage/metering_daily_history.md) (Account Usage).
* [METERING_DAILY_HISTORY view](../../sql-reference/organization-usage/metering_daily_history.md) (Organization Usage).

To reduce the cost of logging:

* Avoid logging frequently over a long period of time.
* [Set the level of messages ingested](telemetry-levels.md) on specific objects. For example, set the
  log level for specific functions or procedures in a session, instead of setting the log level for all functions or procedures.

If you do not want to collect telemetry data, you can do any one of the following:

* Disable or change telemetry levels appropriately. For more information, see [Set telemetry levels](logging-tracing-overview.md).

  This option is not applicable for [Native Apps](../native-apps/native-apps-about.md).
* Uninstall the applications or connectors emitting telemetry data, or drop the unnecessary objects.
* If you do not want any logging and tracing events to be collected at all in the account, execute the following command to deactivate
  the event table:

  ```sqlexample
  ALTER ACCOUNT SET EVENT_TABLE = NONE
  ```
