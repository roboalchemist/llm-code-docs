# Source: https://docs.prefect.io/v3/api-ref/python/prefect-cli-artifact.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# artifact

# `prefect.cli.artifact`

Artifact command — native cyclopts implementation.

Inspect and delete artifacts.

## Functions

### `list_artifacts` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/artifact.py#L29" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
list_artifacts()
```

List artifacts.

### `inspect` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/artifact.py#L107" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
inspect(key: str)
```

View details about an artifact.

### `delete` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/artifact.py#L158" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
delete(key: Annotated[Optional[str], cyclopts.Parameter(help='The key of the artifact to delete.')] = None)
```

Delete an artifact.


Built with [Mintlify](https://mintlify.com).