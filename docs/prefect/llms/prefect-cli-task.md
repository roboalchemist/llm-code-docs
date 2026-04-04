# Source: https://docs.prefect.io/v3/api-ref/python/prefect-cli-task.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# task

# `prefect.cli.task`

Task command — native cyclopts implementation.

Work with task scheduling.

## Functions

### `serve` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/task.py#L44" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
serve(entrypoints: Annotated[Optional[list[str]], cyclopts.Parameter(help='The paths to one or more tasks, in the form of `./path/to/file.py:task_func_name`.')] = None)
```

Serve the provided tasks so that their runs may be submitted to and executed in the engine.


Built with [Mintlify](https://mintlify.com).