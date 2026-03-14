# Source: https://docs.anyscale.com/monitoring/configure-logging.md

# Structured logging

[View Markdown](/monitoring/configure-logging.md)

# Structured logging

Anyscale enables users to configure the Python logging library to output logs in a structured JSON format. This setup standardizes log entries, making them easier to handle.

## Pre-requisites[​](#pre-requisites "Direct link to Pre-requisites")

Use Anyscale Runtime version 2.30 or higher (version 2.32 or higher is recommended).

note

When using Anyscale runtime version 2.36 or higher, logs automatically output with JSON formatting and include additional metadata. If you have set up log exporting with Vector, make sure your transformations are compatible with JSON logs.

## API (alpha)[​](#api-alpha "Direct link to API (alpha)")

### Method 1: Configure structured logging with `ray.init`[​](#method-1-configure-structured-logging-with-rayinit "Direct link to method-1-configure-structured-logging-with-rayinit")

```
ray.init(
    log_to_driver=False,
    logging_config=ray.LoggingConfig(encoding="JSON", log_level="INFO", additional_log_standard_attrs=['name'])
)
```

Users can configure the following parameters:

* `encoding`: The encoding format for the logs. The default is `TEXT` for plain text logs. The other option is `JSON` for structured logs. In both `TEXT` and `JSON` encoding formats, the logs include Ray-specific fields such as `job_id`, `worker_id`, `node_id`, `actor_id`, `actor_name`, `task_id`, `task_name` and `task_function_name`, if available.

* `log_level`: The log level for the driver process. The default is `INFO`. Available log levels are defined in the [Python logging library](https://docs.python.org/3/library/logging.html#logging-levels).

* `additional_log_standard_attrs`: Since Ray 2.43. A list of additional standard Python logger attributes to include in the log record. The default is an empty list. The list of already included standard attributes are: `asctime`, `levelname`, `message`, `filename`, `lineno`, `exc_text`. The list of all valid attributes are specified in the [Python logging library](http://docs.python.org/library/logging.html#logrecord-attributes).

When you set up `logging_config` in `ray.init`, it configures the root loggers for the driver process, Ray actors, and Ray tasks.

note

The `log_to_driver` parameter is set to `False` to disable logging to the driver process as the redirected logs to the driver will include prefixes that made the logs not JSON parsable.

### Method 2: Configure structured logging with an environment variable (Anyscale Runtime 2.32 or higher)[​](#method-2-configure-structured-logging-with-an-environment-variable-anyscale-runtime-232-or-higher "Direct link to Method 2: Configure structured logging with an environment variable (Anyscale Runtime 2.32 or higher)")

You can configure the `RAY_LOGGING_CONFIG_ENCODING` environment variable to set the encoding format for the logs. You can set the value to `TEXT` or `JSON`. Note that the environment variable needs to be set before `import ray`.

```
import os
os.environ["RAY_LOGGING_CONFIG_ENCODING"] = "JSON"

import ray
import logging

ray.init(log_to_driver=False)
# Use the root logger to print log messages.
```

## Example[​](#example "Direct link to Example")

The following example configures the `LoggingConfig` to output logs in a structured JSON format and set the log level to `INFO`. It then logs messages with the root loggers in the driver process, Ray tasks, and Ray actors. The logs include Ray-specific fields such as `job_id`, `worker_id`, `node_id`, `actor_id`, and `task_id`.

```
import ray
import logging

ray.init(
    logging_config=ray.LoggingConfig(encoding="JSON", log_level="INFO", additional_log_standard_attrs=['name'])
)

def init_logger():
    """Get the root logger"""
    return logging.getLogger()

logger = logging.getLogger()
logger.info("Driver process")

@ray.remote
def f():
    logger = init_logger()
    logger.info("A Ray task")

@ray.remote
class actor:
    def print_message(self):
        logger = init_logger()
        logger.info("A Ray actor")

task_obj_ref = f.remote()
ray.get(task_obj_ref)

actor_instance = actor.remote()
ray.get(actor_instance.print_message.remote())

"""
{"asctime": "2025-02-25 22:06:00,967", "levelname": "INFO", "message": "Driver process", "filename": "test-log-config-doc.py", "lineno": 13, "name": "root", "job_id": "01000000", "worker_id": "01000000ffffffffffffffffffffffffffffffffffffffffffffffff", "node_id": "543c939946ec1321c9c1a10899bfb72f59aa6eab7655719f2611da04", "timestamp_ns": 1740549960968002000}
{"asctime": "2025-02-25 22:06:00,974", "levelname": "INFO", "message": "A Ray task", "filename": "test-log-config-doc.py", "lineno": 18, "name": "root", "job_id": "01000000", "worker_id": "162f2bd846e84685b4c07eb75f2c1881b9df1cdbf58ffbbcccbf2c82", "node_id": "543c939946ec1321c9c1a10899bfb72f59aa6eab7655719f2611da04", "task_id": "c8ef45ccd0112571ffffffffffffffffffffffff01000000", "task_name": "f", "task_func_name": "test-log-config-doc.f", "timestamp_ns": 1740549960974027000}
{"asctime": "2025-02-25 22:06:01,314", "levelname": "INFO", "message": "A Ray actor", "filename": "test-log-config-doc.py", "lineno": 24, "name": "root", "job_id": "01000000", "worker_id": "b7fd965bb12b1046ddfa3d73ead5ed54eb7678d97e743d98dfab852b", "node_id": "543c939946ec1321c9c1a10899bfb72f59aa6eab7655719f2611da04", "actor_id": "43b5d1828ad0a003ca6ebcfc01000000", "task_id": "c2668a65bda616c143b5d1828ad0a003ca6ebcfc01000000", "task_name": "actor.print_message", "task_func_name": "test-log-config-doc.actor.print_message", "actor_name": "", "timestamp_ns": 1740549961314391000}
"""
```

Next, you can also add extra fields to the log entries by using the `extra` parameter in the `logger.info` method.

```
import ray
import logging

ray.init(
    log_to_driver=False,
    logging_config=ray.LoggingConfig(encoding="JSON", log_level="INFO")
)

logger = logging.getLogger()
logger.info("Driver process with extra fields", extra={"username": "anyscale"})

# The log entry includes the extra field "username" with the value "anyscale".

# {"asctime": "2024-07-17 21:57:50,891", "levelname": "INFO", "message": "Driver process with extra fields", "filename": "test.py", "lineno": 9, "username": "anyscale", "job_id": "04000000", "worker_id": "04000000ffffffffffffffffffffffffffffffffffffffffffffffff", "node_id": "76cdbaa32b3938587dcfa278201b8cef2d20377c80ec2e92430737ae"}
```

Switch to the **Logs** tab in the Anyscale Workspace and select **Show details** of the log with the message "A Ray actor". Then, you can see the structured log entry in JSON format:

```
{
  "timestamp": "2024-07-15T19:06:09.326Z",
  "timestampNs": 1721070369326343200,
  "payload": {
    "actor_id": "4a03b12afe5598a00eadcf9503000000",
    "job_id": "03000000",
    "levelname": "INFO",
    "message": "A Ray actor",
    "node_id": "824f9d7c6a82a0faf42b91f07b42667df0831034a713f04f28ba84b9",
    "task_id": "0ab01f2d6283d7194a03b12afe5598a00eadcf9503000000",
    "worker_id": "51d62f87e3867cdcad9aecd7b431068ea433b3104c8cc4ed1db6eef7",
    ...
  }
}
```

## Log to driver[​](#log-to-driver "Direct link to Log to driver")

By default, Ray worker logs are redirected to the driver process (see [Redirecting Worker logs to the Driver](https://docs.ray.io/en/latest/ray-observability/user-guides/configure-logging.html#log-redirection-to-driver)). However, this redirection isn't scalable and can cause performance issues when running on large clusters. It also makes duplicated logs in both the driver and the worker logs. Since Ray 2.36.0, an environment variable `RAY_LOG_TO_STDERR` is introduced to be configured to disable the redirection in the entire node. You can set `RAY_LOG_TO_STDERR=1` to disable the redirection. Or manually in your `ray.init()` call to include `log_to_driver=False`.

If you enable log ingestion through using the CLI command `anyscale cloud config update`, Anyscale sets `RAY_LOG_TO_STDERR` to disable the log redirection. See [Cloud API Reference](/reference/cloud.md).
