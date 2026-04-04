# Source: https://docs.kedro.org/en/stable/api/io/kedro.io.MemoryDataset/index.md

## kedro.io.MemoryDataset

```
MemoryDataset(data=_EMPTY, copy_mode=None, metadata=None)
```

Bases: `AbstractDataset`

`MemoryDataset` loads and saves data from/to an in-memory Python object. The `_EPHEMERAL` attribute is set to True to indicate MemoryDataset's non-persistence.

Example:

```
from kedro.io import MemoryDataset
import pandas as pd

data = pd.DataFrame({"col1": [1, 2], "col2": [4, 5], "col3": [5, 6]})
dataset = MemoryDataset(data=data)

loaded_data = dataset.load()
assert loaded_data.equals(data)

new_data = pd.DataFrame({"col1": [1, 2], "col2": [4, 5]})
dataset.save(new_data)
reloaded_data = dataset.load()
assert reloaded_data.equals(new_data)
```

Parameters:

- **`data`** (`Any`, default: `_EMPTY` ) – Python object containing the data.
- **`copy_mode`** (`TCopyMode | None`, default: `None` ) – The copy mode used to copy the data. Possible values are: "deepcopy", "copy" and "assign". If not provided, it is inferred based on the data type.
- **`metadata`** (`dict[str, Any] | None`, default: `None` ) – Any arbitrary metadata. This is ignored by Kedro, but may be consumed by users or external plugins.

Source code in `kedro/io/memory_dataset.py`

```
def __init__(
    self,
    data: Any = _EMPTY,
    copy_mode: TCopyMode | None = None,
    metadata: dict[str, Any] | None = None,
):
    """Creates a new instance of ``MemoryDataset`` pointing to the
    provided Python object.

    Args:
        data: Python object containing the data.
        copy_mode: The copy mode used to copy the data. Possible
            values are: "deepcopy", "copy" and "assign". If not
            provided, it is inferred based on the data type.
        metadata: Any arbitrary metadata.
            This is ignored by Kedro, but may be consumed by users or external plugins.
    """
    self._data = _EMPTY
    self._copy_mode = copy_mode
    self.metadata = metadata
    self._EPHEMERAL = True
    if data is not _EMPTY:
        self.save.__wrapped__(self, data)  # type: ignore[attr-defined]
```

### \_EPHEMERAL

```
_EPHEMERAL = True
```

### \_copy_mode

```
_copy_mode = copy_mode
```

### \_data

```
_data = _EMPTY
```

### metadata

```
metadata = metadata
```

### \_describe

```
_describe()
```

Source code in `kedro/io/memory_dataset.py`

```
def _describe(self) -> dict[str, Any]:
    if self._data is not _EMPTY:
        return {"data": f"<{type(self._data).__name__}>"}
    # the string representation of datasets leaves out __init__
    # arguments that are empty/None, equivalent here is _EMPTY
    return {"data": None}  # pragma: no cover
```

### \_exists

```
_exists()
```

Source code in `kedro/io/memory_dataset.py`

```
def _exists(self) -> bool:
    return self._data is not _EMPTY
```

### \_release

```
_release()
```

Source code in `kedro/io/memory_dataset.py`

```
def _release(self) -> None:
    self._data = _EMPTY
```

### load

```
load()
```

Source code in `kedro/io/memory_dataset.py`

```
def load(self) -> Any:
    if self._data is _EMPTY:
        raise DatasetError("Data for MemoryDataset has not been saved yet.")

    copy_mode = self._copy_mode or _infer_copy_mode(self._data)
    data = _copy_with_mode(self._data, copy_mode=copy_mode)
    return data
```

### save

```
save(data)
```

Source code in `kedro/io/memory_dataset.py`

```
def save(self, data: Any) -> None:
    copy_mode = self._copy_mode or _infer_copy_mode(data)
    self._data = _copy_with_mode(data, copy_mode=copy_mode)
```
