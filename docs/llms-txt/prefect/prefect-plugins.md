# Source: https://docs.prefect.io/v3/api-ref/python/prefect-plugins.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# plugins

# `prefect.plugins`

Utilities for loading plugins that extend Prefect's functionality.

Plugins are detected by entry point definitions in package setup files.

Currently supported entrypoints:

* prefect.collections: Identifies this package as a Prefect collection that
  should be imported when Prefect is imported.

## Functions

### `safe_load_entrypoints` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/plugins.py#L20" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
safe_load_entrypoints(entrypoints: EntryPoints) -> dict[str, Union[Exception, Any]]
```

Load entry points for a group capturing any exceptions that occur.

### `load_prefect_collections` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/plugins.py#L43" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
load_prefect_collections() -> dict[str, Union[ModuleType, Exception]]
```

Load all Prefect collections that define an entrypoint in the group
`prefect.collections`.


Built with [Mintlify](https://mintlify.com).