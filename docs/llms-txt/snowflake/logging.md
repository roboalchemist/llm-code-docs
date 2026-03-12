# Source: https://docs.snowflake.com/en/developer-guide/logging-tracing/logging.md

# Logging messages from functions and procedures

You can log messages (such as warning or error messages) from a stored procedure, UDF, or UDTF, including those you write
[using Snowpark APIs](../snowpark/index.md). You can access the logged messages from an event table (a type of
predefined table that captures events, including logged messages). For a list of supported handler languages, see
Supported languages.

For example, in a Java UDF, you can use the [SLF4J API](http://www.slf4j.org/) to log messages. Later, you can access those logged messages in an event
table.

> **Note:**
>
> Before you can collect log messages, you must [enable telemetry data collection](logging-tracing-enabling.md).
> When you instrument your code, Snowflake generates the data and collects it in an event table.

## Logging example

The Python code in the following example imports the `logging` module, gets a logger, and logs a message at the `INFO` level.

> **Note:**
>
> A message logged from a method that processes an input row will be logged *for every row* processed by the UDF. If the UDF is executed in a
> large table, this can result in a large number of messages in the event table.

```python
import logging

logger = logging.getLogger("mylog")

def test_logging(self):
    logger.info("This is an INFO test.")
```

## Getting started

To get started logging from handler code, follow these high-level steps:

1. [Set up an event table.](event-table-setting-up.md)

   Snowflake will use your event table to store messages logged from your handler code. An event table has
   columns [predefined by Snowflake](event-table-columns.md).
2. Get acquainted with the logging API for the handler language you’ll be using.

   see Supported languages for a list of handler languages, then view
   content about how to log from your language.
3. Add logging code to your handler.
4. Learn how to [retrieve logging data](logging-accessing-messages.md) from the event table.

## Level for log messages

You can manage the level of log event data stored in the event table by setting the log level. Before logging, use this setting to make
sure you’re capturing the log message severity.

For more information, see [Setting levels for logging, metrics, and tracing](telemetry-levels.md).

## Supported languages

You can log messages from code written in the following languages, including when handler code is written with
[Snowpark APIs](../snowpark/index.md).

| Language / Type | Java | JavaScript | Python | Scala | SQL |
| --- | --- | --- | --- | --- | --- |
| Stored procedure handler | ✔ | ✔ | ✔ | ✔ | ✔ \*\* |
| Streamlit app |  |  | ✔ |  |  |
| UDF handler (scalar function) | ✔ | ✔ | ✔ | ✔ |  |
| UDTF handler (table function) | ✔ | ✔ | ✔ | ✔ \* |  |

**Legend**

\*:
:   Scala UDTF handler written in Snowpark.

\*\*:
:   Snowflake Scripting used to write stored procedures.

> **Note:**
>
> Logging is not supported for [Request and response translators in external functions](../../sql-reference/external-functions-translators.md).

### Logging from handler code

To log messages, you can use functions common to your handler code language. Snowflake intercepts messages and stores them in the
event table you create.

For example, in a Java UDF, you can use the [SLF4J API](http://www.slf4j.org/) to log messages. Later, you can access those logged messages in an event table.

If you plan to log messages when errors occur, you should log them from within the construct for handling errors in the language
that you are using. For example, in a Java UDF, call the method for logging a message in the `catch` block where you handle
the exception.

The following table lists handler languages supported for logging, along with links to content on logging from code.

| Language | Logging Library | Documentation |
| --- | --- | --- |
| Java | SLF4J API | [Logging messages in Java](logging-java.md) |
| JavaScript | Snowflake JavaScript API `snowflake` object | [Logging messages in JavaScript](logging-javascript.md) |
| Python | Standard Library `logging` module | [Logging messages in Python](logging-python.md) |
| Scala | SLF4J API | [Logging messages in Scala](logging-scala.md) |
| Snowflake Scripting | Snowflake SYSTEM$LOG function. | [Logging messages in Snowflake Scripting](logging-snowflake-scripting.md) |

## Viewing log messages

You can view the log messages either through Snowsight or by querying the event table in which log entries are stored. For more
information, see [Viewing log messages](logging-accessing-messages.md).
