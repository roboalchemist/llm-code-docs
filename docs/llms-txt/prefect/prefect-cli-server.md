# Source: https://docs.prefect.io/v3/api-ref/python/prefect-cli-server.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# server

# `prefect.cli.server`

Server command — native cyclopts implementation.

Start and manage the Prefect server.

## Functions

### `start` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/server.py#L46" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
start()
```

Start a Prefect server instance.

### `status` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/server.py#L243" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
status()
```

Check the status of the Prefect server.

### `stop` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/server.py#L356" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
stop()
```

Stop a Prefect server instance running in the background.

### `reset` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/server.py#L382" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
reset()
```

Drop and recreate all Prefect database tables.

### `upgrade` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/server.py#L413" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
upgrade()
```

Upgrade the Prefect database.

### `downgrade` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/server.py#L454" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
downgrade()
```

Downgrade the Prefect database.

### `revision` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/server.py#L498" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
revision()
```

Create a new migration for the Prefect database.

### `stamp` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/server.py#L522" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
stamp(revision: str)
```

Stamp the revision table with the given revision; don't run any migrations.

### `list_services` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/server.py#L537" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
list_services()
```

List all available services and their status.

### `start_services` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/server.py#L560" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
start_services()
```

Start all enabled Prefect services in one process.

### `stop_services` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/server.py#L628" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
stop_services()
```

Stop any background Prefect services that were started.

### `run_manager_process` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/server.py#L679" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
run_manager_process()
```

Internal entrypoint for background services.


Built with [Mintlify](https://mintlify.com).