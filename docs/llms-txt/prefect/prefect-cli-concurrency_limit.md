# Source: https://docs.prefect.io/v3/api-ref/python/prefect-cli-concurrency_limit.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# concurrency_limit

# `prefect.cli.concurrency_limit`

Concurrency-limit command — native cyclopts implementation.

Manage task-level concurrency limits.

## Functions

### `create` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/concurrency_limit.py#L34" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
create(tag: str, concurrency_limit: int)
```

Create a concurrency limit against a tag.

### `inspect` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/concurrency_limit.py#L63" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
inspect(tag: str)
```

View details about a concurrency limit.

### `ls` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/concurrency_limit.py#L124" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
ls()
```

View all concurrency limits.

### `reset` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/concurrency_limit.py#L167" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
reset(tag: str)
```

Resets the concurrency limit slots set on the specified tag.

### `delete` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/concurrency_limit.py#L183" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
delete(tag: str)
```

Delete the concurrency limit set on the specified tag.


Built with [Mintlify](https://mintlify.com).