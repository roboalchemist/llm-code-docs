# Source: https://docs.prefect.io/v3/api-ref/python/prefect-logging-handlers.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# handlers

# `prefect.logging.handlers`

## Functions

### `set_api_log_sink` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/logging/handlers.py#L55" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
set_api_log_sink(sink: Callable[[Dict[str, Any]], None] | None) -> None
```

### `emit_api_log` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/logging/handlers.py#L60" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
emit_api_log(log: Dict[str, Any]) -> None
```

## Classes

### `APILogWorker` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/logging/handlers.py#L68" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

**Methods:**

#### `instance` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/logging/handlers.py#L100" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
instance(cls: Type[Self], *args: Any) -> Self
```

#### `max_batch_size` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/logging/handlers.py#L70" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
max_batch_size(self) -> int
```

#### `min_interval` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/logging/handlers.py#L78" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
min_interval(self) -> float | None
```

### `APILogHandler` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/logging/handlers.py#L114" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

A logging handler that sends logs to the Prefect API.

Sends log records to the `APILogWorker` which manages sending batches of logs in
the background.

**Methods:**

#### `aflush` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/logging/handlers.py#L149" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
aflush(cls) -> None
```

Tell the `APILogWorker` to send any currently enqueued logs and block until
completion.

#### `emit` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/logging/handlers.py#L159" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
emit(self, record: logging.LogRecord) -> None
```

Send a log to the `APILogWorker`

#### `flush` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/logging/handlers.py#L122" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
flush(self) -> None
```

Tell the `APILogWorker` to send any currently enqueued logs and block until
completion.

Use `aflush` from async contexts instead.

#### `handleError` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/logging/handlers.py#L177" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
handleError(self, record: logging.LogRecord) -> None
```

#### `prepare` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/logging/handlers.py#L200" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
prepare(self, record: logging.LogRecord) -> Dict[str, Any]
```

Convert a `logging.LogRecord` to the API `LogCreate` schema and serialize.

This infers the linked flow or task run from the log record or the current
run context.

If a flow run id cannot be found, the log will be dropped.

Logs exceeding the maximum size will be dropped.

### `WorkerAPILogHandler` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/logging/handlers.py#L289" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

**Methods:**

#### `aflush` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/logging/handlers.py#L149" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
aflush(cls) -> None
```

Tell the `APILogWorker` to send any currently enqueued logs and block until
completion.

#### `emit` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/logging/handlers.py#L290" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
emit(self, record: logging.LogRecord) -> None
```

#### `emit` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/logging/handlers.py#L159" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
emit(self, record: logging.LogRecord) -> None
```

Send a log to the `APILogWorker`

#### `flush` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/logging/handlers.py#L122" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
flush(self) -> None
```

Tell the `APILogWorker` to send any currently enqueued logs and block until
completion.

Use `aflush` from async contexts instead.

#### `handleError` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/logging/handlers.py#L177" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
handleError(self, record: logging.LogRecord) -> None
```

#### `prepare` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/logging/handlers.py#L298" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
prepare(self, record: logging.LogRecord) -> Dict[str, Any]
```

Convert a `logging.LogRecord` to the API `LogCreate` schema and serialize.

This will add in the worker id to the log.

Logs exceeding the maximum size will be dropped.

#### `prepare` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/logging/handlers.py#L200" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
prepare(self, record: logging.LogRecord) -> Dict[str, Any]
```

Convert a `logging.LogRecord` to the API `LogCreate` schema and serialize.

This infers the linked flow or task run from the log record or the current
run context.

If a flow run id cannot be found, the log will be dropped.

Logs exceeding the maximum size will be dropped.

### `PrefectConsoleHandler` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/logging/handlers.py#L327" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

**Methods:**

#### `emit` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/logging/handlers.py#L367" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
emit(self, record: logging.LogRecord) -> None
```


Built with [Mintlify](https://mintlify.com).