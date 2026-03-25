# Source: https://docs.kedro.org/en/stable/api/kedro.utils/index.md

# kedro.utils

## kedro.utils

This module provides a set of helper functions being used across different components of kedro package.

| Name                                                                | Type        | Description                                                             |
| ------------------------------------------------------------------- | ----------- | ----------------------------------------------------------------------- |
| [`find_kedro_project`](#kedro.utils.find_kedro_project)             | Function    | Given a path, find a Kedro project associated with it.                  |
| [`is_kedro_project`](#kedro.utils.is_kedro_project)                 | Function    | Evaluate if a given path is a root directory of a Kedro project or not. |
| [`load_obj`](#kedro.utils.load_obj)                                 | Function    | Extract an object from a given path.                                    |
| [`experimental`](#kedro.utils.experimental)                         | Decorator   | Decorator to mark a function or class as experimental.                  |
| [`KedroExperimentalWarning`](#kedro.utils.KedroExperimentalWarning) | UserWarning | Warning raised when using an experimental Kedro feature.                |

## kedro.utils.find_kedro_project

```
find_kedro_project(current_dir)
```

Given a path, find a Kedro project associated with it.

Can be

- Itself, if a path is a root directory of a Kedro project.
- One of its parents, if self is not a Kedro project but one of the parent path is.
- None, if neither self nor any parent path is a Kedro project.

Returns:

- `Any` – Kedro project associated with a given path,
- `Any` – or None if no relevant Kedro project is found.

Source code in `kedro/utils.py`

```
def find_kedro_project(current_dir: Path) -> Any:  # pragma: no cover
    """Given a path, find a Kedro project associated with it.

    Can be:
        - Itself, if a path is a root directory of a Kedro project.
        - One of its parents, if self is not a Kedro project but one of the parent path is.
        - None, if neither self nor any parent path is a Kedro project.

    Returns:
        Kedro project associated with a given path,
        or None if no relevant Kedro project is found.
    """
    paths_to_check = [current_dir, *list(current_dir.parents)]
    for parent_dir in paths_to_check:
        if is_kedro_project(parent_dir):
            return parent_dir
    return None
```

## kedro.utils.is_kedro_project

```
is_kedro_project(project_path)
```

Evaluate if a given path is a root directory of a Kedro project or not.

Parameters:

- **`project_path`** (`str | Path`) – Path to be tested for being a root of a Kedro project.

Returns:

- `bool` – True if a given path is a root directory of a Kedro project, otherwise False.

Source code in `kedro/utils.py`

```
def is_kedro_project(project_path: str | Path) -> bool:
    """Evaluate if a given path is a root directory of a Kedro project or not.

    Args:
        project_path: Path to be tested for being a root of a Kedro project.

    Returns:
        True if a given path is a root directory of a Kedro project, otherwise False.
    """
    metadata_file = Path(project_path).expanduser().resolve() / _PYPROJECT
    if not metadata_file.is_file():
        return False

    try:
        return "[tool.kedro]" in metadata_file.read_text(encoding="utf-8")
    except Exception:
        return False
```

## kedro.utils.load_obj

```
load_obj(obj_path, default_obj_path='')
```

Extract an object from a given path.

Parameters:

- **`obj_path`** (`str`) – Path to an object to be extracted, including the object name.
- **`default_obj_path`** (`str`, default: `''` ) – Default object path.

Returns:

- `Any` – Extracted object.

Raises:

- `AttributeError` – When the object does not have the given named attribute.

Source code in `kedro/utils.py`

```
def load_obj(obj_path: str, default_obj_path: str = "") -> Any:
    """Extract an object from a given path.

    Args:
        obj_path: Path to an object to be extracted, including the object name.
        default_obj_path: Default object path.

    Returns:
        Extracted object.

    Raises:
        AttributeError: When the object does not have the given named attribute.

    """
    obj_path_list = obj_path.rsplit(".", 1)
    obj_path = obj_path_list.pop(0) if len(obj_path_list) > 1 else default_obj_path
    obj_name = obj_path_list[0]
    module_obj = importlib.import_module(obj_path)
    return getattr(module_obj, obj_name)
```

## kedro.utils.KedroExperimentalWarning

Bases: `UserWarning`

Warning raised when using an experimental Kedro feature.

## kedro.utils.experimental

```
experimental(obj)
```

Mark a function or class as experimental.

Emits a `KedroExperimentalWarning` when invoked (for functions) or instantiated (for classes). The original API remains fully usable.

Parameters:

- **`obj`** (`Callable | type`) – The function or class to wrap.

Returns:

- `Callable | type` – A wrapped version of the object that emits warnings on use.

Example:

```
@experimental
def sample_func(a, b):
    return a + b

@experimental
class SampleClass:
def __init__(self, x):
    self.x = x
```

Source code in `kedro/utils.py`

````
def experimental(obj: Callable | type) -> Callable | type:
    """Mark a function or class as experimental.

    Emits a ``KedroExperimentalWarning`` when invoked (for functions) or
    instantiated (for classes). The original API remains fully usable.

    Args:
        obj: The function or class to wrap.

    Returns:
        A wrapped version of the object that emits warnings on use.

    Example:
    ```python

    @experimental
    def sample_func(a, b):
        return a + b

    @experimental
    class SampleClass:
    def __init__(self, x):
        self.x = x
    ```
    """
    warning_message = " is experimental and may change in future Kedro releases."
    warned_flag = "__kedro_experimental_warned__"

    # Function or method
    if callable(obj) and not isinstance(obj, type):

        @wraps(obj)
        def wrapper(*args, **kwargs):  # type: ignore[no-untyped-def]
            if not getattr(wrapper, warned_flag, False):
                warnings.warn(
                    f"{obj.__name__}{warning_message}",
                    category=KedroExperimentalWarning,
                    stacklevel=2,
                )
                setattr(wrapper, warned_flag, True)
            return obj(*args, **kwargs)

        setattr(wrapper, "__kedro_experimental__", True)
        setattr(wrapper, "__wrapped__", obj)

        _inject_experimental_doc(wrapper)
        return wrapper

    # Class
    if isinstance(obj, type):
        original_init = obj.__init__

        @wraps(original_init)
        def new_init(self, *args, **kwargs):  # type: ignore[no-untyped-def]
            if not getattr(obj, warned_flag, False):
                warnings.warn(
                    f"{obj.__name__}{warning_message}",
                    category=KedroExperimentalWarning,
                    stacklevel=2,
                )
                setattr(obj, warned_flag, True)
            return original_init(self, *args, **kwargs)

        obj.__init__ = new_init
        setattr(obj, "__kedro_experimental__", True)
        setattr(new_init, "_ wrapped _", original_init)

        _inject_experimental_doc(obj)
        return obj

    return obj
````
