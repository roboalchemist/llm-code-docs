# Source: https://docs.prefect.io/v3/api-ref/python/prefect-cli-shell.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# shell

# `prefect.cli.shell`

Shell command — native cyclopts implementation.

Run shell commands as Prefect flows.

## Functions

### `output_stream` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/shell.py#L26" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
output_stream(pipe: IO[str], logger_function: Callable[[str], None]) -> None
```

Read from a pipe line by line and log using the provided logging function.

### `output_collect` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/shell.py#L33" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
output_collect(pipe: IO[str], container: list[str]) -> None
```

Collect output from a subprocess pipe and store it in a container list.

### `run_shell_process` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/shell.py#L40" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
run_shell_process(command: str, log_output: bool = True, stream_stdout: bool = False, log_stderr: bool = False, popen_kwargs: Optional[dict[str, Any]] = None)
```

Execute a shell command and log its output.

Designed for use within Prefect flows to run shell commands as part of
task execution.

**Args:**

* `command`: The shell command to execute.
* `log_output`: If True, log stdout/stderr to Prefect logs.
* `stream_stdout`: If True, stream stdout to Prefect logs.
* `log_stderr`: If True, log stderr to Prefect logs.
* `popen_kwargs`: Additional keyword arguments for subprocess.Popen.

### `watch` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/shell.py#L113" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
watch(command: str)
```

Execute a shell command and observe it as a Prefect flow.

### `serve` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/shell.py#L159" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
serve(command: str)
```

Create and serve a deployment that runs a shell command.


Built with [Mintlify](https://mintlify.com).