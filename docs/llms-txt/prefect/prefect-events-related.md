# Source: https://docs.prefect.io/v3/api-ref/python/prefect-events-related.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# related

# `prefect.events.related`

## Functions

### `tags_as_related_resources` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/events/related.py#L34" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
tags_as_related_resources(tags: Iterable[str]) -> List[RelatedResource]
```

### `object_as_related_resource` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/events/related.py#L46" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
object_as_related_resource(kind: str, role: str, object: Any) -> RelatedResource
```

### `related_resources_from_run_context` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/events/related.py#L60" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
related_resources_from_run_context(client: 'PrefectClient', exclude: Optional[Set[str]] = None) -> List[RelatedResource]
```


Built with [Mintlify](https://mintlify.com).