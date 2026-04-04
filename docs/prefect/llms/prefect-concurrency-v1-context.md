# Source: https://docs.prefect.io/v3/api-ref/python/prefect-concurrency-v1-context.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# context

# `prefect.concurrency.v1.context`

## Classes

### `ConcurrencyContext` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/concurrency/v1/context.py#L11" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

**Methods:**

#### `get` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/context.py#L194" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
get(cls: type[Self]) -> Optional[Self]
```

Get the current context instance

#### `model_copy` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/context.py#L198" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
model_copy(self: Self) -> Self
```

Duplicate the context model, optionally choosing which fields to include, exclude, or change.

**Attributes:**

* `include`: Fields to include in new model.
* `exclude`: Fields to exclude from new model, as with values this takes precedence over include.
* `update`: Values to change/add in the new model. Note: the data is not validated before creating
  the new model - you should trust this data.
* `deep`: Set to `True` to make a deep copy of the model.

**Returns:**

* A new model instance.

#### `serialize` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/context.py#L219" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
serialize(self, include_secrets: bool = True) -> dict[str, Any]
```

Serialize the context model to a dictionary that can be pickled with cloudpickle.


Built with [Mintlify](https://mintlify.com).