# Source: https://docs.snowflake.com/en/developer-guide/logging-tracing/logging-tracing-enabling.md

# Enabling telemetry collection

You must enable telemetry collection before you can use telemetry data — including log messages, trace event data, and metrics data —
to debug, optimize, and troubleshoot your Snowflake applications.

Use this topic to confirm that you’re set up to capture data.

**To enable telemetry collection:**

1. Ensure that you have an active [event table](event-table-setting-up.md).

   By default, Snowflake includes a [predefined event table](event-table-setting-up.md) that is active for your account
   until you deactivate it or [specify an event table you create](event-table-setting-up.md).
2. Set logging, tracing, and metrics levels.

   You must [set levels](telemetry-levels.md) for the data you want to capture. For example, you
   must set the tracing level to a level other than `OFF` for tracing data to be collected.
3. Add code to your applications, if needed.

   For some telemetry data, data is emitted without your needing to add your own code. For example, Snowflake can record metrics data
   without your needing to add code. For other cases, such as logging and tracing, you can add code to emit your own data to be
   captured in an event table.

   For information on languages supported to emit your own data, see the following:

   * [Logging from handler code](logging.md)
   * [Event tracing from handler code](tracing.md)
