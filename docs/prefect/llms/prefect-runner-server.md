# Source: https://docs.prefect.io/v3/api-ref/python/prefect-runner-server.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# server

# `prefect.runner.server`

## Functions

### `perform_health_check` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/runner/server.py#L40" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
perform_health_check(runner: 'Runner', delay_threshold: int | None = None) -> Callable[..., JSONResponse]
```

### `run_count` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/runner/server.py#L66" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
run_count(runner: 'Runner') -> Callable[..., int]
```

### `shutdown` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/runner/server.py#L74" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
shutdown(runner: 'Runner') -> Callable[..., JSONResponse]
```

### `build_server` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/runner/server.py#L82" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
build_server(runner: 'Runner') -> FastAPI
```

Build a FastAPI server for a runner.

**Args:**

* `runner`: the runner this server interacts with and monitors

### `start_webserver` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/runner/server.py#L102" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
start_webserver(runner: 'Runner', log_level: str | None = None) -> None
```

Run a FastAPI server for a runner.

**Args:**

* `runner`: the runner this server interacts with and monitors
* `log_level`: the log level to use for the server

## Classes

### `RunnerGenericFlowRunRequest` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/runner/server.py#L34" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>


Built with [Mintlify](https://mintlify.com).