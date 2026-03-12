# Source: https://docs.kedro.org/en/stable/api/io/kedro.io.AbstractDataset/index.md

## kedro.io.AbstractDataset

Bases: `ABC`, `Generic[_DI, _DO]`

`AbstractDataset` is the base class for all dataset implementations.

All dataset implementations should extend this abstract class and implement the methods marked as abstract. If a specific dataset implementation cannot be used in conjunction with the `ParallelRunner`, such user-defined dataset should have the attribute `_SINGLE_PROCESS = True`. Example:

```
from pathlib import Path, PurePosixPath
import pandas as pd
from kedro.io import AbstractDataset


class MyOwnDataset(AbstractDataset[pd.DataFrame, pd.DataFrame]):
    def __init__(self, filepath, param1, param2=True):
        self._filepath = PurePosixPath(filepath)
        self._param1 = param1
        self._param2 = param2

    def load(self) -> pd.DataFrame:
        return pd.read_csv(self._filepath)

    def save(self, df: pd.DataFrame) -> None:
        df.to_csv(str(self._filepath))

    def _exists(self) -> bool:
        return Path(self._filepath.as_posix()).exists()

    def _describe(self):
        return dict(param1=self._param1, param2=self._param2)
```

Example catalog.yml specification:

```
my_dataset:
    type: <path-to-my-own-dataset>.MyOwnDataset
    filepath: data/01_raw/my_data.csv
    param1: <param1-value> # param1 is a required argument
    # param2 will be True by default
```

### \_EPHEMERAL

```
_EPHEMERAL = False
```

### \_logger

```
_logger
```

### __init_subclass__

```
__init_subclass__(**kwargs)
```

Customizes the behavior of subclasses of AbstractDataset during their creation. This method is automatically invoked when a subclass of AbstractDataset is defined.

Decorates the `load` and `save` methods provided by the class. If `_load` or `_save` are defined, alias them as a prerequisite.

Source code in `kedro/io/core.py`

```
def __init_subclass__(cls, **kwargs: Any) -> None:
    """Customizes the behavior of subclasses of AbstractDataset during
    their creation. This method is automatically invoked when a subclass
    of AbstractDataset is defined.

    Decorates the `load` and `save` methods provided by the class.
    If `_load` or `_save` are defined, alias them as a prerequisite.
    """

    # Save the original __init__ method of the subclass
    init_func: Callable = cls.__init__

    @wraps(init_func)
    def new_init(self, *args, **kwargs) -> None:  # type: ignore[no-untyped-def]
        """Executes the original __init__, then save the arguments used
        to initialize the instance.
        """
        # Call the original __init__ method
        init_func(self, *args, **kwargs)
        # Capture and save the arguments passed to the original __init__
        self._init_args = getcallargs(init_func, self, *args, **kwargs)
        self._init_args.pop("self", None)  # removed to prevent recursion

    # Replace the subclass's __init__ with the new_init
    # A hook for subclasses to capture initialization arguments and save them
    # in the AbstractDataset._init_args field
    cls.__init__ = new_init  # type: ignore[method-assign]

    super().__init_subclass__(**kwargs)

    if hasattr(cls, "_load") and not cls._load.__qualname__.startswith("Abstract"):
        cls.load = cls._load  # type: ignore[method-assign]

    if hasattr(cls, "_save") and not cls._save.__qualname__.startswith("Abstract"):
        cls.save = cls._save  # type: ignore[method-assign]

    if hasattr(cls, "load") and not cls.load.__qualname__.startswith("Abstract"):
        cls.load = cls._load_wrapper(  # type: ignore[assignment]
            cls.load
            if not getattr(cls.load, "__loadwrapped__", False)
            else cls.load.__wrapped__  # type: ignore[attr-defined]
        )

    if hasattr(cls, "save") and not cls.save.__qualname__.startswith("Abstract"):
        cls.save = cls._save_wrapper(  # type: ignore[assignment]
            cls.save
            if not getattr(cls.save, "__savewrapped__", False)
            else cls.save.__wrapped__  # type: ignore[attr-defined]
        )
```

### __repr__

```
__repr__()
```

Source code in `kedro/io/core.py`

```
def __repr__(self) -> str:
    object_description = self._describe()
    if isinstance(object_description, dict) and all(
        isinstance(key, str) for key in object_description
    ):
        return self._pretty_repr(object_description)

    self._logger.warning(
        f"'{type(self).__module__}.{type(self).__name__}' is a subclass of AbstractDataset and it must "
        f"implement the '_describe' method following the signature of AbstractDataset's '_describe'."
    )
    return f"{type(self).__module__}.{type(self).__name__}()"
```

### \_copy

```
_copy(**overwrite_params)
```

Source code in `kedro/io/core.py`

```
def _copy(self, **overwrite_params: Any) -> AbstractDataset:
    dataset_copy = copy.deepcopy(self)
    for name, value in overwrite_params.items():
        setattr(dataset_copy, name, value)
    return dataset_copy
```

### \_describe

```
_describe()
```

Source code in `kedro/io/core.py`

```
@abc.abstractmethod
def _describe(self) -> dict[str, Any]:
    raise NotImplementedError(
        f"'{self.__class__.__name__}' is a subclass of AbstractDataset and "
        f"it must implement the '_describe' method"
    )
```

### \_exists

```
_exists()
```

Source code in `kedro/io/core.py`

```
def _exists(self) -> bool:
    self._logger.warning(
        "'exists()' not implemented for '%s'. Assuming output does not exist.",
        self.__class__.__name__,
    )
    return False
```

### \_init_config

```
_init_config()
```

Internal method to capture the dataset's initial configuration as provided during instantiation.

This configuration reflects only the arguments supplied at `__init__` time and does not account for any runtime or dynamic changes to the dataset.

Adds a key for the dataset's type using its module and class name and includes the initialization arguments.

For `CachedDataset` it extracts the underlying dataset's configuration, handles the `versioned` flag and removes unnecessary metadata. It also ensures the embedded dataset's configuration is appropriately flattened or transformed.

If the dataset has a version key, it sets the `versioned` flag in the configuration.

Removes the `metadata` key from the configuration if present.

Returns:

- `dict[str, Any]` – A dictionary containing the dataset's type and initialization arguments.

Source code in `kedro/io/core.py`

```
def _init_config(self) -> dict[str, Any]:
    """Internal method to capture the dataset's initial configuration
    as provided during instantiation.

    This configuration reflects only the arguments supplied at `__init__` time
    and does not account for any runtime or dynamic changes to the dataset.

    Adds a key for the dataset's type using its module and class name and
    includes the initialization arguments.

    For `CachedDataset` it extracts the underlying dataset's configuration,
    handles the `versioned` flag and removes unnecessary metadata. It also
    ensures the embedded dataset's configuration is appropriately flattened
    or transformed.

    If the dataset has a version key, it sets the `versioned` flag in the
    configuration.

    Removes the `metadata` key from the configuration if present.

    Returns:
        A dictionary containing the dataset's type and initialization arguments.
    """
    return_config: dict[str, Any] = {
        f"{TYPE_KEY}": f"{type(self).__module__}.{type(self).__name__}"
    }

    if self._init_args:  # type: ignore[attr-defined]
        return_config.update(self._init_args)  # type: ignore[attr-defined]

    if type(self).__name__ == "CachedDataset":
        cached_ds = return_config.pop("dataset")
        cached_ds_return_config: dict[str, Any] = {}
        if isinstance(cached_ds, dict):
            cached_ds_return_config = cached_ds
        elif isinstance(cached_ds, AbstractDataset):
            cached_ds_return_config = cached_ds._init_config()
        if VERSIONED_FLAG_KEY in cached_ds_return_config:
            return_config[VERSIONED_FLAG_KEY] = cached_ds_return_config.pop(
                VERSIONED_FLAG_KEY
            )
        # Pop metadata from configuration
        cached_ds_return_config.pop("metadata", None)
        return_config["dataset"] = cached_ds_return_config

    # Set `versioned` key if version present in the dataset
    if return_config.pop(VERSION_KEY, None):
        return_config[VERSIONED_FLAG_KEY] = True

    # Pop metadata from configuration
    return_config.pop("metadata", None)

    return return_config
```

### \_load_wrapper

```
_load_wrapper(load_func)
```

Decorate `load_func` with logging and error handling code.

Source code in `kedro/io/core.py`

```
@classmethod
def _load_wrapper(cls, load_func: Callable[[Self], _DO]) -> Callable[[Self], _DO]:
    """Decorate `load_func` with logging and error handling code."""

    @wraps(load_func)
    def load(self: Self) -> _DO:
        self._logger.debug("Loading %s", str(self))

        try:
            return load_func(self)
        except DatasetError:
            raise
        except Exception as exc:
            # This exception handling is by design as the composed datasets
            # can throw any type of exception.
            message = f"Failed while loading data from dataset {self!s}.\n{exc!s}"
            raise DatasetError(message) from exc

    load.__annotations__["return"] = load_func.__annotations__.get("return")
    load.__loadwrapped__ = True  # type: ignore[attr-defined]
    return load
```

### \_pretty_repr

```
_pretty_repr(object_description)
```

Source code in `kedro/io/core.py`

```
def _pretty_repr(self, object_description: dict[str, Any]) -> str:
    str_keys = []
    for arg_name, arg_descr in object_description.items():
        if arg_descr is not None:
            descr = pprint.pformat(
                arg_descr,
                sort_dicts=False,
                compact=True,
                depth=2,
                width=sys.maxsize,
            )
            str_keys.append(f"{arg_name}={descr}")

    return f"{type(self).__module__}.{type(self).__name__}({', '.join(str_keys)})"
```

### \_release

```
_release()
```

Source code in `kedro/io/core.py`

```
def _release(self) -> None:
    pass
```

### \_save_wrapper

```
_save_wrapper(save_func)
```

Decorate `save_func` with logging and error handling code.

Source code in `kedro/io/core.py`

```
@classmethod
def _save_wrapper(
    cls, save_func: Callable[[Self, _DI], None]
) -> Callable[[Self, _DI], None]:
    """Decorate `save_func` with logging and error handling code."""

    @wraps(save_func)
    def save(self: Self, data: _DI) -> None:
        if data is None:
            raise DatasetError("Saving 'None' to a 'Dataset' is not allowed")

        try:
            self._logger.debug("Saving %s", str(self))
            save_func(self, data)
        except (DatasetError, FileNotFoundError, NotADirectoryError):
            raise
        except Exception as exc:
            message = f"Failed while saving data to dataset {self!s}.\n{exc!s}"
            raise DatasetError(message) from exc

    save.__annotations__["data"] = save_func.__annotations__.get("data", Any)
    save.__annotations__["return"] = save_func.__annotations__.get("return")
    save.__savewrapped__ = True  # type: ignore[attr-defined]
    return save
```

### exists

```
exists()
```

Checks whether a dataset's output already exists by calling the provided \_exists() method.

Returns:

- `bool` – Flag indicating whether the output already exists.

Raises:

- `DatasetError` – when underlying exists method raises error.

Source code in `kedro/io/core.py`

```
def exists(self) -> bool:
    """Checks whether a dataset's output already exists by calling
    the provided _exists() method.

    Returns:
        Flag indicating whether the output already exists.

    Raises:
        DatasetError: when underlying exists method raises error.

    """
    try:
        self._logger.debug("Checking whether target of %s exists", str(self))
        return self._exists()
    except Exception as exc:
        message = f"Failed during exists check for dataset {self!s}.\n{exc!s}"
        raise DatasetError(message) from exc
```

### from_config

```
from_config(name, config, load_version=None, save_version=None)
```

Create a dataset instance using the configuration provided.

Parameters:

- **`name`** (`str`) – Data set name.
- **`config`** (`dict[str, Any]`) – Data set config dictionary.
- **`load_version`** (`str | None`, default: `None` ) – Version string to be used for load operation if the dataset is versioned. Has no effect on the dataset if versioning was not enabled.
- **`save_version`** (`str | None`, default: `None` ) – Version string to be used for save operation if the dataset is versioned. Has no effect on the dataset if versioning was not enabled.

Returns:

- `AbstractDataset` – An instance of an AbstractDataset subclass.

Raises:

- `DatasetError` – When the function fails to create the dataset from its config.

Source code in `kedro/io/core.py`

```
@classmethod
def from_config(
    cls: type,
    name: str,
    config: dict[str, Any],
    load_version: str | None = None,
    save_version: str | None = None,
) -> AbstractDataset:
    """Create a dataset instance using the configuration provided.

    Args:
        name: Data set name.
        config: Data set config dictionary.
        load_version: Version string to be used for ``load`` operation if
            the dataset is versioned. Has no effect on the dataset
            if versioning was not enabled.
        save_version: Version string to be used for ``save`` operation if
            the dataset is versioned. Has no effect on the dataset
            if versioning was not enabled.

    Returns:
        An instance of an ``AbstractDataset`` subclass.

    Raises:
        DatasetError: When the function fails to create the dataset
            from its config.

    """
    try:
        class_obj, config = parse_dataset_definition(
            config, load_version, save_version
        )
    except Exception as exc:
        raise DatasetError(
            f"An exception occurred when parsing config "
            f"for dataset '{name}':\n{exc!s}"
        ) from exc

    try:
        dataset = class_obj(**config)
    except TypeError as err:
        raise DatasetError(
            f"\n{err}.\nDataset '{name}' must only contain arguments valid for the "
            f"constructor of '{class_obj.__module__}.{class_obj.__qualname__}'."
        ) from err
    except Exception as err:
        raise DatasetError(
            f"\n{err}.\nFailed to instantiate dataset '{name}' "
            f"of type '{class_obj.__module__}.{class_obj.__qualname__}'."
        ) from err
    return dataset
```

### load

```
load()
```

Loads data by delegation to the provided load method.

Returns:

- `_DO` – Data returned by the provided load method.

Raises:

- `DatasetError` – When underlying load method raises error.

Source code in `kedro/io/core.py`

```
@abc.abstractmethod
def load(self) -> _DO:
    """Loads data by delegation to the provided load method.

    Returns:
        Data returned by the provided load method.

    Raises:
        DatasetError: When underlying load method raises error.

    """
    raise NotImplementedError(
        f"'{self.__class__.__name__}' is a subclass of AbstractDataset and "
        f"it must implement the 'load' method"
    )
```

### release

```
release()
```

Release any cached data.

Raises:

- `DatasetError` – when underlying release method raises error.

Source code in `kedro/io/core.py`

```
def release(self) -> None:
    """Release any cached data.

    Raises:
        DatasetError: when underlying release method raises error.

    """
    try:
        self._logger.debug("Releasing %s", str(self))
        self._release()
    except Exception as exc:
        message = f"Failed during release for dataset {self!s}.\n{exc!s}"
        raise DatasetError(message) from exc
```

### save

```
save(data)
```

Saves data by delegation to the provided save method.

Parameters:

- **`data`** (`_DI`) – the value to be saved by provided save method.

Raises:

- `DatasetError` – when underlying save method raises error.
- `FileNotFoundError` – when save method got file instead of dir, on Windows.
- `NotADirectoryError` – when save method got file instead of dir, on Unix.

Source code in `kedro/io/core.py`

```
@abc.abstractmethod
def save(self, data: _DI) -> None:
    """Saves data by delegation to the provided save method.

    Args:
        data: the value to be saved by provided save method.

    Raises:
        DatasetError: when underlying save method raises error.
        FileNotFoundError: when save method got file instead of dir, on Windows.
        NotADirectoryError: when save method got file instead of dir, on Unix.

    """
    raise NotImplementedError(
        f"'{self.__class__.__name__}' is a subclass of AbstractDataset and "
        f"it must implement the 'save' method"
    )
```
