# Source: https://docs.kedro.org/en/stable/api/config/kedro.config.AbstractConfigLoader/index.md

## kedro.config.AbstractConfigLoader

```
AbstractConfigLoader(conf_source, env=None, runtime_params=None, **kwargs)
```

Bases: `UserDict`

`AbstractConfigLoader` is the abstract base class for all `ConfigLoader` implementations. All user-defined `ConfigLoader` implementations should inherit from `AbstractConfigLoader` and implement all relevant abstract methods.

Source code in `kedro/config/abstract_config.py`

```
def __init__(
    self,
    conf_source: str | Path,
    env: str | None = None,
    runtime_params: dict[str, Any] | None = None,
    **kwargs: Any,
):
    super().__init__()
    self.conf_source = conf_source
    self.env = env
    self.runtime_params = runtime_params or {}
```

### conf_source

```
conf_source = conf_source
```

### env

```
env = env
```

### runtime_params

```
runtime_params = runtime_params or {}
```

### get

```
get(key, default=None)
```

D.get(k[,d]) -> D[k] if k in D, else d. d defaults to None.

Source code in `kedro/config/abstract_config.py`

```
def get(self, key: str, default: Any = None) -> Any:
    "D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None."
    try:
        return self[key]
    except KeyError:
        return default
```
