# Source: https://docs.prefect.io/v3/api-ref/python/prefect-utilities-dispatch.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# dispatch

# `prefect.utilities.dispatch`

Provides methods for performing dynamic dispatch for actions on base type to one of its
subtypes.

Example:

```python  theme={null}
@register_base_type
class Base:
    @classmethod
    def __dispatch_key__(cls):
        return cls.__name__.lower()


class Foo(Base):
    ...

key = get_dispatch_key(Foo)  # 'foo'
lookup_type(Base, key) # Foo
```

## Functions

### `get_registry_for_type` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/dispatch.py#L33" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
get_registry_for_type(cls: T) -> Optional[dict[str, T]]
```

Get the first matching registry for a class or any of its base classes.

If not found, `None` is returned.

### `get_dispatch_key` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/dispatch.py#L57" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
get_dispatch_key(cls_or_instance: Any, allow_missing: bool = False) -> Optional[str]
```

Retrieve the unique dispatch key for a class type or instance.

This key is defined at the `__dispatch_key__` attribute. If it is a callable, it
will be resolved.

If `allow_missing` is `False`, an exception will be raised if the attribute is not
defined or the key is null. If `True`, `None` will be returned in these cases.

### `register_base_type` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/dispatch.py#L114" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
register_base_type(cls: T) -> T
```

Register a base type allowing child types to be registered for dispatch with
`register_type`.

The base class may or may not define a `__dispatch_key__` to allow lookups of the
base type.

### `register_type` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/dispatch.py#L140" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
register_type(cls: T) -> T
```

Register a type for lookup with dispatch.

The type or one of its parents must define a unique `__dispatch_key__`.

One of the classes base types must be registered using `register_base_type`.

### `lookup_type` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/dispatch.py#L197" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
lookup_type(cls: T, dispatch_key: str) -> T
```

Look up a dispatch key in the type registry for the given class.


Built with [Mintlify](https://mintlify.com).