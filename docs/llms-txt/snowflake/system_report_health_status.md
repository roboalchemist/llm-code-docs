# Source: https://docs.snowflake.com/en/sql-reference/functions/system_report_health_status.md

Categories:
:   [System functions](../functions-system.md) (Information)

# SYSTEM$REPORT_HEALTH_STATUS

Sends [application health information](../../developer-guide/native-apps/monitoring.md) from a consumer app to the provider account.

## Syntax

```sqlsyntax
SYSTEM$REPORT_HEALTH_STATUS( '<status>' )
```

## Arguments

`'status'`
:   A string literal of type VARCHAR that indicates the health status of the
    application. You can specify one of the following values:

* `'OK'`: The consumer instance is healthy.
* `'FAILED'`: The consumer instance is in an error state.
* `'PAUSED'`: The consumer manually paused the app.

## Usage notes

* This function is intended to be called by consumer applications. Your application
  should call this function periodically to report its health status to the
  provider account.
* Your application logic determines what health status to report based on its own
  monitoring and error handling.
* The health status reported by this function is visible to the provider account
  via the GET_HEALTH_STATUS function. You
  should call GET_HEALTH_STATUS periodically
  from the provider account to monitor the health of consumer instances. If you
  use a task or monitored task to call this function, ensure that the application
  has the correct privileges to run the task. Consider setting up alerts to
  notify you when a consumer instance reports a `FAILED` status, a
  `PAUSED` status, or stops reporting its status.
* Snowflake only retains the most recent health status reported by each
  consumer instance of the application.
* To avoid excessive load on Snowflake, this function is rate limited. If the
  function is called again within 55 minutes from the same consumer instance, it
  will return `false` to indicate that the status report was not accepted.
* For more information about monitoring application health from the provider side,
  see [Use monitoring for an app](../../developer-guide/native-apps/monitoring.md).

## Return value

* This function returns TRUE if the health status was successfully reported.
* This function returns FALSE if the status report failed due to being
  rate limited.
