# Source: https://docs.snowflake.com/en/developer-guide/logging-tracing/telemetry-levels.md

# Setting levels for logging, metrics, and tracing

You can set the threshold levels for log, trace, or metrics telemetry data captured in an event table.

Each type of telemetry data supports its own set of levels that are specific to its purpose. You can set these levels by using the
[parameter](../../sql-reference/parameters.md) Snowflake provides for each. You can also set some levels using Snowsight, which
represents the level parameters in a simplified way.

For each type of telemetry data, you can do the following:

* Set levels specific to each type of telemetry data.
* Set system-wide levels for each that are in effect unless overridden.
* Override system-wide levels by setting the level for a session or on specific objects (such as procedures and UDFs).

  Levels are represented as both [session parameters](../../sql-reference/parameters.md) and [object parameters](../../sql-reference/parameters.md).

> **Note:**
>
> You can use handler code to override the log level you set with SQL (as described in this topic) when your handler is written in Python.
> For more information, see [Overriding log threshold levels with Python](logging-python.md).

## Scope

For each type of telemetry data, you can set levels so that they’re in effect at the scope that best suits your requirements. In many
cases, you can override levels set at a larger scope by setting them at a smaller scope, as described in How Snowflake determines the level in effect.
For example, you might want to have a set of default levels at the account scope and then set different levels for objects in a particular
database.

You can set each of these in the following scopes:

Account:
:   A level set for the account is in effect everywhere in the account except where overridden by being set at the object or session level.

Object:
:   You can set the telemetry levels on the following kinds of objects:

    * Database or schema containing procedures and functions
    * Stored procedure
    * User-defined function (UDF) or a user-defined table function (UDTF)
    * Externally managed Apache Iceberg™ table with automated refresh configured

    For example, to set the log level for a specific UDF, use [ALTER FUNCTION](../../sql-reference/sql/alter-function.md) to set the LOG_LEVEL
    parameter for that UDF. As another example, to set the default log level for all functions and procedures in a database, use
    [ALTER DATABASE](../../sql-reference/sql/alter-database.md) to set the LOG_LEVEL parameter on that database. As another example, to set the log level for a
    specific externally managed Iceberg table with automated refresh configured, use [ALTER ICEBERG TABLE](../../sql-reference/sql/alter-iceberg-table.md) to set the
    LOG_LEVEL parameter on that table.

    > **Note:**
    >
    > You can’t set the level on Streamlit objects. Instead, set the level on the database or schema that contains the object.

Session:
:   You can set the telemetry level for calls to functions and procedures made in the current session.

## Levels

You can set the following levels for each kind of telemetry data:

Logging:
:   When you set a level, only data at that level and more severe levels is captured in an event table and visible in Snowsight.
    For example, setting the LOG_LEVEL parameter to WARN means that messages at the WARN, ERROR, and FATAL levels are captured in the
    event table.

    Set the [LOG_LEVEL](../../sql-reference/parameters.md) parameter.

Metrics:
:   You can currently have all metrics data captured or none.

    Set the [METRIC_LEVEL](../../sql-reference/parameters.md) parameter.

Tracing:
:   You can specify the following characteristics:

    * Scope of trace event data stored in the event table

      Set the [TRACE_LEVEL](../../sql-reference/parameters.md) parameter.
    * Whether to capture SQL text in a traced SQL statement

      This is determined by the [SQL_TRACE_QUERY_TEXT](../../sql-reference/parameters.md) parameter. For more information, see [SQL statement tracing](tracing.md).

## Privileges needed

To set levels on an object, you must use a role that is granted or inherits the privileges described in this section.

For example, the code in the following example grants privileges needed for someone using the `central_log_admin` role to set the
log level for the account:

```sqlexample
GRANT MODIFY LOG LEVEL ON ACCOUNT TO ROLE central_log_admin;
```

For more information about privileges, see [Access control privileges](../../user-guide/security-access-control-privileges.md).

| Level to modify | Parameter to set | Privileges needed |
| --- | --- | --- |
| Log level | [LOG_LEVEL](../../sql-reference/parameters.md) | **Account**   *MODIFY LOG LEVEL on the account   **Object*** MODIFY LOG LEVEL on the account *MODIFY on the object for which you want to set the level* USAGE on the database or schema containing the procedure or UDF for which you want to set the level   **Session**   * MODIFY SESSION LOG LEVEL |
| Metric level | [METRIC_LEVEL](../../sql-reference/parameters.md) | **Account**   *MODIFY METRIC LEVEL on the account   **Object*** MODIFY METRIC LEVEL on the account *MODIFY on the object for which you want to set the level* USAGE on the database or schema containing the procedure or UDF for which you want to set the level   **Session**   * MODIFY SESSION METRIC LEVEL |
| Trace level | [TRACE_LEVEL](../../sql-reference/parameters.md) | **Account**   *MODIFY TRACE LEVEL on the account   **Object*** MODIFY TRACE LEVEL on the account *MODIFY on the object for which you want to set the level* USAGE on the database or schema containing the procedure or UDF for which you want to set the level   **Session**   * MODIFY SESSION TRACE LEVEL |
| SQL text in SQL tracing | [SQL_TRACE_QUERY_TEXT](../../sql-reference/parameters.md) | **Account**   * SQL_TRACE_QUERY_TEXT on the account |

## Setting telemetry levels

You can set telemetry levels using either SQL or, in some cases, Snowsight. In many cases, you can override levels set at a
larger scope by setting them at a smaller scope, as described in How Snowflake determines the level in effect.

Before you set levels, verify that you have access to a role with the privileges needed.

SnowsightSQL

You can use Snowsight to set telemetry levels at the account level.

1. Sign in to [Snowsight](../../user-guide/ui-snowsight-gs.md).
2. In the navigation menu, select Monitoring » Traces & logs.
3. On the Traces & Logs page, select Set Event Level.
4. For Set logging & tracing for, select the scope you want from one of the following:

   * Account
   * The database and, optionally, the schema
5. Select levels for the telemetry data you want to adjust.

   |  |  |
   | --- | --- |
   | All Events | On to turn on collection for all kinds of telemetry data; Off to turn off collection for all kinds of data. |
   | Traces | On to set trace data collection to `ALWAYS`; Off to set trace data collection to `OFF`. For information about levels, see [TRACE_LEVEL](../../sql-reference/parameters.md). |
   | Logs | On to set log data collection to `INFO`. For information about levels, see [LOG_LEVEL](../../sql-reference/parameters.md). |
   | Metrics | On to set trace data collection to `ALL`; Off to set trace data collection to `NONE`. For information about levels, see [METRIC_LEVEL](../../sql-reference/parameters.md). |

You can use SQL to set telemetry levels for the account and for objects such as databases, functions, procedures, and externally managed
Iceberg tables with automated refresh configured.

AccountObjectSession

Use the [ALTER ACCOUNT](../../sql-reference/sql/alter-account.md) command to set the appropriate parameter, based on the telemetry data you want to collect.

The following example sets the log level to ERROR for the account:

```sqlexample
-- Set the log level on the account
ALTER ACCOUNT SET LOG_LEVEL = ERROR;
```

To set the LOG_LEVEL parameter on the object, use the [ALTER <object>](../../sql-reference/sql/alter.md) command.

The following example sets the log level to ERROR for all functions and procedures in the database `db`. The example
overrides this level to WARN for the UDF `f1(int)`.

```sqlexample
USE ROLE central_log_admin;

-- Set the log levels on a database and UDF.
ALTER DATABASE db1 SET LOG_LEVEL = ERROR;
ALTER FUNCTION f1(int) SET LOG_LEVEL = WARN;

-- Set the log levels on a Snowpark Container Services service.
ALTER SERVICE test_service SET LOG_LEVEL = ERROR;
```

For details on how Snowflake determines the effective log level when the LOG LEVEL is set on different objects, see
How Snowflake determines the level in effect.

To set the LOG_LEVEL parameter for the current session, use the [ALTER SESSION](../../sql-reference/sql/alter-session.md) command.

```sqlexample
USE ROLE developer_debugging;

-- Set the logging level to DEBUG for the current session.
ALTER SESSION SET LOG_LEVEL = DEBUG;
```

If the level parameter is set to different levels for the current session and on the functions and procedures called in that
session, Snowflake determines the effective level to use. See How Snowflake determines the level in effect.

## How Snowflake determines the level in effect

You can override the telemetry level-related parameters (for both [objects](../../sql-reference/parameters.md)
and [sessions](../../sql-reference/parameters.md)) by using a [hierarchy of levels](../../sql-reference/parameters.md).

For example, you can set a level to one value for the account, then override it by setting the level for an object, which is lower in the
hierarchy.

The following describes the hierarchy for session and object level parameters.

* For session parameters, the hierarchy is Account » User » Session.

  This means that you can set the parameter for an account, override the account-level parameter for a user, and override the
  user-level parameter for the current session.
* For object parameters, the hierarchy is Account » Database » Schema » Object.

  This means that you can set the parameter for an account, override the account-level parameter for a database or schema, and
  override the database- or schema-level parameter for specific stored procedures and UDFs in that database or schema.

For example, the LOG_LEVEL for a function overrides the LOG_LEVEL for the account that contains the function. If the LOG_LEVEL for
the account is FATAL and the LOG_LEVEL for the Java UDF in the account is INFO, the effective LOG_LEVEL is INFO (the level for the
function, not the account):

```sqlexample
ALTER ACCOUNT SET LOG_LEVEL = FATAL;

ALTER FUNCTION MyJavaUDF SET LOG_LEVEL = INFO;

-- The INFO log level is used because the FUNCTION MYJAVAUDF
-- is lower than the ACCOUNT in the hierarchy.
```

In cases where the level is set in both the session and object parameter hierarchies, the most verbose level is used.

* For log level, the following table lists examples of how parameters set on the session and object affect the log level used.

  | Value for the Session | Value for the Object, Schema, Database, or Account | Log Level Used |
  | --- | --- | --- |
  | (unset) | `WARN` | `WARN` |
  | `DEBUG` | (unset) | `DEBUG` |
  | `WARN` | `ERROR` | `WARN` |
  | `INFO` | `DEBUG` | `DEBUG` |
  | (unset) | (unset) | `OFF` |

* For metric level — `ALL` overrides `NONE`.
* For trace level — `ALWAYS` overrides `ON_EVENT` and `OFF`; `ON_EVENT` overrides `OFF`.
