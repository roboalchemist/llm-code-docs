# Source: https://docs.prefect.io/v3/api-ref/python/prefect-cli-work_queue.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# work_queue

# `prefect.cli.work_queue`

Work queue command — native cyclopts implementation.

Manage work queues.

## Functions

### `create` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/work_queue.py#L68" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
create(name: Annotated[str, cyclopts.Parameter(help='The unique name to assign this work queue')])
```

Create a work queue.

### `set_concurrency_limit` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/work_queue.py#L137" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
set_concurrency_limit(name: Annotated[str, cyclopts.Parameter(help='The name or ID of the work queue')], limit: Annotated[int, cyclopts.Parameter(help='The concurrency limit to set on the queue.')])
```

Set a concurrency limit on a work queue.

### `clear_concurrency_limit` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/work_queue.py#L188" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
clear_concurrency_limit(name: Annotated[str, cyclopts.Parameter(help='The name or ID of the work queue to clear')])
```

Clear any concurrency limits from a work queue.

### `pause` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/work_queue.py#L234" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
pause(name: Annotated[str, cyclopts.Parameter(help='The name or ID of the work queue to pause')])
```

Pause a work queue.

### `resume` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/work_queue.py#L292" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
resume(name: Annotated[str, cyclopts.Parameter(help='The name or ID of the work queue to resume')])
```

Resume a paused work queue.

### `inspect` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/work_queue.py#L337" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
inspect(name: Annotated[str, cyclopts.Parameter(help='The name or ID of the work queue to inspect')])
```

Inspect a work queue by ID.

### `ls` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/work_queue.py#L410" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
ls()
```

View all work queues.

### `preview` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/work_queue.py#L524" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
preview(name: Annotated[str, cyclopts.Parameter(help='The name or ID of the work queue to preview')])
```

Preview a work queue.

### `delete` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/work_queue.py#L622" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
delete(name: Annotated[str, cyclopts.Parameter(help='The name or ID of the work queue to delete')])
```

Delete a work queue by ID.

### `read_wq_runs` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/work_queue.py#L671" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
read_wq_runs(name: Annotated[str, cyclopts.Parameter(help='The name or ID of the work queue to poll')])
```

Get runs in a work queue.

Note that this will trigger an artificial poll of the work queue.


Built with [Mintlify](https://mintlify.com).