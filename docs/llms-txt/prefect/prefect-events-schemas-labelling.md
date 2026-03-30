# Source: https://docs.prefect.io/v3/api-ref/python/prefect-events-schemas-labelling.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# labelling

# `prefect.events.schemas.labelling`

## Classes

### `LabelDiver` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/events/schemas/labelling.py#L6" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

The LabelDiver supports templating use cases for any Labelled object, by
presenting the labels as a graph of objects that may be accessed by attribute.  For
example:

```python  theme={null}
diver = LabelDiver({
    'hello.world': 'foo',
    'hello.world.again': 'bar'
})

assert str(diver.hello.world) == 'foo'
assert str(diver.hello.world.again) == 'bar'
```

### `Labelled` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/events/schemas/labelling.py#L76" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

**Methods:**

#### `as_label_value_array` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/events/schemas/labelling.py#L96" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
as_label_value_array(self) -> List[Dict[str, str]]
```

#### `get` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/events/schemas/labelling.py#L93" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
get(self, label: str, default: Optional[str] = None) -> Optional[str]
```

#### `has_all_labels` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/events/schemas/labelling.py#L103" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
has_all_labels(self, labels: Dict[str, str]) -> bool
```

#### `items` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/events/schemas/labelling.py#L80" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
items(self) -> Iterable[Tuple[str, str]]
```

#### `keys` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/events/schemas/labelling.py#L77" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
keys(self) -> Iterable[str]
```

#### `labels` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/events/schemas/labelling.py#L100" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
labels(self) -> LabelDiver
```


Built with [Mintlify](https://mintlify.com).