# Source: https://docs.prefect.io/v3/api-ref/python/prefect-cli-dev.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# dev

# `prefect.cli.dev`

Dev command — native cyclopts implementation.

Internal Prefect development commands.

## Functions

### `build_docs` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/dev.py#L61" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
build_docs(schema_path: Optional[str] = None)
```

Builds REST API reference documentation for static display.

### `build_ui` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/dev.py#L87" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
build_ui(no_install: bool = False)
```

Installs dependencies and builds UI locally. Requires npm.

### `ui` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/dev.py#L122" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
ui()
```

Starts a hot-reloading development UI.

### `api` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/dev.py#L138" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
api()
```

Starts a hot-reloading development API.

### `start` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/dev.py#L221" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
start()
```

Starts a hot-reloading development server with API, UI, and agent processes.

### `build_image` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/dev.py#L255" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
build_image()
```

Build a docker image for development.

### `container` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/dev.py#L351" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
container()
```

Run a docker container with local code mounted and installed.


Built with [Mintlify](https://mintlify.com).