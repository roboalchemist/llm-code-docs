# Configuration and defaults {#configuration}

This document describes the configuration options available.

If you\'re using the default loader, you must create the
`celeryconfig.py`{.interpreted-text role="file"} module and make sure
it\'s available on the Python path.

::: {.contents local="" depth="2"}
:::

## Example configuration file {#conf-example}

This is an example configuration file to get you started. It should
contain all you need to run a basic Celery set-up.

``` python
## Broker settings.
broker_url = 'amqp://guest:guest@localhost:5672//'

# List of modules to import when the Celery worker starts.
imports = ('myapp.tasks',)

## Using the database to store task state and results.
result_backend = 'db+sqlite:///results.db'

task_annotations = {'tasks.add': {'rate_limit': '10/s'}}
```

## New lowercase settings {#conf-old-settings-map}

Version 4.0 introduced new lower case settings and setting organization.

The major difference between previous versions, apart from the lower
case names, are the renaming of some prefixes, like `celery_beat_` to
`beat_`, `celeryd_` to `worker_`, and most of the top level `celery_`
settings have been moved into a new `task_` prefix.

::: warning
::: title
Warning
:::

Celery will still be able to read old configuration files until Celery
6.0. Afterwards, support for the old configuration files will be
removed. We provide the `celery upgrade` command that should handle
plenty of cases (including
`Django <latentcall-django-admonition>`{.interpreted-text role="ref"}).

Please migrate to the new configuration scheme as soon as possible.
:::

  **Setting name**                                           **Replace with**
  ---------------------------------------------------------- ----------------------------------------------------------------------------
  `CELERY_ACCEPT_CONTENT`                                    `accept_content`{.interpreted-text role="setting"}
  `CELERY_ENABLE_UTC`                                        `enable_utc`{.interpreted-text role="setting"}
  `CELERY_IMPORTS`                                           `imports`{.interpreted-text role="setting"}
  `CELERY_INCLUDE`                                           `include`{.interpreted-text role="setting"}
  `CELERY_TIMEZONE`                                          `timezone`{.interpreted-text role="setting"}
  `CELERYBEAT_MAX_LOOP_INTERVAL`                             `beat_max_loop_interval`{.interpreted-text role="setting"}
  `CELERYBEAT_SCHEDULE`                                      `beat_schedule`{.interpreted-text role="setting"}
  `CELERYBEAT_SCHEDULER`                                     `beat_scheduler`{.interpreted-text role="setting"}
  `CELERYBEAT_SCHEDULE_FILENAME`                             `beat_schedule_filename`{.interpreted-text role="setting"}
  `CELERYBEAT_SYNC_EVERY`                                    `beat_sync_every`{.interpreted-text role="setting"}
  `BROKER_URL`                                               `broker_url`{.interpreted-text role="setting"}
  `BROKER_TRANSPORT`                                         `broker_transport`{.interpreted-text role="setting"}
  `BROKER_TRANSPORT_OPTIONS`                                 `broker_transport_options`{.interpreted-text role="setting"}
  `BROKER_CONNECTION_TIMEOUT`                                `broker_connection_timeout`{.interpreted-text role="setting"}
  `BROKER_CONNECTION_RETRY`                                  `broker_connection_retry`{.interpreted-text role="setting"}
  `BROKER_CONNECTION_MAX_RETRIES`                            `broker_connection_max_retries`{.interpreted-text role="setting"}
  `BROKER_FAILOVER_STRATEGY`                                 `broker_failover_strategy`{.interpreted-text role="setting"}
  `BROKER_HEARTBEAT`                                         `broker_heartbeat`{.interpreted-text role="setting"}
  `BROKER_LOGIN_METHOD`                                      `broker_login_method`{.interpreted-text role="setting"}
  \`\`BROKER_NATIVE_DELAYED_DELIVERY_QUEUE_TYPE              \`[ :setting:\`broker_native_delayed_delivery_queue_type]{.title-ref}
  `BROKER_POOL_LIMIT`                                        `broker_pool_limit`{.interpreted-text role="setting"}
  `BROKER_USE_SSL`                                           `broker_use_ssl`{.interpreted-text role="setting"}
  `CELERY_CACHE_BACKEND`                                     `cache_backend`{.interpreted-text role="setting"}
  `CELERY_CACHE_BACKEND_OPTIONS`                             `cache_backend_options`{.interpreted-text role="setting"}
  `CASSANDRA_COLUMN_FAMILY`                                  `cassandra_table`{.interpreted-text role="setting"}
  `CASSANDRA_ENTRY_TTL`                                      `cassandra_entry_ttl`{.interpreted-text role="setting"}
  `CASSANDRA_KEYSPACE`                                       `cassandra_keyspace`{.interpreted-text role="setting"}
  `CASSANDRA_PORT`                                           `cassandra_port`{.interpreted-text role="setting"}
  `CASSANDRA_READ_CONSISTENCY`                               `cassandra_read_consistency`{.interpreted-text role="setting"}
  `CASSANDRA_SERVERS`                                        `cassandra_servers`{.interpreted-text role="setting"}
  `CASSANDRA_WRITE_CONSISTENCY`                              `cassandra_write_consistency`{.interpreted-text role="setting"}
  `CASSANDRA_OPTIONS`                                        `cassandra_options`{.interpreted-text role="setting"}
  `S3_ACCESS_KEY_ID`                                         `s3_access_key_id`{.interpreted-text role="setting"}
  `S3_SECRET_ACCESS_KEY`                                     `s3_secret_access_key`{.interpreted-text role="setting"}
  `S3_BUCKET`                                                `s3_bucket`{.interpreted-text role="setting"}
  `S3_BASE_PATH`                                             `s3_base_path`{.interpreted-text role="setting"}
  `S3_ENDPOINT_URL`                                          `s3_endpoint_url`{.interpreted-text role="setting"}
  `S3_REGION`                                                `s3_region`{.interpreted-text role="setting"}
  `CELERY_COUCHBASE_BACKEND_SETTINGS`                        `couchbase_backend_settings`{.interpreted-text role="setting"}
  `CELERY_ARANGODB_BACKEND_SETTINGS`                         `arangodb_backend_settings`{.interpreted-text role="setting"}
  `CELERY_MONGODB_BACKEND_SETTINGS`                          `mongodb_backend_settings`{.interpreted-text role="setting"}
  `CELERY_EVENT_QUEUE_EXPIRES`                               `event_queue_expires`{.interpreted-text role="setting"}
  `CELERY_EVENT_QUEUE_TTL`                                   `event_queue_ttl`{.interpreted-text role="setting"}
  `CELERY_EVENT_QUEUE_DURABLE`                               `event_queue_durable`{.interpreted-text role="setting"}
  `CELERY_EVENT_QUEUE_EXCLUSIVE`                             `event_queue_exclusive`{.interpreted-text role="setting"}
  `CELERY_EVENT_QUEUE_PREFIX`                                `event_queue_prefix`{.interpreted-text role="setting"}
  `CELERY_EVENT_SERIALIZER`                                  `event_serializer`{.interpreted-text role="setting"}
  `CELERY_REDIS_DB`                                          `redis_db`{.interpreted-text role="setting"}
  `CELERY_REDIS_HOST`                                        `redis_host`{.interpreted-text role="setting"}
  `CELERY_REDIS_MAX_CONNECTIONS`                             `redis_max_connections`{.interpreted-text role="setting"}
  `CELERY_REDIS_USERNAME`                                    `redis_username`{.interpreted-text role="setting"}
  `CELERY_REDIS_PASSWORD`                                    `redis_password`{.interpreted-text role="setting"}
  `CELERY_REDIS_PORT`                                        `redis_port`{.interpreted-text role="setting"}
  `CELERY_REDIS_BACKEND_USE_SSL`                             `redis_backend_use_ssl`{.interpreted-text role="setting"}
  [\`CELERY_REDIS_BACKEND_CREDENTIAL_PROVIDER]{.title-ref}   [ :setting:\`redis_backend_credential_provider]{.title-ref}
  `CELERY_RESULT_BACKEND`                                    `result_backend`{.interpreted-text role="setting"}
  `CELERY_MAX_CACHED_RESULTS`                                `result_cache_max`{.interpreted-text role="setting"}
  `CELERY_MESSAGE_COMPRESSION`                               `result_compression`{.interpreted-text role="setting"}
  `CELERY_RESULT_EXCHANGE`                                   `result_exchange`{.interpreted-text role="setting"}
  `CELERY_RESULT_EXCHANGE_TYPE`                              `result_exchange_type`{.interpreted-text role="setting"}
  `CELERY_RESULT_EXPIRES`                                    `result_expires`{.interpreted-text role="setting"}
  `CELERY_RESULT_PERSISTENT`                                 `result_persistent`{.interpreted-text role="setting"}
  `CELERY_RESULT_SERIALIZER`                                 `result_serializer`{.interpreted-text role="setting"}
  `CELERY_RESULT_DBURI`                                      Use `result_backend`{.interpreted-text role="setting"} instead.
  `CELERY_RESULT_ENGINE_OPTIONS`                             `database_engine_options`{.interpreted-text role="setting"}
  `[...]_DB_SHORT_LIVED_SESSIONS`                            `database_short_lived_sessions`{.interpreted-text role="setting"}
  `CELERY_RESULT_DB_TABLE_NAMES`                             `database_db_names`{.interpreted-text role="setting"}
  `CELERY_SECURITY_CERTIFICATE`                              `security_certificate`{.interpreted-text role="setting"}
  `CELERY_SECURITY_CERT_STORE`                               `security_cert_store`{.interpreted-text role="setting"}
  `CELERY_SECURITY_KEY`                                      `security_key`{.interpreted-text role="setting"}
  `CELERY_SECURITY_KEY_PASSWORD`                             `security_key_password`{.interpreted-text role="setting"}
  `CELERY_ACKS_LATE`                                         `task_acks_late`{.interpreted-text role="setting"}
  `CELERY_ACKS_ON_FAILURE_OR_TIMEOUT`                        `task_acks_on_failure_or_timeout`{.interpreted-text role="setting"}
  `CELERY_TASK_ALWAYS_EAGER`                                 `task_always_eager`{.interpreted-text role="setting"}
  `CELERY_ANNOTATIONS`                                       `task_annotations`{.interpreted-text role="setting"}
  `CELERY_COMPRESSION`                                       `task_compression`{.interpreted-text role="setting"}
  `CELERY_CREATE_MISSING_QUEUES`                             `task_create_missing_queues`{.interpreted-text role="setting"}
  `CELERY_CREATE_MISSING_QUEUE_TYPE`                         `task_create_missing_queue_type`{.interpreted-text role="setting"}
  \`\`CELERY_CREATE_MISSING_QUEUE_EXCHANGE_TYPE              \`[ :setting:\`task_create_missing_queue_exchange_type]{.title-ref}
  `CELERY_DEFAULT_DELIVERY_MODE`                             `task_default_delivery_mode`{.interpreted-text role="setting"}
  `CELERY_DEFAULT_EXCHANGE`                                  `task_default_exchange`{.interpreted-text role="setting"}
  `CELERY_DEFAULT_EXCHANGE_TYPE`                             `task_default_exchange_type`{.interpreted-text role="setting"}
  `CELERY_DEFAULT_QUEUE`                                     `task_default_queue`{.interpreted-text role="setting"}
  `CELERY_DEFAULT_QUEUE_TYPE`                                `task_default_queue_type`{.interpreted-text role="setting"}
  `CELERY_DEFAULT_RATE_LIMIT`                                `task_default_rate_limit`{.interpreted-text role="setting"}
  `CELERY_DEFAULT_ROUTING_KEY`                               `task_default_routing_key`{.interpreted-text role="setting"}
  `CELERY_EAGER_PROPAGATES`                                  `task_eager_propagates`{.interpreted-text role="setting"}
  `CELERY_IGNORE_RESULT`                                     `task_ignore_result`{.interpreted-text role="setting"}
  `CELERY_PUBLISH_RETRY`                                     `task_publish_retry`{.interpreted-text role="setting"}
  `CELERY_PUBLISH_RETRY_POLICY`                              `task_publish_retry_policy`{.interpreted-text role="setting"}
  `CELERY_QUEUES`                                            `task_queues`{.interpreted-text role="setting"}
  `CELERY_ROUTES`                                            `task_routes`{.interpreted-text role="setting"}
  `CELERY_SEND_SENT_EVENT`                                   `task_send_sent_event`{.interpreted-text role="setting"}
  `CELERY_TASK_SERIALIZER`                                   `task_serializer`{.interpreted-text role="setting"}
  `CELERYD_SOFT_TIME_LIMIT`                                  `task_soft_time_limit`{.interpreted-text role="setting"}
  `CELERY_TASK_TRACK_STARTED`                                `task_track_started`{.interpreted-text role="setting"}
  `CELERY_TASK_REJECT_ON_WORKER_LOST`                        `task_reject_on_worker_lost`{.interpreted-text role="setting"}
  `CELERYD_TIME_LIMIT`                                       `task_time_limit`{.interpreted-text role="setting"}
  `CELERY_ALLOW_ERROR_CB_ON_CHORD_HEADER`                    `task_allow_error_cb_on_chord_header`{.interpreted-text role="setting"}
  `CELERYD_AGENT`                                            `worker_agent`{.interpreted-text role="setting"}
  `CELERYD_AUTOSCALER`                                       `worker_autoscaler`{.interpreted-text role="setting"}
  `CELERYD_CONCURRENCY`                                      `worker_concurrency`{.interpreted-text role="setting"}
  `CELERYD_CONSUMER`                                         `worker_consumer`{.interpreted-text role="setting"}
  `CELERY_WORKER_DIRECT`                                     `worker_direct`{.interpreted-text role="setting"}
  `CELERY_DISABLE_RATE_LIMITS`                               `worker_disable_rate_limits`{.interpreted-text role="setting"}
  `CELERY_ENABLE_REMOTE_CONTROL`                             `worker_enable_remote_control`{.interpreted-text role="setting"}
  `CELERYD_HIJACK_ROOT_LOGGER`                               `worker_hijack_root_logger`{.interpreted-text role="setting"}
  `CELERYD_LOG_COLOR`                                        `worker_log_color`{.interpreted-text role="setting"}
  `CELERY_WORKER_LOG_FORMAT`                                 `worker_log_format`{.interpreted-text role="setting"}
  `CELERYD_WORKER_LOST_WAIT`                                 `worker_lost_wait`{.interpreted-text role="setting"}
  `CELERYD_MAX_TASKS_PER_CHILD`                              `worker_max_tasks_per_child`{.interpreted-text role="setting"}
  `CELERYD_POOL`                                             `worker_pool`{.interpreted-text role="setting"}
  `CELERYD_POOL_PUTLOCKS`                                    `worker_pool_putlocks`{.interpreted-text role="setting"}
  `CELERYD_POOL_RESTARTS`                                    `worker_pool_restarts`{.interpreted-text role="setting"}
  `CELERYD_PREFETCH_MULTIPLIER`                              `worker_prefetch_multiplier`{.interpreted-text role="setting"}
  `CELERYD_ETA_TASK_LIMIT`                                   `worker_eta_task_limit`{.interpreted-text role="setting"}
  `CELERYD_ENABLE_PREFETCH_COUNT_REDUCTION`                  `worker_enable_prefetch_count_reduction`{.interpreted-text role="setting"}
  `CELERYD_REDIRECT_STDOUTS`                                 `worker_redirect_stdouts`{.interpreted-text role="setting"}
  `CELERYD_REDIRECT_STDOUTS_LEVEL`                           `worker_redirect_stdouts_level`{.interpreted-text role="setting"}
  `CELERY_SEND_EVENTS`                                       `worker_send_task_events`{.interpreted-text role="setting"}
  `CELERYD_STATE_DB`                                         `worker_state_db`{.interpreted-text role="setting"}
  `CELERY_WORKER_TASK_LOG_FORMAT`                            `worker_task_log_format`{.interpreted-text role="setting"}
  `CELERYD_TIMER`                                            `worker_timer`{.interpreted-text role="setting"}
  `CELERYD_TIMER_PRECISION`                                  `worker_timer_precision`{.interpreted-text role="setting"}
  `CELERYD_DETECT_QUORUM_QUEUES`                             `worker_detect_quorum_queues`{.interpreted-text role="setting"}

## Configuration Directives

### General settings {#conf-datetime}

::: setting
accept_content
:::

#### `accept_content`

Default: `{'json'}` (set, list, or tuple).

A white-list of content-types/serializers to allow.

If a message is received that\'s not in this list then the message will
be discarded with an error.

By default only json is enabled but any content type can be added,
including pickle and yaml; when this is the case make sure untrusted
parties don\'t have access to your broker. See
`guide-security`{.interpreted-text role="ref"} for more.

Example:

    # using serializer name
    accept_content = ['json']

    # or the actual content-type (MIME)
    accept_content = ['application/json']

::: setting
result_accept_content
:::

#### `result_accept_content`

Default: `None` (can be set, list or tuple).

::: versionadded
4.3
:::

A white-list of content-types/serializers to allow for the result
backend.

If a message is received that\'s not in this list then the message will
be discarded with an error.

By default it is the same serializer as `accept_content`. However, a
different serializer for accepted content of the result backend can be
specified. Usually this is needed if signed messaging is used and the
result is stored unsigned in the result backend. See
`guide-security`{.interpreted-text role="ref"} for more.

Example:

    # using serializer name
    result_accept_content = ['json']

    # or the actual content-type (MIME)
    result_accept_content = ['application/json']

### Time and date settings

::: setting
enable_utc
:::

#### `enable_utc`

::: versionadded
2.5
:::

Default: Enabled by default since version 3.0.

If enabled dates and times in messages will be converted to use the UTC
timezone.

Note that workers running Celery versions below 2.5 will assume a local
timezone for all messages, so only enable if all workers have been
upgraded.

::: setting
timezone
:::

#### `timezone`

::: versionadded
2.5
:::

Default: `"UTC"`.

Configure Celery to use a custom time zone. The timezone value can be
any time zone supported by the
[ZoneInfo](https://docs.python.org/3/library/zoneinfo.html) library.

If not set the UTC timezone is used. For backwards compatibility
there\'s also a `enable_utc`{.interpreted-text role="setting"} setting,
and when this is set to false the system local timezone is used instead.

### Task settings {#conf-tasks}

::: setting
task_annotations
:::

#### `task_annotations`

::: versionadded
2.5
:::

Default: `None`{.interpreted-text role="const"}.

This setting can be used to rewrite any task attribute from the
configuration. The setting can be a dict, or a list of annotation
objects that filter for tasks and return a map of attributes to change.

This will change the `rate_limit` attribute for the `tasks.add` task:

``` python
task_annotations = {'tasks.add': {'rate_limit': '10/s'}}
```

or change the same for all tasks:

``` python
task_annotations = {'*': {'rate_limit': '10/s'}}
```

You can change methods too, for example the `on_failure` handler:

``` python
def my_on_failure(self, exc, task_id, args, kwargs, einfo):
    print('Oh no! Task failed: {0!r}'.format(exc))

task_annotations = {'*': {'on_failure': my_on_failure}}
```

If you need more flexibility then you can use objects instead of a dict
to choose the tasks to annotate:

``` python
class MyAnnotate:

    def annotate(self, task):
        if task.name.startswith('tasks.'):
            return {'rate_limit': '10/s'}

task_annotations = (MyAnnotate(), {other,})
```

::: setting
task_compression
:::

#### `task_compression`

Default: `None`{.interpreted-text role="const"}

Default compression used for task messages. Can be `gzip`, `bzip2` (if
available), or any custom compression schemes registered in the Kombu
compression registry.

The default is to send uncompressed messages.

::: setting
task_protocol
:::

#### `task_protocol`

Default: 2 (since 4.0).

Set the default task message protocol version used to send tasks.
Supports protocols: 1 and 2.

Protocol 2 is supported by 3.1.24 and 4.x+.

::: setting
task_serializer
:::

#### `task_serializer`

Default: `"json"` (since 4.0, earlier: pickle).

A string identifying the default serialization method to use. Can be
[json]{.title-ref} (default), [pickle]{.title-ref}, [yaml]{.title-ref},
[msgpack]{.title-ref}, or any custom serialization methods that have
been registered with `kombu.serialization.registry`{.interpreted-text
role="mod"}.

::: seealso
`calling-serializers`{.interpreted-text role="ref"}.
:::

::: setting
task_publish_retry
:::

#### `task_publish_retry`

::: versionadded
2.2
:::

Default: Enabled.

Decides if publishing task messages will be retried in the case of
connection loss or other connection errors. See also
`task_publish_retry_policy`{.interpreted-text role="setting"}.

::: setting
task_publish_retry_policy
:::

#### `task_publish_retry_policy`

::: versionadded
2.2
:::

Default: See `calling-retry`{.interpreted-text role="ref"}.

Defines the default policy when retrying publishing a task message in
the case of connection loss or other connection errors.

### Task execution settings {#conf-task-execution}

::: setting
task_always_eager
:::

#### `task_always_eager`

Default: Disabled.

If this is `True`{.interpreted-text role="const"}, all tasks will be
executed locally by blocking until the task returns. `apply_async()` and
`Task.delay()` will return an
`~celery.result.EagerResult`{.interpreted-text role="class"} instance,
that emulates the API and behavior of
`~celery.result.AsyncResult`{.interpreted-text role="class"}, except the
result is already evaluated.

That is, tasks will be executed locally instead of being sent to the
queue.

::: setting
task_eager_propagates
:::

#### `task_eager_propagates`

Default: Disabled.

If this is `True`{.interpreted-text role="const"}, eagerly executed
tasks (applied by [task.apply()]{.title-ref}, or when the
`task_always_eager`{.interpreted-text role="setting"} setting is
enabled), will propagate exceptions.

It\'s the same as always running `apply()` with `throw=True`.

::: setting
task_store_eager_result
:::

#### `task_store_eager_result`

::: versionadded
5.1
:::

Default: Disabled.

If this is `True`{.interpreted-text role="const"} and
`task_always_eager`{.interpreted-text role="setting"} is
`True`{.interpreted-text role="const"} and
`task_ignore_result`{.interpreted-text role="setting"} is
`False`{.interpreted-text role="const"}, the results of eagerly executed
tasks will be saved to the backend.

By default, even with `task_always_eager`{.interpreted-text
role="setting"} set to `True`{.interpreted-text role="const"} and
`task_ignore_result`{.interpreted-text role="setting"} set to
`False`{.interpreted-text role="const"}, the result will not be saved.

::: setting
task_remote_tracebacks
:::

#### `task_remote_tracebacks`

Default: Disabled.

If enabled task results will include the workers stack when re-raising
task errors.

This requires the `tblib`{.interpreted-text role="pypi"} library, that
can be installed using `pip`{.interpreted-text role="command"}:

``` console
$ pip install celery[tblib]
```

See `bundles`{.interpreted-text role="ref"} for information on combining
multiple extension requirements.

::: setting
task_ignore_result
:::

#### `task_ignore_result`

Default: Disabled.

Whether to store the task return values or not (tombstones). If you
still want to store errors, just not successful return values, you can
set `task_store_errors_even_if_ignored`{.interpreted-text
role="setting"}.

::: setting
task_store_errors_even_if_ignored
:::

#### `task_store_errors_even_if_ignored`

Default: Disabled.

If set, the worker stores all task errors in the result store even if
`Task.ignore_result <celery.app.task.Task.ignore_result>`{.interpreted-text
role="attr"} is on.

::: setting
task_track_started
:::

#### `task_track_started`

Default: Disabled.

If `True`{.interpreted-text role="const"} the task will report its
status as \'started\' when the task is executed by a worker. The default
value is `False`{.interpreted-text role="const"} as the normal behavior
is to not report that level of granularity. Tasks are either pending,
finished, or waiting to be retried. Having a \'started\' state can be
useful for when there are long running tasks and there\'s a need to
report what task is currently running.

::: setting
task_time_limit
:::

#### `task_time_limit`

Default: No time limit.

Task hard time limit in seconds. The worker processing the task will be
killed and replaced with a new one when this is exceeded.

::: setting
task_allow_error_cb_on_chord_header
:::

#### `task_allow_error_cb_on_chord_header`

::: versionadded
5.3
:::

Default: Disabled.

Enabling this flag will allow linking an error callback to a chord
header, which by default will not link when using `link_error()`, and
preventing from the chord\'s body to execute if any of the tasks in the
header fails.

Consider the following canvas with the flag disabled (default behavior):

``` python
header = group([t1, t2])
body = t3
c = chord(header, body)
c.link_error(error_callback_sig)
```

If *any* of the header tasks failed (`t1` or `t2`), by default, the
chord body (`t3`) would **not execute**, and `error_callback_sig` will
be called **once** (for the body).

Enabling this flag will change the above behavior by:

1.  `error_callback_sig` will be linked to `t1` and `t2` (as well as
    `t3`).
2.  If *any* of the header tasks failed, `error_callback_sig` will be
    called **for each** failed header task **and** the `body` (even if
    the body didn\'t run).

Consider now the following canvas with the flag enabled:

``` python
header = group([failingT1, failingT2])
body = t3
c = chord(header, body)
c.link_error(error_callback_sig)
```

If *all* of the header tasks failed (`failingT1` and `failingT2`), then
the chord body (`t3`) would **not execute**, and `error_callback_sig`
will be called **3 times** (two times for the header and one time for
the body).

Lastly, consider the following canvas with the flag enabled:

``` python
header = group([failingT1, failingT2])
body = t3
upgraded_chord = chain(header, body)
upgraded_chord.link_error(error_callback_sig)
```

This canvas will behave exactly the same as the previous one, since the
`chain` will be upgraded to a `chord` internally.

::: setting
task_soft_time_limit
:::

#### `task_soft_time_limit`

Default: No soft time limit.

Task soft time limit in seconds.

The `~@SoftTimeLimitExceeded`{.interpreted-text role="exc"} exception
will be raised when this is exceeded. For example, the task can catch
this to clean up before the hard time limit comes:

``` python
from celery.exceptions import SoftTimeLimitExceeded

@app.task
def mytask():
    try:
        return do_work()
    except SoftTimeLimitExceeded:
        cleanup_in_a_hurry()
```

::: setting
task_acks_late
:::

#### `task_acks_late`

Default: Disabled.

Late ack means the task messages will be acknowledged **after** the task
has been executed, not *right before* (the default behavior).

::: seealso
FAQ: `faq-acks_late-vs-retry`{.interpreted-text role="ref"}.
:::

::: setting
task_acks_on_failure_or_timeout
:::

#### `task_acks_on_failure_or_timeout`

Default: Enabled

When enabled messages for all tasks will be acknowledged even if they
fail or time out.

Configuring this setting only applies to tasks that are acknowledged
**after** they have been executed and only if
`task_acks_late`{.interpreted-text role="setting"} is enabled.

::: setting
task_reject_on_worker_lost
:::

#### `task_reject_on_worker_lost`

Default: Disabled.

Even if `task_acks_late`{.interpreted-text role="setting"} is enabled,
the worker will acknowledge tasks when the worker process executing them
abruptly exits or is signaled (e.g., `KILL`{.interpreted-text
role="sig"}/`INT`{.interpreted-text role="sig"}, etc).

Setting this to true allows the message to be re-queued instead, so that
the task will execute again by the same worker, or another worker.

::: warning
::: title
Warning
:::

Enabling this can cause message loops; make sure you know what you\'re
doing.
:::

::: setting
task_default_rate_limit
:::

#### `task_default_rate_limit`

Default: No rate limit.

The global default rate limit for tasks.

This value is used for tasks that doesn\'t have a custom rate limit

::: seealso
The `worker_disable_rate_limits`{.interpreted-text role="setting"}
setting can disable all rate limits.
:::

### Task result backend settings {#conf-result-backend}

::: setting
result_backend
:::

#### `result_backend`

Default: No result backend enabled by default.

The backend used to store task results (tombstones). Can be one of the
following:

-   

    `rpc`

    :   Send results back as AMQP messages See
        `conf-rpc-result-backend`{.interpreted-text role="ref"}.

-   

    `database`

    :   Use a relational database supported by
        [SQLAlchemy](http://sqlalchemy.org). See
        `conf-database-result-backend`{.interpreted-text role="ref"}.

-   

    `redis`

    :   Use [Redis](#redis) to store the results. See
        `conf-redis-result-backend`{.interpreted-text role="ref"}.

-   

    `cache`

    :   Use [Memcached](http://memcached.org) to store the results. See
        `conf-cache-result-backend`{.interpreted-text role="ref"}.

-   

    `mongodb`

    :   Use [MongoDB](http://mongodb.org) to store the results. See
        `conf-mongodb-result-backend`{.interpreted-text role="ref"}.

-   

    `cassandra`

    :   Use [Cassandra](http://cassandra.apache.org/) to store the
        results. See `conf-cassandra-result-backend`{.interpreted-text
        role="ref"}.

-   

    `elasticsearch`

    :   Use
        [Elasticsearch](https://aws.amazon.com/elasticsearch-service/)
        to store the results. See
        `conf-elasticsearch-result-backend`{.interpreted-text
        role="ref"}.

-   

    `ironcache`

    :   Use [IronCache](http://www.iron.io/cache) to store the results.
        See `conf-ironcache-result-backend`{.interpreted-text
        role="ref"}.

-   

    `couchbase`

    :   Use [Couchbase](https://www.couchbase.com/) to store the
        results. See `conf-couchbase-result-backend`{.interpreted-text
        role="ref"}.

-   

    `arangodb`

    :   Use [ArangoDB](https://www.arangodb.com/) to store the results.
        See `conf-arangodb-result-backend`{.interpreted-text
        role="ref"}.

-   

    `couchdb`

    :   Use [CouchDB](http://www.couchdb.com/) to store the results. See
        `conf-couchdb-result-backend`{.interpreted-text role="ref"}.

-   

    `cosmosdbsql (experimental)`

    :   Use the
        [CosmosDB](https://azure.microsoft.com/en-us/services/cosmos-db/)
        PaaS to store the results. See
        `conf-cosmosdbsql-result-backend`{.interpreted-text role="ref"}.

-   

    `filesystem`

    :   Use a shared directory to store the results. See
        `conf-filesystem-result-backend`{.interpreted-text role="ref"}.

-   

    `consul`

    :   Use the [Consul](https://consul.io/) K/V store to store the
        results See `conf-consul-result-backend`{.interpreted-text
        role="ref"}.

-   

    `azureblockblob`

    :   Use the
        [AzureBlockBlob](https://azure.microsoft.com/en-us/services/storage/blobs/)
        PaaS store to store the results See
        `conf-azureblockblob-result-backend`{.interpreted-text
        role="ref"}.

-   

    `s3`

    :   Use the [S3](https://aws.amazon.com/s3/) to store the results
        See `conf-s3-result-backend`{.interpreted-text role="ref"}.

-   

    `gcs`

    :   Use the [GCS](https://cloud.google.com/storage/) to store the
        results See `conf-gcs-result-backend`{.interpreted-text
        role="ref"}.

> While the AMQP result backend is very efficient, you must make sure
> you only receive the same result once. See
> `userguide/calling`{.interpreted-text role="doc"}).

::: setting
result_backend_always_retry
:::

#### `result_backend_always_retry`

Default: `False`{.interpreted-text role="const"}

If enable, backend will try to retry on the event of recoverable
exceptions instead of propagating the exception. It will use an
exponential backoff sleep time between 2 retries.

::: setting
result_backend_max_sleep_between_retries_ms
:::

#### `result_backend_max_sleep_between_retries_ms`

Default: 10000

This specifies the maximum sleep time between two backend operation
retry.

::: setting
result_backend_base_sleep_between_retries_ms
:::

#### `result_backend_base_sleep_between_retries_ms`

Default: 10

This specifies the base amount of sleep time between two backend
operation retry.

::: setting
result_backend_max_retries
:::

#### `result_backend_max_retries`

Default: Inf

This is the maximum of retries in case of recoverable exceptions.

::: setting
result_backend_thread_safe
:::

#### `result_backend_thread_safe`

Default: False

If True, then the backend object is shared across threads. This may be
useful for using a shared connection pool instead of creating a
connection for every thread.

::: setting
result_backend_transport_options
:::

#### `result_backend_transport_options`

Default: `{}` (empty mapping).

A dict of additional options passed to the underlying transport.

See your transport user manual for supported options (if any).

Example setting the visibility timeout (supported by Redis and SQS
transports):

``` python
result_backend_transport_options = {'visibility_timeout': 18000}  # 5 hours
```

::: setting
result_serializer
:::

#### `result_serializer`

Default: `json` since 4.0 (earlier: pickle).

Result serialization format.

See `calling-serializers`{.interpreted-text role="ref"} for information
about supported serialization formats.

::: setting
result_compression
:::

#### `result_compression`

Default: No compression.

Optional compression method used for task results. Supports the same
options as the `task_compression`{.interpreted-text role="setting"}
setting.

::: setting
result_extended
:::

#### `result_extended`

Default: `False`

Enables extended task result attributes (name, args, kwargs, worker,
retries, queue, delivery_info) to be written to backend.

::: setting
result_expires
:::

#### `result_expires`

Default: Expire after 1 day.

Time (in seconds, or a `~datetime.timedelta`{.interpreted-text
role="class"} object) for when after stored task tombstones will be
deleted.

A built-in periodic task will delete the results after this time
(`celery.backend_cleanup`), assuming that `celery beat` is enabled. The
task runs daily at 4am.

A value of `None`{.interpreted-text role="const"} or 0 means results
will never expire (depending on backend specifications).

::: note
::: title
Note
:::

For the moment this only works with the AMQP, database, cache,
Couchbase, filesystem and Redis backends.

When using the database or filesystem backend, `celery beat` must be
running for the results to be expired.
:::

::: setting
result_cache_max
:::

#### `result_cache_max`

Default: Disabled by default.

Enables client caching of results.

This can be useful for the old deprecated \'amqp\' backend where the
result is unavailable as soon as one result instance consumes it.

This is the total number of results to cache before older results are
evicted. A value of 0 or None means no limit, and a value of
`-1`{.interpreted-text role="const"} will disable the cache.

Disabled by default.

::: setting
result_chord_join_timeout
:::

#### `result_chord_join_timeout`

Default: 3.0.

The timeout in seconds (int/float) when joining a group\'s results
within a chord.

::: setting
result_chord_retry_interval
:::

#### `result_chord_retry_interval`

Default: 1.0.

Default interval for retrying chord tasks.

::: setting
override_backends
:::

#### `override_backends`

Default: Disabled by default.

Path to class that implements backend.

Allows to override backend implementation. This can be useful if you
need to store additional metadata about executed tasks, override retry
policies, etc.

Example:

``` python
override_backends = {"db": "custom_module.backend.class"}
```

### Database backend settings {#conf-database-result-backend}

#### Database URL Examples

To use the database backend you have to configure the
`result_backend`{.interpreted-text role="setting"} setting with a
connection URL and the `db+` prefix:

``` python
result_backend = 'db+scheme://user:password@host:port/dbname'
```

Examples:

    # sqlite (filename)
    result_backend = 'db+sqlite:///results.sqlite'

    # mysql
    result_backend = 'db+mysql://scott:tiger@localhost/foo'

    # postgresql
    result_backend = 'db+postgresql://scott:tiger@localhost/mydatabase'

    # oracle
    result_backend = 'db+oracle://scott:tiger@127.0.0.1:1521/sidname'

``` python
```

Please see [Supported
Databases](http://www.sqlalchemy.org/docs/core/engines.html#supported-databases)
for a table of supported databases, and [Connection
String](http://www.sqlalchemy.org/docs/core/engines.html#database-urls)
for more information about connection strings (this is the part of the
URI that comes after the `db+` prefix).

::: setting
database_create_tables_at_setup
:::

#### `database_create_tables_at_setup`

::: versionadded
5.5.0
:::

Default: True by default.

-   If [True]{.title-ref}, Celery will create the tables in the database
    during setup.
-   If [False]{.title-ref}, Celery will create the tables lazily, i.e.
    wait for the first task to be executed before creating the tables.

::: note
::: title
Note
:::

Before celery 5.5, the tables were created lazily i.e. it was equivalent
to [database_create_tables_at_setup]{.title-ref} set to False.
:::

::: setting
database_engine_options
:::

#### `database_engine_options`

Default: `{}` (empty mapping).

To specify additional SQLAlchemy database engine options you can use the
`database_engine_options`{.interpreted-text role="setting"} setting:

    # echo enables verbose logging from SQLAlchemy.
    app.conf.database_engine_options = {'echo': True}

::: setting
database_short_lived_sessions
:::

#### `database_short_lived_sessions`

Default: Disabled by default.

Short lived sessions are disabled by default. If enabled they can
drastically reduce performance, especially on systems processing lots of
tasks. This option is useful on low-traffic workers that experience
errors as a result of cached database connections going stale through
inactivity. For example, intermittent errors like [(OperationalError)
(2006, \'MySQL server has gone away\')]{.title-ref} can be fixed by
enabling short lived sessions. This option only affects the database
backend.

::: setting
database_table_schemas
:::

#### `database_table_schemas`

Default: `{}` (empty mapping).

When SQLAlchemy is configured as the result backend, Celery
automatically creates two tables to store result meta-data for tasks.
This setting allows you to customize the schema of the tables:

``` python
# use custom schema for the database result backend.
database_table_schemas = {
    'task': 'celery',
    'group': 'celery',
}
```

::: setting
database_table_names
:::

#### `database_table_names`

Default: `{}` (empty mapping).

When SQLAlchemy is configured as the result backend, Celery
automatically creates two tables to store result meta-data for tasks.
This setting allows you to customize the table names:

``` python
# use custom table names for the database result backend.
database_table_names = {
    'task': 'myapp_taskmeta',
    'group': 'myapp_groupmeta',
}
```

### RPC backend settings {#conf-rpc-result-backend}

::: setting
result_persistent
:::

#### `result_persistent`

Default: Disabled by default (transient messages).

If set to `True`{.interpreted-text role="const"}, result messages will
be persistent. This means the messages won\'t be lost after a broker
restart.

#### Example configuration

``` python
result_backend = 'rpc://'
result_persistent = False
```

**Please note**: using this backend could trigger the raise of
`celery.backends.rpc.BacklogLimitExceeded` if the task tombstone is too
*old*.

E.g.

``` python
for i in range(10000):
    r = debug_task.delay()

print(r.state)  # this would raise celery.backends.rpc.BacklogLimitExceeded
```

### Cache backend settings {#conf-cache-result-backend}

::: note
::: title
Note
:::

The cache backend supports the `pylibmc`{.interpreted-text role="pypi"}
and `python-memcached`{.interpreted-text role="pypi"} libraries. The
latter is used only if `pylibmc`{.interpreted-text role="pypi"} isn\'t
installed.
:::

Using a single Memcached server:

``` python
result_backend = 'cache+memcached://127.0.0.1:11211/'
```

Using multiple Memcached servers:

``` python
result_backend = """
    cache+memcached://172.19.26.240:11211;172.19.26.242:11211/
""".strip()
```

The \"memory\" backend stores the cache in memory only:

``` python
result_backend = 'cache'
cache_backend = 'memory'
```

::: setting
cache_backend_options
:::

#### `cache_backend_options`

Default: `{}` (empty mapping).

You can set `pylibmc`{.interpreted-text role="pypi"} options using the
`cache_backend_options`{.interpreted-text role="setting"} setting:

``` python
cache_backend_options = {
    'binary': True,
    'behaviors': {'tcp_nodelay': True},
}
```

::: setting
cache_backend
:::

#### `cache_backend`

This setting is no longer used in celery\'s builtin backends as it\'s
now possible to specify the cache backend directly in the
`result_backend`{.interpreted-text role="setting"} setting.

::: note
::: title
Note
:::

The `django-celery-results`{.interpreted-text role="ref"} library uses
`cache_backend` for choosing django caches.
:::

### MongoDB backend settings {#conf-mongodb-result-backend}

::: note
::: title
Note
:::

The MongoDB backend requires the `pymongo`{.interpreted-text role="mod"}
library: <http://github.com/mongodb/mongo-python-driver/tree/master>
:::

::: setting
mongodb_backend_settings
:::

#### mongodb_backend_settings

This is a dict supporting the following keys:

-   

    database

    :   The database name to connect to. Defaults to `celery`.

-   

    taskmeta_collection

    :   The collection name to store task meta data. Defaults to
        `celery_taskmeta`.

-   

    max_pool_size

    :   Passed as max_pool_size to PyMongo\'s Connection or MongoClient
        constructor. It is the maximum number of TCP connections to keep
        open to MongoDB at a given time. If there are more open
        connections than max_pool_size, sockets will be closed when they
        are released. Defaults to 10.

-   options

    > Additional keyword arguments to pass to the mongodb connection
    > constructor. See the `pymongo`{.interpreted-text role="mod"} docs
    > to see a list of arguments supported.

::: note
::: title
Note
:::

With pymongo\>=4.14, options are case-sensitive when they were
previously case-insensitive. See
`~pymongo.mongo_client.MongoClient`{.interpreted-text role="class"} to
determine the correct case.
:::

#### Example configuration {#example-mongodb-result-config}

``` python
result_backend = 'mongodb://localhost:27017/'
mongodb_backend_settings = {
    'database': 'mydb',
    'taskmeta_collection': 'my_taskmeta_collection',
}
```

### Redis backend settings {#conf-redis-result-backend}

#### Configuring the backend URL

::: note
::: title
Note
:::

The Redis backend requires the `redis`{.interpreted-text role="pypi"}
library.

To install this package use `pip`{.interpreted-text role="command"}:

``` console
$ pip install celery[redis]
```

See `bundles`{.interpreted-text role="ref"} for information on combining
multiple extension requirements.
:::

This backend requires the `result_backend`{.interpreted-text
role="setting"} setting to be set to a Redis or [Redis over
TLS](https://www.iana.org/assignments/uri-schemes/prov/rediss) URL:

    result_backend = 'redis://username:password@host:port/db'

For example:

    result_backend = 'redis://localhost/0'

is the same as:

    result_backend = 'redis://'

Use the `rediss://` protocol to connect to redis over TLS:

    result_backend = 'rediss://username:password@host:port/db?ssl_cert_reqs=required'

Note that the `ssl_cert_reqs` string should be one of `required`,
`optional`, or `none` (though, for backwards compatibility with older
Celery versions, the string may also be one of `CERT_REQUIRED`,
`CERT_OPTIONAL`, `CERT_NONE`, but those values only work for Celery, not
for Redis directly).

If a Unix socket connection should be used, the URL needs to be in the
format::

    result_backend = 'socket:///path/to/redis.sock'

The fields of the URL are defined as follows:

1.  `username`

    > ::: versionadded
    > 5.1.0
    > :::
    >
    > Username used to connect to the database.
    >
    > Note that this is only supported in Redis\>=6.0 and with
    > py-redis\>=3.4.0 installed.
    >
    > If you use an older database version or an older client version
    > you can omit the username:
    >
    >     result_backend = 'redis://:password@host:port/db'

2.  `password`

    > Password used to connect to the database.

3.  `host`

    > Host name or IP address of the Redis server (e.g.,
    > [localhost]{.title-ref}).

4.  `port`

    > Port to the Redis server. Default is 6379.

5.  `db`

    > Database number to use. Default is 0. The db can include an
    > optional leading slash.

When using a TLS connection (protocol is `rediss://`), you may pass in
all values in `broker_use_ssl`{.interpreted-text role="setting"} as
query parameters. Paths to certificates must be URL encoded, and
`ssl_cert_reqs` is required. Example:

``` python
result_backend = 'rediss://:password@host:port/db?\
    ssl_cert_reqs=required\
    &ssl_ca_certs=%2Fvar%2Fssl%2Fmyca.pem\                  # /var/ssl/myca.pem
    &ssl_certfile=%2Fvar%2Fssl%2Fredis-server-cert.pem\     # /var/ssl/redis-server-cert.pem
    &ssl_keyfile=%2Fvar%2Fssl%2Fprivate%2Fworker-key.pem'   # /var/ssl/private/worker-key.pem
```

Note that the `ssl_cert_reqs` string should be one of `required`,
`optional`, or `none` (though, for backwards compatibility, the string
may also be one of `CERT_REQUIRED`, `CERT_OPTIONAL`, `CERT_NONE`).

::: setting
redis_backend_health_check_interval
:::

::: versionadded
5.1.0
:::

#### `redis_backend_health_check_interval`

Default: Not configured

The Redis backend supports health checks. This value must be set as an
integer whose value is the number of seconds between health checks. If a
ConnectionError or a TimeoutError is encountered during the health
check, the connection will be re-established and the command retried
exactly once.

::: setting
redis_backend_use_ssl
:::

#### `redis_backend_use_ssl`

Default: Disabled.

The Redis backend supports SSL. This value must be set in the form of a
dictionary. The valid key-value pairs are the same as the ones mentioned
in the `redis` sub-section under `broker_use_ssl`{.interpreted-text
role="setting"}.

::: setting
redis_backend_credential_provider
:::

::: versionadded
5.6
:::

#### `redis_backend_credential_provider`

Default: Disabled.

The Redis backend supports credential provider. This value must be set
in the form of a class path string or a class instance. e.g.
`mymodule.myfile.myclass` check more details in
[RedisCredentialProvider](https://redis.readthedocs.io/en/stable/examples/connection_examples.html#Connecting-to-a-redis-instance-with-standard-credential-provider)
doc.

::: setting
redis_max_connections
:::

#### `redis_max_connections`

Default: No limit.

Maximum number of connections available in the Redis connection pool
used for sending and retrieving results.

::: warning
::: title
Warning
:::

Redis will raise a [ConnectionError]{.title-ref} if the number of
concurrent connections exceeds the maximum.
:::

::: setting
redis_socket_connect_timeout
:::

#### `redis_socket_connect_timeout`

::: versionadded
4.0.1
:::

Default: `None`{.interpreted-text role="const"}

Socket timeout for connections to Redis from the result backend in
seconds (int/float)

::: setting
redis_socket_timeout
:::

#### `redis_socket_timeout`

Default: 120.0 seconds.

Socket timeout for reading/writing operations to the Redis server in
seconds (int/float), used by the redis result backend.

::: setting
redis_retry_on_timeout
:::

#### `redis_retry_on_timeout`

::: versionadded
4.4.1
:::

Default: `False`{.interpreted-text role="const"}

To retry reading/writing operations on TimeoutError to the Redis server,
used by the redis result backend. Shouldn\'t set this variable if using
Redis connection by unix socket.

::: setting
redis_socket_keepalive
:::

#### `redis_socket_keepalive`

::: versionadded
4.4.1
:::

Default: `False`{.interpreted-text role="const"}

Socket TCP keepalive to keep connections healthy to the Redis server,
used by the redis result backend.

::: setting
redis_client_name
:::

#### `redis_client_name`

::: versionadded
5.6
:::

Default: `None`{.interpreted-text role="const"}

Sets the client name for Redis connections used by the result backend.
This can help identify connections in Redis monitoring tools.

### Cassandra/AstraDB backend settings {#conf-cassandra-result-backend}

::: note
::: title
Note
:::

This Cassandra backend driver requires
`cassandra-driver`{.interpreted-text role="pypi"}.

This backend can refer to either a regular Cassandra installation or a
managed Astra DB instance. Depending on which one, exactly one between
the `cassandra_servers`{.interpreted-text role="setting"} and
`cassandra_secure_bundle_path`{.interpreted-text role="setting"}
settings must be provided (but not both).

To install, use `pip`{.interpreted-text role="command"}:

``` console
$ pip install celery[cassandra]
```

See `bundles`{.interpreted-text role="ref"} for information on combining
multiple extension requirements.
:::

This backend requires the following configuration directives to be set.

::: setting
cassandra_servers
:::

#### `cassandra_servers`

Default: `[]` (empty list).

List of `host` Cassandra servers. This must be provided when connecting
to a Cassandra cluster. Passing this setting is strictly exclusive to
`cassandra_secure_bundle_path`{.interpreted-text role="setting"}.
Example:

    cassandra_servers = ['localhost']

::: setting
cassandra_secure_bundle_path
:::

#### `cassandra_secure_bundle_path`

Default: None.

Absolute path to the secure-connect-bundle zip file to connect to an
Astra DB instance. Passing this setting is strictly exclusive to
`cassandra_servers`{.interpreted-text role="setting"}. Example:

    cassandra_secure_bundle_path = '/home/user/bundles/secure-connect.zip'

When connecting to Astra DB, it is necessary to specify the plain-text
auth provider and the associated username and password, which take the
value of the Client ID and the Client Secret, respectively, of a valid
token generated for the Astra DB instance. See below for an Astra DB
configuration example.

::: setting
cassandra_port
:::

#### `cassandra_port`

Default: 9042.

Port to contact the Cassandra servers on.

::: setting
cassandra_keyspace
:::

#### `cassandra_keyspace`

Default: None.

The keyspace in which to store the results. For example:

    cassandra_keyspace = 'tasks_keyspace'

::: setting
cassandra_table
:::

#### `cassandra_table`

Default: None.

The table (column family) in which to store the results. For example:

    cassandra_table = 'tasks'

::: setting
cassandra_read_consistency
:::

#### `cassandra_read_consistency`

Default: None.

The read consistency used. Values can be `ONE`, `TWO`, `THREE`,
`QUORUM`, `ALL`, `LOCAL_QUORUM`, `EACH_QUORUM`, `LOCAL_ONE`.

::: setting
cassandra_write_consistency
:::

#### `cassandra_write_consistency`

Default: None.

The write consistency used. Values can be `ONE`, `TWO`, `THREE`,
`QUORUM`, `ALL`, `LOCAL_QUORUM`, `EACH_QUORUM`, `LOCAL_ONE`.

::: setting
cassandra_entry_ttl
:::

#### `cassandra_entry_ttl`

Default: None.

Time-to-live for status entries. They will expire and be removed after
that many seconds after adding. A value of `None`{.interpreted-text
role="const"} (default) means they will never expire.

::: setting
cassandra_auth_provider
:::

#### `cassandra_auth_provider`

Default: `None`{.interpreted-text role="const"}.

AuthProvider class within `cassandra.auth` module to use. Values can be
`PlainTextAuthProvider` or `SaslAuthProvider`.

::: setting
cassandra_auth_kwargs
:::

#### `cassandra_auth_kwargs`

Default: `{}` (empty mapping).

Named arguments to pass into the authentication provider. For example:

``` python
cassandra_auth_kwargs = {
    username: 'cassandra',
    password: 'cassandra'
}
```

::: setting
cassandra_options
:::

#### `cassandra_options`

Default: `{}` (empty mapping).

Named arguments to pass into the `cassandra.cluster` class.

``` python
cassandra_options = {
    'cql_version': '3.2.1'
    'protocol_version': 3
}
```

#### Example configuration (Cassandra)

``` python
result_backend = 'cassandra://'
cassandra_servers = ['localhost']
cassandra_keyspace = 'celery'
cassandra_table = 'tasks'
cassandra_read_consistency = 'QUORUM'
cassandra_write_consistency = 'QUORUM'
cassandra_entry_ttl = 86400
```

#### Example configuration (Astra DB)

``` python
result_backend = 'cassandra://'
cassandra_keyspace = 'celery'
cassandra_table = 'tasks'
cassandra_read_consistency = 'QUORUM'
cassandra_write_consistency = 'QUORUM'
cassandra_auth_provider = 'PlainTextAuthProvider'
cassandra_auth_kwargs = {
  'username': '<<CLIENT_ID_FROM_ASTRA_DB_TOKEN>>',
  'password': '<<CLIENT_SECRET_FROM_ASTRA_DB_TOKEN>>'
}
cassandra_secure_bundle_path = '/path/to/secure-connect-bundle.zip'
cassandra_entry_ttl = 86400
```

#### Additional configuration

The Cassandra driver, when establishing the connection, undergoes a
stage of negotiating the protocol version with the server(s). Similarly,
a load-balancing policy is automatically supplied (by default
`DCAwareRoundRobinPolicy`, which in turn has a `local_dc` setting, also
determined by the driver upon connection). When possible, one should
explicitly provide these in the configuration: moreover, future versions
of the Cassandra driver will require at least the load-balancing policy
to be specified (using [execution
profiles](https://docs.datastax.com/en/developer/python-driver/3.25/execution_profiles/),
as shown below).

A full configuration for the Cassandra backend would thus have the
following additional lines:

``` python
from cassandra.policies import DCAwareRoundRobinPolicy
from cassandra.cluster import ExecutionProfile
from cassandra.cluster import EXEC_PROFILE_DEFAULT
myEProfile = ExecutionProfile(
  load_balancing_policy=DCAwareRoundRobinPolicy(
    local_dc='datacenter1', # replace with your DC name
  )
)
cassandra_options = {
  'protocol_version': 5,    # for Cassandra 4, change if needed
  'execution_profiles': {EXEC_PROFILE_DEFAULT: myEProfile},
}
```

And similarly for Astra DB:

``` python
from cassandra.policies import DCAwareRoundRobinPolicy
from cassandra.cluster import ExecutionProfile
from cassandra.cluster import EXEC_PROFILE_DEFAULT
myEProfile = ExecutionProfile(
  load_balancing_policy=DCAwareRoundRobinPolicy(
    local_dc='europe-west1',  # for Astra DB, region name = dc name
  )
)
cassandra_options = {
  'protocol_version': 4,      # for Astra DB
  'execution_profiles': {EXEC_PROFILE_DEFAULT: myEProfile},
}
```

### S3 backend settings {#conf-s3-result-backend}

::: note
::: title
Note
:::

This s3 backend driver requires `s3`{.interpreted-text role="pypi"}.

To install, use `s3`{.interpreted-text role="command"}:

``` console
$ pip install celery[s3]
```

See `bundles`{.interpreted-text role="ref"} for information on combining
multiple extension requirements.
:::

This backend requires the following configuration directives to be set.

::: setting
s3_access_key_id
:::

#### `s3_access_key_id`

Default: None.

The s3 access key id. For example:

    s3_access_key_id = 'access_key_id'

::: setting
s3_secret_access_key
:::

#### `s3_secret_access_key`

Default: None.

The s3 secret access key. For example:

    s3_secret_access_key = 'access_secret_access_key'

::: setting
s3_bucket
:::

#### `s3_bucket`

Default: None.

The s3 bucket name. For example:

    s3_bucket = 'bucket_name'

::: setting
s3_base_path
:::

#### `s3_base_path`

Default: None.

A base path in the s3 bucket to use to store result keys. For example:

    s3_base_path = '/prefix'

::: setting
s3_endpoint_url
:::

#### `s3_endpoint_url`

Default: None.

A custom s3 endpoint url. Use it to connect to a custom self-hosted s3
compatible backend (Ceph, Scality\...). For example:

    s3_endpoint_url = 'https://.s3.custom.url'

::: setting
s3_region
:::

#### `s3_region`

Default: None.

The s3 aws region. For example:

    s3_region = 'us-east-1'

#### Example configuration

``` python
s3_access_key_id = 's3-access-key-id'
s3_secret_access_key = 's3-secret-access-key'
s3_bucket = 'mybucket'
s3_base_path = '/celery_result_backend'
s3_endpoint_url = 'https://endpoint_url'
```

### Azure Block Blob backend settings {#conf-azureblockblob-result-backend}

To use
[AzureBlockBlob](https://azure.microsoft.com/en-us/services/storage/blobs/)
as the result backend you simply need to configure the
`result_backend`{.interpreted-text role="setting"} setting with the
correct URL.

The required URL format is `azureblockblob://` followed by the storage
connection string. You can find the storage connection string in the
`Access Keys` pane of your storage account resource in the Azure Portal.

#### Example configuration

``` python
result_backend = 'azureblockblob://DefaultEndpointsProtocol=https;AccountName=somename;AccountKey=Lou...bzg==;EndpointSuffix=core.windows.net'
```

::: setting
azureblockblob_container_name
:::

#### `azureblockblob_container_name`

Default: celery.

The name for the storage container in which to store the results.

::: setting
azureblockblob_base_path
:::

#### `azureblockblob_base_path`

::: versionadded
5.1
:::

Default: None.

A base path in the storage container to use to store result keys. For
example:

    azureblockblob_base_path = 'prefix/'

::: setting
azureblockblob_retry_initial_backoff_sec
:::

#### `azureblockblob_retry_initial_backoff_sec`

Default: 2.

The initial backoff interval, in seconds, for the first retry.
Subsequent retries are attempted with an exponential strategy.

::: setting
azureblockblob_retry_increment_base
:::

#### `azureblockblob_retry_increment_base`

Default: 2.

::: setting
azureblockblob_retry_max_attempts
:::

#### `azureblockblob_retry_max_attempts`

Default: 3.

The maximum number of retry attempts.

::: setting
azureblockblob_connection_timeout
:::

#### `azureblockblob_connection_timeout`

Default: 20.

Timeout in seconds for establishing the azure block blob connection.

::: setting
azureblockblob_read_timeout
:::

#### `azureblockblob_read_timeout`

Default: 120.

Timeout in seconds for reading of an azure block blob.

### GCS backend settings {#conf-gcs-result-backend}

::: note
::: title
Note
:::

This gcs backend driver requires
`google-cloud-storage`{.interpreted-text role="pypi"} and
`google-cloud-firestore`{.interpreted-text role="pypi"}.

To install, use `gcs`{.interpreted-text role="command"}:

``` console
$ pip install celery[gcs]
```

See `bundles`{.interpreted-text role="ref"} for information on combining
multiple extension requirements.
:::

GCS could be configured via the URL provided in
`result_backend`{.interpreted-text role="setting"}, for example:

    result_backend = 'gs://mybucket/some-prefix?gcs_project=myproject&ttl=600'
    result_backend = 'gs://mybucket/some-prefix?gcs_project=myproject?firestore_project=myproject2&ttl=600'

This backend requires the following configuration directives to be set:

::: setting
gcs_bucket
:::

#### `gcs_bucket`

Default: None.

The gcs bucket name. For example:

    gcs_bucket = 'bucket_name'

::: setting
gcs_project
:::

#### `gcs_project`

Default: None.

The gcs project name. For example:

    gcs_project = 'test-project'

::: setting
gcs_base_path
:::

#### `gcs_base_path`

Default: None.

A base path in the gcs bucket to use to store all result keys. For
example:

    gcs_base_path = '/prefix'

#### `gcs_ttl`

Default: 0.

The time to live in seconds for the results blobs. Requires a GCS bucket
with \"Delete\" Object Lifecycle Management action enabled. Use it to
automatically delete results from Cloud Storage Buckets.

For example to auto remove results after 24 hours:

    gcs_ttl = 86400

#### `gcs_threadpool_maxsize`

Default: 10.

Threadpool size for GCS operations. Same value defines the connection
pool size. Allows to control the number of concurrent operations. For
example:

    gcs_threadpool_maxsize = 20

#### `firestore_project`

Default: gcs_project.

The Firestore project for Chord reference counting. Allows native chord
ref counts. If not specified defaults to `gcs_project`{.interpreted-text
role="setting"}. For example:

    firestore_project = 'test-project2'

#### Example configuration

``` python
gcs_bucket = 'mybucket'
gcs_project = 'myproject'
gcs_base_path = '/celery_result_backend'
gcs_ttl = 86400
```

### Elasticsearch backend settings {#conf-elasticsearch-result-backend}

To use [Elasticsearch](https://aws.amazon.com/elasticsearch-service/) as
the result backend you simply need to configure the
`result_backend`{.interpreted-text role="setting"} setting with the
correct URL.

#### Example configuration

``` python
result_backend = 'elasticsearch://example.com:9200/index_name/doc_type'
```

::: setting
elasticsearch_retry_on_timeout
:::

#### `elasticsearch_retry_on_timeout`

Default: `False`{.interpreted-text role="const"}

Should timeout trigger a retry on different node?

::: setting
elasticsearch_max_retries
:::

#### `elasticsearch_max_retries`

Default: 3.

Maximum number of retries before an exception is propagated.

::: setting
elasticsearch_timeout
:::

#### `elasticsearch_timeout`

Default: 10.0 seconds.

Global timeout,used by the elasticsearch result backend.

::: setting
elasticsearch_save_meta_as_text
:::

#### `elasticsearch_save_meta_as_text`

Default: `True`{.interpreted-text role="const"}

Should meta saved as text or as native json. Result is always serialized
as text.

### AWS DynamoDB backend settings {#conf-dynamodb-result-backend}

::: note
::: title
Note
:::

The Dynamodb backend requires the `boto3`{.interpreted-text role="pypi"}
library.

To install this package use `pip`{.interpreted-text role="command"}:

``` console
$ pip install celery[dynamodb]
```

See `bundles`{.interpreted-text role="ref"} for information on combining
multiple extension requirements.
:::

::: warning
::: title
Warning
:::

The Dynamodb backend is not compatible with tables that have a sort key
defined.

If you want to query the results table based on something other than the
partition key, please define a global secondary index (GSI) instead.
:::

This backend requires the `result_backend`{.interpreted-text
role="setting"} setting to be set to a DynamoDB URL:

    result_backend = 'dynamodb://aws_access_key_id:aws_secret_access_key@region:port/table?read=n&write=m'

For example, specifying the AWS region and the table name:

    result_backend = 'dynamodb://@us-east-1/celery_results'

or retrieving AWS configuration parameters from the environment, using
the default table name (`celery`) and specifying read and write
provisioned throughput:

    result_backend = 'dynamodb://@/?read=5&write=5'

or using the [downloadable
version](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.html)
of DynamoDB
[locally](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.Endpoint.html):

    result_backend = 'dynamodb://@localhost:8000'

or using downloadable version or other service with conforming API
deployed on any host:

    result_backend = 'dynamodb://@us-east-1'
    dynamodb_endpoint_url = 'http://192.168.0.40:8000'

The fields of the DynamoDB URL in `result_backend` are defined as
follows:

1.  `aws_access_key_id & aws_secret_access_key`

    > The credentials for accessing AWS API resources. These can also be
    > resolved by the `boto3`{.interpreted-text role="pypi"} library
    > from various sources, as described
    > [here](http://boto3.readthedocs.io/en/latest/guide/configuration.html#configuring-credentials).

2.  `region`

    > The AWS region, e.g. `us-east-1` or `localhost` for the
    > [Downloadable
    > Version](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.html).
    > See the `boto3`{.interpreted-text role="pypi"} library
    > [documentation](http://boto3.readthedocs.io/en/latest/guide/configuration.html#environment-variable-configuration)
    > for definition options.

3.  `port`

    The listening port of the local DynamoDB instance, if you are using
    the downloadable version. If you have not specified the `region`
    parameter as `localhost`, setting this parameter has **no effect**.

4.  `table`

    > Table name to use. Default is `celery`. See the [DynamoDB Naming
    > Rules](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html#limits-naming-rules)
    > for information on the allowed characters and length.

5.  `read & write`

    > The Read & Write Capacity Units for the created DynamoDB table.
    > Default is `1` for both read and write. More details can be found
    > in the [Provisioned Throughput
    > documentation](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ProvisionedThroughput.html).

6.  `ttl_seconds`

    > Time-to-live (in seconds) for results before they expire. The
    > default is to not expire results, while also leaving the DynamoDB
    > table\'s Time to Live settings untouched. If `ttl_seconds` is set
    > to a positive value, results will expire after the specified
    > number of seconds. Setting `ttl_seconds` to a negative value means
    > to not expire results, and also to actively disable the DynamoDB
    > table\'s Time to Live setting. Note that trying to change a
    > table\'s Time to Live setting multiple times in quick succession
    > will cause a throttling error. More details can be found in the
    > [DynamoDB TTL
    > documentation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TTL.html)

### IronCache backend settings {#conf-ironcache-result-backend}

::: note
::: title
Note
:::

The IronCache backend requires the `iron_celery`{.interpreted-text
role="pypi"} library:

To install this package use `pip`{.interpreted-text role="command"}:

``` console
$ pip install iron_celery
```
:::

IronCache is configured via the URL provided in
`result_backend`{.interpreted-text role="setting"}, for example:

    result_backend = 'ironcache://project_id:token@'

Or to change the cache name:

    ironcache:://project_id:token@/awesomecache

For more information, see: <https://github.com/iron-io/iron_celery>

### Couchbase backend settings {#conf-couchbase-result-backend}

::: note
::: title
Note
:::

The Couchbase backend requires the `couchbase`{.interpreted-text
role="pypi"} library.

To install this package use `pip`{.interpreted-text role="command"}:

``` console
$ pip install celery[couchbase]
```

See `bundles`{.interpreted-text role="ref"} for instructions how to
combine multiple extension requirements.
:::

This backend can be configured via the
`result_backend`{.interpreted-text role="setting"} set to a Couchbase
URL:

``` python
result_backend = 'couchbase://username:password@host:port/bucket'
```

::: setting
couchbase_backend_settings
:::

#### `couchbase_backend_settings`

Default: `{}` (empty mapping).

This is a dict supporting the following keys:

-   `host`

    > Host name of the Couchbase server. Defaults to `localhost`.

-   `port`

    > The port the Couchbase server is listening to. Defaults to `8091`.

-   `bucket`

    > The default bucket the Couchbase server is writing to. Defaults to
    > `default`.

-   `username`

    > User name to authenticate to the Couchbase server as (optional).

-   `password`

    > Password to authenticate to the Couchbase server (optional).

### ArangoDB backend settings {#conf-arangodb-result-backend}

::: note
::: title
Note
:::

The ArangoDB backend requires the `pyArango`{.interpreted-text
role="pypi"} library.

To install this package use `pip`{.interpreted-text role="command"}:

``` console
$ pip install celery[arangodb]
```

See `bundles`{.interpreted-text role="ref"} for instructions how to
combine multiple extension requirements.
:::

This backend can be configured via the
`result_backend`{.interpreted-text role="setting"} set to a ArangoDB
URL:

``` python
result_backend = 'arangodb://username:password@host:port/database/collection'
```

::: setting
arangodb_backend_settings
:::

#### `arangodb_backend_settings`

Default: `{}` (empty mapping).

This is a dict supporting the following keys:

-   `host`

    > Host name of the ArangoDB server. Defaults to `localhost`.

-   `port`

    > The port the ArangoDB server is listening to. Defaults to `8529`.

-   `database`

    > The default database in the ArangoDB server is writing to.
    > Defaults to `celery`.

-   `collection`

    > The default collection in the ArangoDB servers database is writing
    > to. Defaults to `celery`.

-   `username`

    > User name to authenticate to the ArangoDB server as (optional).

-   `password`

    > Password to authenticate to the ArangoDB server (optional).

-   `http_protocol`

    > HTTP Protocol in ArangoDB server connection. Defaults to `http`.

-   `verify`

    > HTTPS Verification check while creating the ArangoDB connection.
    > Defaults to `False`.

### CosmosDB backend settings (experimental) {#conf-cosmosdbsql-result-backend}

To use [CosmosDB](https://azure.microsoft.com/en-us/services/cosmos-db/)
as the result backend, you simply need to configure the
`result_backend`{.interpreted-text role="setting"} setting with the
correct URL.

#### Example configuration

``` python
result_backend = 'cosmosdbsql://:{InsertAccountPrimaryKeyHere}@{InsertAccountNameHere}.documents.azure.com'
```

::: setting
cosmosdbsql_database_name
:::

#### `cosmosdbsql_database_name`

Default: celerydb.

The name for the database in which to store the results.

::: setting
cosmosdbsql_collection_name
:::

#### `cosmosdbsql_collection_name`

Default: celerycol.

The name of the collection in which to store the results.

::: setting
cosmosdbsql_consistency_level
:::

#### `cosmosdbsql_consistency_level`

Default: Session.

Represents the consistency levels supported for Azure Cosmos DB client
operations.

Consistency levels by order of strength are: Strong, BoundedStaleness,
Session, ConsistentPrefix and Eventual.

::: setting
cosmosdbsql_max_retry_attempts
:::

#### `cosmosdbsql_max_retry_attempts`

Default: 9.

Maximum number of retries to be performed for a request.

::: setting
cosmosdbsql_max_retry_wait_time
:::

#### `cosmosdbsql_max_retry_wait_time`

Default: 30.

Maximum wait time in seconds to wait for a request while the retries are
happening.

### CouchDB backend settings {#conf-couchdb-result-backend}

::: note
::: title
Note
:::

The CouchDB backend requires the `pycouchdb`{.interpreted-text
role="pypi"} library:

To install this Couchbase package use `pip`{.interpreted-text
role="command"}:

``` console
$ pip install celery[couchdb]
```

See `bundles`{.interpreted-text role="ref"} for information on combining
multiple extension requirements.
:::

This backend can be configured via the
`result_backend`{.interpreted-text role="setting"} set to a CouchDB URL:

    result_backend = 'couchdb://username:password@host:port/container'

The URL is formed out of the following parts:

-   `username`

    > User name to authenticate to the CouchDB server as (optional).

-   `password`

    > Password to authenticate to the CouchDB server (optional).

-   `host`

    > Host name of the CouchDB server. Defaults to `localhost`.

-   `port`

    > The port the CouchDB server is listening to. Defaults to `8091`.

-   `container`

    > The default container the CouchDB server is writing to. Defaults
    > to `default`.

### File-system backend settings {#conf-filesystem-result-backend}

This backend can be configured using a file URL, for example:

    CELERY_RESULT_BACKEND = 'file:///var/celery/results'

The configured directory needs to be shared and writable by all servers
using the backend.

If you\'re trying Celery on a single system you can simply use the
backend without any further configuration. For larger clusters you could
use NFS, [GlusterFS](http://www.gluster.org/), CIFS,
[HDFS](http://hadoop.apache.org/) (using FUSE), or any other
file-system.

### Consul K/V store backend settings {#conf-consul-result-backend}

::: note
::: title
Note
:::

The Consul backend requires the `python-consul2`{.interpreted-text
role="pypi"} library:

To install this package use `pip`{.interpreted-text role="command"}:

``` console
$ pip install python-consul2
```
:::

The Consul backend can be configured using a URL, for example:

    CELERY_RESULT_BACKEND = 'consul://localhost:8500/'

or:

    result_backend = 'consul://localhost:8500/'

The backend will store results in the K/V store of Consul as individual
keys. The backend supports auto expire of results using TTLs in Consul.
The full syntax of the URL is:

``` text
consul://host:port[?one_client=1]
```

The URL is formed out of the following parts:

-   `host`

    > Host name of the Consul server.

-   `port`

    > The port the Consul server is listening to.

-   `one_client`

    > By default, for correctness, the backend uses a separate client
    > connection per operation. In cases of extreme load, the rate of
    > creation of new connections can cause HTTP 429 \"too many
    > connections\" error responses from the Consul server when under
    > load. The recommended way to handle this is to enable retries in
    > `python-consul2` using the patch at
    > <https://github.com/poppyred/python-consul2/pull/31>.
    >
    > Alternatively, if `one_client` is set, a single client connection
    > will be used for all operations instead. This should eliminate the
    > HTTP 429 errors, but the storage of results in the backend can
    > become unreliable.

### Message Routing {#conf-messaging}

::: {#conf-messaging-routing}
::: setting
task_queues
:::
:::

#### `task_queues`

Default: `None`{.interpreted-text role="const"} (queue taken from
default queue settings).

Most users will not want to specify this setting and should rather use
the `automatic routing facilities <routing-automatic>`{.interpreted-text
role="ref"}.

If you really want to configure advanced routing, this setting should be
a list of `kombu.Queue`{.interpreted-text role="class"} objects the
worker will consume from.

Note that workers can be overridden this setting via the
`-Q <celery worker -Q>`{.interpreted-text role="option"} option, or
individual queues from this list (by name) can be excluded using the
`-X <celery worker -X>`{.interpreted-text role="option"} option.

Also see `routing-basics`{.interpreted-text role="ref"} for more
information.

The default is a queue/exchange/binding key of `celery`, with exchange
type `direct`.

See also `task_routes`{.interpreted-text role="setting"}

::: setting
task_routes
:::

#### `task_routes`

Default: `None`{.interpreted-text role="const"}.

A list of routers, or a single router used to route tasks to queues.
When deciding the final destination of a task the routers are consulted
in order.

A router can be specified as either:

-   A function with the signature
    `(name, args, kwargs, options, task=None, **kwargs)`

-   A string providing the path to a router function.

-   

    A dict containing router specification:

    :   Will be converted to a
        `celery.routes.MapRoute`{.interpreted-text role="class"}
        instance.

-   

    A list of `(pattern, route)` tuples:

    :   Will be converted to a
        `celery.routes.MapRoute`{.interpreted-text role="class"}
        instance.

Examples:

``` python
task_routes = {
    'celery.ping': 'default',
    'mytasks.add': 'cpu-bound',
    'feed.tasks.*': 'feeds',                           # <-- glob pattern
    re.compile(r'(image|video)\.tasks\..*'): 'media',  # <-- regex
    'video.encode': {
        'queue': 'video',
        'exchange': 'media',
        'routing_key': 'media.video.encode',
    },
}

task_routes = ('myapp.tasks.route_task', {'celery.ping': 'default'})
```

Where `myapp.tasks.route_task` could be:

``` python
def route_task(self, name, args, kwargs, options, task=None, **kw):
    if task == 'celery.ping':
        return {'queue': 'default'}
```

`route_task` may return a string or a dict. A string then means it\'s a
queue name in `task_queues`{.interpreted-text role="setting"}, a dict
means it\'s a custom route.

When sending tasks, the routers are consulted in order. The first router
that doesn\'t return `None` is the route to use. The message options is
then merged with the found route settings, where the task\'s settings
have priority.

Example if `~celery.execute.apply_async`{.interpreted-text role="func"}
has these arguments:

``` python
Task.apply_async(immediate=False, exchange='video',
                 routing_key='video.compress')
```

and a router returns:

``` python
{'immediate': True, 'exchange': 'urgent'}
```

the final message options will be:

``` python
immediate=False, exchange='video', routing_key='video.compress'
```

(and any default message options defined in the
`~celery.app.task.Task`{.interpreted-text role="class"} class)

Values defined in `task_routes`{.interpreted-text role="setting"} have
precedence over values defined in `task_queues`{.interpreted-text
role="setting"} when merging the two.

With the follow settings:

``` python
task_queues = {
    'cpubound': {
        'exchange': 'cpubound',
        'routing_key': 'cpubound',
    },
}

task_routes = {
    'tasks.add': {
        'queue': 'cpubound',
        'routing_key': 'tasks.add',
        'serializer': 'json',
    },
}
```

The final routing options for `tasks.add` will become:

``` javascript
{'exchange': 'cpubound',
 'routing_key': 'tasks.add',
 'serializer': 'json'}
```

See `routers`{.interpreted-text role="ref"} for more examples.

::: setting
task_queue_max_priority
:::

#### `task_queue_max_priority`

brokers

:   RabbitMQ

Default: `None`{.interpreted-text role="const"}.

See `routing-options-rabbitmq-priorities`{.interpreted-text role="ref"}.

::: setting
task_default_priority
:::

#### `task_default_priority`

brokers

:   RabbitMQ, Redis

Default: `None`{.interpreted-text role="const"}.

See `routing-options-rabbitmq-priorities`{.interpreted-text role="ref"}.

::: setting
task_inherit_parent_priority
:::

#### `task_inherit_parent_priority`

brokers

:   RabbitMQ

Default: `False`{.interpreted-text role="const"}.

If enabled, child tasks will inherit priority of the parent task.

``` python
# The last task in chain will also have priority set to 5.
chain = celery.chain(add.s(2) | add.s(2).set(priority=5) | add.s(3))
```

Priority inheritance also works when calling child tasks from a parent
task with [delay]{.title-ref} or [apply_async]{.title-ref}.

See `routing-options-rabbitmq-priorities`{.interpreted-text role="ref"}.

::: setting
worker_direct
:::

#### `worker_direct`

Default: Disabled.

This option enables so that every worker has a dedicated queue, so that
tasks can be routed to specific workers.

The queue name for each worker is automatically generated based on the
worker hostname and a `.dq` suffix, using the `C.dq2` exchange.

For example the queue name for the worker with node name
`w1@example.com` becomes:

    w1@example.com.dq

Then you can route the task to the worker by specifying the hostname as
the routing key and the `C.dq2` exchange:

    task_routes = {
        'tasks.add': {'exchange': 'C.dq2', 'routing_key': 'w1@example.com'}
    }

::: setting
task_create_missing_queues
:::

#### `task_create_missing_queues`

Default: Enabled.

If enabled (default), any queues specified that aren\'t defined in
`task_queues`{.interpreted-text role="setting"} will be automatically
created. See `routing-automatic`{.interpreted-text role="ref"}.

::: setting
task_create_missing_queue_type
:::

`task_create_missing_queue_type`
\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~ ..
versionadded:: 5.6

Default: `"classic"`

When Celery needs to declare a queue that doesn't exist (i.e., when
`task_create_missing_queues` is enabled), this setting defines what type
of RabbitMQ queue to create.

-   `"classic"` (default): declares a standard classic queue.
-   `"quorum"`: declares a RabbitMQ quorum queue (adds
    `x-queue-type: quorum`).

::: setting
task_create_missing_queue_exchange_type
:::

`task_create_missing_queue_exchange_type`
\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~
.. versionadded:: 5.6

Default: `None`

If this option is None or the empty string (the default), Celery leaves
the exchange exactly as returned by your
`app.amqp.Queues.autoexchange`{.interpreted-text role="attr"} hook.

You can set this to a specific exchange type, such as `"direct"`,
`"topic"`, or `"fanout"`, to create the missing queue with that exchange
type.

::: tip
::: title
Tip
:::
:::

Combine this setting with task_create_missing_queue_type = \"quorum\" to
create quorum queues bound to a topic exchange, for example:

    app.conf.task_create_missing_queues=True
    app.conf.task_create_missing_queue_type="quorum"
    app.conf.task_create_missing_queue_exchange_type="topic"

::: note
::: title
Note
:::
:::

Like the queue-type setting above, this option does not affect queues
that you define explicitly in `task_queues`{.interpreted-text
role="setting"}; it applies only to queues created implicitly at
runtime.

::: setting
task_default_queue
:::

#### `task_default_queue`

Default: `"celery"`.

The name of the default queue used by [.apply_async]{.title-ref} if the
message has no route or no custom queue has been specified.

This queue must be listed in `task_queues`{.interpreted-text
role="setting"}. If `task_queues`{.interpreted-text role="setting"}
isn\'t specified then it\'s automatically created containing one queue
entry, where this name is used as the name of that queue.

::: seealso
`routing-changing-default-queue`{.interpreted-text role="ref"}
:::

::: setting
task_default_queue_type
:::

#### `task_default_queue_type`

::: versionadded
5.5
:::

Default: `"classic"`.

This setting is used to allow changing the default queue type for the
`task_default_queue`{.interpreted-text role="setting"} queue. The other
viable option is `"quorum"` which is only supported by RabbitMQ and sets
the queue type to `quorum` using the `x-queue-type` queue argument.

If the `worker_detect_quorum_queues`{.interpreted-text role="setting"}
setting is enabled, the worker will automatically detect the queue type
and disable the global QoS accordingly.

::: warning
::: title
Warning
:::

Quorum queues require confirm publish to be enabled. Use
`broker_transport_options`{.interpreted-text role="setting"} to enable
confirm publish by setting:

``` python
broker_transport_options = {"confirm_publish": True}
```

For more information, see [RabbitMQ
documentation](https://www.rabbitmq.com/docs/quorum-queues#use-cases).
:::

::: setting
task_default_exchange
:::

#### `task_default_exchange`

Default: Uses the value set for `task_default_queue`{.interpreted-text
role="setting"}.

Name of the default exchange to use when no custom exchange is specified
for a key in the `task_queues`{.interpreted-text role="setting"}
setting.

::: setting
task_default_exchange_type
:::

#### `task_default_exchange_type`

Default: `"direct"`.

Default exchange type used when no custom exchange type is specified for
a key in the `task_queues`{.interpreted-text role="setting"} setting.

::: setting
task_default_routing_key
:::

#### `task_default_routing_key`

Default: Uses the value set for `task_default_queue`{.interpreted-text
role="setting"}.

The default routing key used when no custom routing key is specified for
a key in the `task_queues`{.interpreted-text role="setting"} setting.

::: setting
task_default_delivery_mode
:::

#### `task_default_delivery_mode`

Default: `"persistent"`.

Can be [transient]{.title-ref} (messages not written to disk) or
[persistent]{.title-ref} (written to disk).

### Broker Settings {#conf-broker-settings}

::: setting
broker_url
:::

#### `broker_url`

Default: `"amqp://"`

Default broker URL. This must be a URL in the form of:

    transport://userid:password@hostname:port/virtual_host

Only the scheme part (`transport://`) is required, the rest is optional,
and defaults to the specific transports default values.

The transport part is the broker implementation to use, and the default
is `amqp`, (uses `librabbitmq` if installed or falls back to `pyamqp`).
There are also other choices available, including; `redis://`, `sqs://`,
and `qpid://`.

The scheme can also be a fully qualified path to your own transport
implementation:

    broker_url = 'proj.transports.MyTransport://localhost'

More than one broker URL, of the same transport, can also be specified.
The broker URLs can be passed in as a single string that\'s semicolon
delimited:

    broker_url = 'transport://userid:password@hostname:port//;transport://userid:password@hostname:port//'

Or as a list:

    broker_url = [
        'transport://userid:password@localhost:port//',
        'transport://userid:password@hostname:port//'
    ]

The brokers will then be used in the
`broker_failover_strategy`{.interpreted-text role="setting"}.

See `kombu:connection-urls`{.interpreted-text role="ref"} in the Kombu
documentation for more information.

::: setting
broker_read_url
:::

::: setting
broker_write_url
:::

#### `broker_read_url` / `broker_write_url`

Default: Taken from `broker_url`{.interpreted-text role="setting"}.

These settings can be configured, instead of
`broker_url`{.interpreted-text role="setting"} to specify different
connection parameters for broker connections used for consuming and
producing.

Example:

    broker_read_url = 'amqp://user:pass@broker.example.com:56721'
    broker_write_url = 'amqp://user:pass@broker.example.com:56722'

Both options can also be specified as a list for failover alternates,
see `broker_url`{.interpreted-text role="setting"} for more information.

::: setting
broker_failover_strategy
:::

#### `broker_failover_strategy`

Default: `"round-robin"`.

Default failover strategy for the broker Connection object. If supplied,
may map to a key in \'kombu.connection.failover_strategies\', or be a
reference to any method that yields a single item from a supplied list.

Example:

    # Random failover strategy
    def random_failover_strategy(servers):
        it = list(servers)  # don't modify callers list
        shuffle = random.shuffle
        for _ in repeat(None):
            shuffle(it)
            yield it[0]

    broker_failover_strategy = random_failover_strategy

::: setting
broker_heartbeat
:::

#### `broker_heartbeat`

transports supported

:   `pyamqp`

Default: `120.0` (negotiated by server).

Note: This value is only used by the worker, clients do not use a
heartbeat at the moment.

It\'s not always possible to detect connection loss in a timely manner
using TCP/IP alone, so AMQP defines something called heartbeats that\'s
is used both by the client and the broker to detect if a connection was
closed.

If the heartbeat value is 10 seconds, then the heartbeat will be
monitored at the interval specified by the
`broker_heartbeat_checkrate`{.interpreted-text role="setting"} setting
(by default this is set to double the rate of the heartbeat value, so
for the 10 seconds, the heartbeat is checked every 5 seconds).

::: setting
broker_heartbeat_checkrate
:::

#### `broker_heartbeat_checkrate`

transports supported

:   `pyamqp`

Default: 2.0.

At intervals the worker will monitor that the broker hasn\'t missed too
many heartbeats. The rate at which this is checked is calculated by
dividing the `broker_heartbeat`{.interpreted-text role="setting"} value
with this value, so if the heartbeat is 10.0 and the rate is the default
2.0, the check will be performed every 5 seconds (twice the heartbeat
sending rate).

::: setting
broker_use_ssl
:::

#### `broker_use_ssl`

transports supported

:   `pyamqp`, `redis`

Default: Disabled.

Toggles SSL usage on broker connection and SSL settings.

The valid values for this option vary by transport.

##### `pyamqp`

If `True` the connection will use SSL with default SSL settings. If set
to a dict, will configure SSL connection according to the specified
policy. The format used is Python\'s `ssl.wrap_socket`{.interpreted-text
role="func"} options.

Note that SSL socket is generally served on a separate port by the
broker.

Example providing a client cert and validating the server cert against a
custom certificate authority:

``` python
import ssl

broker_use_ssl = {
  'keyfile': '/var/ssl/private/worker-key.pem',
  'certfile': '/var/ssl/amqp-server-cert.pem',
  'ca_certs': '/var/ssl/myca.pem',
  'cert_reqs': ssl.CERT_REQUIRED
}
```

::: versionadded
5.1

Starting from Celery 5.1, py-amqp will always validate certificates
received from the server and it is no longer required to manually set
`cert_reqs` to `ssl.CERT_REQUIRED`.

The previous default, `ssl.CERT_NONE` is insecure and we its usage
should be discouraged. If you\'d like to revert to the previous insecure
default set `cert_reqs` to `ssl.CERT_NONE`
:::

##### `redis`

The setting must be a dict with the following keys:

-   

    `ssl_cert_reqs` (required): one of the `SSLContext.verify_mode` values:

    :   -   `ssl.CERT_NONE`
        -   `ssl.CERT_OPTIONAL`
        -   `ssl.CERT_REQUIRED`

-   `ssl_ca_certs` (optional): path to the CA certificate

-   `ssl_certfile` (optional): path to the client certificate

-   `ssl_keyfile` (optional): path to the client key

::: setting
broker_pool_limit
:::

#### `broker_pool_limit`

::: versionadded
2.3
:::

Default: 10.

The maximum number of connections that can be open in the connection
pool.

The pool is enabled by default since version 2.5, with a default limit
of ten connections. This number can be tweaked depending on the number
of threads/green-threads (eventlet/gevent) using a connection. For
example running eventlet with 1000 greenlets that use a connection to
the broker, contention can arise and you should consider increasing the
limit.

If set to `None`{.interpreted-text role="const"} or 0 the connection
pool will be disabled and connections will be established and closed for
every use.

::: setting
broker_connection_timeout
:::

#### `broker_connection_timeout`

Default: 4.0.

The default timeout in seconds before we give up establishing a
connection to the AMQP server. This setting is disabled when using
gevent.

::: note
::: title
Note
:::

The broker connection timeout only applies to a worker attempting to
connect to the broker. It does not apply to producer sending a task, see
`broker_transport_options`{.interpreted-text role="setting"} for how to
provide a timeout for that situation.
:::

::: setting
broker_connection_retry
:::

#### `broker_connection_retry`

Default: Enabled.

Automatically try to re-establish the connection to the AMQP broker if
lost after the initial connection is made.

The time between retries is increased for each retry, and is not
exhausted before `broker_connection_max_retries`{.interpreted-text
role="setting"} is exceeded.

::: warning
::: title
Warning
:::

The broker_connection_retry configuration setting will no longer
determine whether broker connection retries are made during startup in
Celery 6.0 and above. If you wish to refrain from retrying connections
on startup, you should set broker_connection_retry_on_startup to False
instead.
:::

::: setting
broker_connection_retry_on_startup
:::

#### `broker_connection_retry_on_startup`

Default: Enabled.

Automatically try to establish the connection to the AMQP broker on
Celery startup if it is unavailable.

The time between retries is increased for each retry, and is not
exhausted before `broker_connection_max_retries`{.interpreted-text
role="setting"} is exceeded.

::: setting
broker_connection_max_retries
:::

#### `broker_connection_max_retries`

Default: 100.

Maximum number of retries before we give up re-establishing a connection
to the AMQP broker.

If this is set to `None`{.interpreted-text role="const"}, we\'ll retry
forever.

#### `broker_channel_error_retry`

::: versionadded
5.3
:::

Default: Disabled.

Automatically try to re-establish the connection to the AMQP broker if
any invalid response has been returned.

The retry count and interval is the same as that of
[broker_connection_retry]{.title-ref}. Also, this option doesn\'t work
when [broker_connection_retry]{.title-ref} is [False]{.title-ref}.

::: setting
broker_login_method
:::

#### `broker_login_method`

Default: `"AMQPLAIN"`.

Set custom amqp login method.

::: setting
broker_native_delayed_delivery_queue_type
:::

#### `broker_native_delayed_delivery_queue_type`

::: versionadded
5.5
:::

transports supported

:   `pyamqp`

Default: `"quorum"`.

This setting is used to allow changing the default queue type for the
native delayed delivery queues. The other viable option is `"classic"`
which is only supported by RabbitMQ and sets the queue type to `classic`
using the `x-queue-type` queue argument.

::: setting
broker_transport_options
:::

#### `broker_transport_options`

::: versionadded
2.2
:::

Default: `{}` (empty mapping).

A dict of additional options passed to the underlying transport.

See your transport user manual for supported options (if any).

Example setting the visibility timeout (supported by Redis and SQS
transports):

``` python
broker_transport_options = {'visibility_timeout': 18000}  # 5 hours
```

Example setting the producer connection maximum number of retries (so
producers won\'t retry forever if the broker isn\'t available at the
first task execution):

``` python
broker_transport_options = {'max_retries': 5}
```

Example enabling publisher confirms (supported by the `pyamqp`
transport). Without this, messages can be silently dropped when the
broker hits resource limits:

``` python
broker_transport_options = {'confirm_publish': True}
```

### Worker {#conf-worker}

::: setting
imports
:::

#### `imports`

Default: `[]` (empty list).

A sequence of modules to import when the worker starts.

This is used to specify the task modules to import, but also to import
signal handlers and additional remote control commands, etc.

The modules will be imported in the original order.

::: setting
include
:::

#### `include`

Default: `[]` (empty list).

Exact same semantics as `imports`{.interpreted-text role="setting"}, but
can be used as a means to have different import categories.

The modules in this setting are imported after the modules in
`imports`{.interpreted-text role="setting"}.

::: setting
worker_deduplicate_successful_tasks
:::

#### `worker_deduplicate_successful_tasks`

::: versionadded
5.1
:::

Default: False

Before each task execution, instruct the worker to check if this task is
a duplicate message.

Deduplication occurs only with tasks that have the same identifier,
enabled late acknowledgment, were redelivered by the message broker and
their state is `SUCCESS` in the result backend.

To avoid overflowing the result backend with queries, a local cache of
successfully executed tasks is checked before querying the result
backend in case the task was already successfully executed by the same
worker that received the task.

This cache can be made persistent by setting the
`worker_state_db`{.interpreted-text role="setting"} setting.

If the result backend is not
[persistent](https://github.com/celery/celery/blob/main/celery/backends/base.py#L102)
(the RPC backend, for example), this setting is ignored.

::: {#conf-concurrency}
::: setting
worker_concurrency
:::
:::

#### `worker_concurrency`

Default: Number of CPU cores.

The number of concurrent worker processes/threads/green threads
executing tasks.

If you\'re doing mostly I/O you can have more processes, but if mostly
CPU-bound, try to keep it close to the number of CPUs on your machine.
If not set, the number of CPUs/cores on the host will be used.

::: setting
worker_prefetch_multiplier
:::

#### `worker_prefetch_multiplier`

Default: 4.

How many messages to prefetch at a time multiplied by the number of
concurrent processes. The default is 4 (four messages for each process).
The default setting is usually a good choice, however \-- if you have
very long running tasks waiting in the queue and you have to start the
workers, note that the first worker to start will receive four times the
number of messages initially. Thus the tasks may not be fairly
distributed to the workers.

To limit the broker to only deliver one message per process at a time,
set `worker_prefetch_multiplier`{.interpreted-text role="setting"} to 1.
Changing that setting to 0 will allow the worker to keep consuming as
many messages as it wants.

If you need to completely disable broker prefetching while still using
early acknowledgments, enable
`worker_disable_prefetch`{.interpreted-text role="setting"}. When this
option is enabled the worker only fetches a task from the broker when
one of its processes is available.

::: note
::: title
Note
:::

This feature is currently only supported when using Redis as the broker.
:::

You can also enable this via the
`--disable-prefetch <celery worker --disable-prefetch>`{.interpreted-text
role="option"} command line flag.

For more on prefetching, read
`optimizing-prefetch-limit`{.interpreted-text role="ref"}

::: setting
worker_eta_task_limit
:::

#### `worker_eta_task_limit`

::: versionadded
5.6
:::

Default: No limit (None).

The maximum number of ETA/countdown tasks that a worker can hold in
memory at once. When this limit is reached, the worker will not receive
new tasks from the broker until some of the existing ETA tasks are
executed.

This setting helps prevent memory exhaustion when a queue contains a
large number of tasks with ETA/countdown values, as these tasks are held
in memory until their execution time. Without this limit, workers may
fetch thousands of ETA tasks into memory, potentially causing
out-of-memory issues.

::: note
::: title
Note
:::

Tasks with ETA/countdown aren\'t affected by prefetch limits.
:::

::: setting
worker_disable_prefetch
:::

#### `worker_disable_prefetch`

::: versionadded
5.6
:::

Default: `False`.

When enabled, a worker will only consume messages from the broker when
it has an available process to execute them. This disables prefetching
while still using early acknowledgments, ensuring that tasks are fairly
distributed between workers.

::: note
::: title
Note
:::

This feature is currently only supported when using Redis as the broker.
Using this setting with other brokers will result in a warning and the
setting will be ignored.
:::

::: setting
worker_enable_prefetch_count_reduction
:::

#### `worker_enable_prefetch_count_reduction`

::: versionadded
5.4
:::

Default: Enabled.

The `worker_enable_prefetch_count_reduction` setting governs the
restoration behavior of the prefetch count to its maximum allowable
value following a connection loss to the message broker. By default,
this setting is enabled.

Upon a connection loss, Celery will attempt to reconnect to the broker
automatically, provided the
`broker_connection_retry_on_startup`{.interpreted-text role="setting"}
or `broker_connection_retry`{.interpreted-text role="setting"} is not
set to False. During the period of lost connection, the message broker
does not keep track of the number of tasks already fetched. Therefore,
to manage the task load effectively and prevent overloading, Celery
reduces the prefetch count based on the number of tasks that are
currently running.

The prefetch count is the number of messages that a worker will fetch
from the broker at a time. The reduced prefetch count helps ensure that
tasks are not fetched excessively during periods of reconnection.

With `worker_enable_prefetch_count_reduction` set to its default value
(Enabled), the prefetch count will be gradually restored to its maximum
allowed value each time a task that was running before the connection
was lost is completed. This behavior helps maintain a balanced
distribution of tasks among the workers while managing the load
effectively.

To disable the reduction and restoration of the prefetch count to its
maximum allowed value on reconnection, set
`worker_enable_prefetch_count_reduction` to False. Disabling this
setting might be useful in scenarios where a fixed prefetch count is
desired to control the rate of task processing or manage the worker
load, especially in environments with fluctuating connectivity.

The `worker_enable_prefetch_count_reduction` setting provides a way to
control the restoration behavior of the prefetch count following a
connection loss, aiding in maintaining a balanced task distribution and
effective load management across the workers.

::: setting
worker_lost_wait
:::

#### `worker_lost_wait`

Default: 10.0 seconds.

In some cases a worker may be killed without proper cleanup, and the
worker may have published a result before terminating. This value
specifies how long we wait for any missing results before raising a
`@WorkerLostError`{.interpreted-text role="exc"} exception.

::: setting
worker_max_tasks_per_child
:::

#### `worker_max_tasks_per_child`

Maximum number of tasks a pool worker process can execute before it\'s
replaced with a new one. Default is no limit.

::: setting
worker_max_memory_per_child
:::

#### `worker_max_memory_per_child`

Default: No limit. Type: int (kilobytes)

Maximum amount of resident memory, in kilobytes (1024 bytes), that may
be consumed by a worker before it will be replaced by a new worker. If a
single task causes a worker to exceed this limit, the task will be
completed, and the worker will be replaced afterwards.

Example:

``` python
worker_max_memory_per_child = 12288  # 12 * 1024 = 12 MB
```

::: setting
worker_disable_rate_limits
:::

#### `worker_disable_rate_limits`

Default: Disabled (rate limits enabled).

Disable all rate limits, even if tasks has explicit rate limits set.

::: setting
worker_state_db
:::

#### `worker_state_db`

Default: `None`{.interpreted-text role="const"}.

Name of the file used to stores persistent worker state (like revoked
tasks). Can be a relative or absolute path, but be aware that the suffix
[.db]{.title-ref} may be appended to the file name (depending on Python
version).

Can also be set via the `celery worker --statedb`{.interpreted-text
role="option"} argument.

::: setting
worker_timer_precision
:::

#### `worker_timer_precision`

Default: 1.0 seconds.

Set the maximum time in seconds that the ETA scheduler can sleep between
rechecking the schedule.

Setting this value to 1 second means the schedulers precision will be 1
second. If you need near millisecond precision you can set this to 0.1.

::: setting
worker_enable_remote_control
:::

#### `worker_enable_remote_control`

Default: Enabled by default.

Specify if remote control of the workers is enabled.

::: setting
worker_proc_alive_timeout
:::

#### `worker_proc_alive_timeout`

Default: 4.0.

The timeout in seconds (int/float) when waiting for a new worker process
to start up.

::: setting
worker_cancel_long_running_tasks_on_connection_loss
:::

#### `worker_cancel_long_running_tasks_on_connection_loss`

::: versionadded
5.1
:::

Default: Disabled by default.

Kill all long-running tasks with late acknowledgment enabled on
connection loss.

Tasks which have not been acknowledged before the connection loss cannot
do so anymore since their channel is gone and the task is redelivered
back to the queue. This is why tasks with late acknowledged enabled must
be idempotent as they may be executed more than once. In this case, the
task is being executed twice per connection loss (and sometimes in
parallel in other workers).

When turning this option on, those tasks which have not been completed
are cancelled and their execution is terminated. Tasks which have
completed in any way before the connection loss are recorded as such in
the result backend as long as `task_ignore_result`{.interpreted-text
role="setting"} is not enabled.

::: warning
::: title
Warning
:::

This feature was introduced as a future breaking change. If it is turned
off, Celery will emit a warning message.

In Celery 6.0, the
`worker_cancel_long_running_tasks_on_connection_loss`{.interpreted-text
role="setting"} will be set to `True` by default as the current behavior
leads to more problems than it solves.
:::

::: setting
worker_detect_quorum_queues
:::

#### `worker_detect_quorum_queues`

::: versionadded
5.5
:::

Default: Enabled.

Automatically detect if any of the queues in
`task_queues`{.interpreted-text role="setting"} are quorum queues
(including the `task_default_queue`{.interpreted-text role="setting"})
and disable the global QoS if any quorum queue is detected.

::: setting
worker_soft_shutdown_timeout
:::

#### `worker_soft_shutdown_timeout`

::: versionadded
5.5
:::

Default: 0.0.

The standard `warm shutdown <worker-warm-shutdown>`{.interpreted-text
role="ref"} will wait for all tasks to finish before shutting down
unless the cold shutdown is triggered. The
`soft shutdown <worker-soft-shutdown>`{.interpreted-text role="ref"}
will add a waiting time before the cold shutdown is initiated. This
setting specifies how long the worker will wait before the cold shutdown
is initiated and the worker is terminated.

This will apply also when the worker initiate
`cold shutdown <worker-cold-shutdown>`{.interpreted-text role="ref"}
without doing a warm shutdown first.

If the value is set to 0.0, the soft shutdown will be practically
disabled. Regardless of the value, the soft shutdown will be disabled if
there are no tasks running (unless
`worker_enable_soft_shutdown_on_idle`{.interpreted-text role="setting"}
is enabled).

Experiment with this value to find the optimal time for your tasks to
finish gracefully before the worker is terminated. Recommended values
can be 10, 30, 60 seconds. Too high value can lead to a long waiting
time before the worker is terminated and trigger a
`KILL`{.interpreted-text role="sig"} signal to forcefully terminate the
worker by the host system.

::: setting
worker_enable_soft_shutdown_on_idle
:::

#### `worker_enable_soft_shutdown_on_idle`

::: versionadded
5.5
:::

Default: False.

If the `worker_soft_shutdown_timeout`{.interpreted-text role="setting"}
is set to a value greater than 0.0, the worker will skip the
`soft shutdown <worker-soft-shutdown>`{.interpreted-text role="ref"}
anyways if there are no tasks running. This setting will enable the soft
shutdown even if there are no tasks running.

::: tip
::: title
Tip
:::

When the worker received ETA tasks, but the ETA has not been reached
yet, and a shutdown is initiated, the worker will **skip** the soft
shutdown and initiate the cold shutdown immediately if there are no
tasks running. This may lead to failure in re-queueing the ETA tasks
during worker teardown. To mitigate this, enable this configuration to
ensure the worker waits regadless, which gives enough time for a
graceful shutdown and successful re-queueing of the ETA tasks.
:::

### Events {#conf-events}

::: setting
worker_send_task_events
:::

#### `worker_send_task_events`

Default: Disabled by default.

Send task-related events so that tasks can be monitored using tools like
[flower]{.title-ref}. Sets the default value for the workers
`-E <celery worker -E>`{.interpreted-text role="option"} argument.

::: setting
task_send_sent_event
:::

#### `task_send_sent_event`

::: versionadded
2.2
:::

Default: Disabled by default.

If enabled, a `task-sent`{.interpreted-text role="event"} event will be
sent for every task so tasks can be tracked before they\'re consumed by
a worker.

::: setting
event_queue_ttl
:::

#### `event_queue_ttl`

transports supported

:   `amqp`

Default: 5.0 seconds.

Message expiry time in seconds (int/float) for when messages sent to a
monitor clients event queue is deleted (`x-message-ttl`)

For example, if this value is set to 10 then a message delivered to this
queue will be deleted after 10 seconds.

::: setting
event_queue_expires
:::

#### `event_queue_expires`

transports supported

:   `amqp`

Default: 60.0 seconds.

Expiry time in seconds (int/float) for when after a monitor clients
event queue will be deleted (`x-expires`).

::: setting
event_queue_durable
:::

#### `event_queue_durable`

transports supported

:   `amqp`

::: versionadded
5.6
:::

Default: `False`

If enabled, the event receiver\'s queue will be marked as *durable*,
meaning it will survive broker restarts.

::: setting
event_queue_exclusive
:::

#### `event_queue_exclusive`

transports supported

:   `amqp`

::: versionadded
5.6
:::

Default: `False`

If enabled, the event queue will be *exclusive* to the current
connection and automatically deleted when the connection closes.

::: warning
::: title
Warning
:::

You **cannot** set both `event_queue_durable` and
`event_queue_exclusive` to `True` at the same time. Celery will raise an
`ImproperlyConfigured`{.interpreted-text role="exc"} error if both are
set.
:::

::: setting
event_queue_prefix
:::

#### `event_queue_prefix`

Default: `"celeryev"`.

The prefix to use for event receiver queue names.

::: setting
event_exchange
:::

#### `event_exchange`

Default: `"celeryev"`.

Name of the event exchange.

::: warning
::: title
Warning
:::

This option is in experimental stage, please use it with caution.
:::

::: setting
event_serializer
:::

#### `event_serializer`

Default: `"json"`.

Message serialization format used when sending event messages.

::: seealso
`calling-serializers`{.interpreted-text role="ref"}.
:::

::: setting
events_logfile
:::

#### `events_logfile`

::: versionadded
5.4
:::

Default: `None`{.interpreted-text role="const"}

An optional file path for `celery events`{.interpreted-text
role="program"} to log into (defaults to [stdout]{.title-ref}).

::: setting
events_pidfile
:::

#### `events_pidfile`

::: versionadded
5.4
:::

Default: `None`{.interpreted-text role="const"}

An optional file path for `celery events`{.interpreted-text
role="program"} to create/store its PID file (default to no PID file
created).

::: setting
events_uid
:::

#### `events_uid`

::: versionadded
5.4
:::

Default: `None`{.interpreted-text role="const"}

An optional user ID to use when events `celery events`{.interpreted-text
role="program"} drops its privileges (defaults to no UID change).

::: setting
events_gid
:::

#### `events_gid`

::: versionadded
5.4
:::

Default: `None`{.interpreted-text role="const"}

An optional group ID to use when `celery events`{.interpreted-text
role="program"} daemon drops its privileges (defaults to no GID change).

::: setting
events_umask
:::

#### `events_umask`

::: versionadded
5.4
:::

Default: `None`{.interpreted-text role="const"}

An optional [umask]{.title-ref} to use when
`celery events`{.interpreted-text role="program"} creates files (log,
pid\...) when daemonizing.

::: setting
events_executable
:::

#### `events_executable`

::: versionadded
5.4
:::

Default: `None`{.interpreted-text role="const"}

An optional [python]{.title-ref} executable path for
`celery events`{.interpreted-text role="program"} to use when
deaemonizing (defaults to `sys.executable`{.interpreted-text
role="data"}).

### Remote Control Commands {#conf-control}

::: note
::: title
Note
:::

To disable remote control commands see the
`worker_enable_remote_control`{.interpreted-text role="setting"}
setting.
:::

::: setting
control_queue_ttl
:::

#### `control_queue_ttl`

Default: 300.0

Time in seconds, before a message in a remote control command queue will
expire.

If using the default of 300 seconds, this means that if a remote control
command is sent and no worker picks it up within 300 seconds, the
command is discarded.

This setting also applies to remote control reply queues.

::: setting
control_queue_expires
:::

#### `control_queue_expires`

Default: 10.0

Time in seconds, before an unused remote control command queue is
deleted from the broker.

This setting also applies to remote control reply queues.

::: setting
control_exchange
:::

#### `control_exchange`

Default: `"celery"`.

Name of the control command exchange.

::: warning
::: title
Warning
:::

This option is in experimental stage, please use it with caution.
:::

::: {#conf-logging}
::: setting
control_queue_durable
:::
:::

### `control_queue_durable`

-   **Default:** `False`
-   **Type:** `bool`

If set to `True`, the control exchange and queue will be durable ---
they will survive broker restarts.

::: setting
control_queue_exclusive
:::

### `control_queue_exclusive`

-   **Default:** `False`
-   **Type:** `bool`

If set to `True`, the control queue will be exclusive to a single
connection. This is generally not recommended in distributed
environments.

::: warning
::: title
Warning
:::

Setting both `control_queue_durable` and `control_queue_exclusive` to
`True` is not supported and will raise an error.
:::

### Logging

::: setting
worker_hijack_root_logger
:::

#### `worker_hijack_root_logger`

::: versionadded
2.2
:::

Default: Enabled by default (hijack root logger).

By default any previously configured handlers on the root logger will be
removed. If you want to customize your own logging handlers, then you
can disable this behavior by setting [worker_hijack_root_logger =
False]{.title-ref}.

::: note
::: title
Note
:::

Logging can also be customized by connecting to the
`celery.signals.setup_logging`{.interpreted-text role="signal"} signal.
:::

::: setting
worker_log_color
:::

#### `worker_log_color`

Default: Enabled if app is logging to a terminal.

Enables/disables colors in logging output by the Celery apps.

::: setting
worker_log_format
:::

#### `worker_log_format`

Default:

``` text
"[%(asctime)s: %(levelname)s/%(processName)s] %(message)s"
```

The format to use for log messages.

See the Python `logging`{.interpreted-text role="mod"} module for more
information about log formats.

::: setting
worker_task_log_format
:::

#### `worker_task_log_format`

Default:

``` text
"[%(asctime)s: %(levelname)s/%(processName)s]
    %(task_name)s[%(task_id)s]: %(message)s"
```

The format to use for log messages logged in tasks.

See the Python `logging`{.interpreted-text role="mod"} module for more
information about log formats.

::: setting
worker_redirect_stdouts
:::

#### `worker_redirect_stdouts`

Default: Enabled by default.

If enabled [stdout]{.title-ref} and [stderr]{.title-ref} will be
redirected to the current logger.

Used by `celery worker`{.interpreted-text role="program"} and
`celery beat`{.interpreted-text role="program"}.

::: setting
worker_redirect_stdouts_level
:::

#### `worker_redirect_stdouts_level`

Default: `WARNING`{.interpreted-text role="const"}.

The log level output to [stdout]{.title-ref} and [stderr]{.title-ref} is
logged as. Can be one of `DEBUG`{.interpreted-text role="const"},
`INFO`{.interpreted-text role="const"}, `WARNING`{.interpreted-text
role="const"}, `ERROR`{.interpreted-text role="const"}, or
`CRITICAL`{.interpreted-text role="const"}.

### Security {#conf-security}

::: setting
security_key
:::

#### `security_key`

Default: `None`{.interpreted-text role="const"}.

::: versionadded
2.5
:::

The relative or absolute path to a file containing the private key used
to sign messages when `message-signing`{.interpreted-text role="ref"} is
used.

::: setting
security_key_password
:::

#### `security_key_password`

Default: `None`{.interpreted-text role="const"}.

::: versionadded
5.3.0
:::

The password used to decrypt the private key when
`message-signing`{.interpreted-text role="ref"} is used.

::: setting
security_certificate
:::

#### `security_certificate`

Default: `None`{.interpreted-text role="const"}.

::: versionadded
2.5
:::

The relative or absolute path to an X.509 certificate file used to sign
messages when `message-signing`{.interpreted-text role="ref"} is used.

::: setting
security_cert_store
:::

#### `security_cert_store`

Default: `None`{.interpreted-text role="const"}.

::: versionadded
2.5
:::

The directory containing X.509 certificates used for
`message-signing`{.interpreted-text role="ref"}. Can be a glob with
wild-cards, (for example `/etc/certs/*.pem`{.interpreted-text
role="file"}).

::: setting
security_digest
:::

#### `security_digest`

Default: `sha256`{.interpreted-text role="const"}.

::: versionadded
4.3
:::

A cryptography digest used to sign messages when
`message-signing`{.interpreted-text role="ref"} is used.
<https://cryptography.io/en/latest/hazmat/primitives/cryptographic-hashes/#module-cryptography.hazmat.primitives.hashes>

### Custom Component Classes (advanced) {#conf-custom-components}

::: setting
worker_pool
:::

#### `worker_pool`

Default: `"prefork"` (`celery.concurrency.prefork:TaskPool`).

Name of the pool class used by the worker.

::: admonition
Eventlet/Gevent

Never use this option to select the eventlet or gevent pool. You must
use the `-P <celery worker -P>`{.interpreted-text role="option"} option
to `celery worker`{.interpreted-text role="program"} instead, to ensure
the monkey patches aren\'t applied too late, causing things to break in
strange ways.
:::

::: setting
worker_pool_restarts
:::

#### `worker_pool_restarts`

Default: Disabled by default.

If enabled the worker pool can be restarted using the
`pool_restart`{.interpreted-text role="control"} remote control command.

::: setting
worker_autoscaler
:::

#### `worker_autoscaler`

::: versionadded
2.2
:::

Default: `"celery.worker.autoscale:Autoscaler"`.

Name of the autoscaler class to use.

::: setting
worker_consumer
:::

#### `worker_consumer`

Default: `"celery.worker.consumer:Consumer"`.

Name of the consumer class used by the worker.

::: setting
worker_timer
:::

#### `worker_timer`

Default: `"kombu.asynchronous.hub.timer:Timer"`.

Name of the ETA scheduler class used by the worker. Default is or set by
the pool implementation.

::: setting
worker_logfile
:::

#### `worker_logfile`

::: versionadded
5.4
:::

Default: `None`{.interpreted-text role="const"}

An optional file path for `celery worker`{.interpreted-text
role="program"} to log into (defaults to [stdout]{.title-ref}).

::: setting
worker_pidfile
:::

#### `worker_pidfile`

::: versionadded
5.4
:::

Default: `None`{.interpreted-text role="const"}

An optional file path for `celery worker`{.interpreted-text
role="program"} to create/store its PID file (defaults to no PID file
created).

::: setting
worker_uid
:::

#### `worker_uid`

::: versionadded
5.4
:::

Default: `None`{.interpreted-text role="const"}

An optional user ID to use when `celery worker`{.interpreted-text
role="program"} daemon drops its privileges (defaults to no UID change).

::: setting
worker_gid
:::

#### `worker_gid`

::: versionadded
5.4
:::

Default: `None`{.interpreted-text role="const"}

An optional group ID to use when `celery worker`{.interpreted-text
role="program"} daemon drops its privileges (defaults to no GID change).

::: setting
worker_umask
:::

#### `worker_umask`

::: versionadded
5.4
:::

Default: `None`{.interpreted-text role="const"}

An optional [umask]{.title-ref} to use when
`celery worker`{.interpreted-text role="program"} creates files (log,
pid\...) when daemonizing.

::: setting
worker_executable
:::

#### `worker_executable`

::: versionadded
5.4
:::

Default: `None`{.interpreted-text role="const"}

An optional [python]{.title-ref} executable path for
`celery worker`{.interpreted-text role="program"} to use when
deaemonizing (defaults to `sys.executable`{.interpreted-text
role="data"}).

### Beat Settings (`celery beat`{.interpreted-text role="program"}) {#conf-celerybeat}

::: setting
beat_schedule
:::

#### `beat_schedule`

Default: `{}` (empty mapping).

The periodic task schedule used by `~celery.bin.beat`{.interpreted-text
role="mod"}. See `beat-entries`{.interpreted-text role="ref"}.

::: setting
beat_scheduler
:::

#### `beat_scheduler`

Default: `"celery.beat:PersistentScheduler"`.

The default scheduler class. May be set to
`"django_celery_beat.schedulers:DatabaseScheduler"` for instance, if
used alongside `django-celery-beat`{.interpreted-text role="pypi"}
extension.

Can also be set via the `celery beat -S`{.interpreted-text
role="option"} argument.

::: setting
beat_schedule_filename
:::

#### `beat_schedule_filename`

Default: `"celerybeat-schedule"`.

Name of the file used by [PersistentScheduler]{.title-ref} to store the
last run times of periodic tasks. Can be a relative or absolute path,
but be aware that the suffix [.db]{.title-ref} may be appended to the
file name (depending on Python version).

Can also be set via the `celery beat --schedule`{.interpreted-text
role="option"} argument.

::: setting
beat_sync_every
:::

#### `beat_sync_every`

Default: 0.

The number of periodic tasks that can be called before another database
sync is issued. A value of 0 (default) means sync based on timing -
default of 3 minutes as determined by scheduler.sync_every. If set to 1,
beat will call sync after every task message sent.

::: setting
beat_max_loop_interval
:::

#### `beat_max_loop_interval`

Default: 0.

The maximum number of seconds `~celery.bin.beat`{.interpreted-text
role="mod"} can sleep between checking the schedule.

The default for this value is scheduler specific. For the default Celery
beat scheduler the value is 300 (5 minutes), but for the
`django-celery-beat`{.interpreted-text role="pypi"} database scheduler
it\'s 5 seconds because the schedule may be changed externally, and so
it must take changes to the schedule into account.

Also when running Celery beat embedded
(`-B <celery worker -B>`{.interpreted-text role="option"}) on Jython as
a thread the max interval is overridden and set to 1 so that it\'s
possible to shut down in a timely manner.

::: setting
beat_cron_starting_deadline
:::

#### `beat_cron_starting_deadline`

::: versionadded
5.3
:::

Default: None.

When using cron, the number of seconds
`~celery.bin.beat`{.interpreted-text role="mod"} can look back when
deciding whether a cron schedule is due. When set to [None]{.title-ref},
cronjobs that are past due will always run immediately.

::: warning
::: title
Warning
:::

Setting this higher than 3600 (1 hour) is highly discouraged.
:::

::: setting
beat_logfile
:::

#### `beat_logfile`

::: versionadded
5.4
:::

Default: `None`{.interpreted-text role="const"}

An optional file path for `celery beat`{.interpreted-text
role="program"} to log into (defaults to [stdout]{.title-ref}).

::: setting
beat_pidfile
:::

#### `beat_pidfile`

::: versionadded
5.4
:::

Default: `None`{.interpreted-text role="const"}

An optional file path for `celery beat`{.interpreted-text
role="program"} to create/store it PID file (defaults to no PID file
created).

::: setting
beat_uid
:::

#### `beat_uid`

::: versionadded
5.4
:::

Default: `None`{.interpreted-text role="const"}

An optional user ID to use when beat `celery beat`{.interpreted-text
role="program"} drops its privileges (defaults to no UID change).

::: setting
beat_gid
:::

#### `beat_gid`

::: versionadded
5.4
:::

Default: `None`{.interpreted-text role="const"}

An optional group ID to use when `celery beat`{.interpreted-text
role="program"} daemon drops its privileges (defaults to no GID change).

::: setting
beat_umask
:::

#### `beat_umask`

::: versionadded
5.4
:::

Default: `None`{.interpreted-text role="const"}

An optional [umask]{.title-ref} to use when
`celery beat`{.interpreted-text role="program"} creates files (log,
pid\...) when daemonizing.

::: setting
beat_executable
:::

#### `beat_executable`

::: versionadded
5.4
:::

Default: `None`{.interpreted-text role="const"}

An optional [python]{.title-ref} executable path for
`celery beat`{.interpreted-text role="program"} to use when deaemonizing
(defaults to `sys.executable`{.interpreted-text role="data"}).
