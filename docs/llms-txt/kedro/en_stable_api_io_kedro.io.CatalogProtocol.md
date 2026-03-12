# Source: https://docs.kedro.org/en/stable/api/io/kedro.io.CatalogProtocol/index.md

## kedro.io.CatalogProtocol

Bases: `Protocol[_C, _DS]`

### \_datasets

```
_datasets
```

### __contains__

```
__contains__(ds_name)
```

Check if a dataset is in the catalog.

Source code in `kedro/io/core.py`

```
def __contains__(self, ds_name: str) -> bool:
    """Check if a dataset is in the catalog."""
    ...
```

### __getitem__

```
__getitem__(ds_name)
```

Get a dataset by name from an internal collection of datasets.

Source code in `kedro/io/core.py`

```
def __getitem__(self, ds_name: str) -> _DS:
    """Get a dataset by name from an internal collection of datasets."""
    ...
```

### __iter__

```
__iter__()
```

Returns an iterator for the object.

Source code in `kedro/io/core.py`

```
def __iter__(self) -> Iterator[str]:
    """Returns an iterator for the object."""
    ...
```

### __repr__

```
__repr__()
```

Returns the canonical string representation of the object.

Source code in `kedro/io/core.py`

```
def __repr__(self) -> str:
    """Returns the canonical string representation of the object."""
    ...
```

### __setitem__

```
__setitem__(key, value)
```

Adds dataset using the given key as a dataset name and the provided data as the value.

Source code in `kedro/io/core.py`

```
def __setitem__(self, key: str, value: Any) -> None:
    """Adds dataset using the given key as a dataset name and the provided data as the value."""
    ...
```

### confirm

```
confirm(name)
```

Confirm a dataset by its name.

Source code in `kedro/io/core.py`

```
def confirm(self, name: str) -> None:
    """Confirm a dataset by its name."""
    ...
```

### exists

```
exists(name)
```

Checks whether registered dataset exists by calling its `exists()` method.

Source code in `kedro/io/core.py`

```
def exists(self, name: str) -> bool:
    """Checks whether registered dataset exists by calling its `exists()` method."""
    ...
```

### from_config

```
from_config(catalog)
```

Create a catalog instance from configuration.

Source code in `kedro/io/core.py`

```
@classmethod
def from_config(cls, catalog: dict[str, dict[str, Any]] | None) -> _C:
    """Create a catalog instance from configuration."""
    ...
```

### get

```
get(key, fallback_to_runtime_pattern=False)
```

Get a dataset by name from an internal collection of datasets.

Source code in `kedro/io/core.py`

```
def get(self, key: str, fallback_to_runtime_pattern: bool = False) -> _DS | None:
    """Get a dataset by name from an internal collection of datasets."""
    ...
```

### items

```
items()
```

List all dataset names and datasets registered in the catalog.

Source code in `kedro/io/core.py`

```
def items(self) -> List[tuple[str, _DS]]:  # noqa: UP006
    """List all dataset names and datasets registered in the catalog."""
    ...
```

### keys

```
keys()
```

List all dataset names registered in the catalog.

Source code in `kedro/io/core.py`

```
def keys(self) -> List[str]:  # noqa: UP006
    """List all dataset names registered in the catalog."""
    ...
```

### load

```
load(name, version=None)
```

Load data from a registered dataset.

Source code in `kedro/io/core.py`

```
def load(self, name: str, version: str | None = None) -> Any:
    """Load data from a registered dataset."""
    ...
```

### release

```
release(name)
```

Release any cached data associated with a dataset.

Source code in `kedro/io/core.py`

```
def release(self, name: str) -> None:
    """Release any cached data associated with a dataset."""
    ...
```

### save

```
save(name, data)
```

Save data to a registered dataset.

Source code in `kedro/io/core.py`

```
def save(self, name: str, data: Any) -> None:
    """Save data to a registered dataset."""
    ...
```

### values

```
values()
```

List all datasets registered in the catalog.

Source code in `kedro/io/core.py`

```
def values(self) -> List[_DS]:  # noqa: UP006
    """List all datasets registered in the catalog."""
    ...
```
