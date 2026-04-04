# Source: https://docs.prefect.io/v3/api-ref/python/prefect-workers-server.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# server

# `prefect.workers.server`

## Functions

### `build_healthcheck_server` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/workers/server.py#L11" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
build_healthcheck_server(worker: BaseWorker[Any, Any, Any], query_interval_seconds: float, log_level: str = 'error') -> uvicorn.Server
```

Build a healthcheck FastAPI server for a worker.

**Args:**

* `worker`: the worker whose health we will check
* `log_level`: the log

### `start_healthcheck_server` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/workers/server.py#L53" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
start_healthcheck_server(worker: BaseWorker[Any, Any, Any], query_interval_seconds: float, log_level: str = 'error') -> None
```

Run a healthcheck FastAPI server for a worker.

**Args:**

* `worker`: the worker whose health we will check
* `log_level`: the log level to use for the server


Built with [Mintlify](https://mintlify.com).